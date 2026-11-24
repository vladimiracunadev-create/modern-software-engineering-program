# Peligro

[↑ Glosario](../../README.md) · [← PDU](./pdu.md) · [Peor caso →](./peor-caso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Un **peligro** (*hazard*) es una condición o estado del sistema que, con ciertas circunstancias, puede llevar a daño ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md)). Ejemplo de la clase: «calentador conectado con la puerta abierta».

## Por qué importa

Separar peligro, riesgo y control evita documentos donde el control aparece como si fuera el peligro («falta un limitador») o donde el riesgo se declara aceptable sin decir quién lo acepta ni con qué supuestos.

## Cómo funciona

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) fija tres piezas: el **peligro** es una condición; el **riesgo** añade cuánto daño y con qué frecuencia («una quemadura grave, una vez cada cien mil usos, si el operador no reacciona»); el **control** es lo que cambia uno de esos dos factores y se puede verificar («el contacto de la puerta corta la potencia por hardware»). La disciplina mínima es escribir cada peligro con su contexto operativo (fase de uso, usuario, entorno) y cada control con la forma de verificarlo.

## Ejemplo

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md): el equipo del *Horno de curado* analiza peligros antes de un piloto de tres meses. El árbol de fallos muestra una probabilidad de sobretemperatura aceptable. Al repasarlo con el técnico aparece algo no escrito: el mismo técnico calibra, el mismo día y con el mismo patrón, el sensor del lazo y el del limitador. Se añade el evento «calibración compartida» y la probabilidad sube de golpe. La decisión es cambiar el proceso (patrones distintos, registrar quién y cuándo).

## Errores y confusiones comunes

Describir el control como peligro; analizar fallos como independientes cuando comparten causa.

## Límites y cuándo no aplica

El caso es un ejercicio de la clase, no una medición de un equipo real. Un análisis de peligros cubre los que se imaginaron; la búsqueda de causas comunes es lo que reduce el riesgo de no verlos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Daño](../d/dano.md), [Estado](../e/estado.md), [Acción de control no segura](../a/accion-de-control-no-segura.md), [Causa común](../c/causa-comun.md), [Corte mínimo](../c/corte-minimo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← PDU](./pdu.md) · [Peor caso →](./peor-caso.md)
