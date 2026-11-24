# Diseño desde consumidor

## Definición

El **diseño desde consumidor** es, en el taller de `SE-119`, la práctica de escribir la prueba de un paquete **desde un directorio externo al repositorio, usando solo imports públicos**, y sin *mocks* de internals. La prueba se coloca en la posición de quien consume el producto: no conoce la estructura interna, no puede importar módulos privados y depende solo de lo que el paquete publica. Es una técnica del programa asociada a las pruebas de contrato escritas «desde el consumidor».

## Por qué importa

Quien escribe una biblioteca sabe cosas que el consumidor ignora: qué módulo contiene cada función, qué argumentos tienen valores razonables por defecto, qué excepción se espera. Esas suposiciones se cuelan en las pruebas hechas desde dentro, que pasan aunque el uso real sea incómodo o imposible. La decisión que cambia es qué prueba cuenta como evidencia de que el paquete es usable: la que ejecuta alguien que solo tiene lo público. `SE-119` dice que esto revela **nombres, defaults, errores y documentación** que el autor daba por supuestos.

## Cómo funciona

Cuatro reglas hacen que la prueba sea de consumidor de verdad:

- **Directorio externo.** La prueba vive fuera del árbol de código del paquete, para que Python no resuelva imports contra el código fuente y se use el paquete **instalado**.
- **Solo imports públicos.** Se importa lo que la API declara; si hace falta entrar a un módulo interno para algo corriente, falta un símbolo público.
- **Sin mocks de internals.** Si se simulan funciones privadas, se prueba la implementación, no la promesa. Se pueden simular recursos externos (red, disco), pero no el interior del paquete.
- **Entorno limpio.** Se instala el artefacto en un entorno vacío, de modo que una dependencia no declarada aparezca como fallo.

Cada fricción que aparece es información: un nombre confuso, un parámetro obligatorio que debería tener valor por defecto, un error que no dice qué hacer. La causa de que el método encuentre esto es que elimina el conocimiento privilegiado del autor.

## Ejemplo

En el taller de `SE-119`, la prueba del paquete reutilizable vive fuera del repositorio y solo hace esto:

```python
# prueba_consumidor.py  (en un directorio aparte, con el paquete instalado)
from engineering_sdk import choose_next      # único import: público

def test_elige_el_mas_urgente():
    casos = [{"id": 1, "prioridad": 2}, {"id": 2, "prioridad": 1}]
    assert choose_next(casos)["id"] == 2
```

Si para escribirla hace falta importar `engineering_sdk._interno.reglas`, o pasar cinco argumentos que el autor siempre usa igual, el diseño tiene un defecto de uso. Los dos fallos documentados por la clase aparecen aquí: el archivo de datos no encontrado (falta `package-data`) y el `ModuleNotFoundError` solo en entorno limpio (dependencia no declarada).

## Errores y confusiones comunes

- **Prueba dentro del paquete.** Importa por rutas relativas y oculta problemas de instalación.
- **Mockear internals.** La prueba pasa aunque el comportamiento público esté roto.
- **Usar el código fuente en lugar del instalado.** El resultado no representa lo que recibe el consumidor.
- **Reescribir la prueba del autor y llamarla de consumidor.** Si usa los mismos atajos, no aporta información nueva.

## Límites y cuándo no aplica

El taller verifica una versión y un entorno principal (`SE-119`); no cubre otros sistemas ni versiones de dependencias, tarea de la matriz de compatibilidad. La prueba de consumidor encuentra problemas de usabilidad en lo que ejercita, pero no sustituye las pruebas unitarias del interior, que localizan defectos con más precisión. Para módulos internos no publicados, que nadie consume desde fuera, el enfoque no tiene sentido.
