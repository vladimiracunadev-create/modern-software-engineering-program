# Árbol de utilidad

[↑ Glosario](../../README.md) · [← Árbol de trabajo](./arbol-de-trabajo.md) · [Árbol, raíz y subárbol →](./arbol-raiz-y-subarbol.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Jerarquía de atributos y escenarios ordenados por importancia y dificultad.

Definición de trabajo de [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md): Jerarquía de atributos de calidad refinada en escenarios priorizados por importancia y dificultad.

## Por qué importa

La clase donde se define, [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), existe con este propósito: el taller existe para que revises una arquitectura completa contra escenarios con un modelo ejecutable, para que sepas cuánto se puede fiar de esa revisión según quién la haga y para que distingas los parámetros que de verdad deciden un veredicto de los que solo parecen importar.

## Cómo funciona

Según [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md):

Un método como ATAM evalúa una arquitectura contra escenarios de calidad en lugar de contra una lista de buenas prácticas. Se presentan los drivers, se genera y prioriza un conjunto de escenarios (un árbol de utilidad), se analiza cómo responde la arquitectura a cada uno y se concluye con tres tipos de hallazgo: **riesgos** (decisiones que pueden causar problemas), **puntos de sensibilidad** (parámetros de los que depende mucho un atributo) y **compromisos** (decisiones que mejoran un atributo a costa de otro). La ventaja es que cada afirmación se apoya en un escenario concreto y se puede discutir y repetir.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md):

El equipo convoca la revisión con tres perfiles (rendimiento, operaciones, evolución del negocio) y pide a cada uno cinco escenarios fuera de su zona. Ejecuta el modelo sobre la propuesta en servicios: seis fallas, cuatro con raíz en archivos y antivirus. Propone tres variantes (monolito modular, monolito con archivos asíncronos y una tercera con más instancias) y las evalúa contra los mismos escenarios. La segunda cumple el pico (120 peticiones por segundo de capacidad) y arregla E02 y E09; deja E04, E08, E10 y E12.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md)) son:

- **La revisión termina en «parece bien»** — causa: no hay escenarios ni veredictos. Corrección: evaluar un conjunto de escenarios con un modelo ejecutable.
- **Se descubren fallas al construir** — causa: los revisores compartían especialidad. Corrección: exigir perfiles distintos y escenarios fuera de la zona propia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se presentan los drivers, se genera y prioriza un conjunto de escenarios (un árbol de utilidad), se analiza cómo responde la arquitectura a cada uno y se concluye con tres tipos de hallazgo: ([SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributos de calidad](./atributos-de-calidad.md), [Atributo](./atributo.md), [Escenario](../e/escenario.md), [Barrido de parámetros](../b/barrido-de-parametros.md), [Compromiso](../c/compromiso.md), [Importancia por contexto](../i/importancia-por-contexto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-347 — Taller: seleccionar un estilo con escenarios de calidad](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

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

[↑ Glosario](../../README.md) · [← Árbol de trabajo](./arbol-de-trabajo.md) · [Árbol, raíz y subárbol →](./arbol-raiz-y-subarbol.md)
