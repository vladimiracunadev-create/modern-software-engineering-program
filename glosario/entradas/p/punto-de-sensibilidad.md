# Punto de sensibilidad

[↑ Glosario](../../README.md) · [← Punto de no retorno](./punto-de-no-retorno.md) · [Puntuación de Brier →](./puntuacion-de-brier.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Parámetro cuyo cambio pequeño invierte la decisión o cambia mucho una medida.

Definición de trabajo de [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md): Parámetro del que depende de forma notable un atributo de calidad.
- En [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md): Parámetro cuyo cambio pequeño invierte la decisión.

## Por qué importa

En [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), el tema «Punto de sensibilidad» importa porque señala qué vigilar.

## Cómo funciona

Según [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md):

Para saber cómo depende la decisión del tamaño de la organización se calculó la utilidad de cada candidato con 2 a 30 equipos. Con cliente dominante, la celda gana en todos los tamaños: su utilidad baja de 0,813 con 2 equipos a 0,696 con 30, y sigue por encima del monolito (0,698 y 0,582) y de los microservicios (0,583, que no depende de los equipos porque su coordinación es cero). Sin cliente dominante, el monolito modular gana hasta 25 equipos y los microservicios, desde 26, porque la utilidad del monolito cae con la coordinación (0,807 con 2 equipos, 0,668 con 30) mientras la de los microservicios se mantiene en 0,670.

Según [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md):

Un método como ATAM evalúa una arquitectura contra escenarios de calidad en lugar de contra una lista de buenas prácticas. Se presentan los drivers, se genera y prioriza un conjunto de escenarios (un árbol de utilidad), se analiza cómo responde la arquitectura a cada uno y se concluye con tres tipos de hallazgo: **riesgos** (decisiones que pueden causar problemas), **puntos de sensibilidad** (parámetros de los que depende mucho un atributo) y **compromisos** (decisiones que mejoran un atributo a costa de otro). La ventaja es que cada afirmación se apoya en un escenario concreto y se puede discutir y repetir.

## Ejemplo

Ejemplo de [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sección «Ejemplo profesional»):

El equipo convoca la revisión con tres perfiles (rendimiento, operaciones, evolución del negocio) y pide a cada uno cinco escenarios fuera de su zona. Ejecuta el modelo sobre la propuesta en servicios: seis fallas, cuatro con raíz en archivos y antivirus. Propone tres variantes (monolito modular, monolito con archivos asíncronos y una tercera con más instancias) y las evalúa contra los mismos escenarios. La segunda cumple el pico (120 peticiones por segundo de capacidad) y arregla E02 y E09; deja E04, E08, E10 y E12.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El punto de sensibilidad respecto de los equipos es 26: la regla «separa cuando hay más de unos 25 equipos» sale de este modelo y no de un estudio, y es una cifra que depende de todos los supuestos anteriores. ([SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md))
- **riesgos** (decisiones que pueden causar problemas), **puntos de sensibilidad** (parámetros de los que depende mucho un atributo) y **compromisos** (decisiones que mejoran un atributo a costa de otro). ([SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributos de calidad](../a/atributos-de-calidad.md), [Atributo](../a/atributo.md), [Medida](../m/medida.md), [Parámetro](./parametro.md), [Árbol de utilidad](../a/arbol-de-utilidad.md), [Compromiso](../c/compromiso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — evaluación de arquitectura contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — características de calidad del producto; autoridad: ISO.
- [Kruchten, «The 4+1 View Model of Architecture» (IEEE Software, 1995)](https://doi.org/10.1109/52.469759) — escenarios que unen las vistas; autoridad: IEEE Software.
- [Google SRE, «Embracing Risk»](https://sre.google/sre-book/embracing-risk/) — riesgo aceptable y presupuesto de error; autoridad: Google SRE.
- [Python: `copy`](https://docs.python.org/3/library/copy.html) — copias profundas para la sensibilidad; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Punto de no retorno](./punto-de-no-retorno.md) · [Puntuación de Brier →](./puntuacion-de-brier.md)
