# Atributos de calidad

[↑ Glosario](../../README.md) · [← Atributo](./atributo.md) · [AUC →](./auc.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Los **atributos de calidad** son propiedades del sistema, distintas de su función, como rendimiento, fiabilidad, seguridad, usabilidad o mantenibilidad ([SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md)). Describen cuán rápido, cuán seguro o cuán fácil de cambiar es el sistema, más allá de lo que hace. También se llaman requisitos no funcionales, aunque ese nombre hace pensar que son secundarios.

## Por qué importa

El cliente suele pedirlos con una palabra («rápido», «seguro») y esa palabra no es un requisito: no se puede construir ni probar. Cambia lo que se pregunta en la elicitación: no solo qué debe hacer el sistema sino cuánto, con qué fiabilidad y a qué costo. Y cambia la arquitectura, porque la mayoría de las decisiones estructurales responden a atributos de calidad.

## Cómo funciona

[SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) usa ISO/IEC 25010 como vocabulario común (rendimiento, fiabilidad, seguridad, usabilidad, mantenibilidad, portabilidad y otros). Su utilidad es de **lista de preguntas**: ayuda a no olvidar dimensiones. No decide por sí misma cuáles importan: una plataforma de entregas de tareas que se usa dos veces al día no necesita el mismo nivel de disponibilidad que un servicio de emergencias.

El paso de la palabra al requisito es convertirla en un **escenario de calidad verificable**: un estímulo, un contexto y una medida. «La recuperación es rápida» se vuelve «tras un fallo del servidor, el 95 % de las entradas se recupera en menos de 30 segundos». Dos precauciones de la clase: la media oculta la cola donde se concentra el daño (se fija un percentil y una fracción de peticiones), y una ventana anual diluye una caída larga (se declara la ventana mensual o un tope de caída continua).

Además los atributos **compiten** entre sí (compromisos entre atributos): mejorar uno suele costar otro, y la especificación debe mostrar con cuál compite y quién decide cuál cede.

## Ejemplo

El cliente pide «que sea seguro y rápido». Con el vocabulario de calidad, el equipo pregunta: ¿seguro frente a qué amenazas?, ¿rápido para qué operación y con qué percentil? Resultado: dos escenarios, «el 95 % de las subidas de menos de 10 MB termina en menos de 3 segundos» y «tras cinco intentos de acceso fallidos se bloquea la cuenta durante un tiempo». Ahora hay algo que probar y, además, se ve el roce entre ellos. (Ilustración del método de [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md).)

## Errores y confusiones comunes

- **Tablero verde y gente quejándose**: el objetivo usa la media y la cola concentra el daño.
- **99,9 % anual con un mes catastrófico**: la ventana anual diluye una caída larga.
- **Tratar la lista de ISO 25010 como obligatoria**: es una guía de preguntas.
- **Especificar un atributo sin medida.**

## Límites y cuándo no aplica

La clase usa datos sintéticos y no midió un sistema real. Algunos atributos son difíciles de medir antes de construir (mantenibilidad), y se aproximan con indicadores indirectos. La taxonomía puede variar entre normas; lo que importa es que cada atributo relevante tenga una medida y un decisor.

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
