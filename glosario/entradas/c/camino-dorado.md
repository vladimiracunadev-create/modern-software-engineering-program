# Camino dorado

[↑ Glosario](../../README.md) · [← Camino crítico](./camino-critico.md) · [Camino feliz →](./camino-feliz.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Un **camino dorado** (o camino pavimentado) es la forma recomendada, soportada y automatizada de realizar una tarea frecuente, como crear un servicio nuevo, con las guardas ya incorporadas ([SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)). [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) precisa lo que no es: no es obligatorio. Es una vía fácil y respaldada, no una prohibición de salirse.

## Por qué importa

Sin camino dorado, cada equipo debe recordar por su cuenta los límites de recursos, el usuario sin privilegios, la etiqueta de dueño, las sondas de salud y las imágenes con versión fija; olvidar una guarda es solo cuestión de tiempo. La decisión que cambia es dónde se pone la seguridad y la consistencia: no en documentos que alguien debe leer, sino en el camino que la gente ya recorre. [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) lo resume: el camino más fácil debe ser también el correcto.

## Cómo funciona

El mecanismo es económico antes que técnico. Si lo correcto exige más pasos que lo incorrecto, la gente elige lo incorrecto; por eso el camino automatiza lo correcto y baja su costo por debajo de la alternativa manual. Incluye las guardas por defecto, de modo que un servicio creado por el camino nace conforme.

Como no es una obligación, quien tenga una necesidad distinta puede apartarse, asumiendo el costo de mantener lo suyo. Esa salida no se prohíbe; se registra (el programa lo relaciona con la excepción registrada) para que el equipo de plataforma vea qué casos el camino no cubre.

[SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) añade cómo saber si funciona: se mide, no se supone. Dos indicadores bastan para empezar: la **cobertura** (qué parte de las tareas pasa por el camino) y el **costo de empezar** (pasos para llegar a algo funcionando). Un camino con baja cobertura o con costo alto de arranque es un camino que nadie usa.

## Ejemplo

Una plataforma ofrece una plantilla que, al crear un servicio, genera el despliegue con límites de recursos, usuario sin privilegios, etiqueta de dueño, sondas de salud e imágenes fijadas. Un equipo con un requisito especial se aparta, documenta la excepción y mantiene su propia configuración. Ilustración del mecanismo de [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

## Errores y confusiones comunes

- **Nadie usa el camino dorado** ([SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md)): causa, cobertura baja o costo de empezar alto; corrección, medir ambos y ampliar la cobertura o simplificar el inicio.
- **Volverlo obligatorio**: pasa a ser un estándar impuesto y pierde la señal que da la excepción.
- **Confundirlo con una plantilla pasiva**: sin soporte y automatización no es un camino, es un ejemplo.
- **Medir solo cuántos servicios tiene la plataforma** en vez de cuántos equipos lo eligen.

## Límites y cuándo no aplica

Vale para tareas frecuentes y parecidas entre equipos; para un caso único, construir el camino cuesta más de lo que ahorra. Un camino que cubre mal los casos reales se vuelve un proyecto de infraestructura con su propia agenda, como advierte [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) de las plataformas sin usuarios identificados. Y las guardas incorporadas envejecen: requieren mantenimiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Guarda](../g/guarda.md), [Tarea](../t/tarea.md), [Autoservicio](../a/autoservicio.md), [Carga cognitiva](./carga-cognitiva.md), [Catálogo de servicios](./catalogo-de-servicios.md), [Excepción registrada](../e/excepcion-registrada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — qué es una plataforma interna y qué ofrece; autoridad: CNCF TAG App Delivery.
- [Team Topologies](https://teamtopologies.com/) — equipos de plataforma y carga cognitiva; autoridad: sitio de los autores del libro.
- [DORA](https://dora.dev/) — investigación sobre desempeño de entrega de software; autoridad: programa de investigación DORA.
- [Backstage: What is Backstage?](https://backstage.io/docs/overview/what-is-backstage/) — portal de desarrollo con catálogo y plantillas; autoridad: documentación del proyecto.
- [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) — políticas como código; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Camino crítico](./camino-critico.md) · [Camino feliz →](./camino-feliz.md)
