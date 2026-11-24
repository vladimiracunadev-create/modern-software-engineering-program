# Recuperación

[↑ Glosario](../../README.md) · [← Recuperabilidad](./recuperabilidad.md) · [Recurrencias y umbral práctico →](./recurrencias-y-umbral-practico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

**Recuperación** tiene cuatro sentidos en el programa. En [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) (IA asistida) es la búsqueda que devuelve fragmentos de un índice relevantes para una consulta. En [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) (Git) es traer de vuelta lo que parece perdido. En [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) (releases) es el conjunto de simulacros de pérdida de una versión publicada (retroceso, y otros). En [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) (ML) es la vuelta a un estado sano verificado con la métrica. Esta entrada desarrolla sobre todo el sentido de Git y de release, y señala los otros.

## Por qué importa

Lo que no se ensaya no se sabe que funciona ([SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md)). Y recuperar es posible solo dentro de una frontera: saber qué sigue en la base y qué se perdió determina qué comando sirve. Cambia la política de respaldo y de publicación: se decide de antemano qué se puede recuperar y se practica.

## Cómo funciona

**Git ([SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)).** Git solo puede recuperar lo que entró en su base de objetos. Un commit que dejó de ser alcanzable sigue ahí hasta que el **reflog** expira y se poda; se encuentra con `git reflog`. Un archivo agregado al índice crea un blob que `git fsck --lost-found` puede hallar. En cambio, un cambio que **nunca se agregó** y un archivo sin rastrear **no tienen copia**. La política de recuperación empieza por esa frontera: lo que se quiere poder recuperar debe entrar en la base (commit o al menos `git add`). La distinción de fondo es entre «existe» y «es alcanzable».

**Release ([SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md)).** Cuatro simulacros examinan cuatro formas de perder algo. El **retroceso** es la más frecuente: la versión nueva tiene un defecto y se quiere la anterior. El verificador, para evitar que un atacante sirva versiones viejas, rechaza una secuencia menor; por tanto el retroceso **no es reinstalar el bundle antiguo**, sino publicar el contenido anterior como una versión nueva (por ejemplo, 1.4.2 con una secuencia mayor que la defectuosa). Los otros simulacros cubren la pérdida de claves y de otros elementos del canal.

**Recuperación (retrieval) en IA ([SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md)).** El sistema recupera fragmentos de un índice (por ejemplo con BM25 y fragmentos de 200 palabras con filtro de versión vigente) para dárselos como contexto a un asistente. **ML ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md)).** La recuperación es volver a un modelo o estado sano y comprobarlo con la métrica.

## Ejemplo

Tras un `git reset --hard HEAD~3`, tres commits dejan de estar en la rama. `git reflog` los lista; se crea una rama en el commit deseado y vuelve el trabajo. En cambio, un archivo nuevo que nunca se añadió con `git add` y se borró con `git clean` no tiene copia en Git. (Comportamiento estándar de Git, tal como lo describe [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).)

## Errores y confusiones comunes

- **Creer que Git guarda todo**: solo lo que entró en su base de objetos.
- **Reinstalar el paquete antiguo para retroceder**: el verificador lo rechaza; hay que publicar el contenido anterior como versión nueva.
- **No ensayar la recuperación.**
- **Confundir los cuatro sentidos.**

## Límites y cuándo no aplica

El reflog es local y expira; no protege a otras personas ni a clones. Un procedimiento de recuperación solo vale si se ensayó. En ML, la vuelta a un estado sano exige que haya una versión anterior verificada y una métrica clara para decidir.

## Relación con otros conceptos

- **Prerrequisito:** [Índice](../i/indice.md).
- **Ver también:** [Estado](../e/estado.md), [Fragmento](../f/fragmento.md), [Métrica](../m/metrica.md), [Bisección](../b/biseccion.md), [Caducidad de la evidencia](../c/caducidad-de-la-evidencia.md), [Commit atómico](../c/commit-atomico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (460 clases más lo mencionan; las que más):

[SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Pro Git: Maintenance and Data Recovery](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery) — recuperación y poda; autoridad: Pro Git.
- [The Update Framework](https://theupdateframework.io/specification/) — roles de claves, secuencia, caducidad y recuperación; autoridad: proyecto TUF, CNCF.
- [Lewis et al., «Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks»](https://arxiv.org/abs/2005.11401) — generación con recuperación de memoria externa; autoridad: NeurIPS 2020.
- [Anthropic: effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — el contexto como recurso finito y la recuperación justo a tiempo; autoridad: Anthropic.
- [git-bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria y `bisect run`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Recuperabilidad](./recuperabilidad.md) · [Recurrencias y umbral práctico →](./recurrencias-y-umbral-practico.md)
