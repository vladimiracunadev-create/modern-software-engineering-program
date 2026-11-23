# RPN

[↑ Glosario](../../README.md) · [← Rotación declarada](./rotacion-declarada.md) · [RPO (objetivo de punto de recuperación) →](./rpo-objetivo-de-punto-de-recuperacion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Producto de las valoraciones de gravedad, ocurrencia y detección de un modo de fallo.

Definición de trabajo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

## Por qué importa

La clase donde se define, [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), existe con este propósito: la clase existe para que distingas tres cosas que en un proyecto suelen mezclarse: un **peligro** (una condición del sistema que puede llevar a daño), un **riesgo** (la combinación estimada de gravedad y probabilidad de ese daño) y una **medida de control** (algo que baja uno de los dos y que se puede verificar).

## Cómo funciona

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

El análisis de modos de fallo y efectos recorre cada componente, enumera cómo puede fallar, qué efecto tiene y cómo se detectaría. La práctica clásica multiplica tres valoraciones de 1 a 10 (gravedad, ocurrencia, detección) y llama al producto *número de prioridad de riesgo* (RPN). En el laboratorio, el relé del limitador soldado tiene gravedad 10, la máxima, y queda en el cuarto puesto por RPN (160); la deriva de calibración, de gravedad 8, queda primera (280). Además, las 1000 combinaciones posibles de las tres valoraciones producen solo 120 valores distintos de RPN y 24 combinaciones comparten el mismo número, con gravedades desde 2 hasta 10: dos modos de fallo con el mismo RPN pueden ser uno trivial y otro letal.

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

El equipo del *Horno de curado* hace un análisis de peligros antes de un piloto de tres meses en un laboratorio. El árbol de fallos muestra una probabilidad de sobretemperatura aceptable y el FMEA tiene pocas filas con RPN alto. Al repasar el árbol con el técnico que calibra los equipos aparece algo que nadie había escrito: el mismo técnico ajusta, el mismo día y con el mismo patrón, el sensor del lazo y el del limitador. El equipo añade el evento «calibración compartida», recalcula y la probabilidad del tope sube de golpe. La decisión no es cambiar el árbol, es cambiar el proceso: calibrar con patrones distintos y registrar quién y cuándo, y añadir al requisito del limitador un sensor de otro principio de medición.

## Ejemplo

Ejemplo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) (sección «Ejemplo profesional»):

El equipo del *Horno de curado* hace un análisis de peligros antes de un piloto de tres meses en un laboratorio. El árbol de fallos muestra una probabilidad de sobretemperatura aceptable y el FMEA tiene pocas filas con RPN alto. Al repasar el árbol con el técnico que calibra los equipos aparece algo que nadie había escrito: el mismo técnico ajusta, el mismo día y con el mismo patrón, el sensor del lazo y el del limitador. El equipo añade el evento «calibración compartida», recalcula y la probabilidad del tope sube de golpe.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Además, las 1000 combinaciones posibles de las tres valoraciones producen solo 120 valores distintos de RPN y 24 combinaciones comparten el mismo número, con gravedades desde 2 hasta 10: dos modos de fallo con el mismo RPN pueden ser uno trivial y otro letal. ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modo de fallo](../m/modo-de-fallo.md), [Gravedad](../g/gravedad.md), [Producto](../p/producto.md), [Acción de control no segura](../a/accion-de-control-no-segura.md), [Causa común](../c/causa-comun.md), [Corte mínimo](../c/corte-minimo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Rotación declarada](./rotacion-declarada.md) · [RPO (objetivo de punto de recuperación) →](./rpo-objetivo-de-punto-de-recuperacion.md)
