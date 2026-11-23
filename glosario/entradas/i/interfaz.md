# Interfaz

[↑ Glosario](../../README.md) · [← Interés público](./interes-publico.md) · [Interfaz de secuencia →](./interfaz-de-secuencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Una **interfaz** es el punto en que dos partes intercambian información, control o responsabilidad. El programa la usa en varias escalas con ese núcleo:

- **En la frontera de un sistema** ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)): punto de intercambio de información, control o responsabilidad, que puede ser entre un equipo y un proveedor tanto como entre dos programas.
- **En la descomposición** ([SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md)): el contrato entre subproblemas.
- **En módulos** ([SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md)): el comportamiento público esperado por los consumidores, distinto de los nombres internos.
- **En integración** ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)): el punto en que un componente expone o consume datos de otro (una respuesta JSON, una tabla compartida, una cola).

## Por qué importa

Una interfaz fija qué puede asumir cada parte de la otra, y por eso concentra los defectos de integración. [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) lo dice así: cada componente asume algo sobre la otra parte (nombres, tipos, valores posibles, orden, cuántos elementos aparecen por página), y un defecto de integración es una asunción que ya no se cumple; ninguna prueba de una sola parte lo ve, porque cada una se comprueba contra su propia versión de la asunción.

## Cómo funciona

El mecanismo es separar lo **público** de lo **interno**. [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) lo ilustra con módulos de Python: los consumidores importan nombres internos y se rompen al refactorizar porque no hay una interfaz pública declarada; la corrección es declararla (`__all__`, guion bajo) y probar sobre ella. [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) la ve como contrato entre subproblemas: quien resuelve una parte solo necesita saber la interfaz de las demás. En integración ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)), la consecuencia práctica es una prueba por interfaz crítica: ejecutar dos o más piezas reales juntas y comprobar que la asunción de una coincide con la de la otra. En la frontera de un sistema ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)), las interfaces con proveedores deben documentarse con contrato, señal de degradación, respuesta local y escalamiento.

## Ejemplo

En [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), un componente espera una respuesta con cierto orden y cantidad de elementos por página; el otro cambia la paginación. Cada una de las dos partes pasa sus pruebas aisladas, y solo una prueba de integración sobre esa interfaz muestra el defecto. En [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), un proveedor externo aparece en el mapa del sistema con su interfaz y su modo de fallo en vez de quedar como una caja sin contrato.

## Errores y confusiones comunes

- **Un fallo de extremo a extremo tarda horas en localizarse.** Solo hay recorridos completos; corrección ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)): añadir una prueba por interfaz crítica.
- **Un proveedor aparece sin interfaz ni fallo.** Se trató «externo» como «irrelevante»; corrección ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)): documentar contrato, señal de degradación, respuesta local y escalamiento.
- **Consumidores que importan nombres internos.** No hay interfaz pública declarada ([SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md)).

## Límites y cuándo no aplica

Una interfaz describe lo que se promete, no lo que ocurre dentro: [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) aclara que una prueba de integración comprueba que las asunciones coinciden, no que cada pieza sea correcta. Y la palabra cambia de alcance entre clases (de una función pública a la frontera entre equipos), de modo que al leerla hay que confirmar cuál es.

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
