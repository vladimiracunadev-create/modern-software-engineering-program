# Contrato de datos

[↑ Glosario](../../README.md) · [← Contrato de consumidor](./contrato-de-consumidor.md) · [Contrato de delegación →](./contrato-de-delegacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Un **contrato de datos** es un acuerdo versionado entre un productor y sus consumidores sobre el esquema, la semántica, la calidad y el servicio de un conjunto de datos ([SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)). [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) lo usa en un sentido algo más acotado: el esquema y las garantías de calidad y frescura que el productor ofrece. Es la contraparte, para los datos, del contrato de una interfaz.

## Por qué importa

Los consumidores de datos (informes, modelos, otros equipos) dependen de campos que el productor puede cambiar sin saberlo. Sin un acuerdo explícito, un cambio incompatible rompe aguas abajo, y el productor se entera después. La decisión que cambia es quién es responsable de qué: el productor se compromete a lo que publica y a cómo lo cambia; el consumidor sabe en qué puede confiar.

## Cómo funciona

El contrato tiene cuatro partes, siguiendo la definición de [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md):

- **Esquema**: campos, tipos y obligatoriedad.
- **Semántica**: qué significa cada campo. Un cambio de significado sin cambio de tipo es el más difícil de detectar (cambio semántico).
- **Calidad**: reglas que los datos cumplen, como unicidad o rangos.
- **Servicio**: garantías como la frescura, es decir, cuánto retraso máximo tiene el dato.

Está **versionado**: los cambios se rigen por reglas de promoción y de compatibilidad (hacia atrás y hacia adelante). La clase [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) lo trabaja con un verificador y un registro de esquemas, que comparan una versión propuesta con la vigente y rechazan cambios incompatibles. La causa de que funcione es que convierte una convención informal en algo comprobable de forma automática antes de publicar.

Un detalle de alcance: [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) usa el término dentro de otro tema, sin una sección propia; el mecanismo completo (registro, compatibilidad) es el de esa clase. El paso siguiente, [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), construye el linaje y el catálogo que dicen quién consume cada campo, pieza necesaria para saber a quién afecta un cambio.

## Ejemplo

El productor publica `entregas` v1 con `nota` entero y frescura máxima de una hora. Quiere cambiar `nota` a decimal. El verificador compara con la versión vigente y marca el cambio como incompatible para consumidores que esperan entero; el productor debe publicar v2 y dar un plazo de convivencia. Escenario construido en la línea de [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md).

## Errores y confusiones comunes

- **Reducirlo al esquema**: sin semántica ni calidad, un cambio de significado pasa inadvertido.
- **No versionarlo**: no hay forma de cambiar sin romper.
- **Confundirlo con la documentación**: un contrato se comprueba automáticamente; una documentación se lee.
- **Creer que lo cumple quien consume**: obliga al productor.

## Límites y cuándo no aplica

[SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) declara que sus esquemas, reglas de promoción y registros son construcciones del autor y que el verificador es una simplificación: no cubre tipos anidados, enumeraciones ni uniones. No se ejecutó un registro de esquemas real ni se midió el costo de un cambio incompatible en una organización. Para datos con un único productor y consumidor dentro del mismo equipo, el costo formal puede ser mayor que el beneficio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Frescura](../f/frescura.md), [Garantía](../g/garantia.md), [Semántica](../s/semantica.md), [Cambio semántico](./cambio-semantico.md), [Compatibilidad hacia adelante](./compatibilidad-hacia-adelante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md).

**Aparece en los casos de estudio:** [Cloudflare](../../../casos/exito/cloudflare.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Contrato de consumidor](./contrato-de-consumidor.md) · [Contrato de delegación →](./contrato-de-delegacion.md)
