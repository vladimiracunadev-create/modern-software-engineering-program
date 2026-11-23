# Interoperabilidad

[↑ Glosario](../../README.md) · [← Internationalization Engineer](./internationalization-engineer.md) · [Interpretación →](./interpretacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Capacidad de dos sistemas de intercambiar datos conservando su significado.

Definición de trabajo de [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md).

## Por qué importa

En [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), el tema «Interoperabilidad y representación» importa porque un dato válido para un lenguaje puede cambiar en otro.

## Cómo funciona

Según [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md):

La **interoperabilidad** es la capacidad de que dos sistemas intercambien datos con el mismo significado. Un formato estándar fija la sintaxis y deja libres cosas que importan: JSON dice que un número es una secuencia de dígitos, y cada implementación decide su rango y su precisión. Un identificador de 64 bits que un lector convierte a decimal de doble precisión pierde los dígitos bajos si supera 2⁵³. El texto tiene el mismo problema con las formas de normalización (la «é» puede ser un solo carácter o una «e» más una marca combinada: se ven igual y no son iguales). El dinero guardado como decimal binario acumula errores de representación. Una fecha «03/04» se lee de dos formas según la región.

## Ejemplo

Ejemplo de [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) (sección «Caso conductor»):

El mensaje de entrega de la plataforma es el caso conductor de la [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md). Esta clase deja el noveno artefacto: un contrato de interoperabilidad y una matriz ejecutable. `SE-442` preguntará cómo se mide la experiencia de quien usa el producto en dispositivos distintos y con presupuestos explícitos. Cambia después un solo dato, la política de lectura (estricta o tolerante), y observa cuántos pares dejan de ser compatibles.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)) son:

- **Acentos rotos en un sistema y no en otro** — causa: codificación por defecto distinta. Corrección: especificar `encoding="utf-8"` siempre.
- **Un archivo difiere de bytes y tiene el mismo tamaño** — causa: fin de línea o codificación distintos. Corrección: fijar `newline` y `encoding` y comparar hashes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)) son: Las definiciones son operativas para el mensaje de entrega de la plataforma. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos, uno de ellos con sondas reales en Windows 11 y Ubuntu 24.04 bajo WSL2 y los otros con datos sintéticos y semillas fijas con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Lector tolerante](../l/lector-tolerante.md), [Matriz de compatibilidad](../m/matriz-de-compatibilidad.md), [Normalización Unicode](../n/normalizacion-unicode.md), [Portabilidad](../p/portabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8259: JSON](https://www.rfc-editor.org/rfc/rfc8259) — números y su interoperabilidad; autoridad: IETF.
- [Unicode UAX #15](https://unicode.org/reports/tr15/) — formas de normalización; autoridad: Unicode Consortium.
- [Microsoft: nombres de archivo, rutas y espacios de nombres](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file) — reglas de nombres en Windows; autoridad: documentación de Microsoft.
- [Fowler, «TolerantReader»](https://martinfowler.com/bliki/TolerantReader.html) — lector que tolera cambios aditivos; autoridad: autor del texto.
- [Python: multiprocessing](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods) — métodos de inicio por plataforma; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Internationalization Engineer](./internationalization-engineer.md) · [Interpretación →](./interpretacion.md)
