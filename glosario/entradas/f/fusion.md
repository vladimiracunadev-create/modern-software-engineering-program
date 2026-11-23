# Fusión

[↑ Glosario](../../README.md) · [← Funciones puras y transparencia referencial](./funciones-puras-y-transparencia-referencial.md) · [Fusión de tres ramas →](./fusion-de-tres-ramas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Regla que decide el estado final cuando dos copias de un dato han cambiado sin ver el cambio de la otra.

Definición de trabajo de [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md).

## Por qué importa

En [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), el tema «Dos copias del mismo dato» importa porque en cuanto hay dos dispositivos, hay dos escritores y toda política de fusión decide qué se pierde.

## Cómo funciona

Según [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md):

Resultado: quedarse con el último registro pierde **100,68** intenciones en media con relojes alineados, **101,11** con un reloj 60 pasos adelantado y **106,57** con 300; fusionar por campo pierde **47,85** en los tres casos. La fusión por campo es insensible al reloj y reduce las pérdidas a menos de la mitad, pero no las elimina: cuando dos dispositivos editan el mismo campo una intención se pierde.

Según [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md):

El equipo del cliente escribe el inventario de datos con una fila por dato: ubicación (base local, archivo, caché), garantía (transacción confirmada, reemplazo atómico, sin garantía), política de borrado y política de fusión. El borrador va en la base con transacciones cortas; la configuración, en un archivo con reemplazo atómico; la caché de tareas, en un directorio que el sistema puede limpiar. La fusión del borrador es por campo, con detección explícita cuando ambos editan el mismo, y se avisa a la persona en lugar de elegir en silencio.

## Ejemplo

Ejemplo de [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) (sección «Ejemplo profesional»):

El equipo del cliente escribe el inventario de datos con una fila por dato: ubicación (base local, archivo, caché), garantía (transacción confirmada, reemplazo atómico, sin garantía), política de borrado y política de fusión. El borrador va en la base con transacciones cortas; la configuración, en un archivo con reemplazo atómico; la caché de tareas, en un directorio que el sistema puede limpiar. La fusión del borrador es por campo, con detección explícita cuando ambos editan el mismo, y se avisa a la persona en lugar de elegir en silencio.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cambio del teléfono desaparece tras sincronizar** — causa: la fusión elige el último registro entero. Corrección: fusionar por campo y avisar de los conflictos reales. ([SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La fusión por campo es insensible al reloj y reduce las pérdidas a menos de la mitad, pero no las elimina: cuando dos dispositivos editan el mismo campo una intención se pierde. ([SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Regla](../r/regla.md), [Durabilidad](../d/durabilidad.md), [Escritura atómica](../e/escritura-atomica.md), [Intención perdida](../i/intencion-perdida.md), [Transacción](../t/transaccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (26 clases más lo mencionan; las que más):

[SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md), [Discord](../../../casos/exito/discord.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

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

[↑ Glosario](../../README.md) · [← Funciones puras y transparencia referencial](./funciones-puras-y-transparencia-referencial.md) · [Fusión de tres ramas →](./fusion-de-tres-ramas.md)
