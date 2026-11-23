# Doble

[↑ Glosario](../../README.md) · [← DMA](./dma.md) · [Doble de prueba →](./doble-de-prueba.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Objeto que sustituye a un colaborador en una prueba.

Definición de trabajo de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md): Sustituto controlado de un colaborador.

## Por qué importa

En [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), el tema «Doble y verificación» importa porque mezclarlos produce discusiones sin objeto.

## Cómo funciona

Según [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

Un **doble** es un objeto que ocupa el lugar de un colaborador en una prueba. Fowler distingue varios: un *stub* devuelve respuestas preparadas; un *fake* tiene una implementación real pero simplificada (una base de datos en memoria); un *mock* se programa con expectativas sobre las llamadas que recibirá. En Python, `unittest.mock.Mock` sirve para los tres usos según cómo se configure. Lo importante no es el nombre sino qué se verifica después: si el estado resultante o las llamadas recibidas.

Según [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md):

El equipo decide la política de dobles para *Avisos*. Para el **canal**, que envía mensajes por la red, usa un doble que registra lo que recibe y puede fallar bajo demanda; la verificación de la llamada es la verificación del efecto. Para el **reloj**, un reloj fijo, porque el tiempo es una entrada y no una conversación. Para el **repositorio**, un repositorio real en memoria que implemente la misma interfaz que el de producción, porque las consultas son detalles que pueden cambiar. La suite clásica protege los refactores; un par de pruebas de contrato con el repositorio real de producción garantizan que el doble no miente.

## Ejemplo

Ejemplo de [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) (sección «Ejemplo profesional»):

El equipo decide la política de dobles para *Avisos*. Para el **canal**, que envía mensajes por la red, usa un doble que registra lo que recibe y puede fallar bajo demanda; la verificación de la llamada es la verificación del efecto. Para el **reloj**, un reloj fijo, porque el tiempo es una entrada y no una conversación. Para el **repositorio**, un repositorio real en memoria que implemente la misma interfaz que el de producción, porque las consultas son detalles que pueden cambiar. La suite clásica protege los refactores; un par de pruebas de contrato con el repositorio real de producción garantizan que el doble no miente.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **escuela clásica** (de Detroit, por el origen de XP) usa objetos reales cuando puede y dobles cuando el real es lento, externo o no determinista, y verifica estado. ([SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Objeto](../o/objeto.md), [Cambio de contrato](../c/cambio-de-contrato.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](../e/efecto.md), [Ejemplo como especificación](../e/ejemplo-como-especificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-543 — TDD en la práctica: escuelas de Londres y clásica, y sus límites](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (146 clases más lo mencionan; las que más):

[SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python `unittest` documentation](https://docs.python.org/3/library/unittest.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← DMA](./dma.md) · [Doble de prueba →](./doble-de-prueba.md)
