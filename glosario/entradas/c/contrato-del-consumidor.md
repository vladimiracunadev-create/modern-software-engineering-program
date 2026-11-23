# Contrato del consumidor

[↑ Glosario](../../README.md) · [← Contrato de salida](./contrato-de-salida.md) · [Contrato dirigido por el consumidor →](./contrato-dirigido-por-el-consumidor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Declaración de los campos y comportamientos que un cliente usa de un proveedor.

Definición de trabajo de [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md).

## Por qué importa

En [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), el tema «Contrato del consumidor» importa porque declara solo lo que el cliente lee; evita alertas por cambios inocuos.

## Cómo funciona

Según [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md):

La **instantánea** compara la respuesta completa con una copia guardada: cualquier diferencia es una alerta. La **diferencia de esquema** compara la forma del documento (qué campos, de qué tipo) con un esquema guardado. El **contrato del consumidor** comprueba solo los campos y tipos que el cliente lee. Las tres detectan todos los cambios que rompen; difieren en las falsas alarmas, que son cambios que no rompen pero producen alerta.

Según [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md):

Es un buen insumo: «cambia este endpoint sin romper estos contratos». El agente no debe poder modificar el contrato del consumidor para que su cambio pase.

## Ejemplo

Ejemplo de [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) (sección «Caso conductor»):

*Avisos* consume la API de la plataforma y la traduce con la capa de `SE-546`. El contrato del consumidor es lo que la plataforma debe respetar para no romperlo; las precondiciones del servicio son lo que *Avisos* promete a su vez. `SE-548` pasa de las fronteras entre sistemas a la frontera entre una especificación y el código.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **contrato del consumidor** comprueba solo los campos y tipos que el cliente lee. ([SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Falsa alarma](../f/falsa-alarma.md), [Instantánea](../i/instantanea.md), [Invariante](../i/invariante.md), [Poscondición](../p/poscondicion.md), [Precondición](../p/precondicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-547 — Diseño por contrato y pruebas de contrato como oráculo](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Contrato de salida](./contrato-de-salida.md) · [Contrato dirigido por el consumidor →](./contrato-dirigido-por-el-consumidor.md)
