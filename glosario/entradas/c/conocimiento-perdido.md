# Conocimiento perdido

[↑ Glosario](../../README.md) · [← Conjunto curado](./conjunto-curado.md) · [Conocimiento tácito y supuestos →](./conocimiento-tacito-y-supuestos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Información sobre un sistema que ya no está documentada ni disponible en las personas que lo conocieron.

Definición de trabajo de [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md).

## Por qué importa

La clase donde se define, [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), existe con este propósito: el taller existe para que practiques lo que ocurre cuando la documentación no se escribió o ya no se encuentra: recuperar qué hizo el sistema, cuándo cambió y por qué, a partir de lo que sobrevive en el historial y en las personas, y declarar con honestidad qué es evidencia, qué es inferencia y qué es hipótesis.

## Cómo funciona

[SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md):

El equipo de la plataforma aplica el taller al valor `TIMEOUT = 30`. Localiza el commit con `git log -S`, observa que su mensaje es «fix» y que cambió también un archivo de exportación, deduce que el cambio coincidió con la incorporación de la exportación a la secretaría y formula la hipótesis de que se amplió porque tardaba más de 10 segundos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md)) son:

- **La reconstrucción cuenta una historia coherente y nadie puede comprobarla** — causa: mezcla observación, inferencia e hipótesis. Corrección: clasificar cada afirmación y citar su fuente.
- **La búsqueda por mensaje no encuentra el cambio** — causa: el mensaje no dice qué cambió. Corrección: buscar por contenido y por archivo, y seguir los renombrados.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún repositorio real ni se entrevistó a nadie: la autoría concentrada, la proporción de mensajes genéricos y la fiabilidad de las fuentes son supuestos del autor, y la búsqueda por contenido se probó con un cambio de una línea.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [ADR retrospectivo](../a/adr-retrospectivo.md), [Búsqueda por contenido](../b/busqueda-por-contenido.md), [Factor de camión](../f/factor-de-camion.md), [Independencia de fuentes](../i/independencia-de-fuentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

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

[↑ Glosario](../../README.md) · [← Conjunto curado](./conjunto-curado.md) · [Conocimiento tácito y supuestos →](./conocimiento-tacito-y-supuestos.md)
