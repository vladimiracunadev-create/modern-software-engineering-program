# Atributos de calidad

[↑ Glosario](../../README.md) · [← Atributo](./atributo.md) · [AUC →](./auc.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Propiedades del sistema, distintas de su función, como rendimiento, fiabilidad, seguridad o mantenibilidad.

Definición de trabajo de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).

## Por qué importa

En [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), el tema «Atributos de calidad» importa porque nombran las dimensiones de la calidad (rendimiento, fiabilidad, seguridad) que el cliente suele pedir con una palabra.

## Cómo funciona

Según [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), en la sección «Atributos de calidad»:

Un atributo de calidad es una propiedad del sistema que importa más allá de lo que hace: cuán rápido, cuán seguro, cuán fácil de cambiar. ISO/IEC 25010 ofrece un vocabulario común (rendimiento, fiabilidad, seguridad, usabilidad, mantenibilidad, portabilidad y otros), útil como lista de preguntas para no olvidar dimensiones. No decide por sí misma cuáles importan: una plataforma de entregas de tareas que se usa dos veces al día no necesita el mismo nivel de disponibilidad que un servicio de emergencias.

## Ejemplo

Caso medido en la sección «Atributos de calidad» de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md):

Un atributo de calidad es una propiedad del sistema que importa más allá de lo que hace: cuán rápido, cuán seguro, cuán fácil de cambiar. ISO/IEC 25010 ofrece un vocabulario común (rendimiento, fiabilidad, seguridad, usabilidad, mantenibilidad, portabilidad y otros), útil como lista de preguntas para no olvidar dimensiones. No decide por sí misma cuáles importan: una plataforma de entregas de tareas que se usa dos veces al día no necesita el mismo nivel de disponibilidad que un servicio de emergencias.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son:

- **El tablero está verde y la gente se queja** — causa: el objetivo usa la media y la cola concentra el daño. Corrección: fijar percentil y fracción de peticiones, y vigilar la cola.
- **Se cumple el 99,9 % anual con un mes catastrófico** — causa: la ventana anual diluye una caída larga. Corrección: declarar la ventana (mensual) o añadir un tope de caída continua.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): los dos primeros con salidas idénticas y el tercero con tiempos propios de cada equipo. No se midió ningún sistema real, la cola lenta y los incidentes son supuestos y el costo de PBKDF2 corresponde a una corrida. La siguiente clase cuenta los requisitos desde la perspectiva de quien los usa: casos de uso, historias y job stories.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Propiedad](../p/propiedad.md), [Rendimiento](../r/rendimiento.md), [Seguridad](../s/seguridad.md), [Compromisos entre atributos](../c/compromisos-entre-atributos.md), [Escenario de calidad](../e/escenario-de-calidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto; autoridad: ISO e IEC.
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos, percentiles y ventanas; autoridad: Google.
- [Google SRE: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — relación entre disponibilidad, riesgo y costo; autoridad: Google.
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — parámetros recomendados para almacenar contraseñas; autoridad: OWASP.
- [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) — requisitos de autenticación y almacenamiento de secretos memorizados; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Atributo](./atributo.md) · [AUC →](./auc.md)
