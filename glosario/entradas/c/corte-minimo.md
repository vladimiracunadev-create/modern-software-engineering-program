# Corte mínimo

[↑ Glosario](../../README.md) · [← Corte](./corte.md) · [Corte vertical →](./corte-vertical.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Conjunto mínimo de eventos básicos que, juntos, producen el evento tope.

Definición de trabajo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

## Por qué importa

La clase donde se define, [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), existe con este propósito: la clase existe para que distingas tres cosas que en un proyecto suelen mezclarse: un **peligro** (una condición del sistema que puede llevar a daño), un **riesgo** (la combinación estimada de gravedad y probabilidad de ese daño) y una **medida de control** (algo que baja uno de los dos y que se puede verificar).

## Cómo funciona

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

El análisis por árbol de fallos parte de un evento tope («horno sobrecalentado sin corte») y lo descompone con puertas Y y O hasta eventos básicos. Un **corte mínimo** es un conjunto mínimo de eventos básicos cuya ocurrencia conjunta produce el tope. En el laboratorio, el tope exige que falle el control (sensor en lectura baja, fallo del software o triac en cortocircuito) y a la vez la protección (relé soldado, sensor del limitador o lógica del limitador): nueve cortes de orden dos, con una probabilidad anual exacta de 2,07 × 10⁻⁵ frente a 2,08 × 10⁻⁵ por la aproximación de suceso raro (la suma de los productos de cada corte). El número de cortes de orden uno, que no necesitan ningún otro fallo, es lo primero que se mira.

## Ejemplo

Caso medido en la sección «FTA: del evento tope hacia las causas, y los cortes mínimos» de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

El análisis por árbol de fallos parte de un evento tope («horno sobrecalentado sin corte») y lo descompone con puertas Y y O hasta eventos básicos. Un **corte mínimo** es un conjunto mínimo de eventos básicos cuya ocurrencia conjunta produce el tope.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md)) son: Las tasas de fallo, las valoraciones y los parámetros de la planta son del autor, no hay un producto real analizado y el texto de las normas de pago no se reproduce ni se cita. El siguiente paso, `SE-446`, toma el análisis y lo expresa en el marco genérico de la seguridad funcional: niveles de integridad, probabilidad de fallo bajo demanda y arquitecturas redundantes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento tope](../e/evento-tope.md), [Conjunto](./conjunto.md), [Evento](../e/evento.md), [Acción de control no segura](../a/accion-de-control-no-segura.md), [Causa común](./causa-comun.md), [Peligro](../p/peligro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Corte](./corte.md) · [Corte vertical →](./corte-vertical.md)
