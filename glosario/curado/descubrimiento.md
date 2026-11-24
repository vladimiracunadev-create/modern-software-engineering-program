# Descubrimiento

## Definición

En el contexto de plugins (`SE-115`), el **descubrimiento** es el mecanismo por el que una aplicación **enumera los proveedores de extensión disponibles** junto con su metadata: por *entry points* (declaración en el paquete del plugin que la aplicación consulta) o por **registro explícito** (el plugin se inscribe en un registro conocido). `SE-338` lo formula desde la arquitectura: define quién puede añadir un complemento y cómo se declara. Este término no es el «descubrimiento» de producto de la Parte 10; aquí designa la enumeración de extensiones.

## Por qué importa

Una aplicación extensible necesita saber qué extensiones existen sin conocerlas de antemano. Si lo hace mal, aparecen dos problemas: no se sabe de dónde viene cada plugin ni en qué orden se cargará, y el arranque se encarece con cada plugin instalado. La decisión que cambia es **qué hace el sistema con lo que encuentra**: `SE-115` separa explícitamente descubrir de activar. Que algo esté instalado no significa que deba ejecutarse; esa decisión la toma el usuario o una política.

## Cómo funciona

Hay dos formas habituales:

- **Entry points:** el paquete del plugin declara en sus metadatos un nombre que apunta a un objeto de su código. La aplicación lee los metadatos de todos los paquetes instalados y obtiene nombres y destinos **sin importar el código**. Python ofrece este mecanismo en `importlib.metadata`.
- **Registro explícito:** el plugin llama a una función de la aplicación para registrarse, o se lista en un archivo de configuración.

Las dos dejan **procedencia** (qué paquete trajo qué extensión). El escaneo de carpetas con importación automática, en cambio, mezcla procedencia y orden de carga y obliga a ejecutar código para saber qué hay. De ahí el principio de `SE-115`: **descubrir no implica activar**. Se enumeran los nombres, se aplica la política (lista permitida, versión compatible) y solo entonces se carga lo solicitado. Eso resuelve dos fallos documentados: la aplicación que no arranca porque un plugin no se importa (carga ansiosa sin aislamiento, corregida cargando por plugin con `try/except` y registrando el fallo) y el arranque que tarda más cuanto más plugins hay (se cargan todos aunque se use uno; se corrige descubriendo los nombres y cargando solo el pedido).

## Ejemplo

El SDK+CLI de `SE-115` expone un punto de extensión. La CLI lista las extensiones sin cargarlas y carga la elegida:

```python
from importlib.metadata import entry_points

disponibles = {ep.name: ep for ep in entry_points(group="engineering_sdk.plugins")}
print(sorted(disponibles))           # descubrir: solo nombres
plugin = disponibles["mi-regla"].load()   # activar: solo el solicitado
```

Si `mi-regla` falla al importarse, se registra el error y el resto de la aplicación sigue funcionando.

## Errores y confusiones comunes

- **Cargar todo al arrancar.** El costo y el riesgo crecen con cada plugin instalado.
- **Escanear carpetas.** Mezcla procedencia y orden, y ejecuta código desconocido solo para listar.
- **Confundir descubrir con confiar.** Un plugin descubierto no está aprobado.
- **Sin aislamiento de fallos.** Un plugin roto derriba la aplicación entera.

## Límites y cuándo no aplica

Con dos o tres extensiones previsibles y un solo equipo, una interfaz y tres implementaciones en el mismo repositorio (el patrón Strategy de la Parte 26) dan la misma extensión sin descubrimiento, sin versión y sin aislamiento (`SE-338`). El descubrimiento resuelve extensión por terceros; si nadie ajeno va a extender el sistema, es complejidad innecesaria. Tampoco ofrece seguridad por sí mismo: ejecutar plugins de terceros exige además permisos y verificación de origen.
