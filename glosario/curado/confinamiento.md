# Confinamiento

## Definición

El **confinamiento** restringe las rutas (o la región) que un agente puede tocar: la limitación de lo que una operación puede tocar a una región resuelta, como un directorio o un dominio (`SE-569`, `SE-582`).

## Por qué importa

Acota el daño que un agente puede hacer con sus herramientas. Es un control barato y exacto en lo que cubre, pero no cubre todo, y la diferencia importa.

## Cómo funciona

El confinamiento por rutas **resuelve** cada ruta que el agente quiere leer o escribir (siguiendo `..` y enlaces simbólicos) y la compara con la raíz permitida. En el laboratorio de `SE-582`, bloquea dos de las cinco acciones (el borrado con `../home/config.txt` y la escritura con una ruta absoluta) y deja los dos archivos «personales» intactos. No cubre un proceso hijo lanzado con una herramienta permitida: ese proceso no pasa por la comprobación de rutas.

## Ejemplo

```python
from pathlib import Path
raiz = Path("/proyecto").resolve()
def permitido(ruta):
    return Path(ruta).resolve().is_relative_to(raiz)
```

Resolver antes de comparar evita que `../` o un enlace escapen de la raíz.

## Errores y confusiones comunes

Comparar texto sin resolver la ruta; creer que el confinamiento por rutas aísla procesos.

## Límites y cuándo no aplica

Un contenedor lo cubre y lo supera para procesos hijos y red: `SE-582` explica que el confinamiento es un control del arnés que decide qué *llamadas* acepta, y el contenedor decide qué puede *ocurrir*; se complementan.
