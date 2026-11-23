# Riesgo arquitectónico

[↑ Glosario](../../README.md) · [← Riesgo aceptado](./riesgo-aceptado.md) · [Riesgo de cola →](./riesgo-de-cola.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Decisión que, con los escenarios dados, puede producir problemas.

Definición de trabajo de [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md).

## Por qué importa

La clase donde se define, [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), existe con este propósito: el taller existe para que revises una arquitectura completa contra escenarios con un modelo ejecutable, para que sepas cuánto se puede fiar de esa revisión según quién la haga y para que distingas los parámetros que de verdad deciden un veredicto de los que solo parecen importar.

## Cómo funciona

[SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md):

El equipo convoca la revisión con tres perfiles (rendimiento, operaciones, evolución del negocio) y pide a cada uno cinco escenarios fuera de su zona. Ejecuta el modelo sobre la propuesta en servicios: seis fallas, cuatro con raíz en archivos y antivirus. Propone tres variantes (monolito modular, monolito con archivos asíncronos y una tercera con más instancias) y las evalúa contra los mismos escenarios. La segunda cumple el pico (120 peticiones por segundo de capacidad) y arregla E02 y E09; deja E04, E08, E10 y E12.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md)) son:

- **La revisión termina en «parece bien»** — causa: no hay escenarios ni veredictos. Corrección: evaluar un conjunto de escenarios con un modelo ejecutable.
- **Se descubren fallas al construir** — causa: los revisores compartían especialidad. Corrección: exigir perfiles distintos y escenarios fuera de la zona propia.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres análisis con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna arquitectura real ni se observó a ningún revisor: el modelo, sus parámetros y los pesos de sesgo son construcciones del autor. La siguiente clase integra todo en un dossier de arquitectura defendible y verificable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario](../e/escenario.md), [Problemas](../p/problemas.md), [Árbol de utilidad](../a/arbol-de-utilidad.md), [Compromiso](../c/compromiso.md), [Modelo ejecutable de arquitectura](../m/modelo-ejecutable-de-arquitectura.md), [Punto de sensibilidad](../p/punto-de-sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

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

[↑ Glosario](../../README.md) · [← Riesgo aceptado](./riesgo-aceptado.md) · [Riesgo de cola →](./riesgo-de-cola.md)
