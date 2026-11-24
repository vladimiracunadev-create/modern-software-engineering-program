# Compromisos entre atributos

[↑ Glosario](../../README.md) · [← Compromiso probabilístico](./compromiso-probabilistico.md) · [Compuerta →](./compuerta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Los **compromisos entre atributos** (en inglés, *trade-offs*) son las relaciones en las que mejorar un atributo de calidad cuesta otro. Es el sentido de [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md): la calidad no se compra por atributos aislados, porque rendimiento, seguridad, disponibilidad, costo o simplicidad compiten por los mismos recursos y decisiones de diseño.

## Por qué importa

Cambia el momento en que se descubre el choque. [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) lo resume así: descubrirlo al redactar el requisito cuesta una conversación; descubrirlo en producción cuesta un incidente. Un requisito de calidad aislado («que sea muy seguro», «que esté siempre disponible») es una promesa sin precio: quien lo escribe no ha decidido qué está dispuesto a perder para obtenerlo.

## Cómo funciona

[SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) da dos ejemplos del mecanismo. Una derivación de contraseña más costosa protege mejor frente a un ataque de fuerza bruta, pero hace más lento cada acceso legítimo: el mismo trabajo que encarece el ataque encarece el uso. Más réplicas aumentan la disponibilidad, pero también el costo de mantener la consistencia entre ellas. En ambos casos el atributo mejora porque se gasta otro.

La especificación debe, por eso, mostrar con qué otro atributo compite cada requisito y quién decide cuál cede. La forma operativa es escribir cada atributo como escenario verificable (estímulo, medida, umbral) y revisar los escenarios por pares buscando los que tiran en direcciones opuestas. Los umbrales deben fijar percentil y ventana: un objetivo con media oculta una cola lenta que concentra el daño, y una disponibilidad anual del 99,9 % puede cumplirse con un mes catastrófico si la ventana diluye una caída larga; por eso se declara la ventana mensual o se añade un tope de caída continua.

## Ejemplo

En [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), el requisito conductor de la plataforma de entregas se escribe con tres escenarios de calidad verificables. Al ponerlos juntos, el de latencia de la subida y el de seguridad del acceso compiten por presupuesto de tiempo de cada petición; el registro nombra quién decide cuál cede cuando chocan, en lugar de dejar que lo decida el primero que lo implemente.

## Errores y confusiones comunes

- **El tablero está verde y la gente se queja.** El objetivo usa la media y la cola concentra el daño; fijar percentil y fracción de peticiones.
- **Se cumple el 99,9 % anual con un mes catastrófico.** La ventana anual diluye la caída; declarar la ventana.
- **Pedir todos los atributos al máximo.** Es una especificación sin decisión.
- **Creer que un compromiso es un defecto.** Es una propiedad del problema; el defecto es no decidirlo.

## Límites y cuándo no aplica

No todos los atributos compiten en cada sistema: algunos compromisos desaparecen con otra arquitectura o más presupuesto, y el análisis debe distinguir un conflicto real de uno supuesto. Los experimentos de [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) usan datos sintéticos y no midieron un sistema real, de modo que las cifras ilustran el mecanismo y no establecen magnitudes. Y el compromiso lo cierra una decisión de negocio documentada, no el instinto de quien programa.

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
