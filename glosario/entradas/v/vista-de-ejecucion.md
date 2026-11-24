# Vista de ejecución

[↑ Glosario](../../README.md) · [← Vista arquitectónica](./vista-arquitectonica.md) · [Vista lógica →](./vista-logica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

La **vista de ejecución** (también de procesos) es la vista arquitectónica que muestra qué se llama en tiempo de ejecución, en qué orden, de forma síncrona o asíncrona y con qué concurrencia ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md)). Responde a la pregunta «¿qué pasa cuando llega esta petición?» y gobierna la latencia y la capacidad.

## Por qué importa

Un sistema con módulos bien separados puede ser lento por la forma en que sus partes se llaman en ejecución. La decisión que cambia es dónde se busca el origen de la latencia: no en el diagrama de módulos, sino en la cadena de llamadas, sus esperas y su solapamiento.

## Cómo funciona

[SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) explica lo que la vista permite ver. Una petición que atraviesa ocho servicios en **serie** suma ocho latencias y hereda la cola de cada una. En **paralelo**, solo espera a la más lenta. La clase cita a Dean y Barroso para el efecto de fondo: cuando una petición depende de muchas llamadas, la probabilidad de tocar una lenta crece rápidamente, aunque cada servicio sea rápido casi siempre; es la razón por la que la cola de la distribución importa más que la mediana.

La vista complementa a otras. La **vista lógica** muestra módulos y dependencias permitidas (modificabilidad); la de ejecución muestra lo que realmente sucede (latencia y capacidad). La clase enseña que mezclar módulos, procesos y servidores en un solo diagrama produce un dibujo que no responde las preguntas de operaciones; la corrección es separar las vistas y decir qué pregunta responde cada una. Y para comprobar que la vista lógica coincide con la realidad, se compara con **trazas** de ejecución o con el código en cada cambio.

## Ejemplo

Una petición de «ver mis entregas» llama en serie a autenticación, entregas, calificaciones y avisos. La vista de ejecución muestra que las latencias se suman y que la cola de cada servicio se hereda. Llamar a calificaciones y avisos en paralelo reduce el tiempo total a la más lenta de las dos. Escenario de [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md).

## Errores y confusiones comunes

- **El diagrama no responde las preguntas de operaciones**: mezcla módulos, procesos y servidores; se corrige separando vistas.
- **Creer que «paralelizar siempre» es la lección**: la figura muestra qué se suma y qué se solapa.
- **Mirar solo la mediana de cada servicio**.
- **Dibujarla sin trazas reales**: refleja intenciones, no ejecución.

## Límites y cuándo no aplica

La vista muestra la estructura de las llamadas, no su costo exacto: para eso hay que medir. Paralelizar añade complejidad y consumo; no siempre compensa. Y un diagrama de ejecución envejece rápido si el sistema cambia; debe comprobarse contra trazas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Concurrencia](../c/concurrencia.md), [Vista](./vista.md), [Radio de explosión](../r/radio-de-explosion.md), [Traza](../t/traza.md), [Vista arquitectónica](./vista-arquitectonica.md), [Vista lógica](./vista-logica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kruchten, «The 4+1 View Model of Architecture» (IEEE Software, 1995)](https://doi.org/10.1109/52.469759) — vistas lógica, de procesos, de desarrollo y física; autoridad: IEEE Software.
- [Rozanski y Woods, «Viewpoints and Perspectives»](https://www.viewpoints-and-perspectives.info/) — puntos de vista y perspectivas arquitectónicas; autoridad: autores del libro.
- [C4 model](https://c4model.com/) — niveles de diagramas de arquitectura; autoridad: Simon Brown.
- [Dean y Barroso, «The Tail at Scale» (CACM, 2013)](https://doi.org/10.1145/2408776.2408794) — latencia extrema en sistemas de muchas llamadas; autoridad: Communications of the ACM.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Vista arquitectónica](./vista-arquitectonica.md) · [Vista lógica →](./vista-logica.md)
