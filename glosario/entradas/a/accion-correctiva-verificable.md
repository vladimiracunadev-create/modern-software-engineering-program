# Acción correctiva verificable

[↑ Glosario](../../README.md) · [← Acción compensable](./accion-compensable.md) · [Acción de control no segura →](./accion-de-control-no-segura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Cambio con propietario, fecha y criterio que permite comprobar que funciona.

Definición de trabajo de [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md).

## Por qué importa

La clase donde se define, [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), existe con este propósito: la clase existe para que conviertas un incidente en cambios del sistema: que escribas un postmortem que describa lo ocurrido sin buscar a quién culpar, que veas los factores contribuyentes en lugar de una única causa y que fijes acciones con propietario, fecha y criterio de verificación que se cierren de verdad.

## Cómo funciona

[SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo escribe el postmortem del incidente del certificado con esta estructura. Resumen: entregas rechazadas durante 47 minutos por un certificado vencido. Impacto: 1 240 entregas rechazadas, 12 % de las peticiones en la franja, 4 instituciones afectadas, 31 % del presupuesto de error de 28 días. Línea de tiempo con horas: 14:02 vence el certificado, 14:09 salta la alerta de consumo, 14:21 se identifica la causa, 14:49 se instala el certificado nuevo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md)) son:

- **El postmortem culpa a una persona** — causa: análisis detenido en «error humano». Corrección: preguntar por qué la acción tenía sentido y qué lo facilitó.
- **El incidente se repite** — causa: acciones sin propietario, fecha o verificación. Corrección: acciones verificables y seguimiento semanal.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propietario](../p/propietario.md), [Factor contribuyente](../f/factor-contribuyente.md), [Postmortem](../p/postmortem.md), [Postmortem sin culpa](../p/postmortem-sin-culpa.md), [Sesgo de retrospectiva](../s/sesgo-de-retrospectiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — práctica sin culpa; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) — adopción y errores comunes; autoridad: Google, SRE Workbook.
- [Cook, «How Complex Systems Fail»](https://how.complexsystems.fail/) — múltiples causas contribuyentes; autoridad: texto del autor, Richard I. Cook.
- [Fischhoff, «Hindsight ≠ foresight»](https://doi.org/10.1037/0096-1523.1.3.288) — sesgo de retrospectiva; autoridad: Journal of Experimental Psychology, 1975.
- [Dekker, «The Field Guide to Understanding “Human Error”»](https://openlibrary.org/isbn/9781472439055) — ISBN 978-1-4724-3905-5; autoridad: libro, CRC Press, 2014.

---

[↑ Glosario](../../README.md) · [← Acción compensable](./accion-compensable.md) · [Acción de control no segura →](./accion-de-control-no-segura.md)
