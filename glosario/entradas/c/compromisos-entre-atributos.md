# Compromisos entre atributos

[↑ Glosario](../../README.md) · [← Compromiso probabilístico](./compromiso-probabilistico.md) · [Compuerta →](./compuerta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Relaciones en las que mejorar un atributo cuesta otro.

Definición de trabajo de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).

## Por qué importa

En [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), el tema «Compromisos entre atributos» importa porque mejorar uno suele costar otro; decidirlo a tiempo evita descubrirlo en producción.

## Cómo funciona

Según [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), en la sección «Compromisos entre atributos»:

Casi todo atributo cuesta otro. Una derivación de contraseña más costosa protege mejor frente a un ataque de fuerza bruta y hace más lento cada acceso legítimo. Más réplicas aumentan la disponibilidad y el costo de consistencia. Un requisito de calidad aislado es una promesa sin precio; la especificación debe mostrar con qué otro atributo compite y quién decide cuál cede. Descubrir el choque en la redacción cuesta una conversación; descubrirlo en producción cuesta un incidente.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md):

Tres escenarios de calidad del requisito conductor, escritos de forma verificable:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son:

- **El tablero está verde y la gente se queja** — causa: el objetivo usa la media y la cola concentra el daño. Corrección: fijar percentil y fracción de peticiones, y vigilar la cola.
- **Se cumple el 99,9 % anual con un mes catastrófico** — causa: la ventana anual diluye una caída larga. Corrección: declarar la ventana (mensual) o añadir un tope de caída continua.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): los dos primeros con salidas idénticas y el tercero con tiempos propios de cada equipo. No se midió ningún sistema real, la cola lenta y los incidentes son supuestos y el costo de PBKDF2 corresponde a una corrida. La siguiente clase cuenta los requisitos desde la perspectiva de quien los usa: casos de uso, historias y job stories.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Relación](../r/relacion.md), [Atributos de calidad](../a/atributos-de-calidad.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Medidas y ventanas](../m/medidas-y-ventanas.md), [Restricciones](../r/restricciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-147 — Atributos de calidad y restricciones](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

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

[↑ Glosario](../../README.md) · [← Compromiso probabilístico](./compromiso-probabilistico.md) · [Compuerta →](./compuerta.md)
