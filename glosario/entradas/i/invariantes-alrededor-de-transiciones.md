# Invariantes alrededor de transiciones

[↑ Glosario](../../README.md) · [← Invariante del flujo](./invariante-del-flujo.md) · [Invariantes y pruebas de propiedades →](./invariantes-y-pruebas-de-propiedades.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

**Invariantes alrededor de transiciones** es la disciplina que [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md) propone para programar con estado mutable: **no se trata de prohibir la mutación, sino de acotarla**. Una *transición* es un cambio de estado; una *invariante* es una condición que debe cumplirse antes y después de cada transición (por ejemplo, «la prioridad nunca es negativa» o «la autorización se preserva»). Antes de la transición se comprueban las **precondiciones**; después deben sostenerse las invariantes. Lo que no puede ocurrir es que un estado intermedio inválido sea observable.

## Por qué importa

El estado mutable es la fuente de muchos errores porque cualquier parte del programa puede dejarlo en una condición inesperada. La respuesta no es la inmutabilidad total (a menudo impracticable) sino concentrar los cambios en puntos bien definidos y verificables. La decisión que cambia es cómo se razona sobre un programa: en lugar de seguir cada asignación, se razona por transiciones completas, cada una con su contrato. [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md) señala la condición: una función que **deja un estado intermedio observable rompe el razonamiento, incluso si luego intenta repararlo**.

## Cómo funciona

El patrón tiene tres partes:

1. **Precondiciones:** lo que debe ser cierto para que la transición tenga sentido (el caso existe, está abierto, el valor es válido). Si no se cumplen, se rechaza sin tocar el estado.
2. **Cambio:** la modificación del estado, idealmente en un único lugar.
3. **Postcondiciones e invariantes:** lo que debe seguir siendo cierto al terminar.

Para que la transición sea indivisible desde fuera, se aplica una técnica sencilla: **calcular sobre una copia y confirmar al final**. Si algo falla en medio, el estado original no cambió. La clase documenta dos síntomas de no hacerlo: un rechazo que deja el puntaje distinto del inicial porque se mutó antes de decidir el resultado (se calcula sobre una copia y se confirma al final), y una copia «aislada» que cambia cuando se modifica la original porque la copia es superficial y comparte listas o diccionarios internos (se copia en profundidad solo lo mutable o se usan estructuras inmutables).

## Ejemplo

Una operación que aplica una penalización al puntaje de un caso, con la regla «el puntaje nunca es negativo» y «una operación rechazada no cambia nada»:

```python
def penalizar(caso, puntos):
    if puntos < 0 or not caso["abierto"]:           # precondiciones
        raise ValueError("penalización inválida")
    nuevo = dict(caso)                               # copia: no se toca el original
    nuevo["puntaje"] = max(0, caso["puntaje"] - puntos)
    assert nuevo["puntaje"] >= 0                     # invariante
    caso.update(nuevo)                               # confirmar al final
```

Si `puntos` fuera inválido, se rechaza antes de mutar nada. Un estado intermedio (puntaje ya restado pero sin verificar) nunca queda visible para otro código.

## Errores y confusiones comunes

- **Mutar antes de decidir.** Un rechazo deja el estado a medio cambiar.
- **Copia superficial.** La copia comparte objetos internos con la original.
- **Reparar después.** Un estado inválido que se corrige al final fue observable en medio.
- **Confundir invariantes con validación de entrada.** La validación revisa datos de afuera; la invariante describe el estado interno siempre.

## Límites y cuándo no aplica

La ejecución secuencial no explica por sí sola la concurrencia, la persistencia ni la consistencia distribuida ([SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md)): con varios hilos, un estado intermedio observable es posible aunque cada transición parezca indivisible, y se necesitan cerrojos o estructuras inmutables. La clase siguiente reduce la superficie mutable con procedimientos de contratos estrechos. En scripts breves, formalizar precondiciones e invariantes puede ser más peso que valor.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Mutación](../m/mutacion.md), [Asignación, aliasing y mutación](../a/asignacion-aliasing-y-mutacion.md), [Comandos, expresiones y secuencia](../c/comandos-expresiones-y-secuencia.md), [Estado como memoria de la ejecución](../e/estado-como-memoria-de-la-ejecucion.md), [Estado local, compartido y persistente](../e/estado-local-compartido-y-persistente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Invariante del flujo](./invariante-del-flujo.md) · [Invariantes y pruebas de propiedades →](./invariantes-y-pruebas-de-propiedades.md)
