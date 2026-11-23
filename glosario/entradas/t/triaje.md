# Triaje

[↑ Glosario](../../README.md) · [← Triage y contención](./triage-y-contencion.md) · [Triaje por riesgo →](./triaje-por-riesgo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Primera revisión de un reporte para decidir si es válido, reproducirlo y asignarle prioridad.

Definición de trabajo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md): Clasificación provisional de un uso para decidir qué análisis exige.

## Por qué importa

En [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), el tema «Dimensionar el triaje» importa porque el tiempo de respuesta es un requisito con capacidad.

## Cómo funciona

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

**Cómo leer la figura.** El eje horizontal son las personas de triaje y el vertical las horas hasta el primer acuse; cada línea es un percentil. Mira que las tres caen mucho de una a dos personas y casi se aplanan de dos a tres: el límite pasa a ser el horario, no la cola. **Dónde deja de valer:** las llegadas de Poisson, la proporción de inválidos y los tiempos de trabajo son del autor. Un acuse automático inmediato elimina la columna sin añadir personas, y una guardia fuera de horario reduce los percentiles altos.

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

El equipo publica `/.well-known/security.txt` con un `Contact` a un buzón con dos responsables y suplentes y un `Expires` a un año vista, y una política con alcance, reglas para quien prueba y plazos: acuse en 24 horas hábiles automáticamente y de una persona en 48, evaluación en 5 días hábiles, corrección o mitigación de las críticas en 14 días y de las altas en 30, y divulgación coordinada a los 90 días o antes si hay parche. El triaje usa un formulario con el vector CVSS, el contexto (datos expuestos, alcance desde internet) y la evidencia de explotación de los propios registros; la prioridad la fija una regla escrita (explotado y alcanzable, grave y alcanzable, el resto).

## Ejemplo

Ejemplo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) (sección «Ejemplo profesional»):

El equipo publica `/.well-known/security.txt` con un `Contact` a un buzón con dos responsables y suplentes y un `Expires` a un año vista, y una política con alcance, reglas para quien prueba y plazos: acuse en 24 horas hábiles automáticamente y de una persona en 48, evaluación en 5 días hábiles, corrección o mitigación de las críticas en 14 días y de las altas en 30, y divulgación coordinada a los 90 días o antes si hay parche.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md)) son:

- **Un reporte se publica sin respuesta** — causa: canal sin responsable ni plazo. Corrección: `security.txt`, buzón con suplentes y acuse automático.
- **Se discute el puntaje en vez del riesgo** — causa: CVSS tratado como medida. Corrección: vector a la vista, puntaje ambiental y evidencia de explotación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un programa sin recompensas pero con una política clara, un canal que responde y un agradecimiento público recibe reportes de buena fe; una recompensa económica atrae más volumen y exige más capacidad de triaje. ([SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis](../a/analisis.md), [Revisión](../r/revision.md), [Alto riesgo](../a/alto-riesgo.md), [CVSS](../c/cvss.md), [Divulgación coordinada](../d/divulgacion-coordinada.md), [Explotación conocida](../e/explotacion-conocida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [FIRST: CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document) — fórmula y métricas; autoridad: FIRST.
- [CISA: catálogo KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — vulnerabilidades explotadas conocidas; autoridad: CISA.
- [FIRST: EPSS](https://www.first.org/epss/) — probabilidad de explotación; autoridad: FIRST.
- [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116) — archivo `security.txt`; autoridad: IETF.
- [CERT/CC: divulgación coordinada](https://vuls.cert.org/confluence/display/CVD) — guía del proceso; autoridad: CERT/CC.

---

[↑ Glosario](../../README.md) · [← Triage y contención](./triage-y-contencion.md) · [Triaje por riesgo →](./triaje-por-riesgo.md)
