# Puerto

[↑ Glosario](../../README.md) · [← Puerta trasera](./puerta-trasera.md) · [Pull request →](./pull-request.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Interfaz que describe lo que la lógica de la aplicación necesita de su entorno, independiente de cómo lo ofrezca cada plataforma.

Definición de trabajo de [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md): Contrato que el dominio o la aplicación declara para comunicarse con lo que está fuera de ellos.

## Por qué importa

En [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), el tema «Puertos, adaptadores y dobles» importa porque un puerto es la forma de la dependencia; un doble de pruebas es un adaptador, y debe cumplir el mismo contrato.

## Cómo funciona

Según [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md):

Compartir es posible cuando el comportamiento es igual; adaptar, cuando existe pero difiere y se puede ocultar tras un puerto; excluir, cuando la plataforma no lo ofrece. Excluir una función de una plataforma es una decisión sobre las personas que la usan y debe ser explícita. La clasificación no es estática: una función igual hoy puede dejar de serlo con una versión nueva del sistema.

Según [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md):

El equipo del cliente de entregas hace el taller en cuatro pasos. Primero ejecuta el inventario de diferencias en los dos sistemas y lo guarda como tabla con la salida de cada uno. Segundo, clasifica cada función como igual, a adaptar o ausente y estima el coste con un intervalo. Tercero, define puertos para almacenamiento, hora, notificaciones y selección de archivos, y escribe un contrato ejecutable por puerto que se corre contra el adaptador real de cada plataforma y contra el falso. Cuarto, escribe qué se comparte (reglas del borrador, sincronización), qué se adapta (rutas, notificaciones) y qué se excluye en una plataforma, con el aviso a la persona.

## Ejemplo

Ejemplo de [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) (sección «Ejemplo mínimo»):

El fragmento comprueba un puerto de almacenamiento con un contrato mínimo. Antes de ejecutarlo, predice qué falla si el adaptador devuelve una cadena vacía al leer una clave ausente.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las pruebas pasan y la plataforma real falla** — causa: el doble no cumple el contrato del puerto. Corrección: ejecutar el mismo contrato contra el doble y el real. ([SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md))
- **Cambiar la base de datos toca decenas de módulos** — causa: el dominio depende de la infraestructura. Corrección: invertir la dependencia con un puerto y comprobar las importaciones. ([SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md))
- **Hay interfaces con una sola implementación y sin motivo** — causa: indirección por pureza. Corrección: quitar el puerto o escribir el escenario que lo justifica. ([SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Compartir es posible cuando el comportamiento es igual; adaptar, cuando existe pero difiere y se puede ocultar tras un puerto; excluir, cuando la plataforma no lo ofrece. ([SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md))
- Comparten la idea central de que las dependencias apuntan hacia la regla de negocio y los detalles se enchufan por puertos. ([SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Dominio](../d/dominio.md), [Entorno](../e/entorno.md), [Interfaz](../i/interfaz.md), [Adaptador](../a/adaptador.md), [Contrato de puerto](../c/contrato-de-puerto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-328 — Capas, hexagonal, clean y ports and adapters](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (44 clases más lo mencionan; las que más):

[SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), [SE-104](../../../classes/part-08-entornos-herramientas-y-depuracion/se-104-dev-containers-y-entornos-desechables/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cockburn, «Hexagonal architecture»](https://alistair.cockburn.us/hexagonal-architecture/) — puertos y adaptadores; autoridad: Alistair Cockburn.
- [Microsoft, «Naming Files, Paths, and Namespaces»](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file) — reglas de nombres de archivo en Windows; autoridad: Microsoft.
- [PEP 686, «Make UTF-8 mode default»](https://peps.python.org/pep-0686/) — codificación por defecto de Python según el sistema; autoridad: Python Software Foundation.
- [Python, `os`](https://docs.python.org/3/library/os.html) — comportamiento de rutas, separadores y reemplazo de archivos; autoridad: Python Software Foundation.
- [Electron, «Process Model»](https://www.electronjs.org/docs/latest/tutorial/process-model) — separación entre lógica compartida y procesos de plataforma; autoridad: OpenJS Foundation.

---

[↑ Glosario](../../README.md) · [← Puerta trasera](./puerta-trasera.md) · [Pull request →](./pull-request.md)
