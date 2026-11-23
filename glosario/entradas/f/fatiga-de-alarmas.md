# Fatiga de alarmas

[↑ Glosario](../../README.md) · [← Fase reversible](./fase-reversible.md) · [Fatiga de alertas →](./fatiga-de-alertas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Reducción de la respuesta a los avisos por exceso de avisos poco útiles.

Definición de trabajo de [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md).

## Por qué importa

La clase donde se define, [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), existe con este propósito: la clase existe para que diseñes un sistema que maneja datos de salud sabiendo que un error de privacidad no se corrige después, que un error de identidad puede mezclar la historia de dos personas y que un exceso de alertas es en sí un riesgo para el paciente.

## Cómo funciona

Según [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md):

Una alarma es una decisión automática de interrumpir a una persona. Cada umbral compra sensibilidad con avisos: si baja, detecta más deterioros y avisa por muchos que no lo son; si sube, avisa poco y deja pasar algunos. La **fatiga de alarmas** es el fenómeno por el cual un exceso de avisos falsos reduce la respuesta a los reales, y se documenta como problema de seguridad del paciente. Las defensas son priorizar por gravedad, exigir persistencia antes de avisar, combinar señales y revisar con el personal qué avisos no sirven. El software de apoyo propone; la decisión clínica es de una persona.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md):

El equipo de la plataforma separa el módulo en tres almacenes: `identidad` (nombre y documento, acceso mínimo, retención larga), `atenciones` (seudónimo, edad, motivo, acceso por rol) y `estudio` (generalizado: tramos de 10 años y 2 dígitos, con una clase mínima de 5 y comprobación de que ninguna clase tenga un único diagnóstico). La fusión de fichas usa tres zonas: sobre 0,95 se fusiona, entre 0,85 y 0,95 va a revisión de una persona de secretaría con las fichas lado a lado, y bajo 0,85 no se une.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md)) son:

- **Un conjunto sin nombre identifica a personas** — causa: cuasi-identificadores sin generalizar. Corrección: medir la unicidad y generalizar hasta una clase mínima declarada.
- **La pertenencia a una clase revela el diagnóstico** — causa: clases homogéneas. Corrección: comprobar la diversidad del atributo sensible y suprimir o agrupar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **fatiga de alarmas** es el fenómeno por el cual un exceso de avisos falsos reduce la respuesta a los reales, y se documenta como problema de seguridad del paciente. ([SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reducción](../r/reduccion.md), [Cuasi-identificador](../c/cuasi-identificador.md), [Fusión errónea](./fusion-erronea.md), [K-anonimato](../k/k-anonimato.md), [Seudonimización](../s/seudonimizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-295 — Salud, datos sensibles y sistemas regulados](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sendelbach y Funk, «Alarm Fatigue» (AACN Advanced Critical Care, 2013)](https://doi.org/10.4037/NCI.0b013e3182a903f9) — fatiga de alarmas como problema de seguridad del paciente; autoridad: AACN Advanced Critical Care.
- [Sweeney, «k-anonymity: a model for protecting privacy» (2002)](https://doi.org/10.1142/S0218488502001648) — definición del k-anonimato; autoridad: International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems.
- [45 CFR § 164.514, desidentificación (eCFR)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514) — métodos de desidentificación de la regla de privacidad de HIPAA; autoridad: Electronic Code of Federal Regulations.
- [HL7, FHIR](https://hl7.org/fhir/) — estándar de intercambio de datos de salud; autoridad: HL7 International.
- [FDA, Software as a Medical Device (SaMD)](https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd) — software con función médica propia; autoridad: U.S. Food and Drug Administration.

---

[↑ Glosario](../../README.md) · [← Fase reversible](./fase-reversible.md) · [Fatiga de alertas →](./fatiga-de-alertas.md)
