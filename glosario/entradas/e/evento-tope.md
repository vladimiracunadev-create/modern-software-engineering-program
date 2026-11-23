# Evento tope

[↑ Glosario](../../README.md) · [← Evento tardío](./evento-tardio.md) · [Evento, productor y manejador →](./evento-productor-y-manejador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

El suceso no deseado que un árbol de fallos descompone.

Definición de trabajo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

## Por qué importa

En [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), el tema «FTA» importa porque recorre un evento tope hacia abajo y revela combinaciones.

## Cómo funciona

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

El análisis por árbol de fallos parte de un evento tope («horno sobrecalentado sin corte») y lo descompone con puertas Y y O hasta eventos básicos. Un **corte mínimo** es un conjunto mínimo de eventos básicos cuya ocurrencia conjunta produce el tope. En el laboratorio, el tope exige que falle el control (sensor en lectura baja, fallo del software o triac en cortocircuito) y a la vez la protección (relé soldado, sensor del limitador o lógica del limitador): nueve cortes de orden dos, con una probabilidad anual exacta de 2,07 × 10⁻⁵ frente a 2,08 × 10⁻⁵ por la aproximación de suceso raro (la suma de los productos de cada corte). El número de cortes de orden uno, que no necesitan ningún otro fallo, es lo primero que se mira.

Según [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md):

No siempre. Hace falta hacer la que responde la pregunta que importa: si el riesgo es del sistema y no de un componente, STPA o HARA; si hay un evento tope cuantificable, FTA; si hay una lista de componentes y se quiere saber cómo se detectan, FMEA. Lo que no se admite es usar una sola y declarar que cubre todo.

## Ejemplo

Ejemplo de [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) (sección «Preguntas frecuentes»):

No siempre. Hace falta hacer la que responde la pregunta que importa: si el riesgo es del sistema y no de un componente, STPA o HARA; si hay un evento tope cuantificable, FTA; si hay una lista de componentes y se quiere saber cómo se detectan, FMEA. Lo que no se admite es usar una sola y declarar que cubre todo.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El análisis por árbol de fallos parte de un evento tope («horno sobrecalentado sin corte») y lo descompone con puertas Y y O hasta eventos básicos. ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md))
- Hace falta hacer la que responde la pregunta que importa: si el riesgo es del sistema y no de un componente, STPA o HARA; si hay un evento tope cuantificable, FTA; si hay una lista de componentes y se quiere saber cómo se detectan, FMEA. ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](../a/arbol.md), [Acción de control no segura](../a/accion-de-control-no-segura.md), [Causa común](../c/causa-comun.md), [Corte mínimo](../c/corte-minimo.md), [Peligro](../p/peligro.md), [Riesgo](../r/riesgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Evento tardío](./evento-tardio.md) · [Evento, productor y manejador →](./evento-productor-y-manejador.md)
