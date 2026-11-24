# Artefacto e instalación

## Definición

En `SE-119`, **artefacto e instalación** es el paso de comprobar un paquete como lo recibirá quien lo consume: se construyen la distribución fuente (**sdist**) y la rueda (**wheel**), se inspeccionan sus contenidos y se instalan en un entorno virtual limpio. El artefacto es el archivo que se entrega; la instalación es la prueba de que ese archivo, y no el árbol de trabajo del autor, funciona. Se trata de un procedimiento de verificación propio del taller, apoyado en las especificaciones de empaquetado de Python.

## Por qué importa

Ejecutar el código desde el checkout prueba el repositorio, no el paquete. El repositorio tiene archivos que el paquete puede no incluir, una raíz en `sys.path` que el entorno del consumidor no tendrá y dependencias instaladas por accidente. `SE-119` lo resume: «ejecutar desde checkout no cuenta». La decisión que cambia es qué evidencia basta para publicar. Una prueba verde sobre el árbol de trabajo no es evidencia de que el paquete sea instalable; la evidencia es una instalación limpia con una prueba de humo.

## Cómo funciona

El flujo tiene cuatro pasos con una causa cada uno:

1. **Construir** sdist y wheel desde la configuración del proyecto. La wheel es lo que se instala; el sdist permite reconstruir.
2. **Inspeccionar** el contenido. Un wheel es un archivo zip: listar sus entradas (`namelist()`) y compararlas con una lista esperada revela archivos ausentes, como datos declarados mal, o sobrantes, como pruebas o secretos incluidos por error.
3. **Instalar en un entorno virtual vacío**, sin dependencias previas ni el directorio del proyecto en la ruta de importación. Si algo falla aquí, el consumidor también lo vería.
4. **Probar el comportamiento** instalado: importar el módulo, ejecutar la CLI y leer el archivo de datos.

Se conservan los **hashes** del artefacto para poder comparar después lo probado con lo entregado: si el archivo que se publica no tiene el mismo hash que el que se probó, la prueba no respalda la publicación.

## Ejemplo

`SE-119` empaqueta una capacidad reutilizable y documenta dos fallos que solo aparecen con este procedimiento. Primero, el paquete instalado no encuentra su archivo de datos porque falta `package-data`; la comparación del contenido del wheel contra la lista esperada lo detecta antes de instalar. Segundo, aparece `ModuleNotFoundError` únicamente en un entorno limpio porque una dependencia se usaba sin declararse; en la máquina del autor estaba instalada por otro motivo. La corrección es declararla en `dependencies` y repetir la prueba de humo en un entorno vacío. Una verificación mínima (ilustración):

```bash
python -m build
python -m venv .venv-limpio && .venv-limpio/bin/pip install dist/*.whl
.venv-limpio/bin/python -c "import paquete; print(paquete.__version__)"
```

## Errores y confusiones comunes

- **Probar con instalación editable y darlo por bueno.** La instalación editable enlaza al árbol de trabajo y puede ocultar archivos que el wheel no contiene.
- **Reutilizar el entorno del desarrollo.** Un entorno con dependencias previas no reproduce el del consumidor.
- **No inspeccionar el contenido.** Que el wheel se construya sin error no dice qué contiene.
- **Perder el vínculo entre lo probado y lo publicado.** Sin hash, se publica un archivo distinto del probado.

## Límites y cuándo no aplica

El taller verifica una versión y un entorno principal (`SE-119`); instalar en un solo sistema y versión de Python no garantiza compatibilidad en otros, tarea de la matriz de compatibilidad que construye el proyecto siguiente. Tampoco demuestra procedencia ni seguridad del artefacto. Y para scripts que nunca se distribuyen como paquete, construir wheels es esfuerzo sin retorno; el procedimiento se justifica cuando alguien más instalará el resultado.
