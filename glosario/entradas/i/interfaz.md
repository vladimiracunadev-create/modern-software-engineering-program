# Interfaz

[↑ Glosario](../../README.md) · [← Interés público](./interes-publico.md) · [Interfaz de secuencia →](./interfaz-de-secuencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Punto en el que un componente expone o consume datos de otro.

Definición de trabajo de [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md): Punto de intercambio de información, control o responsabilidad.
- En [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md): Comportamiento público esperado por consumidores.
- En [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md): Contrato entre subproblemas.

## Por qué importa

En [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), el tema «Qué es una integración» importa porque un defecto de integración vive en la interfaz, no en ninguna de las partes.

## Cómo funciona

Según [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md):

Los componentes se comunican a través de interfaces: una respuesta JSON, una tabla compartida, una cola. Cada uno asume algo sobre la otra parte: nombres, tipos, valores posibles, orden, cuántos elementos aparecen por página. Un defecto de integración es una asunción que ya no se cumple. Ninguna prueba de una sola parte lo ve, porque cada una se comprueba contra su propia versión de la asunción. Las pruebas de integración ejecutan dos o más piezas reales juntas y comprueban que la asunción de una coincide con el comportamiento de la otra.

Según [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md):

El equipo del servicio de notas mantiene en su repositorio una carpeta `contratos/` con un archivo por consumidor (`panel.json`, `exportador.json`, `avisos.json`) que lista los campos, tipos y valores que ese consumidor usa y, desde un incidente, el orden de la lista. La integración continua del servicio ejecuta los tres contratos contra su respuesta en cada propuesta de cambio y falla con el nombre del consumidor afectado. Los equipos de los consumidores abren un contrato nuevo cuando empiezan a usar un campo, y retiran las cláusulas que dejaron de usar. Las pruebas de integración del panel ejecutan el panel contra la respuesta real del servicio con una base sembrada, una por interfaz del recorrido; los tres recorridos de extremo a extremo (`SE-424`) quedan para el comportamiento visible.

## Ejemplo

Ejemplo de [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sección «Ejemplo profesional»):

El equipo del servicio de notas mantiene en su repositorio una carpeta `contratos/` con un archivo por consumidor (`panel.json`, `exportador.json`, `avisos.json`) que lista los campos, tipos y valores que ese consumidor usa y, desde un incidente, el orden de la lista. La integración continua del servicio ejecuta los tres contratos contra su respuesta en cada propuesta de cambio y falla con el nombre del consumidor afectado. Los equipos de los consumidores abren un contrato nuevo cuando empiezan a usar un campo, y retiran las cláusulas que dejaron de usar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un fallo de extremo a extremo tarda horas en localizarse** — causa: solo hay recorridos completos. Corrección: añadir una prueba por interfaz crítica. ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md))
- **un proveedor aparece sin interfaz ni fallo** — causa: se trató “externo” como “irrelevante”. Corrección: documenta contrato, señal de degradación, respuesta local y escalamiento. ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md))
- **todas las cajas pertenecen al equipo** — causa: se omitieron afectados y trabajo invisible. Corrección: incorpora soporte, operación, canales alternativos y personas sin interfaz directa. ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con varios recorridos que comparten tramos se puede acotar por intersección, pero no siempre a una interfaz. ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Componente](../c/componente.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Responsabilidad](../r/responsabilidad.md), [Abstracción](../a/abstraccion.md), [Capacidad](../c/capacidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (182 clases más lo mencionan; las que más):

[SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «IntegrationTest»](https://martinfowler.com/bliki/IntegrationTest.html) — pruebas de integración; autoridad: autor del texto.
- [Martin Fowler, «ContractTest»](https://martinfowler.com/bliki/ContractTest.html) — pruebas de contrato; autoridad: autor del texto.
- [Ian Robinson, «Consumer-Driven Contracts»](https://martinfowler.com/articles/consumerDrivenContracts.html) — contratos por consumidor; autoridad: autor del texto.
- [Documentación de Pact](https://docs.pact.io/) — herramienta de contratos; autoridad: documentación oficial.
- [Especificación de JSON Schema](https://json-schema.org/specification) — descripción de documentos JSON; autoridad: especificación oficial.

---

[↑ Glosario](../../README.md) · [← Interés público](./interes-publico.md) · [Interfaz de secuencia →](./interfaz-de-secuencia.md)
