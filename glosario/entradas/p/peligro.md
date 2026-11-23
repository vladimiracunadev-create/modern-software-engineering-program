# Peligro

[↑ Glosario](../../README.md) · [← PDU](./pdu.md) · [Peor caso →](./peor-caso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Condición o estado del sistema que, con ciertas circunstancias, puede llevar a daño.

Definición de trabajo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

## Por qué importa

En [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), el tema «Peligro, riesgo y control» importa porque fija el vocabulario con el que se discute qué es aceptable.

## Cómo funciona

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

Un peligro es una condición o un estado: «calentador conectado con la puerta abierta». Un riesgo añade cuánto daño y con qué frecuencia: «una quemadura grave, una vez cada cien mil usos, si el operador no reacciona». Un control es lo que cambia uno de los dos factores y se puede verificar: «el contacto de la puerta corta la potencia por hardware». Confundirlos produce documentos donde el control aparece como si fuera el peligro («falta un limitador») o donde el riesgo se declara aceptable sin decir quién lo acepta ni con qué supuestos. La disciplina mínima es escribir cada peligro con su contexto operativo (en qué fase de uso, con qué usuario, con qué entorno) y cada control con su método de verificación.

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

El equipo del *Horno de curado* hace un análisis de peligros antes de un piloto de tres meses en un laboratorio. El árbol de fallos muestra una probabilidad de sobretemperatura aceptable y el FMEA tiene pocas filas con RPN alto. Al repasar el árbol con el técnico que calibra los equipos aparece algo que nadie había escrito: el mismo técnico ajusta, el mismo día y con el mismo patrón, el sensor del lazo y el del limitador. El equipo añade el evento «calibración compartida», recalcula y la probabilidad del tope sube de golpe. La decisión no es cambiar el árbol, es cambiar el proceso: calibrar con patrones distintos y registrar quién y cuándo, y añadir al requisito del limitador un sensor de otro principio de medición.

## Ejemplo

Ejemplo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) (sección «Ejemplo profesional»):

El equipo del *Horno de curado* hace un análisis de peligros antes de un piloto de tres meses en un laboratorio. El árbol de fallos muestra una probabilidad de sobretemperatura aceptable y el FMEA tiene pocas filas con RPN alto. Al repasar el árbol con el técnico que calibra los equipos aparece algo que nadie había escrito: el mismo técnico ajusta, el mismo día y con el mismo patrón, el sensor del lazo y el del limitador. El equipo añade el evento «calibración compartida», recalcula y la probabilidad del tope sube de golpe.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Confundirlos produce documentos donde el control aparece como si fuera el peligro («falta un limitador») o donde el riesgo se declara aceptable sin decir quién lo acepta ni con qué supuestos. ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md))
- Escribe tres peligros con contexto, construye un árbol de fallos de uno de ellos y busca al menos una causa común. ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Daño](../d/dano.md), [Estado](../e/estado.md), [Acción de control no segura](../a/accion-de-control-no-segura.md), [Causa común](../c/causa-comun.md), [Corte mínimo](../c/corte-minimo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← PDU](./pdu.md) · [Peor caso →](./peor-caso.md)
