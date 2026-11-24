# Semántica antes que sintaxis

[↑ Glosario](../../README.md) · [← Semántica](./semantica.md) · [Semánticas de entrega →](./semanticas-de-entrega.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

**Semántica antes que sintaxis** es el principio de comparación de [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md): **dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para casos normales, límite y de error**. La semántica es lo que el programa *significa* (qué devuelve, qué rechaza, en qué orden resuelve un empate); la sintaxis, cómo está escrito. Antes de comparar la longitud, la elegancia o el estilo de dos soluciones, hay que haber establecido que hacen lo mismo.

## Por qué importa

Es fácil comparar implementaciones por lo visible: cuántas líneas tienen, cuántos *tokens*. Pero [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) advierte que **contar líneas o *tokens* sin verificar la semántica premia las omisiones**: la versión más corta puede serlo porque no valida entradas, no maneja el empate o ignora un caso de error. La decisión que cambia es el orden de las preguntas: primero «¿hacen lo mismo?» y solo si la respuesta es sí, «¿cuál es más clara, corta o mantenible?».

## Cómo funciona

El procedimiento de la clase es:

1. **Congelar el contrato:** la entrada aceptada, la salida, el **orden de empate**, los errores y los casos (normales, límite, error).
2. **Buscar una representación equivalente** en cada modelo. [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) da ejemplos de mapeos: `None` puede corresponder a `Option`; una excepción recuperable, a `Result`; un diccionario heterogéneo, a un registro con campos (*struct*).
3. **Juzgar la equivalencia por comportamiento, no por parecido textual,** con fixtures comunes. Solo se normalizan diferencias de **presentación** (formato de un texto de salida), no de decisión.

La razón de fondo es que los lenguajes y paradigmas representan el mismo concepto de maneras distintas, y un parecido textual engaña: dos funciones que se parecen mucho pueden diferir en un caso límite, y dos que no se parecen nada pueden ser equivalentes. Solo ejecutar el mismo conjunto de casos lo revela.

## Ejemplo

Dos versiones de una regla de aprobación:

```python
# A: corta
def aprobar(c): return c["puntaje"] > 60

# B: más larga, maneja los casos de borde
def aprobar_b(c):
    if "puntaje" not in c or not isinstance(c["puntaje"], (int, float)):
        raise ValueError("puntaje inválido")
    return c["puntaje"] > 60
```

A es tres veces más corta y pierde frente a B en solidez: ante un caso sin puntaje, A lanza `KeyError`, y ante un puntaje de texto, `TypeError`; el contrato congelado decía que debía lanzar `ValueError("puntaje inválido")`. Con el fixture común (que incluye «dato inválido») las dos no son comparables hasta que A cumpla el mismo contrato. Solo entonces tiene sentido comparar longitud y claridad. [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) documenta dos riesgos relacionados: elegir un paradigma por moda, por falta de criterios explícitos, y que la comparación favorezca al paradigma conocido porque las reglas son simples y no ejercitan lo propio de otros (se incluye una regla que dependa de otra o de estado).

## Errores y confusiones comunes

- **Comparar por líneas o *tokens*.** Premia omitir casos.
- **Juzgar equivalencia por parecido.** Solo la ejecución común lo establece.
- **Normalizar diferencias de decisión.** Solo se normalizan las de presentación.
- **Casos solo felices.** Sin límite ni error, la equivalencia es aparente.

## Límites y cuándo no aplica

Una matriz organiza el juicio, no sustituye un prototipo ni datos de mantenimiento ([SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md)). La equivalencia total es difícil en la práctica: los paradigmas expresan ciertos casos con dificultad o no los expresan, y esa imposibilidad es información, no un defecto del método. Para decisiones de estilo puro, donde ambas versiones ya son equivalentes y probadas, la comparación sintáctica es legítima.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Dominio](../d/dominio.md), [Límite](../l/limite.md), [Resultado](../r/resultado.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Costo cognitivo y operativo](../c/costo-cognitivo-y-operativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-082 — Selección y combinación responsable de paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Semántica](./semantica.md) · [Semánticas de entrega →](./semanticas-de-entrega.md)
