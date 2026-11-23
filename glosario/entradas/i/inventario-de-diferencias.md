# Inventario de diferencias

[↑ Glosario](../../README.md) · [← Inventario](./inventario.md) · [Inventario físico / reservado / vendible →](./inventario-fisico-reservado-vendible.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Tabla de comportamientos del producto que pueden variar entre plataformas, ejecutados y registrados en cada una.

Definición de trabajo de [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md).

## Por qué importa

En [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), el tema «Inventario de diferencias» importa porque las diferencias se miden, no se recuerdan.

## Cómo funciona

Según [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), en la sección «Inventario de diferencias»:

Un inventario enumera cada comportamiento del producto que puede variar entre plataformas, lo ejecuta en cada una y registra el resultado. Lo que se recuerda («Linux distingue mayúsculas») suele ser cierto pero incompleto; lo que se mide encuentra lo que nadie recordó. El inventario es una tabla viva: cada diferencia nueva descubierta en uso se añade con su prueba.

## Ejemplo

Ejemplo de [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) (sección «Ejemplo profesional»):

El equipo del cliente de entregas hace el taller en cuatro pasos. Primero ejecuta el inventario de diferencias en los dos sistemas y lo guarda como tabla con la salida de cada uno. Segundo, clasifica cada función como igual, a adaptar o ausente y estima el coste con un intervalo. Tercero, define puertos para almacenamiento, hora, notificaciones y selección de archivos, y escribe un contrato ejecutable por puerto que se corre contra el adaptador real de cada plataforma y contra el falso. Cuarto, escribe qué se comparte (reglas del borrador, sincronización), qué se adapta (rutas, notificaciones) y qué se excluye en una plataforma, con el aviso a la persona.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md)) son:

- **Un adjunto no se guarda en una plataforma y sí en otra** — causa: reglas de nombres distintas. Corrección: sanear el nombre en el adaptador y probar en ambas.
- **Un archivo exportado cambia al abrirlo en otro sistema** — causa: saltos de línea o codificación por defecto distintos. Corrección: fijar codificación y saltos de línea al escribir.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): el inventario mostró siete diferencias de siete medidas, y el coste y el contrato dieron salidas idénticas. No se midió ningún teléfono ni macOS, y los estados y costes de las funciones son del autor. La siguiente clase es el proyecto que integra todo.

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
