# Vista de ejecución

[↑ Glosario](../../README.md) · [← Vista arquitectónica](./vista-arquitectonica.md) · [Vista lógica →](./vista-logica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Vista que muestra qué se llama en tiempo de ejecución, en qué orden y con qué concurrencia.

Definición de trabajo de [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md).

## Por qué importa

En [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), el tema «Vista de ejecución» importa porque gobierna latencia y concurrencia: qué se llama y en qué orden.

## Cómo funciona

Según [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), en la sección «Vista de ejecución»:

La **vista de ejecución** (de procesos o de ejecución) muestra qué se llama en tiempo de ejecución, en qué orden, de forma síncrona o asíncrona, y qué concurrencia hay. Responde a «¿qué pasa cuando llega esta petición?» y gobierna la latencia y la capacidad. En ella se ve que una petición que atraviesa ocho servicios en serie suma ocho latencias y hereda la cola de cada una; en paralelo solo espera a la más lenta. Dean y Barroso explican por qué: cuando una petición depende de muchas llamadas, la probabilidad de tocar una lenta crece rápidamente, aunque cada servicio sea rápido casi siempre.

## Ejemplo

Ejemplo de [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sección «Preguntas frecuentes»):

C4 cubre bien la estructura en niveles de zoom. No sustituye la vista de ejecución con orden y concurrencia ni la de despliegue con la topología real; además, no comprueba por sí mismo que los niveles no se contradigan.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md)) son:

- **El diagrama no responde las preguntas de operaciones** — causa: mezcla módulos, procesos y servidores. Corrección: separar vistas y decir qué pregunta responde cada una.
- **El código tiene dependencias que nadie dibujó** — causa: la vista lógica declara lo permitido y no se verifica. Corrección: comparar con trazas o con el código en cada cambio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La figura no dice «paralelizar siempre»: dice que la vista de ejecución muestra qué se suma y qué se solapa, y que la cola importa más que la mediana. ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md))

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
