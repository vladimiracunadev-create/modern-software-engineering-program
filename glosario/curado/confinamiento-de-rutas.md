# Confinamiento de rutas

## Definición

El **confinamiento de rutas** (*path confinement*) es la comprobación de que una ruta resuelta queda dentro de una carpeta permitida, tras normalizarla. `SE-262` (firma, sandbox y seguridad del cliente) lo presenta como defensa de la debilidad CWE-22 (recorrido de rutas); `SE-570` y `SE-579` lo reutilizan para el agente: resolver la ruta y comprobar que queda dentro de la raíz permitida.

## Por qué importa

Cuando una aplicación construye una ruta con una entrada externa (un nombre de archivo, un parámetro de una herramienta), esa entrada puede escapar de la carpeta prevista. `SE-262` insiste en que una ruta recibida de fuera debe normalizarse y compararse con la raíz, no filtrarse por apariencia. `SE-570` lo llama el control más repetido y el que más se escribe mal.

## Cómo funciona

La debilidad CWE-22 consiste en construir una ruta con entrada externa sin limitarla a una carpeta. Las defensas ingenuas fallan:

- **Comprobar el prefijo:** `/datos/curso` también es prefijo de `/datos/curso-secreto`; la carpeta con nombre parecido pasa.
- **Rechazar `..`:** no cubre separadores distintos (`\` frente a `/`) ni rutas absolutas que reemplazan la base.

La defensa correcta, según `SE-262`:

1. **Normalizar** la ruta resultante (resolver `.`, `..` y separadores).
2. **Comprobar que está dentro de la raíz usando el separador**, es decir, que la raíz seguida del separador es prefijo, o que la ruta es la propia raíz.
3. **Probar con una lista de casos** de entradas hostiles.

En un disco real, los **enlaces simbólicos** exigen una comprobación adicional: hay que resolver el destino real del enlace y comprobarlo, porque un enlace dentro de la carpeta puede apuntar fuera.

## Ejemplo

Esbozo ilustrativo en Python (no es código de la clase):

```python
from pathlib import Path

def confinar(raiz: str, pedida: str) -> Path:
    base = Path(raiz).resolve()
    destino = (base / pedida).resolve()
    if destino != base and base not in destino.parents:
        raise ValueError("ruta fuera de la raíz")
    return destino
```

`SE-570` lo aplica a los controles del agente del servicio *Avisos*: ganchos, habilidades y confinamiento de rutas, junto con la declaración del entorno donde se ejecuta.

## Errores y confusiones comunes

- **Comprobar solo el prefijo de texto**, que acepta carpetas de nombre parecido.
- **Filtrar «..» como cadena**, que ignora rutas absolutas y otros separadores.
- **Olvidar los enlaces simbólicos** en un disco real (`SE-262`).
- **Creer que el confinamiento reemplaza al sandbox:** es una capa, no el aislamiento del proceso.

## Límites y cuándo no aplica

La comprobación se hace en un momento y el sistema de archivos puede cambiar después (una condición de carrera entre comprobar y usar). No protege contra lo que la propia carpeta permitida ya contiene. En la clase se probó con una lista de casos, no sobre un disco con enlaces reales; esa parte la advierte la clase como comprobación adicional.
