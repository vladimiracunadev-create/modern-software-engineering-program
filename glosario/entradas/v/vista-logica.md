# Vista lógica

[↑ Glosario](../../README.md) · [← Vista de ejecución](./vista-de-ejecucion.md) · [VLAN →](./vlan.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

La **vista lógica** es la vista arquitectónica que muestra módulos o componentes y las dependencias *permitidas* entre ellos ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md)). Responde a la pregunta «¿qué puedo cambiar sin romper a quién?» y gobierna la modificabilidad.

## Por qué importa

Un diagrama de módulos suele leerse como una descripción del sistema, pero describe una intención. La decisión que cambia es cómo se trata ese diagrama: como una regla que se verifica contra el código y las trazas, no como un dibujo que se acepta.

## Cómo funciona

[SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) señala el defecto característico de la vista lógica: **declara lo permitido, no lo que ocurre**. Con el tiempo, el código acumula dependencias que nadie dibujó: un módulo importa algo de otro por comodidad, y el diagrama sigue mostrando las flechas originales. La vista deja de ser un mapa fiel y pasa a ser una ilusión de orden.

La corrección es tratarla como una regla comprobable: comparar con las dependencias reales del código (un comprobador de importaciones) o con las trazas de ejecución en cada cambio. Hay dos señales de desajuste:

- Una **dependencia real no dibujada**: el código la usa y el diagrama no la permite (violación).
- Una **arista declarada que nunca se usa**: o el diagrama está viejo o hay código muerto.

Se relaciona con el monolito modular, que impone justo esta clase de regla con un comprobador, y con la vista de ejecución, que muestra la otra cara: lo que realmente se llama y en qué orden. La clase subraya que son vistas distintas y que mezclarlas produce diagramas que no responden bien a ninguna pregunta.

## Ejemplo

La vista lógica dice que Avisos puede depender de Entregas pero no de Calificaciones. Un comprobador recorre las importaciones y detecta que Avisos importa una función interna de Calificaciones, una arista que nadie dibujó. La integración falla hasta que se corrige. Aplicación del principio de [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md).

## Errores y confusiones comunes

- **El código tiene dependencias que nadie dibujó**: la vista lógica declara lo permitido y no se verifica; se corrige comparando con trazas o con el código en cada cambio.
- **Tomar el diagrama como descripción de la realidad**.
- **Mezclarla con la vista de ejecución** en un solo dibujo.
- **Ignorar las aristas declaradas pero no usadas**.

## Límites y cuándo no aplica

La vista lógica solo dice qué dependencias están permitidas, no cuánto se usan ni cuándo: para latencia y capacidad hace falta la vista de ejecución. Su valor depende de verificarla; sin comprobación automática, tiende a desactualizarse. En sistemas muy pequeños, mantenerla formalmente puede costar más de lo que aporta.

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
