# Determinismo de una prueba

[↑ Glosario](../../README.md) · [← Determinismo](./determinismo.md) · [Determinismo y diff →](./determinismo-y-diff.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Propiedad de dar el mismo resultado con las mismas entradas, sin importar cuándo o dónde se ejecute.

Definición de trabajo de [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md).

## Por qué importa

La clase donde se define, [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), existe con este propósito: la clase existe para que diseñes un componente pensando desde el principio en tres personas que lo tocarán después: quien lo cambia, quien lo prueba y quien lo opera de madrugada, y para que conviertas esa intención en decisiones concretas (qué esconde cada módulo, qué se inyecta, qué deja rastro) con una medida cada una.

## Cómo funciona

[SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md):

El equipo de `tarifas` hace tres cambios de diseño, uno por preocupación. Para el cambio, agrupa en un módulo `moneda` todo lo relativo al redondeo y al formato; los cuatro módulos que redondeaban por su cuenta pasan a pedirle el monto; la próxima petición de cambio solo toca `moneda`. Para la prueba, la regla de recargo recibe el instante y la zona horaria como parámetros y el reloj real solo se llama en el borde; la suite incluye las medianoches de los husos que atiende.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md)) son:

- **Un cambio de redondeo toca cuatro módulos** — causa: la decisión está repartida entre pasos del flujo. Corrección: esconderla en un módulo y hacer que los demás pidan el monto.
- **Una prueba pasa de lunes a viernes y falla el sábado** — causa: depende del reloj real. Corrección: inyectar el instante y probar los bordes de día y de huso.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis y modelos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún reloj real ni ningún sistema de registros real; las matrices de conocimiento, los pesos de cambio, los husos y el modelo de solicitudes son construcciones del autor. La siguiente clase separa la complejidad esencial del problema de la que añade el diseño.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Resultado](../r/resultado.md), [Decisión oculta](./decision-oculta.md), [Identificador de correlación](../i/identificador-de-correlacion.md), [Inyección de dependencias](../i/inyeccion-de-dependencias.md), [Observabilidad](../o/observabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

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

[↑ Glosario](../../README.md) · [← Determinismo](./determinismo.md) · [Determinismo y diff →](./determinismo-y-diff.md)
