# Interoperabilidad

[↑ Glosario](../../README.md) · [← Internationalization Engineer](./internationalization-engineer.md) · [Interpretación →](./interpretacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

La **interoperabilidad** es la capacidad de que dos sistemas intercambien datos con el mismo significado ([SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md)).

## Por qué importa

Un formato estándar fija la sintaxis pero deja libres cosas que importan. Compartir un formato no basta para compartir significado.

## Cómo funciona

[SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) da ejemplos: JSON dice que un número es una secuencia de dígitos, y cada implementación decide su rango y precisión; un identificador de 64 bits que un lector convierte a decimal de doble precisión pierde los dígitos bajos si supera 2⁵³. El texto tiene el mismo problema con las formas de normalización (la «é» puede ser un solo carácter o una «e» más un acento combinante), la codificación por defecto y el fin de línea. La defensa es hacer explícito lo que el estándar deja implícito: codificación, normalización, rango numérico.

## Ejemplo

Un identificador de 64 bits enviado como número JSON y leído por un cliente JavaScript pierde precisión; se envía como cadena.

## Errores y confusiones comunes

- **Acentos rotos en un sistema y no en otro.** Codificación por defecto distinta; especificar `encoding="utf-8"` siempre.
- **Un archivo difiere de bytes y tiene el mismo tamaño.** Fin de línea o codificación distintos; fijar `newline` y `encoding` y comparar hashes.

## Límites y cuándo no aplica

No se logra por declaración: se verifica con pruebas de contrato entre las implementaciones reales. Y no equivale a reproducibilidad entre sistemas, aunque comparten las mismas causas.

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
