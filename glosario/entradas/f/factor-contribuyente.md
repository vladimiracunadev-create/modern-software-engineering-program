# Factor contribuyente

[↑ Glosario](../../README.md) · [← Factor causal](./factor-causal.md) · [Factor de autobús →](./factor-de-autobus.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Condición que, de haber sido distinta, habría evitado o reducido el incidente.

Definición de trabajo de [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md).

## Por qué importa

En [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), el tema «Factores contribuyentes» importa porque una causa única esconde las que convergen.

## Cómo funciona

Según [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md):

Se construye un grafo de 12 factores contribuyentes a un incidente de certificado vencido y de despliegue sin verificación (cada factor tiene de cero a dos causas). Se simulan 400 analistas que recorren el grafo eligiendo una causa al azar en cada paso hasta llegar a una raíz, y 2 000 grupos de cuatro analistas que juntan sus factores.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo escribe el postmortem del incidente del certificado con esta estructura. Resumen: entregas rechazadas durante 47 minutos por un certificado vencido. Impacto: 1 240 entregas rechazadas, 12 % de las peticiones en la franja, 4 instituciones afectadas, 31 % del presupuesto de error de 28 días. Línea de tiempo con horas: 14:02 vence el certificado, 14:09 salta la alerta de consumo, 14:21 se identifica la causa, 14:49 se instala el certificado nuevo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md)) son:

- **El postmortem culpa a una persona** — causa: análisis detenido en «error humano». Corrección: preguntar por qué la acción tenía sentido y qué lo facilitó.
- **El incidente se repite** — causa: acciones sin propietario, fecha o verificación. Corrección: acciones verificables y seguimiento semanal.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se construye un grafo de 12 factores contribuyentes a un incidente de certificado vencido y de despliegue sin verificación (cada factor tiene de cero a dos causas). ([SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Incidente](../i/incidente.md).
- **Ver también:** [Condición](../c/condicion.md), [Acción correctiva verificable](../a/accion-correctiva-verificable.md), [Postmortem](../p/postmortem.md), [Postmortem sin culpa](../p/postmortem-sin-culpa.md), [Sesgo de retrospectiva](../s/sesgo-de-retrospectiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md).

**Aparece en los casos de estudio:** [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Factores contribuyentes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — práctica sin culpa; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) — adopción y errores comunes; autoridad: Google, SRE Workbook.
- [Cook, «How Complex Systems Fail»](https://how.complexsystems.fail/) — múltiples causas contribuyentes; autoridad: texto del autor, Richard I. Cook.
- [Fischhoff, «Hindsight ≠ foresight»](https://doi.org/10.1037/0096-1523.1.3.288) — sesgo de retrospectiva; autoridad: Journal of Experimental Psychology, 1975.
- [Dekker, «The Field Guide to Understanding “Human Error”»](https://openlibrary.org/isbn/9781472439055) — ISBN 978-1-4724-3905-5; autoridad: libro, CRC Press, 2014.

---

[↑ Glosario](../../README.md) · [← Factor causal](./factor-causal.md) · [Factor de autobús →](./factor-de-autobus.md)
