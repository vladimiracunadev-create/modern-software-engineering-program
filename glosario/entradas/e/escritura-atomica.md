# Escritura atómica

[↑ Glosario](../../README.md) · [← Escenario decorativo](./escenario-decorativo.md) · [Escritura condicional →](./escritura-condicional.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Guardado que deja siempre el estado anterior o el nuevo completos, nunca uno parcial, mediante un archivo temporal sincronizado y un reemplazo.

Definición de trabajo de [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md): Publicación de un archivo de modo que un lector ve el contenido anterior o el nuevo completo, nunca una mezcla.
- En [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md): Reemplazo observado como cambio indivisible bajo supuestos del sistema.
- En [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md): Guardado que deja el estado anterior o el nuevo completos, nunca uno parcial.

## Por qué importa

En [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), el tema «Escritura atómica» importa porque guardar a medias deja el estado corrupto justo cuando más hace falta.

En [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), el tema «Escritura atómica» importa porque oculta el trabajo a medias a los lectores.

## Cómo funciona

Según [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), en la sección «Escritura atómica»:

Escribir encima del archivo y ser interrumpido deja un archivo parcial. El patrón conocido escribe un archivo temporal, fuerza su sincronización y lo reemplaza de una vez; el estado anterior sigue válido hasta el reemplazo. Tiene un coste que crece con el tamaño del estado, y ese coste decide qué cabe en un gancho de pausa y qué debe guardarse antes.

## Ejemplo

Ejemplo de [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) (sección «Caso conductor»):

La herramienta `notas` es el caso conductor de la [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md). Esta clase deja su publicación nocturna con claves por fila, escritura atómica y reanudación verificada. `SE-225` aplica la misma técnica a una actualización de binarios: descargar a un temporal, verificar y reemplazar. Cambia después un solo detalle, el tamaño del lote de 20 a 200 filas, y revisa si la matriz de caídas sigue dando los mismos resultados y cuánto cuesta repetir un lote.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md)) son:

- **El borrador vuelve vacío tras cambiar de aplicación** — causa: se guardaba solo en un evento de cierre que no se entregó. Corrección: guardar al pasar a segundo plano y de forma periódica durante la edición.
- **La aplicación se cierra al abrirla tras actualizar** — causa: la lectura estricta rechaza el estado de la versión anterior. Corrección: versión en el archivo, migraciones y prueba por versión.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos. No se midió ningún dispositivo móvil ni el plazo real de ningún gancho: los porcentajes son del autor. La siguiente clase compara formas de construir el cliente.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estado](./estado.md), [Reemplazo](../r/reemplazo.md), [Supuestos](../s/supuestos.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Contrato](../c/contrato.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-256 — Almacenamiento local y sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-225](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-225-distribucion-de-binarios-y-actualizaciones/README.md), [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `os.replace`](https://docs.python.org/3/library/os.html) — reemplazo de archivo usado en la escritura atómica.
- [Android Developers, «The activity lifecycle»](https://developer.android.com/guide/components/activities/activity-lifecycle) — estados y transiciones de una actividad; autoridad: Google.
- [Android Developers, «Save UI states»](https://developer.android.com/topic/libraries/architecture/saving-states) — qué estado guardar y dónde; autoridad: Google.
- [Android Developers, «Processes and app lifecycle»](https://developer.android.com/guide/components/activities/process-lifecycle) — prioridad de procesos y cuándo el sistema los termina; autoridad: Google.
- [Apple Developer, «Managing your app's life cycle»](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) — estados de una aplicación de iOS; autoridad: Apple.

---

[↑ Glosario](../../README.md) · [← Escenario decorativo](./escenario-decorativo.md) · [Escritura condicional →](./escritura-condicional.md)
