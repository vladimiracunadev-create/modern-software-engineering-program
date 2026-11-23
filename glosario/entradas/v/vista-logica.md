# Vista lógica

[↑ Glosario](../../README.md) · [← Vista de ejecución](./vista-de-ejecucion.md) · [VLAN →](./vlan.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Vista que muestra módulos y las dependencias permitidas entre ellos.

Definición de trabajo de [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md).

## Por qué importa

En [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), el tema «Vista lógica» importa porque gobierna la modificabilidad: quién puede depender de quién.

## Cómo funciona

Según [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), en la sección «Vista lógica»:

La **vista lógica** muestra módulos o componentes y las dependencias *permitidas* entre ellos. Responde a «¿qué puedo cambiar sin romper a quién?» y gobierna la modificabilidad. Su defecto característico es que declara lo permitido, no lo que ocurre: con el tiempo, el código acumula dependencias que nadie dibujó. Por eso conviene tratarla como una regla que se verifica contra el código o contra las trazas, no como un dibujo que se acepta. Una arista declarada que nunca se usa es otra señal: o el diagrama está viejo o hay código muerto.

## Ejemplo

Ejemplo de [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sección «Ejemplo mínimo»):

El atajo `web → bd` no estaba en la vista lógica. Registra versión, comando y salida; añade una dependencia declarada que nunca se use y comprueba que aparece en la segunda diferencia.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El código tiene dependencias que nadie dibujó** — causa: la vista lógica declara lo permitido y no se verifica. Corrección: comparar con trazas o con el código en cada cambio. ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **vista lógica** muestra módulos o componentes y las dependencias *permitidas* entre ellos. ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Módulo](../m/modulo.md), [Vista](./vista.md), [Radio de explosión](../r/radio-de-explosion.md), [Traza](../t/traza.md), [Vista arquitectónica](./vista-arquitectonica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

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

[↑ Glosario](../../README.md) · [← Vista de ejecución](./vista-de-ejecucion.md) · [VLAN →](./vlan.md)
