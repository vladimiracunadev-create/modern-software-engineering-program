# Medidas y ventanas

[↑ Glosario](../../README.md) · [← Medida de la respuesta](./medida-de-la-respuesta.md) · [Memoización →](./memoizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Estadístico, población y periodo sobre los que se evalúa el cumplimiento de un escenario.

Definición de trabajo de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).

## Por qué importa

En [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), el tema «Medidas y ventanas» importa porque un objetivo sin estadístico ni ventana admite veredictos opuestos.

## Cómo funciona

Según [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), en la sección «Medidas y ventanas»:

Una medida sin estadístico es ambigua porque distribuciones distintas dan resúmenes distintos: la media esconde la cola, el máximo depende de una sola petición, el percentil 99 de una muestra pequeña es inestable. Una medida sin ventana es igual de ambigua: 99,9 % «de disponibilidad» puede ser mensual, trimestral o anual, y cada ventana tolera una caída continua diferente. Escribe siempre el estadístico, la población sobre la que se calcula (¿todas las peticiones o solo las exitosas?), la ventana y el método de medición.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md):

Tres escenarios de calidad del requisito conductor, escritos de forma verificable:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son:

- **El tablero está verde y la gente se queja** — causa: el objetivo usa la media y la cola concentra el daño. Corrección: fijar percentil y fracción de peticiones, y vigilar la cola.
- **Se cumple el 99,9 % anual con un mes catastrófico** — causa: la ventana anual diluye una caída larga. Corrección: declarar la ventana (mensual) o añadir un tope de caída continua.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): los dos primeros con salidas idénticas y el tercero con tiempos propios de cada equipo. No se midió ningún sistema real, la cola lenta y los incidentes son supuestos y el costo de PBKDF2 corresponde a una corrida. La siguiente clase cuenta los requisitos desde la perspectiva de quien los usa: casos de uso, historias y job stories.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario](../e/escenario.md), [Sobre](../s/sobre.md), [Atributos de calidad](../a/atributos-de-calidad.md), [Compromisos entre atributos](../c/compromisos-entre-atributos.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Restricciones](../r/restricciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

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

[↑ Glosario](../../README.md) · [← Medida de la respuesta](./medida-de-la-respuesta.md) · [Memoización →](./memoizacion.md)
