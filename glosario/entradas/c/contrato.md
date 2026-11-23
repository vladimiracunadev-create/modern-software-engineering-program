# Contrato

[↑ Glosario](../../README.md) · [← Contrapresión](./contrapresion.md) · [Contrato compatible →](./contrato-compatible.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Un **contrato** es la descripción verificable de lo que una pieza de software promete a quienes la usan y de lo que espera de ellos. Es una de las palabras más cargadas del programa y su sentido cambia con la pieza de la que se hable, siempre con el mismo núcleo (qué entra, qué sale, qué se garantiza):

- **De una función o programa:** [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) lo define como la definición observable de entradas, salidas, errores y efectos.
- **De un tipo o clase:** [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) lo concreta como el conjunto de precondiciones, poscondiciones e invariantes que un cliente puede esperar de un tipo.
- **De una herramienta de línea de comandos:** [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) lo compone de nombre, subcomandos, opciones, flujos (`stdin`, `stdout`, `stderr`) y códigos de salida, que son interfaz pública.
- **Entre un proveedor y un consumidor:** [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) lo define como la descripción verificable de lo que un consumidor espera de un proveedor (campos, tipos, valores, orden).
- **De una arquitectura con complementos:** [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) lo entiende como interfaz, versión y garantías que el núcleo ofrece a los complementos y viceversa.

En el programa, «contrato» no significa un acuerdo legal ni un documento aparte: significa una promesa **observable y comprobable**.

## Por qué importa

Sin contrato escrito, cada persona infiere de la implementación lo que puede esperar, y cualquier cambio interno rompe a alguien. El contrato fija la frontera: lo que está dentro puede cambiar con libertad, lo que está en el contrato solo cambia con un proceso de versión. También convierte el diagnóstico en una pregunta con respuesta: cuando algo falla, se puede preguntar si incumplió el proveedor o el consumidor. [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) lo muestra con una suite de 15 pruebas donde el nombre de cada prueba es una frase del contrato, de modo que un fallo se lee como diagnóstico.

## Cómo funciona

Un contrato se sostiene en tres actos: **escribirlo**, **ejecutarlo** y **versionarlo**.

1. **Escribirlo.** Se declaran las entradas válidas, las salidas, los errores y los efectos. Para una clase se usan precondiciones (obligación del llamador), poscondiciones (obligación de quien implementa) e invariantes (válidos antes y después de cada operación pública), como en [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md) y [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md).
2. **Ejecutarlo.** Un contrato que no se comprueba es documentación que se desactualiza. Las pruebas de contrato ([SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md)) comprueban lo que el consumidor espera del proveedor, y los mismos casos pueden ejecutarse en otro lenguaje: en [SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), un puerto en Rust debe cumplir los mismos cuatro casos del archivo de contrato que la referencia en Python; lo que se transfiere es el contrato observable, no la sintaxis ni el paquete.
3. **Versionarlo.** Cambiar un contrato es cambiar una promesa. Las reglas de compatibilidad ([SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md)) distinguen qué cambios no rompen a los consumidores existentes.

La causa de que el contrato de una herramienta de línea de comandos importe tanto la explica [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md): una herramienta es una API cuyo consumidor es otro programa. Si los mensajes de error se mezclan con los datos en `stdout`, el comando deja de poder encadenarse en una tubería.

## Ejemplo

[SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) invocó una herramienta de diagnóstico con catorce entradas en Windows y Linux. La ruta feliz produjo código de salida 0 y un JSON en `stdout`, sin una línea en `stderr`. Los argumentos ausentes terminaron con 2 y un mensaje de uso; un JSON roto o una línea inválida, con 3; una prueba no autorizada, repetida o contradictoria, con 4; un archivo ausente o no UTF-8, con 5. En todos los errores, `stdout` quedó vacío y `stderr` tuvo una línea JSON con `error` y `detail`. Ese conjunto de reglas es el contrato; permite escribir `herramienta ... | otra_herramienta` sin que un error contamine los datos.

## Errores y confusiones comunes

- **Probar solo el caso feliz.** Se usa el ejemplo como especificación; hay que derivar del contrato los casos de error, vacío y frontera ([SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md)).
- **«Funciona» en otro lenguaje pero falla un caso.** Se tradujo la sintaxis sin el contrato; la corrección es ejecutar los mismos casos en ambos ([SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md)).
- **Confundir el contrato de un laboratorio con un estándar.** Los códigos 0/2/3/4/5 de [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) son del laboratorio; POSIX solo fija 0 como éxito.
- **Pensar que un mapa de pruebas mide la protección.** Dice qué prueba apunta a qué contrato, no cuán bien lo protege ([SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md)).

## Límites y cuándo no aplica

Un contrato describe lo que se prometió, no lo que ocurre fuera de lo prometido: los límites del contrato educativo de [SE-072](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) (por ejemplo, el tamaño máximo de entrada) no protegen contra otros agotamientos como la memoria o la CPU con entradas patológicas. Un contrato escrito y un contrato comprobado son cosas distintas, y solo el segundo se mantiene vivo. Y como la palabra tiene varios sentidos, en cada clase hay que confirmar a cuál se refiere antes de trasladar una conclusión de una a otra.

## Relación con otros conceptos

- **Prerrequisito:** [Interfaz](../i/interfaz.md).
- **Ver también:** [Complemento](./complemento.md), [Conjunto](./conjunto.md), [Efecto](../e/efecto.md), [Espera](../e/espera.md), [Adaptador](../a/adaptador.md), [Degradación](../d/degradacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-030 — PowerShell, Bash y portabilidad de scripts](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-061 — Valores, expresiones, tipos y variables](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-064 — Funciones, parámetros, retorno y alcance](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-065 — Errores, excepciones y resultados explícitos](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-066 — Colecciones y transformación de datos](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-071 — Taller: transferir una solución entre lenguajes](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-072 — Proyecto: herramienta de línea de comandos probada](../../../classes/part-05-fundamentos-de-programacion/se-072-proyecto-herramienta-de-linea-de-comandos-probada/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-302 — SOLID y sus límites](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-338 — Microkernel y arquitecturas de plugins](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-423 — Integración, componentes y contratos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (307 clases más lo mencionan; las que más):

[SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python `unittest` documentation](https://docs.python.org/3/library/unittest.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — documenta ownership, tipos de error, traits y concurrencia usados como contraste semántico.
- [Python `argparse` documentation](https://docs.python.org/3/library/argparse.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Contrapresión](./contrapresion.md) · [Contrato compatible →](./contrato-compatible.md)
