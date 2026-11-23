# Data mesh

[↑ Glosario](../../README.md) · [← Data Engineer](./data-engineer.md) · [Database Reliability Engineer →](./database-reliability-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Enfoque organizativo y técnico que reparte la propiedad de los datos entre los dominios que los producen.

Definición de trabajo de [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md).

## Por qué importa

La clase donde se define, [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), existe con este propósito: la clase existe para que evalúes el data mesh como lo que es, una decisión sobre quién es dueño de los datos y quién responde por su calidad, y no como una arquitectura de herramientas.

## Cómo funciona

Según [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md):

Los cuatro principios del data mesh son de naturaleza distinta. La propiedad orientada al dominio es una decisión de organización: quién posee y responde. Los datos como producto es una decisión de práctica: cada conjunto tiene un dueño, una interfaz, un contrato y consumidores a quienes servir. La plataforma de autoservicio es técnica: reducir el costo de publicar un producto. La gobernanza federada y computacional es de gobierno: reglas globales (formatos, identificadores, políticas de privacidad) que se aplican como código en la plataforma y no como una reunión. Adoptar la plataforma sin la propiedad deja a un equipo central con mejores herramientas; adoptar la propiedad sin la plataforma pide a cada dominio construir su propia infraestructura de datos.

Según [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md):

El equipo de datos de *Avisos* mide el tiempo que tardan en entregarse las solicitudes del último trimestre: la mediana es de tres días y el percentil 90, de cinco semanas, con cola creciente. La dirección propone un data mesh. El equipo evita la discusión de principios y propone un piloto con un solo dominio: el equipo de notificaciones publicará su producto «avisos enviados» con un contrato de seis campos, una comprobación de esquema, otra de frescura (24 horas) y una de distribución, y un dueño nombrado. Se fija una métrica (tiempo desde la solicitud hasta el acceso) y un criterio de salida (si en seis semanas el percentil 90 baja de dos semanas a cinco días y no hay incidentes de calidad sin dueño, se amplía a tres dominios).

## Ejemplo

Ejemplo de [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) (sección «Ejemplo profesional»):

El equipo de datos de *Avisos* mide el tiempo que tardan en entregarse las solicitudes del último trimestre: la mediana es de tres días y el percentil 90, de cinco semanas, con cola creciente. La dirección propone un data mesh. El equipo evita la discusión de principios y propone un piloto con un solo dominio: el equipo de notificaciones publicará su producto «avisos enviados» con un contrato de seis campos, una comprobación de esquema, otra de frescura (24 horas) y una de distribución, y un dueño nombrado.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La lectura honesta es que el data mesh no es una reducción de costo; es una redistribución que se justifica si el conocimiento del dominio es el cuello de botella y no la capacidad técnica. ([SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](./dominio.md), [Propiedad](../p/propiedad.md), [Contrato de datos](../c/contrato-de-datos.md), [Deriva semántica](./deriva-semantica.md), [Gobernanza federada y computacional](../g/gobernanza-federada-y-computacional.md), [Producto de datos](../p/producto-de-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Data Engineer](./data-engineer.md) · [Database Reliability Engineer →](./database-reliability-engineer.md)
