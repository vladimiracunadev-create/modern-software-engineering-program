# Mapa de contextos

## Definición

Un **mapa de contextos** es la descripción de los contextos delimitados de un sistema y de la naturaleza de cada relación entre ellos (`SE-329`). `SE-546` lo usa como el diagrama de contextos y relaciones. Es un artefacto del diseño orientado al dominio que hace explícito quién depende de quién y de qué manera.

## Por qué importa

Cuando varios modelos coexisten y no se declara cómo se relacionan, cada cambio es una negociación improvisada y el acoplamiento se reparte sin control. La decisión que cambia es dónde se concentra el acoplamiento: en contratos pequeños y declarados entre contextos, no en un modelo compartido por todos.

## Cómo funciona

`SE-329` enumera los tipos de relación que el mapa declara:

- **Socios** que coordinan cambios.
- **Cliente y proveedor**, donde uno depende de otro.
- **Conformista**: un contexto que acepta el modelo del vecino tal cual.
- **Capa anticorrupción**: un contexto que traduce el modelo ajeno al propio para que no lo contamine.

Lo importante es que **cada relación se declare**, porque define quién debe coordinar con quién. Un contrato pequeño y estable entre contextos (tres atributos compartidos, no catorce) concentra el acoplamiento donde puede gestionarse y deja el resto libre para cambiar.

La causa de su utilidad es que convierte lo implícito en explícito. Los síntomas que enumera la clase apuntan a su ausencia: cada cambio de un atributo exige coordinar a tres equipos (un modelo único compartido), o la misma palabra significa cosas distintas en reuniones (hay varios contextos sin declarar). En ambos casos, la corrección es separar contextos, escribir el significado en cada uno y dibujar el mapa de relaciones. `SE-546` lo aplica al diseño de un sistema pequeño con avisos y entregas.

## Ejemplo

Un sistema tiene los contextos Académico, Avisos y Facturación. El mapa declara: Avisos es cliente de Académico y adopta su modelo de entrega a través de una capa anticorrupción; Facturación es conformista respecto de Académico; Académico y Avisos coordinan cambios como socios en un contrato de tres atributos. Con eso queda claro quién debe hablar con quién antes de cambiar algo. Ejemplo ilustrativo siguiendo `SE-329`.

## Errores y confusiones comunes

- **Cada cambio de un atributo exige coordinar a tres equipos**: un modelo único compartido; se corrige separando contextos y reduciendo el contrato a lo necesario.
- **La misma palabra significa cosas distintas en reuniones**: hay varios contextos sin declarar.
- **Dibujar solo cajas**: sin declarar la naturaleza de cada relación no es un mapa.
- **Confundirlo con un diagrama de despliegue**: muestra relaciones entre modelos, no entre servidores.

## Límites y cuándo no aplica

El mapa solo tiene sentido si hay dos o más contextos; en un sistema con un único modelo no hace falta. Un mapa deja de valer en cuanto la realidad cambia y nadie lo actualiza. Y declarar una relación no la hace cumplirse: la capa anticorrupción o el contrato pequeño deben existir en el código, no solo en el diagrama.
