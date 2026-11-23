# Recuperación

[↑ Glosario](../../README.md) · [← Recuperabilidad](./recuperabilidad.md) · [Recurrencias y umbral práctico →](./recurrencias-y-umbral-practico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Búsqueda que devuelve fragmentos de un índice relevantes para una consulta.

Definición de trabajo de [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md): Vuelta a un estado sano verificado con la métrica.

## Por qué importa

En [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), el tema «Recuperación» importa porque distingue lo que sigue en la base de lo que se perdió y qué comando lo trae de vuelta.

En [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), el tema «Recuperación» importa porque lo que no se ensaya no se sabe que funciona.

## Cómo funciona

Según [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), en la sección «Recuperación»:

Git solo puede recuperar lo que entró en su base de objetos. Un commit que dejó de ser alcanzable sigue ahí hasta que el reflog expira y se poda, y se encuentra con `git reflog`. Un archivo agregado al índice crea un blob que `git fsck --lost-found` puede hallar. Un cambio que nunca se agregó y un archivo sin rastrear no tienen copia. La política de recuperación empieza por esa frontera: lo confirmado se recupera, lo agregado a veces, lo demás no.

Según [SE-480 — Proyecto: release firmado y recuperable](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md), en la sección «Recuperación»:

Los cuatro simulacros examinan cuatro formas de perder algo. El **retroceso** es la más frecuente: la versión nueva tiene un defecto y se quiere la anterior. El verificador, para evitar que un atacante sirva versiones viejas, rechaza una secuencia menor; por tanto el retroceso no es reinstalar el bundle antiguo, sino publicar el contenido anterior como una versión nueva (aquí, 1.4.2 con secuencia 16) que supera la memoria del cliente. La **pérdida del repositorio** se resuelve porque el build es reproducible: la fuente reconstruye la misma huella y el manifiesto firmado sigue siendo válido. La **rotación** funciona si la declaración de la clave nueva se firmó con la vigente antes de necesitarla.

## Ejemplo

Ejemplo de [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo diseña el contexto para tres tareas. Para «explicar la regla de redondeo» no recupera nada: aporta la función entera y la sección de decisiones fechada, y exige que la respuesta cite líneas. Para «¿qué decidimos sobre las notas ausentes?» recupera por BM25 con fragmentos de 200 palabras y filtro de versión vigente; la respuesta debe incluir la fecha de la decisión. Para «convenciones de estilo» usa un archivo versionado con dueño, no la memoria de la herramienta. Fija una caducidad de 30 días para las notas guardadas por el asistente y una revisión mensual del archivo de convenciones.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La recuperación acierta en pruebas y falla en uso** — causa: las pruebas usan consultas con clave única. Corrección: probar con paráfrasis y preguntas reales. ([SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **pérdida de la clave privada sin rotación previa** no tiene solución automática: los clientes con la clave antigua fijada rechazan toda versión nueva, y la recuperación exige distribuir una clave nueva por un canal que los clientes ya acepten, con una acción humana. ([SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md))

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
