# Trazas comparables

[↑ Glosario](../../README.md) · [← Trazabilidad bidireccional](./trazabilidad-bidireccional.md) · [Tres capacidades →](./tres-capacidades.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Las **trazas comparables** son, en el taller de [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md), registros del razonamiento de un programa que tienen **la misma forma en todas las implementaciones** y por eso pueden contrastarse: se registra la **entrada normalizada, las reglas consideradas, la decisión, el error y los efectos**. Una traza responde a «¿cómo llegó el programa a este resultado?»; que sea *comparable* significa que las cinco versiones de la regla (en cinco paradigmas) la producen con el mismo esquema, aunque la calculen de maneras distintas.

## Por qué importa

Dos implementaciones pueden devolver el mismo resultado final por razones distintas, o coincidir **por accidente**. Si solo se compara la salida, esas coincidencias parecen equivalencias. [SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md) lo dice: **comparar solo el resultado final oculta por qué dos programas coinciden por accidente**. La decisión que cambia es qué se compara: el resultado y el camino. Con trazas comparables, una divergencia aparece en la regla exacta donde las implementaciones empiezan a diferir, en lugar de solo en el resultado, donde puede ya ser tarde para entenderla.

## Cómo funciona

El diseño de una traza útil tiene condiciones:

- **Contenido definido:** la **entrada normalizada** (cómo se interpretó), las **reglas consideradas** (cuáles se evaluaron y con qué resultado), la **decisión**, el **error** si lo hubo y los **efectos** (qué se escribió, qué se envió).
- **Estable:** el mismo caso produce la misma traza; sin marcas de tiempo variables, identificadores aleatorios ni orden no determinista.
- **Sin detalles internos irrelevantes:** no debe revelar cómo está implementado cada paradigma (nombres de clases, estructuras internas), porque eso impediría compararlas y acoplaría la prueba a la implementación.

Las trazas dan valor en dos usos. En la **comparación**, se ejecutan los mismos casos del fixture en cada versión y se comparan las trazas campo a campo. En el **diagnóstico**, una traza permite disputar una decisión incorrecta: qué reglas se consideraron y por qué ganó una. Esto conecta con el requisito del motor de reglas del programa: quién puede producir una decisión, qué estado observa, cómo falla y qué rastro permite disputarla.

## Ejemplo

Una traza con la misma forma en todas las versiones (ilustración):

```json
{
  "entrada": {"id": "c-17", "monto": 1500, "autorizado": true},
  "reglas": [
    {"regla": "autorizacion", "resultado": "ok"},
    {"regla": "umbral_monto", "resultado": "supera"}
  ],
  "decision": "revisar",
  "error": null,
  "efectos": []
}
```

Si la versión de objetos produce `"reglas"` en otro orden o la versión funcional omite `umbral_monto` porque la evalúa de forma perezosa, la comparación lo muestra, aunque ambas lleguen a `"revisar"`. Dos fallos documentados en la clase se descubren con este instrumento: las pruebas pasan pero un defecto plantado sobrevive (falta el caso que ejercita esa regla), y dos versiones divergen solo con ciertos tipos (el contrato no definía los inválidos).

## Errores y confusiones comunes

- **Comparar solo el resultado final.** Oculta coincidencias accidentales.
- **Trazas inestables.** Marcas de tiempo o identificadores aleatorios hacen imposible compararlas.
- **Trazas que filtran la implementación.** Acoplan la comparación a detalles internos.
- **Omitir los efectos.** Dos versiones pueden decidir igual y actuar distinto.

## Límites y cuándo no aplica

El taller compara un cambio y una carga pequeña; no demuestra mantenibilidad a largo plazo ([SE-083](../../../classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)). Registrar trazas tiene costo (tiempo, espacio y posible exposición de datos); en producción deben revisarse por privacidad. Para reglas triviales de un solo paso, la traza es redundante con la decisión. Y las trazas muestran qué pasó, no si la regla era la correcta: eso lo da el fixture con resultados esperados.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Efecto](../e/efecto.md), [Regla](../r/regla.md), [Cambio dirigido](../c/cambio-dirigido.md), [Fixture semántico común](../f/fixture-semantico-comun.md), [Implementaciones idiomáticas](../i/implementaciones-idiomaticas.md), [Retrospectiva basada en evidencia](../r/retrospectiva-basada-en-evidencia.md).
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

[↑ Glosario](../../README.md) · [← Trazabilidad bidireccional](./trazabilidad-bidireccional.md) · [Tres capacidades →](./tres-capacidades.md)
