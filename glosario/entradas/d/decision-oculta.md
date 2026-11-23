# Decisión oculta

[↑ Glosario](../../README.md) · [← Decisión irreversible (de un sentido)](./decision-irreversible-de-un-sentido.md) · [Decisión reversible →](./decision-reversible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Decisión de diseño que un módulo encapsula de modo que su interfaz no la revele.

Definición de trabajo de [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md).

## Por qué importa

La clase donde se define, [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), existe con este propósito: la clase existe para que diseñes un componente pensando desde el principio en tres personas que lo tocarán después: quien lo cambia, quien lo prueba y quien lo opera de madrugada, y para que conviertas esa intención en decisiones concretas (qué esconde cada módulo, qué se inyecta, qué deja rastro) con una medida cada una.

## Cómo funciona

Según [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md):

Seis decisiones de `tarifas` (tarifas, zonas, descuentos, moneda y redondeo, canal de aviso, persistencia), con pesos de cambio supuestos por el autor (0,2; 0,2; 0,3; 0,1; 0,1; 0,1). Dos descomposiciones: por pasos del flujo (leer, calcular, formatear, guardar, avisar), donde cada paso conoce las decisiones que usa, y por decisión oculta (un módulo por decisión más un orquestador que no conoce ninguna). Se cuenta cuántos módulos conocen cada decisión y la media en 1000 cambios sorteados con semilla fija.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md):

El equipo de `tarifas` hace tres cambios de diseño, uno por preocupación. Para el cambio, agrupa en un módulo `moneda` todo lo relativo al redondeo y al formato; los cuatro módulos que redondeaban por su cuenta pasan a pedirle el monto; la próxima petición de cambio solo toca `moneda`. Para la prueba, la regla de recargo recibe el instante y la zona horaria como parámetros y el reloj real solo se llama en el borde; la suite incluye las medianoches de los husos que atiende.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md)) son:

- **Un cambio de redondeo toca cuatro módulos** — causa: la decisión está repartida entre pasos del flujo. Corrección: esconderla en un módulo y hacer que los demás pidan el monto.
- **Una prueba pasa de lunes a viernes y falla el sábado** — causa: depende del reloj real. Corrección: inyectar el instante y probar los bordes de día y de huso.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Dos descomposiciones: por pasos del flujo (leer, calcular, formatear, guardar, avisar), donde cada paso conoce las decisiones que usa, y por decisión oculta (un módulo por decisión más un orquestador que no conoce ninguna). ([SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Módulo](../m/modulo.md), [Determinismo de una prueba](./determinismo-de-una-prueba.md), [Identificador de correlación](../i/identificador-de-correlacion.md), [Inyección de dependencias](../i/inyeccion-de-dependencias.md), [Observabilidad](../o/observabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Parnas (CACM, 1972)](https://doi.org/10.1145/361598.361623) — ocultar decisiones probablemente cambiantes; autoridad: Communications of the ACM.
- [Cockburn, «Hexagonal architecture»](https://alistair.cockburn.us/hexagonal-architecture/) — puertos y adaptadores; autoridad: su autor.
- [W3C, «Trace Context»](https://www.w3.org/TR/trace-context/) — propagación de un identificador de traza; autoridad: W3C.
- [OpenTelemetry: registros](https://opentelemetry.io/docs/concepts/signals/logs/) — registros estructurados correlacionables con trazas; autoridad: proyecto OpenTelemetry.
- [Fowler, «Test Double»](https://martinfowler.com/bliki/TestDouble.html) — dobles de prueba; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Decisión irreversible (de un sentido)](./decision-irreversible-de-un-sentido.md) · [Decisión reversible →](./decision-reversible.md)
