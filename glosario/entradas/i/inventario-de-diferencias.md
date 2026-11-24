# Inventario de diferencias

[↑ Glosario](../../README.md) · [← Inventario](./inventario.md) · [Inventario físico / reservado / vendible →](./inventario-fisico-reservado-vendible.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Un **inventario de diferencias** es una tabla de los comportamientos del producto que pueden variar entre plataformas, cada uno ejecutado y registrado en cada plataforma. Es el sentido de [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) (taller: adaptar un producto a dos plataformas). Lo distintivo es el verbo: no se enumera lo que se recuerda, se *ejecuta* y se registra el resultado.

## Por qué importa

Las diferencias se miden, no se recuerdan. Lo que se recuerda («Linux distingue mayúsculas») suele ser cierto pero incompleto; lo que se mide encuentra lo que nadie recordó. Para adaptar un producto a dos plataformas, el inventario decide qué se comparte, qué se adapta y qué se excluye.

## Cómo funciona

Según [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md):

1. **Enumerar** cada comportamiento que pueda variar (rutas, mayúsculas en nombres, finales de línea, hora, notificaciones, selección de archivos).
2. **Ejecutarlo** en cada plataforma, con el mismo programa de prueba.
3. **Registrar** la salida de cada una en la tabla.
4. **Mantenerlo vivo:** cada diferencia nueva descubierta en uso se añade con su prueba.

Con el inventario se clasifica cada función como *igual*, *a adaptar* o *ausente*, y se estima el costo con un intervalo. Después se aíslan las diferencias detrás de **puertos** (almacenamiento, hora, notificaciones, selección de archivos) con un contrato ejecutable por puerto, que se corre contra el adaptador real de cada plataforma y contra uno falso.

## Ejemplo

El equipo del cliente de entregas hace el taller en cuatro pasos ([SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md)): ejecuta el inventario en los dos sistemas y guarda la tabla con la salida de cada uno; clasifica cada función y estima el costo con un intervalo; define puertos y escribe un contrato ejecutable por puerto; y escribe qué se comparte (reglas del borrador, sincronización), qué se adapta (rutas, notificaciones) y qué se excluye en una plataforma, con el aviso a la persona.

## Errores y confusiones comunes

- **Un adjunto no se guarda en una plataforma** por una diferencia que nadie había registrado (por ejemplo, nombres de archivo); el remedio es añadirla al inventario con su prueba.
- **Llenar el inventario de memoria** sin ejecutar.
- **Hacerlo una vez y abandonarlo,** cuando es una tabla viva.
- **Confundirlo con una matriz de compatibilidad de versiones,** que trata de versiones de un mismo sistema.

## Límites y cuándo no aplica

Solo cubre las diferencias que alguien pensó en probar; no demuestra ausencia de otras. Mide el comportamiento en las plataformas y versiones concretas ejecutadas. Para un producto de una sola plataforma no hace falta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plataforma](../p/plataforma.md), [Producto](../p/producto.md), [Adaptador](../a/adaptador.md), [Contrato de puerto](../c/contrato-de-puerto.md), [Doble de prueba](../d/doble-de-prueba.md), [Puerto](../p/puerto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft, «Naming Files, Paths, and Namespaces»](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file) — reglas de nombres de archivo en Windows; autoridad: Microsoft.
- [Cockburn, «Hexagonal architecture»](https://alistair.cockburn.us/hexagonal-architecture/) — puertos y adaptadores; autoridad: Alistair Cockburn.
- [PEP 686, «Make UTF-8 mode default»](https://peps.python.org/pep-0686/) — codificación por defecto de Python según el sistema; autoridad: Python Software Foundation.
- [Python, `os`](https://docs.python.org/3/library/os.html) — comportamiento de rutas, separadores y reemplazo de archivos; autoridad: Python Software Foundation.
- [Electron, «Process Model»](https://www.electronjs.org/docs/latest/tutorial/process-model) — separación entre lógica compartida y procesos de plataforma; autoridad: OpenJS Foundation.

---

[↑ Glosario](../../README.md) · [← Inventario](./inventario.md) · [Inventario físico / reservado / vendible →](./inventario-fisico-reservado-vendible.md)
