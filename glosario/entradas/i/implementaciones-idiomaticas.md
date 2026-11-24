# Implementaciones idiomáticas

[↑ Glosario](../../README.md) · [← Impacto habilitado](./impacto-habilitado.md) · [Implicación →](./implicacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Una **implementación idiomática** es una solución escrita con los mecanismos propios del paradigma o del lenguaje en que se expresa, no una traducción línea por línea de otra. En el taller de [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md), donde la misma regla de negocio se implementa en cinco paradigmas, el principio es: **equivalencia no exige traducir línea por línea**. Lo que debe ser igual es el comportamiento observable (el fixture compartido); lo que debe ser distinto es la forma en que cada modelo lo logra. «Idiomático» significa «a la manera natural de ese modelo».

## Por qué importa

Si se traduce mecánicamente una solución a otro paradigma, el resultado conserva la forma del original y pierde las ventajas del nuevo: un código funcional escrito con bucles y variables mutables, una clase que solo envuelve una función. La comparación entonces mide la traducción, no el paradigma. La decisión que cambia es cómo se escribe cada candidato en una comparación: cada uno como lo escribiría alguien que domina ese modelo, siempre bajo el mismo contrato de comportamiento.

## Cómo funciona

[SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) enumera el mecanismo propio de cada versión:

- **Transición explícita** (estilo imperativo): una secuencia de pasos que cambia el estado, con precondiciones y postcondiciones.
- **Objeto que protege invariantes** (orientado a objetos): el estado y las operaciones juntos, con el objeto responsable de rechazar transiciones inválidas.
- **Composición de valores** (funcional): funciones puras que transforman datos y se combinan.
- **Tabla de reglas** (declarativo): las reglas como datos que un intérprete evalúa.
- **Evento correlacionado** (reactivo): hechos que llegan en el tiempo y se relacionan para producir una conclusión.

Hay una restricción: ninguna versión puede **inventar una política distinta para lucir mejor**. Si una implementación cambia lo que decide (por ejemplo, resuelve un empate de otra forma porque su modelo lo hace natural), ya no compite en las mismas condiciones. El fixture semántico común es el árbitro: todas deben producir los mismos resultados para los mismos casos, y un caso que un modelo no puede expresar es un hallazgo, no un motivo para cambiarlo.

## Ejemplo

La regla «aprobar si el puntaje supera el umbral y hay autorización» se escribe de dos formas idiomáticas:

```python
# funcional: composición de valores
def decidir(caso, umbral):
    return "aprobar" if caso["autorizado"] and caso["puntaje"] > umbral else "rechazar"

# declarativo: tabla de reglas
REGLAS = [(lambda c: not c["autorizado"], "rechazar"),
          (lambda c: c["puntaje"] > UMBRAL, "aprobar")]
def decidir_tabla(caso):
    return next((r for cond, r in REGLAS if cond(caso)), "rechazar")
```

Ambas pasan el mismo fixture. La versión con tabla expone el orden de las reglas como dato; la funcional lo deja en una expresión. Ninguna es una transcripción de la otra.

## Errores y confusiones comunes

- **Traducir línea por línea.** El resultado conserva la forma del paradigma original.
- **Cambiar la política para encajar en el modelo.** La comparación deja de ser válida.
- **Tomar «idiomático» como sinónimo de «conciso».** Se trata de usar bien el mecanismo propio.
- **Defectos que sobreviven a las pruebas.** Si falta el caso que ejercita una regla, un defecto plantado sobrevive; se añade el caso mínimo y se comprueba que el mutante falla ([SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)).

## Límites y cuándo no aplica

El taller compara un cambio y una carga pequeña, y no demuestra mantenibilidad a largo plazo ([SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)). Lo «idiomático» depende de la comunidad y del lenguaje y puede ser discutible; no hay una autoridad única. Y en un equipo con experiencia desigual, la solución más idiomática puede no ser la más mantenible para quienes la leerán.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Cambio dirigido](../c/cambio-dirigido.md), [Fixture semántico común](../f/fixture-semantico-comun.md), [Retrospectiva basada en evidencia](../r/retrospectiva-basada-en-evidencia.md), [Trazas comparables](../t/trazas-comparables.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-083 — Taller: una regla de negocio en cinco paradigmas](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Impacto habilitado](./impacto-habilitado.md) · [Implicación →](./implicacion.md)
