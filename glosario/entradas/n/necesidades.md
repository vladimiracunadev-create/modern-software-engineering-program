# Necesidades

[↑ Glosario](../../README.md) · [← Navegación facetada](./navegacion-facetada.md) · [Negación y mundo cerrado →](./negacion-y-mundo-cerrado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Una **necesidad** es el resultado que una persona busca, expresado desde su perspectiva y sin nombrar la solución («necesito… para…») ([SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md)). Se distingue del requisito, que es una decisión del equipo sobre cómo satisfacerla.

## Por qué importa

Una necesidad bien formulada no menciona la solución y deja abiertas varias respuestas posibles. Cambia el orden del razonamiento: primero se entiende qué busca la persona; después se elige cómo resolverlo. Si el requisito aparece antes que la necesidad, la solución ya fue elegida sin comprobar alternativas.

## Cómo funciona

[SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) cita el Service Manual del gobierno británico, que propone redactar las necesidades como «**necesito / quiero / espero… para…**», con palabras que la persona reconocería, basadas en evidencia y centradas en su problema, no en una solución. Su ejemplo es útil: la necesidad es un **recordatorio**, no un correo ni una carta; el correo y la carta son soluciones posibles.

En la plataforma de entregas: «necesito saber que mi entrega llegó para no repetirla». Admite una confirmación en pantalla, un correo, un recibo descargable o un indicador de estado. Cada una es un requisito posible; la necesidad es una sola. La formulación tiene dos partes: **lo que la persona necesita** (saber que llegó) y **para qué** (no repetirla); el «para qué» es lo que permite juzgar si una solución sirve.

La clase conecta con el resto del descubrimiento: las peticiones se descomponen (observación, inferencia, solución), se agrupan por necesidad (contar necesidades, no peticiones) y se reformulan como problema. La necesidad es la unidad que sobrevive a cambios de solución y por eso es la que se prioriza. La regla práctica es reformular la petición como necesidad antes de proponer opciones, o la reunión discutirá la solución durante una hora sin acordar el problema.

## Ejemplo

Petición: «un correo de confirmación al entregar». Necesidad: «necesito saber que mi entrega llegó para no repetirla». Opciones: confirmación en pantalla con hora, correo, recibo con identificador, estado visible en la lista. Si se descubre que la mayoría entrega desde el móvil con conexión inestable y no revisa el correo, la confirmación en pantalla con recibo guardado sirve mejor que el correo. (Ilustración del enfoque de [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md).)

## Errores y confusiones comunes

- **Discutir la solución sin acordar el problema**: la petición se aceptó como requisito; corrección: reformular como necesidad.
- **Necesidad que contiene la solución** («necesito un botón de…»).
- **Necesidades sin evidencia**: inventadas por el equipo.
- **Confundir necesidad con deseo o con característica.**

## Límites y cuándo no aplica

Las necesidades se infieren y se contrastan; son hipótesis hasta que las personas las reconocen. Algunas necesidades se descubren solo al usar el producto. Con restricciones fijas (una norma que exige una solución concreta), la necesidad deja de ser el punto de partida y el requisito viene dado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Resultado](../r/resultado.md), [Causa y evidencia](../c/causa-y-evidencia.md), [Oportunidades](../o/oportunidades.md), [Problemas](../p/problemas.md), [Síntomas y peticiones](../s/sintomas-y-peticiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-121 — Problemas, síntomas, necesidades y oportunidades](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (86 clases más lo mencionan; las que más):

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md), [Quibi](../../../casos/fallo/quibi.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — marco oficial para investigar necesidades antes y durante el desarrollo; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato de necesidad de usuario y criterios para validarla; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — la discovery empieza reformulando una solución dada como problema por resolver; autoridad: Government Digital Service.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — propone observar el trabajo que la persona intenta hacer antes que sus características demográficas; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — vocabulario para gestionar riesgo de privacidad al recoger datos de personas; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Navegación facetada](./navegacion-facetada.md) · [Negación y mundo cerrado →](./negacion-y-mundo-cerrado.md)
