# Runtime e implementación

## Definición

**Runtime e implementación** nombra, en `SE-102`, la distinción de que **la versión del lenguaje, la implementación y la arquitectura son dimensiones distintas**: «Python 3.12» no identifica por sí solo qué programa corre. Una misma versión del lenguaje puede ejecutarse con distintas **implementaciones** (CPython, PyPy y otras), sobre distintas **arquitecturas** de procesador (x86-64, ARM) y con distintos *builds* (opciones de compilación, distribución del sistema, versión de la biblioteca de C). El término *runtime* designa el entorno que ejecuta el programa; la implementación es una de sus dimensiones.

## Por qué importa

Cuando alguien dice «funciona en Python 3.12», comunica menos de lo que parece. Las extensiones nativas se compilan para una arquitectura y una interfaz binaria (ABI) concretas; la velocidad y el comportamiento de ciertas operaciones cambian entre implementaciones; la distribución del sistema trae su propia biblioteca de C. `SE-102` extrae la consecuencia práctica: **«Python 3.12» no identifica necesariamente *build*, ABI ni distribución**. La decisión que cambia es qué se declara como soportado y qué se prueba de verdad.

## Cómo funciona

Hay tres dimensiones que conviene mantener separadas:

- **Versión del lenguaje:** qué sintaxis y qué biblioteca estándar existen (3.9, 3.12).
- **Implementación:** el programa concreto que interpreta o compila el lenguaje. Cumplen la misma especificación general, pero difieren en rendimiento, gestión de memoria y soporte de extensiones nativas.
- **Arquitectura y *build*:** el procesador y el sistema, y la forma de construir el intérprete. Determinan si un paquete binario precompilado (una rueda) existe para esa combinación o hay que compilar desde el código fuente.

La consecuencia de que sean dimensiones distintas es que las pruebas en una combinación no se transfieren a las demás. El proyecto debe **declarar un rango soportado** (qué promete) y mantener una **matriz realmente probada** (qué verificó), y distinguir ambas: el rango es una intención, la matriz es evidencia. Una celda sin ejecutar es «no verificada», no «soportada».

## Ejemplo

Un script de medición produce tiempos distintos en dos equipos. Antes de culpar al código, se registra el entorno completo:

```python
import platform, sys
print(sys.version.split()[0],            # versión
      platform.python_implementation(),  # CPython, PyPy...
      platform.machine(),                # x86_64, arm64...
      platform.platform())               # sistema y versión
```

`SE-102` documenta el síntoma: la medición no se repite en otro equipo por compilación o sistema distintos; la corrección es registrar versión y sistema con cada medición. Y el síntoma de la resolución del intérprete: el script usa otro Python en otra máquina porque se invoca `python` a secas, y se corrige declarando la versión y verificándola al inicio.

## Errores y confusiones comunes

- **Equiparar versión con entorno.** «3.12» no basta para reproducir un resultado.
- **Declarar soporte sin probar.** El rango declarado no es la matriz verificada.
- **Ignorar la arquitectura.** Una rueda precompilada puede no existir para ARM o para otra distribución.
- **Comparar mediciones de equipos distintos.** Sin registrar el entorno, la comparación no es válida.

## Límites y cuándo no aplica

Fijar el *runtime* no aísla paquetes instalados (`SE-102`). Para código puro de Python sin extensiones nativas, las diferencias de arquitectura casi no se notan, y el rigor sobre ABI y *build* es innecesario. La distinción importa más cuanto más dependa el proyecto de código nativo, de rendimiento o de comportamiento específico del intérprete.
