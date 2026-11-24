# Resolución por PATH

## Definición

La **resolución por PATH** es el mecanismo por el que el *shell* decide qué ejecutable corre cuando se escribe un nombre de comando como `python`. Según `SE-102`, el *shell* busca el ejecutable según el **PATH** (la lista ordenada de directorios de búsqueda), pero también según **alias**, **launchers** (lanzadores como `py` en Windows) y **shims** (ejecutables intermedios de los gestores de versiones). El resultado puede cambiar según la terminal y el directorio: el mismo nombre no identifica un único programa.

## Por qué importa

Un script que invoca `python` a secas depende de qué `python` resuelva el *shell* en ese momento. En otra máquina, otra terminal o tras activar un entorno, es otro intérprete, con otra versión y otros paquetes. `SE-102` documenta el síntoma: el script usa otro Python en otra máquina porque se invoca `python` a secas; la corrección es declarar la versión y verificarla al inicio. La decisión que cambia es cómo se diagnostica y cómo se escribe: se sabe qué ejecutable se está usando realmente, y no se asume.

## Cómo funciona

La búsqueda sigue un orden:

1. **Alias y funciones del *shell*:** tienen prioridad sobre lo que haya en disco.
2. **Directorios del PATH, de izquierda a derecha:** el primero que contenga un ejecutable con ese nombre gana. Por eso el orden del PATH importa: añadir un directorio al principio hace que sus programas tapen a los de más abajo.
3. **Shims y lanzadores:** programas pequeños que ocupan un nombre y delegan en otro ejecutable según una regla (un archivo del proyecto, una variable). Los gestores de versiones se basan en ellos.

Todo esto ocurre **en cada terminal por separado**, con el PATH que esa terminal tenga: una terminal abierta antes de modificar el PATH no ve el cambio. Y varía por directorio si el gestor lee un archivo de configuración del proyecto. Para diagnosticar, `SE-102` aconseja **registrar la ruta absoluta observada** (con `which python`, `where python` o, desde el propio programa, `sys.executable`). En cambio, **escribir esa ruta fija dentro del proyecto reduce la portabilidad**: la ruta de un equipo no existe en otro.

## Ejemplo

```bash
which python         # /home/ana/.pyenv/shims/python   (un shim)
python -c "import sys; print(sys.executable, sys.version.split()[0])"
# /home/ana/.pyenv/versions/3.12.4/bin/python 3.12.4
```

En la primera línea se ve que `python` es un *shim*; en la segunda, qué intérprete corre realmente. Un script robusto lo comprueba al inicio:

```python
import sys
if sys.version_info < (3, 11):
    raise SystemExit(f"Se requiere Python >= 3.11; se usa {sys.executable}")
```

Otra consecuencia que la clase documenta: una medición no se repite en otro equipo por compilación o sistema distintos; se registran versión y sistema con cada medición.

## Errores y confusiones comunes

- **Invocar `python` a secas en scripts compartidos.** Resuelve a lo que haya.
- **Fijar rutas absolutas en el proyecto.** No son portables.
- **Olvidar que cada terminal tiene su PATH.** Un cambio no se ve en terminales ya abiertas.
- **Confundir alias con ejecutable.** Un alias solo existe en el *shell* interactivo, no en un script.

## Límites y cuándo no aplica

Fijar el *runtime* no aísla los paquetes instalados (`SE-102`): la resolución dice qué intérprete corre, no qué bibliotecas ve. En contenedores o entornos con PATH controlado, la resolución es estable y el diagnóstico más sencillo. Y la sintaxis y los nombres de las herramientas de diagnóstico (`which`, `where`, `Get-Command`) varían según el sistema y el *shell*.
