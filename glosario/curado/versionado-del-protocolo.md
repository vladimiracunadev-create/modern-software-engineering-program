# Versionado del protocolo

## Definición

El **versionado del protocolo** es, en `SE-115`, la práctica por la que **el anfitrión (*host*) y el plugin negocian versión y capacidades antes de ejecutar** cualquier trabajo conjunto. El protocolo es el contrato entre la aplicación que extiende y el complemento: qué funciones se invocan, qué datos se pasan. Tiene su propia versión, independiente de la del paquete: un plugin dice «hablo la versión 2 del protocolo» y el anfitrión responde si la soporta.

## Por qué importa

Una versión del paquete no basta cuando hay **contratos independientes**: la aplicación puede pasar de 1.4 a 1.5 sin tocar el protocolo de plugins, o cambiar el protocolo sin que el paquete pase a una mayor. Si el plugin y el anfitrión asumen una versión sin comprobarla, una incompatibilidad se manifiesta como un fallo opaco o, peor, como **corrupción silenciosa**: datos mal interpretados que no producen error. La decisión que cambia es cuándo se detecta la incompatibilidad: antes de ejecutar, con un error accionable.

## Cómo funciona

El mecanismo tiene tres pasos:

1. **Declaración:** el plugin declara, en su metadata, la versión (o rango) del protocolo que implementa y las **capacidades** opcionales que ofrece.
2. **Negociación:** el anfitrión compara con las versiones y capacidades que soporta. Si hay intersección, elige la más alta común; si no, rechaza.
3. **Ejecución condicionada:** solo se invoca lo acordado; una capacidad no negociada no se usa.

`SE-115` fija la exigencia sobre el resultado: una **incompatibilidad produce un error accionable** («el plugin X requiere el protocolo 3; este anfitrión soporta 1 y 2; actualice el anfitrión o use la versión 1.x del plugin»), **no una corrupción silenciosa**. Esto se parece a lo que hace el protocolo de servidores de lenguaje, donde cliente y servidor negocian capacidades al inicializar. La separación entre versión del protocolo y versión del paquete permite evolucionar cada una a su ritmo, y aplicar a cada una las reglas de compatibilidad que correspondan.

## Ejemplo

Un anfitrión que soporta los protocolos 1 y 2:

```python
SOPORTADAS = {1, 2}

def cargar(plugin):
    pedidas = set(plugin.metadata["protocolo"])        # p. ej. {2, 3}
    comunes = pedidas & SOPORTADAS
    if not comunes:
        raise ErrorDePlugin(
            f"{plugin.nombre} requiere protocolo {sorted(pedidas)}; "
            f"este anfitrión soporta {sorted(SOPORTADAS)}. "
            "Actualice el anfitrión o instale una versión anterior del plugin."
        )
    return plugin.iniciar(version=max(comunes))
```

El fallo se detecta al cargar, con un mensaje que dice qué hacer. Sin la negociación, el plugin podría ejecutarse con formatos de mensaje distintos y producir resultados erróneos sin que nada lo avisara. `SE-115` complementa con dos defectos del arranque: la aplicación no arranca porque un plugin no se importa (carga ansiosa sin aislamiento; se carga por plugin con `try/except` y se registra) y el arranque tarda más cuantos más plugins hay (se descubren los nombres y se carga solo el solicitado).

## Errores y confusiones comunes

- **Usar la versión del paquete como versión del protocolo.** Son contratos distintos.
- **No negociar.** Se asume la versión y los fallos aparecen en ejecución.
- **Errores opacos.** La incompatibilidad debe decir qué falta y qué hacer.
- **Cambiar el protocolo sin versionarlo.** Rompe a los plugins existentes.

## Límites y cuándo no aplica

Un protocolo reduce el acoplamiento, pero **no hace seguro el código arbitrario** (`SE-115`): negociar versiones no impide que un plugin haga algo dañino; para eso se necesitan permisos, aislamiento y verificación de origen. Si el anfitrión y los plugins se publican siempre juntos y se despliegan a la vez, la negociación es sobrecarga. Y el versionado del protocolo no resuelve la compatibilidad semántica: dos versiones pueden «hablar igual» y significar cosas distintas si el contrato no está bien especificado.
