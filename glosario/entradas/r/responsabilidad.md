# Responsabilidad

[↑ Glosario](../../README.md) · [← Respaldo](./respaldo.md) · [Responsabilidad compartida →](./responsabilidad-compartida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Algo que un objeto sabe o hace.

Definición de trabajo de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md).

## Por qué importa

La clase donde se define, [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), existe con este propósito: la clase existe para que, ante una función o un dato nuevo, puedas responder con un criterio y no con un gusto a la pregunta **«¿a quién le toca esto?»**.

## Cómo funciona

Según [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

El criterio dice que la responsabilidad de hacer algo debe asignarse a la clase que tiene la información necesaria para hacerlo. En el diseño A del experimento, tres clases (`Checkout`, `Factura`, `Informe`) calculan el subtotal leyendo `l.producto.precio * l.cantidad`: las tres «llegan» al precio del producto a través de la línea, y las tres repiten la fórmula (tres copias). En el diseño B, `Linea.subtotal()` calcula el subtotal con sus propios datos y `Pedido.total()` suma subtotales; las tres clases clientes llaman a `pedido.total()` y solo hay dos lecturas del precio del producto, ambas dentro de `Linea`. El análisis con `ast` cuenta **tres clases** en el diseño A que leen el dato de un colaborador de su colaborador y **cero** en el diseño B.

Según [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

El equipo de *Avisos* aplica la tabla de responsabilidades a «enviar el recordatorio de una entrega». Descubre que la regla «no avisar si ya se entregó» está en el controlador de la interfaz, en el servicio de envío y en un trabajo nocturno. Asigna la regla al objeto `Entrega` (Experto: tiene la fecha y el estado), mueve las otras dos copias con el refactor `Move Function`, añade una prueba que cubre los tres caminos y mide con `ast` que las tres clases ya no leen el estado de la entrega a través de otros objetos. Anota la alternativa descartada: dejar la regla en el servicio de envío, por ser lo que cambió más a menudo; se descartó porque el trabajo nocturno no pasa por el servicio.

## Ejemplo

Ejemplo de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* aplica la tabla de responsabilidades a «enviar el recordatorio de una entrega». Descubre que la regla «no avisar si ya se entregó» está en el controlador de la interfaz, en el servicio de envío y en un trabajo nocturno. Asigna la regla al objeto `Entrega` (Experto: tiene la fecha y el estado), mueve las otras dos copias con el refactor `Move Function`, añade una prueba que cubre los tres caminos y mide con `ast` que las tres clases ya no leen el estado de la entrega a través de otros objetos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Son colecciones de criterios de diseño con solapes (alta cohesión y responsabilidad única se parecen), pero GRASP se centra en cómo asignar responsabilidades y SOLID en propiedades de las clases y sus dependencias. ([SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Acoplamiento](../a/acoplamiento.md), [Cohesión](../c/cohesion.md), [Controlador](../c/controlador.md), [Creador](../c/creador.md), [Experto en información](../e/experto-en-informacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (95 clases más lo mencionan; las que más):

[SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md).

**Aparece en los casos de estudio:** [TSB Bank](../../../casos/fallo/tsb.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Respaldo](./respaldo.md) · [Responsabilidad compartida →](./responsabilidad-compartida.md)
