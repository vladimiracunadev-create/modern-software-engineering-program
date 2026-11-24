# Linter

## Definición

Un **linter** es una herramienta de análisis estático que **detecta patrones sospechosos, usos riesgosos de una API o incumplimientos de convenciones** en el código fuente, sin ejecutarlo. En `SE-100` se distingue de otras herramientas: el compilador (verifica la sintaxis y traduce), el formateador (solo cambia la presentación) y el **verificador de tipos**. El linter aplica reglas sobre la **forma** del código, por ejemplo importaciones sin usar o nombres no definidos; el verificador de tipos razona sobre los tipos declarados y detecta usos incompatibles. Cubren defectos distintos y se complementan.

## Por qué importa

Un linter encuentra defectos baratos antes de ejecutar nada: una variable que nunca se usa, una comparación que siempre es falsa, un argumento mutable por defecto. Es la primera red de seguridad de un proyecto. La decisión que cambia es cuándo se detecta un error: al guardar el archivo, no en producción. Además, bien configurado, hace explícitas las convenciones del equipo; mal configurado, produce ruido que las personas aprenden a ignorar, que es peor que no tenerlo.

## Cómo funciona

El linter analiza el código a un árbol sintáctico y recorre ese árbol comprobando cada **regla**. Cada regla tiene tres rasgos que `SE-100` pide tener presentes:

- **Intención:** qué defecto o convención protege («no dejar variables sin usar»).
- **Severidad:** si es un error que bloquea o una advertencia.
- **Posibles falsos positivos:** casos legítimos que la regla marca de todos modos.

Cuando una regla marca un caso legítimo, se **suprime** de forma local. La clase indica cómo: desactivar la regla globalmente por un solo caso local **elimina la señal** para todo el proyecto; una supresión debe incluir **una razón y el alcance mínimo** (esa línea, no todo el archivo). Además, hay una relación entre velocidad y lugar de ejecución: un linter de 0,2 s puede ejecutarse al guardar y en cada confirmación; un verificador de tipos de 2 s sin caché se ejecuta con caché incremental o en integración continua.

## Ejemplo

Un código con dos defectos que un linter detecta sin ejecutarlo:

```python
import os                      # importación sin usar
def total(items=[]):           # argumento mutable por defecto
    return sum(items)
```

La salida del linter apunta a la línea y a la regla. Si en un caso concreto una importación sin usar es deliberada (un efecto al importar), se suprime solo ahí y con razón:

```python
import modulo_con_registro  # noqa: F401  (registra plugins al importarse)
```

`SE-100` documenta un caso inverso: el linter pasa pero hay un defecto conocido porque la regla no está activa; la corrección es revisar el conjunto de reglas y activar la relevante.

## Errores y confusiones comunes

- **Creer que «pasa el linter» significa «es correcto».** Solo significa que no violó las reglas activas.
- **Desactivar reglas globalmente por un caso aislado.** Se pierde la señal para todos los demás casos.
- **Supresiones sin razón.** Nadie sabe después si siguen siendo válidas.
- **Confundirlo con el verificador de tipos o el formateador.** Cada uno cubre defectos distintos.

## Límites y cuándo no aplica

La señal estática no sustituye la experimentación y puede ser ruidosa durante la exploración (`SE-100`): en un cuaderno de pruebas, las reglas de estilo estorban. Un linter no detecta errores de lógica ni de comportamiento en tiempo de ejecución; solo patrones reconocibles. Y un conjunto muy grande de reglas puede abrumar; es preferible un conjunto pequeño que se respete a uno exhaustivo que se ignore.
