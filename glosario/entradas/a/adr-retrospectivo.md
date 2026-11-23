# ADR retrospectivo

[↑ Glosario](../../README.md) · [← ADR](./adr.md) · [Affordance percibida →](./affordance-percibida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Registro de una decisión escrito después de tomarla, que declara su fecha de escritura y distingue lo observado de lo inferido.

Definición de trabajo de [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md).

## Por qué importa

La clase donde se define, [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), existe con este propósito: el taller existe para que practiques lo que ocurre cuando la documentación no se escribió o ya no se encuentra: recuperar qué hizo el sistema, cuándo cambió y por qué, a partir de lo que sobrevive en el historial y en las personas, y declarar con honestidad qué es evidencia, qué es inferencia y qué es hipótesis.

## Cómo funciona

Según [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md):

El equipo de la plataforma aplica el taller al valor `TIMEOUT = 30`. Localiza el commit con `git log -S`, observa que su mensaje es «fix» y que cambió también un archivo de exportación, deduce que el cambio coincidió con la incorporación de la exportación a la secretaría y formula la hipótesis de que se amplió porque tardaba más de 10 segundos. Busca una incidencia de esa fecha, encuentra una conversación en la que la persona que lo cambió menciona un cierre de semestre, y la cita como segunda fuente, independiente del commit. Escribe un ADR retrospectivo que separa «observado», «inferido» e «hipótesis», fija una condición de revisión y se lo muestra a quien opera la exportación.

Según [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md):

Clasificando cada afirmación, citando su fuente y escribiendo qué la confirmaría o la descartaría. Un ADR retrospectivo debe poder leerse sin confundir lo que se vio con lo que se supone.

## Ejemplo

Ejemplo de [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma aplica el taller al valor `TIMEOUT = 30`. Localiza el commit con `git log -S`, observa que su mensaje es «fix» y que cambió también un archivo de exportación, deduce que el cambio coincidió con la incorporación de la exportación a la secretaría y formula la hipótesis de que se amplió porque tardaba más de 10 segundos. Busca una incidencia de esa fecha, encuentra una conversación en la que la persona que lo cambió menciona un cierre de semestre, y la cita como segunda fuente, independiente del commit.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md)) son:

- **La reconstrucción cuenta una historia coherente y nadie puede comprobarla** — causa: mezcla observación, inferencia e hipótesis. Corrección: clasificar cada afirmación y citar su fuente.
- **La búsqueda por mensaje no encuentra el cambio** — causa: el mensaje no dice qué cambió. Corrección: buscar por contenido y por archivo, y seguir los renombrados.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un ADR retrospectivo debe poder leerse sin confundir lo que se vio con lo que se supone. ([SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md))
- Traslada el taller a otro dominio (por ejemplo, un valor de tarifa de espera en un servicio de reparto): cambian el repositorio y las fuentes, se conservan la búsqueda por contenido, la clasificación de afirmaciones, el análisis de independencia y el ADR retrospectivo. ([SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Búsqueda por contenido](../b/busqueda-por-contenido.md), [Conocimiento perdido](../c/conocimiento-perdido.md), [Factor de camión](../f/factor-de-camion.md), [Independencia de fuentes](../i/independencia-de-fuentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Avelino et al., «A novel approach for estimating Truck Factors» (ICPC, 2016)](https://doi.org/10.1109/ICPC.2016.7503718) — estimación del factor de camión a partir de la autoría; autoridad: IEEE/ACM ICPC.
- [Rigby et al., «Quantifying and mitigating turnover-induced knowledge loss» (ICSE, 2016)](https://doi.org/10.1145/2884781.2884851) — pérdida de conocimiento por rotación; autoridad: ACM/IEEE ICSE.
- [Git: `git log`](https://git-scm.com/docs/git-log) — opciones `-S` y `--grep`; autoridad: documentación de Git.
- [Git: `git blame`](https://git-scm.com/docs/git-blame) — atribución de líneas al último cambio; autoridad: documentación de Git.
- [Git: `git fast-import`](https://git-scm.com/docs/git-fast-import) — creación de historiales sintéticos; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← ADR](./adr.md) · [Affordance percibida →](./affordance-percibida.md)
