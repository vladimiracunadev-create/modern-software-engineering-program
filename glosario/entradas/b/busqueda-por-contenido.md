# Búsqueda por contenido

[↑ Glosario](../../README.md) · [← Búsqueda lineal y binaria](./busqueda-lineal-y-binaria.md) · [Bypass de administración →](./bypass-de-administracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Consulta al historial de Git que encuentra los commits que cambian el número de apariciones de una cadena.

Definición de trabajo de [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md).

## Por qué importa

La clase donde se define, [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), existe con este propósito: el taller existe para que practiques lo que ocurre cuando la documentación no se escribió o ya no se encuentra: recuperar qué hizo el sistema, cuándo cambió y por qué, a partir de lo que sobrevive en el historial y en las personas, y declarar con honestidad qué es evidencia, qué es inferencia y qué es hipótesis.

## Cómo funciona

Según [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md):

Git guarda cada cambio con autor, fecha y mensaje. La búsqueda por contenido (`git log -S"TIMEOUT = 30"`) encuentra el commit que cambió el número de apariciones de esa cadena, y `git blame` atribuye cada línea actual a su último cambio. Con ellas se responde cuándo y quién. El porqué solo está si el mensaje o una incidencia lo dicen, y en un historial donde la mayoría de mensajes es «fix», casi nunca lo dice. Buscar por mensaje falla por la misma razón: el motivo no está en el texto que se busca. La reconstrucción debe declarar esto como límite.

Según [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md):

Traslada el taller a otro dominio (por ejemplo, un valor de tarifa de espera en un servicio de reparto): cambian el repositorio y las fuentes, se conservan la búsqueda por contenido, la clasificación de afirmaciones, el análisis de independencia y el ADR retrospectivo. La transferencia está lograda cuando puedes explicar qué parte de la reconstrucción depende de Git y cuál sigue valiendo sin él.

## Ejemplo

Ejemplo de [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) (sección «Ejemplo mínimo»):

El fragmento crea un historial de tres commits y localiza el que cambió un valor. Antes de ejecutarlo, predice cuántos commits devuelve la búsqueda por contenido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md)) son:

- **La reconstrucción cuenta una historia coherente y nadie puede comprobarla** — causa: mezcla observación, inferencia e hipótesis. Corrección: clasificar cada afirmación y citar su fuente.
- **La búsqueda por mensaje no encuentra el cambio** — causa: el mensaje no dice qué cambió. Corrección: buscar por contenido y por archivo, y seguir los renombrados.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el cambio es una sola línea en un archivo que casi nunca se toca, el caso favorable a la búsqueda por contenido; si el valor se hubiera movido de archivo, formateado o dividido, la búsqueda necesitaría seguir los renombrados (`--follow` o `-M`) y podría fallar. ([SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md))
- Traslada el taller a otro dominio (por ejemplo, un valor de tarifa de espera en un servicio de reparto): cambian el repositorio y las fuentes, se conservan la búsqueda por contenido, la clasificación de afirmaciones, el análisis de independencia y el ADR retrospectivo. ([SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [ADR retrospectivo](../a/adr-retrospectivo.md), [Conocimiento perdido](../c/conocimiento-perdido.md), [Factor de camión](../f/factor-de-camion.md), [Independencia de fuentes](../i/independencia-de-fuentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-215 — Taller: reconstruir conocimiento perdido](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

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

[↑ Glosario](../../README.md) · [← Búsqueda lineal y binaria](./busqueda-lineal-y-binaria.md) · [Bypass de administración →](./bypass-de-administracion.md)
