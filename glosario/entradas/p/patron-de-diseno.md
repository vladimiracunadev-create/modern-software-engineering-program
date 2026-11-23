# Patrón de diseño

[↑ Glosario](../../README.md) · [← Patrón de acceso](./patron-de-acceso.md) · [Patrón de traza →](./patron-de-traza.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Solución nombrada a un problema recurrente de diseño, con su intención y sus consecuencias.

Definición de trabajo de [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

## Por qué importa

La clase donde se define, [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), existe con este propósito: la clase existe para que uses los patrones de diseño como vocabulario de problemas recurrentes y no como plantillas que se instalan: sabrás nombrar el problema que un patrón resuelve, el costo que trae y la prueba que lo vuelve visible, y reconocerás cuándo el patrón solo añade estructura.

## Cómo funciona

Según [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

Un patrón de diseño nombra una solución recurrente a un problema recurrente, con sus consecuencias. Su valor principal es de comunicación: decir «aquí hay un observador» permite discutir el orden de las notificaciones y los fallos sin describir las clases. Su riesgo es la aplicación por catálogo: buscar un patrón para cada cosa y terminar con capas sin problema. La unidad de análisis es el problema: el patrón es una de las respuestas posibles.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

El equipo trata los tres problemas por separado. Para la configuración, deja de usar `Config.get()` y construye un objeto `Configuracion` una vez en el arranque que pasa a los módulos que lo necesitan; la suite pasa en cualquier orden y lo comprueba con una ejecución en orden aleatorio con semilla registrada. Para las notificaciones, mantiene el observador, copia la lista antes de recorrerla, aísla cada observador y registra cada excepción en un contador que sube una alarma.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md)) son:

- **La suite pasa en un orden y falla en otro** — causa: estado global compartido (singleton). Corrección: inyectar la dependencia y ejecutar en orden aleatorio con semilla.
- **Un servicio no recibe avisos cuando otro falla** — causa: observadores en un bucle que se corta con la primera excepción. Corrección: aislar cada observador y contar las excepciones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con código de ejemplo y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió el uso de patrones en proyectos reales ni su efecto sobre los defectos; las clases, las probabilidades de fallo y las cinco implementaciones mínimas son construcciones del autor. La siguiente clase examina los patrones funcionales, reactivos y concurrentes, que cambian dónde vive el estado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Consecuencia](../c/consecuencia.md), [Evidencia](../e/evidencia.md), [Intención](../i/intencion.md), [Problemas](./problemas.md), [Adaptador](../a/adaptador.md), [Inyección de dependencias](../i/inyeccion-de-dependencias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gamma, Helm, Johnson y Vlissides, «Design Patterns» (1994)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) — catálogo de patrones; autoridad: los autores (Addison-Wesley).
- [Fowler, «Inversion of Control Containers and the Dependency Injection pattern»](https://martinfowler.com/articles/injection.html) — inyección de dependencias frente a localizador; autoridad: Martin Fowler.
- [Luo et al., «An empirical analysis of flaky tests» (FSE, 2014)](https://doi.org/10.1145/2635868.2635920) — pruebas intermitentes y dependencia del orden; autoridad: ACM SIGSOFT FSE.
- [Python: sentencia `for`](https://docs.python.org/3/reference/compound_stmts.html) — advertencia sobre modificar la secuencia que se recorre; autoridad: documentación de Python.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis sintáctico usado para la huella de cada patrón; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Patrón de acceso](./patron-de-acceso.md) · [Patrón de traza →](./patron-de-traza.md)
