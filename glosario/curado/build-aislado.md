# Build aislado

## Definición

Un **build aislado** es una construcción de paquete que se ejecuta con los **requisitos de build declarados** en el proyecto, en lugar de usar lo que casualmente haya instalado en la máquina de quien construye. En `SE-112` aparece junto al backend de construcción: el proyecto declara qué herramientas necesita para construirse (por ejemplo en `[build-system]` de `pyproject.toml`) y el constructor las instala en un entorno temporal. Es distinto de un build **reproducible**, que además exige que el resultado sea idéntico byte a byte; aislar es condición necesaria, no suficiente.

## Por qué importa

Si un paquete se construye con el entorno del autor, el resultado depende de detalles invisibles: una versión de herramienta instalada hace meses, una variable de entorno, un archivo local. Otra persona (o el servidor de integración) obtiene otro artefacto o un fallo. La decisión que cambia es qué se considera «el build»: no «lo que sale en mi máquina», sino «lo que sale de las entradas declaradas». Así, los requisitos faltantes se convierten en un error inmediato y no en un defecto que aparece en el equipo de un consumidor.

## Cómo funciona

El mecanismo tiene tres elementos:

- **Declaración.** El proyecto lista los requisitos de construcción y el backend que los usa.
- **Entorno temporal vacío.** El constructor crea un entorno limpio, instala solo lo declarado y ejecuta el backend allí. Cualquier módulo no declarado produce un error de importación en lugar de resolverse con lo que hubiera disponible.
- **Resultado como función de las entradas declaradas.** Lo producido (sdist, wheel) depende de fuentes y requisitos, no del entorno del autor.

`SE-112` marca el límite de la idea: aislar no vuelve reproducible. Marcas de tiempo dentro de los archivos, orden de los miembros del archivo comprimido y versión de la cadena de herramientas pueden variar entre construcciones y cambiar los hashes aunque el contenido sea equivalente. Por eso solo se afirma «hash igual» después de **comparar bytes bajo un protocolo declarado** (mismas entradas, misma fecha fijada, mismo entorno), no por haber ejecutado dos veces.

## Ejemplo

En el producto reutilizable con SDK y CLI, el release debe contener artefactos inmutables y procedencia. Un fallo típico que el aislamiento revela es el de un archivo de datos que existe en el árbol de trabajo pero no entra en el paquete: aparece como `FileNotFoundError` solo tras instalar, y la corrección es declarar el archivo en `package-data` y comprobar el contenido de la rueda contra una lista esperada. Otro caso de `SE-112`: `import json` devuelve un objeto raro porque un `json.py` local tapa la biblioteca estándar; se detecta ejecutando con `-I` (modo aislado) o `-P`.

```bash
python -m build            # aísla por defecto: crea un entorno temporal
python -I -c "import json; print(json.__file__)"
```

## Errores y confusiones comunes

- **Tomar «aislado» por «reproducible».** Dos construcciones aisladas pueden producir hashes distintos por marcas de tiempo.
- **Declarar solo dependencias de ejecución.** Las herramientas de construcción también deben declararse, o el build depende del entorno del autor.
- **Afirmar igualdad de hashes sin comparar.** Debe compararse el contenido bajo un protocolo escrito.
- **Dejar archivos locales en la ruta de importación.** Un módulo local con nombre de la biblioteca estándar altera el resultado.

## Límites y cuándo no aplica

Un paquete instalado todavía necesita una interfaz operable y estable (`SE-112`). Un build aislado no protege frente a una dependencia comprometida: instala lo que se declara desde donde se declara, sin verificar procedencia. Y para un script personal que nunca se distribuye, el costo de declarar y aislar construcciones no se compensa. El grado de rigor debería corresponder a cuántas personas consumirán el artefacto.
