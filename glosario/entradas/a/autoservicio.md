# Autoservicio

[↑ Glosario](../../README.md) · [← Autorización, captura, liquidación](./autorizacion-captura-liquidacion.md) · [Backend →](../b/backend.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Capacidad que un equipo obtiene sin esperar a una persona de otro equipo.

Definición de trabajo de [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md).

## Por qué importa

En [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), el tema «Ticket frente a autoservicio» importa porque la cola humana se satura antes de lo que parece.

## Cómo funciona

Según [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md):

Una capacidad que se pide por ticket depende de una cola de personas. Las colas tienen una propiedad que se trató en la clase 376: la espera crece de forma no lineal con la utilización. Con dos personas y tres horas por solicitud, subir la demanda de 0,2 a 0,55 solicitudes por hora (2,75 veces) multiplica la espera media por más de veinte. La respuesta habitual es contratar, pero también se puede cambiar la naturaleza del servicio: el **autoservicio** convierte la capacidad en una acción automatizada con validaciones, que no espera a nadie y no depende de la disponibilidad de una persona. Tiene su costo: construir y mantener la automatización y diseñar los límites (cuotas, aprobaciones) que antes aplicaba una persona.

Según [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md):

El equipo de plataforma de la API de entregas decide tratar sus capacidades como un producto. Para cada una (servicio nuevo, entorno de vista previa, base de datos, cola, alertas) escribe un dueño, una medida de éxito y una fecha de revisión. Para el camino dorado fija una meta de cobertura del 80 % de lo que piden los equipos (medida preguntando a ocho equipos) y un tiempo de empezar de menos de cuatro horas medido desde la solicitud hasta el primer despliegue. El catálogo pasa a validarse cada noche en cuatro niveles; una entrada con dueño inexistente o revisión de más de 180 días abre una incidencia al equipo que figura y baja un indicador de salud visible en el portal.

## Ejemplo

Ejemplo de [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) (sección «Ejemplo profesional»):

El equipo de plataforma de la API de entregas decide tratar sus capacidades como un producto. Para cada una (servicio nuevo, entorno de vista previa, base de datos, cola, alertas) escribe un dueño, una medida de éxito y una fecha de revisión. Para el camino dorado fija una meta de cobertura del 80 % de lo que piden los equipos (medida preguntando a ocho equipos) y un tiempo de empezar de menos de cuatro horas medido desde la solicitud hasta el primer despliegue.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La espera por ticket se dispara en cierres** — causa: utilización cercana a la saturación. Corrección: autoservicio para lo frecuente; medir la utilización. ([SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La respuesta habitual es contratar, pero también se puede cambiar la naturaleza del servicio: el **autoservicio** convierte la capacidad en una acción automatizada con validaciones, que no espera a nadie y no depende de la disponibilidad de una persona. ([SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Camino dorado](../c/camino-dorado.md), [Carga cognitiva](../c/carga-cognitiva.md), [Catálogo de servicios](../c/catalogo-de-servicios.md), [Plataforma interna](../p/plataforma-interna.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-489 — Developer portals y capacidades de plataforma](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CNCF: Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — plataformas internas como producto; autoridad: CNCF TAG App Delivery.
- [CNCF: modelo de madurez de la ingeniería de plataformas](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) — dimensiones de madurez; autoridad: CNCF TAG App Delivery.
- [Backstage: catálogo de software](https://backstage.io/docs/features/software-catalog/) — catálogo basado en metadatos; autoridad: documentación de Backstage.

---

[↑ Glosario](../../README.md) · [← Autorización, captura, liquidación](./autorizacion-captura-liquidacion.md) · [Backend →](../b/backend.md)
