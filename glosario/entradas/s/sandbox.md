# Sandbox

[↑ Glosario](../../README.md) · [← SAN](./san.md) · [Saturación →](./saturacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Un **sandbox** (caja de arena) es un aislamiento que el sistema impone entre aplicaciones. En el sentido de [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) (firma, sandbox y seguridad del cliente), es el aislamiento que la plataforma impone *entre* aplicaciones y que **no protege contra errores de la propia aplicación**. [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) (sandboxes, reversibilidad y control de daño) usa el término de forma más amplia: un entorno que restringe lo que un proceso puede hacer en el sistema, por ejemplo para ejecutar un agente.

## Por qué importa

Es fácil sobrestimarlo. El sandbox impide que una aplicación lea los datos de otra sin permiso, pero no impide que la propia aplicación lea archivos suyos que no debía ni que sirva un archivo cuya ruta eligió un tercero. Los errores de confinamiento ocurren *dentro* del sandbox.

## Cómo funciona

[SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md): en Android, cada aplicación corre con un usuario de sistema propio y el kernel impone el aislamiento; otras plataformas aíslan de otras formas. Ese límite se impone desde fuera, con permisos del sistema operativo sobre archivos, procesos y recursos.

Para el sentido ampliado de [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), el mecanismo es el mismo en espíritu: restringir qué archivos, red y llamadas al sistema puede usar un proceso, de modo que un fallo o un abuso quede acotado. La reversibilidad (poder deshacer lo que el proceso cambió) y el control de daño completan la protección.

La consecuencia de diseño es una **división de responsabilidades**: el sandbox protege una aplicación de otra; la aplicación debe protegerse a sí misma de sus entradas, con validación del lado del servidor, confinamiento de rutas y verificación de las actualizaciones.

## Ejemplo

El equipo del cliente en [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) escribe su modelo de amenazas con una fila por activo (borrador local, token de sesión, paquete de actualización, adjuntos) y una columna por capacidad del atacante (lee el paquete, modifica archivos, observa el tráfico, controla el dispositivo). De la tabla salen reglas: el servidor valida todo, el cliente solo guarda tokens de corta duración emitidos por el servidor, los adjuntos se confinan a una carpeta con normalización, y la actualización se verifica con una firma asimétrica cuya clave privada solo existe en el sistema de compilación.

## Errores y confusiones comunes

- **Creer que el sandbox protege de los errores propios:** no lo hace.
- **Dejar la ruta de un archivo en manos de una entrada externa** dentro del sandbox.
- **Confundirlo con una máquina virtual o un contenedor:** son otros mecanismos de aislamiento, con otras garantías.
- **Considerar el sandbox como control único.**

## Límites y cuándo no aplica

Un sandbox protege hasta donde llegue la implementación del sistema; sus fallos permiten escapes. No cubre lo que la propia aplicación tiene permitido (por ejemplo, un permiso que la persona concedió). Para código de terceros no confiable, el aislamiento debe elegirse con un modelo de amenazas explícito.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aislamiento](../a/aislamiento.md), [Entorno](../e/entorno.md), [Proceso](../p/proceso.md), [Alcance](../a/alcance.md), [Confinamiento](../c/confinamiento.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-582 — Sandboxes, reversibilidad y control de daño](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Android Open Source Project, «Application Sandbox»](https://source.android.com/docs/security/app-sandbox) — aislamiento de aplicaciones por usuario de sistema; autoridad: Google.
- [Android Developers, «Sign your app»](https://developer.android.com/studio/publish/app-signing) — firma de aplicaciones Android; autoridad: Google.
- [Microsoft, «Package signing overview»](https://learn.microsoft.com/en-us/windows/msix/package/signing-package-overview) — firma de paquetes MSIX; autoridad: Microsoft.
- [Electron, «Security»](https://www.electronjs.org/docs/latest/tutorial/security) — prácticas de seguridad en aplicaciones de escritorio; autoridad: OpenJS Foundation.
- [OWASP, «MASVS»](https://mas.owasp.org/MASVS/) — requisitos de seguridad para aplicaciones móviles; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← SAN](./san.md) · [Saturación →](./saturacion.md)
