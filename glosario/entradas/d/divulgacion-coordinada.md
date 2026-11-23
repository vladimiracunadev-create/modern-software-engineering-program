# Divulgación coordinada

[↑ Glosario](../../README.md) · [← Divide y vencerás](./divide-y-venceras.md) · [DMA →](./dma.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Proceso en que quien reporta, quien corrige y, si procede, terceros afectados acuerdan cuándo y cómo se hará pública una vulnerabilidad.

Definición de trabajo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md).

## Por qué importa

En [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), el tema «Divulgación coordinada» importa porque un plazo claro protege a quien reporta y a quien usa el sistema.

## Cómo funciona

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

La **divulgación coordinada** acuerda con quien reporta cuándo se hará público el hallazgo. Los plazos varían: Project Zero publica sus detalles a los 90 días del aviso con independencia de que haya parche (y el texto vigente anuncia un cambio a una política «Full 60» desde febrero de 2027), y el CERT/CC publica una guía con las variantes. Un plazo corto protege a las personas usuarias frente a una vulnerabilidad conocida por pocos pero no corregida; uno largo da tiempo para corregir y para que la mayoría actualice. Hay que decidir además qué se comunica y a quién (aviso a las personas afectadas, identificador CVE si procede, nota técnica) y registrar el caso: qué falló, qué prueba lo habría detectado y qué caso de abuso se añade.

Según [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md):

El equipo publica `/.well-known/security.txt` con un `Contact` a un buzón con dos responsables y suplentes y un `Expires` a un año vista, y una política con alcance, reglas para quien prueba y plazos: acuse en 24 horas hábiles automáticamente y de una persona en 48, evaluación en 5 días hábiles, corrección o mitigación de las críticas en 14 días y de las altas en 30, y divulgación coordinada a los 90 días o antes si hay parche. El triaje usa un formulario con el vector CVSS, el contexto (datos expuestos, alcance desde internet) y la evidencia de explotación de los propios registros; la prioridad la fija una regla escrita (explotado y alcanzable, grave y alcanzable, el resto).

## Ejemplo

Ejemplo de [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) (sección «Ejemplo profesional»):

El equipo publica `/.well-known/security.txt` con un `Contact` a un buzón con dos responsables y suplentes y un `Expires` a un año vista, y una política con alcance, reglas para quien prueba y plazos: acuse en 24 horas hábiles automáticamente y de una persona en 48, evaluación en 5 días hábiles, corrección o mitigación de las críticas en 14 días y de las altas en 30, y divulgación coordinada a los 90 días o antes si hay parche.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md)) son:

- **Un reporte se publica sin respuesta** — causa: canal sin responsable ni plazo. Corrección: `security.txt`, buzón con suplentes y acuse automático.
- **Se discute el puntaje en vez del riesgo** — causa: CVSS tratado como medida. Corrección: vector a la vista, puntaje ambiental y evidencia de explotación.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se reportó ninguna vulnerabilidad real ni se usaron datos de EPSS o KEV; los vectores de los analistas, la población de 3 000 vulnerabilidades con su relación débil entre gravedad y explotación y las llegadas del triaje son construcciones del autor, y la clase no da asesoría legal.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Vulnerabilidad](../v/vulnerabilidad.md), [CVSS](../c/cvss.md), [Explotación conocida](../e/explotacion-conocida.md), [Triaje](../t/triaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-465 — Vulnerabilidades, divulgación y respuesta](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CERT/CC: divulgación coordinada](https://vuls.cert.org/confluence/display/CVD) — guía del proceso; autoridad: CERT/CC.
- [FIRST: CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document) — fórmula y métricas; autoridad: FIRST.
- [CISA: catálogo KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — vulnerabilidades explotadas conocidas; autoridad: CISA.
- [FIRST: EPSS](https://www.first.org/epss/) — probabilidad de explotación; autoridad: FIRST.
- [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116) — archivo `security.txt`; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Divide y vencerás](./divide-y-venceras.md) · [DMA →](./dma.md)
