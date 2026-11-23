# Contrato de puerto

[↑ Glosario](../../README.md) · [← Contrato de línea de comandos](./contrato-de-linea-de-comandos.md) · [Contrato de salida →](./contrato-de-salida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Conjunto de comprobaciones ejecutables que todo adaptador de un puerto debe superar.

Definición de trabajo de [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md).

## Por qué importa

La clase donde se define, [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md), existe con este propósito: el taller existe para que adaptes un producto a dos plataformas con un inventario de diferencias medidas, un coste con intervalo en lugar de una cifra y un contrato de adaptadores que impida que los dobles de prueba prometan lo que la plataforma real no cumple.

## Cómo funciona

[SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md):

El equipo del cliente de entregas hace el taller en cuatro pasos. Primero ejecuta el inventario de diferencias en los dos sistemas y lo guarda como tabla con la salida de cada uno. Segundo, clasifica cada función como igual, a adaptar o ausente y estima el coste con un intervalo. Tercero, define puertos para almacenamiento, hora, notificaciones y selección de archivos, y escribe un contrato ejecutable por puerto que se corre contra el adaptador real de cada plataforma y contra el falso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md)) son:

- **Un adjunto no se guarda en una plataforma y sí en otra** — causa: reglas de nombres distintas. Corrección: sanear el nombre en el adaptador y probar en ambas.
- **Un archivo exportado cambia al abrirlo en otro sistema** — causa: saltos de línea o codificación por defecto distintos. Corrección: fijar codificación y saltos de línea al escribir.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): el inventario mostró siete diferencias de siete medidas, y el coste y el contrato dieron salidas idénticas. No se midió ningún teléfono ni macOS, y los estados y costes de las funciones son del autor. La siguiente clase es el proyecto que integra todo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Adaptador](../a/adaptador.md), [Conjunto](./conjunto.md), [Puerto](../p/puerto.md), [Doble de prueba](../d/doble-de-prueba.md), [Inventario de diferencias](../i/inventario-de-diferencias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-263 — Taller: adaptar un producto a dos plataformas](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

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

[↑ Glosario](../../README.md) · [← Contrato de línea de comandos](./contrato-de-linea-de-comandos.md) · [Contrato de salida →](./contrato-de-salida.md)
