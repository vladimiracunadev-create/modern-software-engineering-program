# Intención perdida

[↑ Glosario](../../README.md) · [← Intención declarada y estrategia de ejecución](./intencion-declarada-y-estrategia-de-ejecucion.md) · [Intensidad aritmética →](./intensidad-aritmetica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Edición que una persona hizo y que no aparece en el estado final tras sincronizar.

Definición de trabajo de [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md).

## Por qué importa

La clase donde se define, [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), existe con este propósito: la clase existe para que decidas dónde vive cada dato del cliente, con qué garantías de escritura y con qué política de fusión cuando dos dispositivos lo cambian, midiendo el coste de cada garantía y lo que cada política sacrifica.

## Cómo funciona

Según [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md):

**Cómo leer la figura.** Cada barra es la media de 300 semillas de ediciones cuya intención no sobrevive a la sincronización; las coral son la política por registro y la verde la política por campo. **Dónde deja de valer:** la definición de «intención perdida» es del autor, y las ediciones se reparten al azar, mientras que las reales se concentran en pocos registros. Los números indican la forma de la diferencia, no una tasa de pérdida de un producto.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md):

El equipo del cliente escribe el inventario de datos con una fila por dato: ubicación (base local, archivo, caché), garantía (transacción confirmada, reemplazo atómico, sin garantía), política de borrado y política de fusión. El borrador va en la base con transacciones cortas; la configuración, en un archivo con reemplazo atómico; la caché de tareas, en un directorio que el sistema puede limpiar. La fusión del borrador es por campo, con detección explícita cuando ambos editan el mismo, y se avisa a la persona en lugar de elegir en silencio.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md)) son:

- **La configuración queda ilegible tras un cierre inesperado** — causa: se escribió encima del archivo. Corrección: temporal sincronizado y reemplazo atómico.
- **Guardar un borrador tarda segundos con muchas ediciones** — causa: una transacción por edición con sincronización completa. Corrección: agrupar escrituras y elegir un modo de sincronización explícito.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la definición de «intención perdida» es del autor, y las ediciones se reparten al azar, mientras que las reales se concentran en pocos registros. ([SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Edición](../e/edicion.md), [Estado](../e/estado.md), [Durabilidad](../d/durabilidad.md), [Escritura atómica](../e/escritura-atomica.md), [Fusión](../f/fusion.md), [Transacción](../t/transaccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite, «Atomic Commit In SQLite»](https://www.sqlite.org/atomiccommit.html) — mecanismo de transacciones atómicas y sus supuestos; autoridad: SQLite.
- [SQLite, «Write-Ahead Logging»](https://www.sqlite.org/wal.html) — modo WAL y sus efectos; autoridad: SQLite.
- [SQLite, «PRAGMA statements»](https://www.sqlite.org/pragma.html) — opciones de sincronización y de diario; autoridad: SQLite.
- [Android Developers, «Room»](https://developer.android.com/training/data-storage/room) — capa de acceso a SQLite en Android; autoridad: Google.
- [Pillai et al., «All File Systems Are Not Created Equal»](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/pillai) — suposiciones de las aplicaciones sobre los sistemas de archivos; autoridad: USENIX OSDI.

---

[↑ Glosario](../../README.md) · [← Intención declarada y estrategia de ejecución](./intencion-declarada-y-estrategia-de-ejecucion.md) · [Intensidad aritmética →](./intensidad-aritmetica.md)
