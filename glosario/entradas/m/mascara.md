# Máscara

[↑ Glosario](../../README.md) · [← Margen de contribución](./margen-de-contribucion.md) · [Matriz →](./matriz.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Máscara selecciona posiciones mediante operaciones bit a bit.

Tomado del glosario de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md).

## Por qué importa

La clase donde se define, [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), existe con este propósito: la clase existe para interpretar un valor binario solo cuando se declaran base, ancho, signo y orden de bytes.

## Cómo funciona

Según [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

Esta regla hace que sumar *da la vuelta*. En ocho bits, `127 + 1` produce `10000000`, que con signo es `-128`: el acarreo que sale del byte se descarta y el resultado cae fuera del rango. La Figura 3 lo muestra con cuatro bits, donde la vuelta es visible en un círculo. Python no muestra este comportamiento porque sus enteros no tienen ancho; para simularlo se impone una máscara. La expresión `((n & 0xFF) ^ 0x80) - 0x80` interpreta los ocho bajos de `n` como un byte con signo: aplicada a 128 da `-128`, y a 255 da `-1`, tal como `int.from_bytes(b'\xff', 'big', signed=True)`. El mismo `0xff` vale 255 sin signo y -1 con signo; el patrón no decide.

Según [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

Un segundo fallo controlado explora el desbordamiento. Serializa en dos bytes sin signo el valor 65 535 y luego 65 536: `int.to_bytes` lanza `OverflowError: int too big to convert`, lo que convierte el error en visible. Ahora repite con la máscara `& 0xFFFF`: el valor 65 536 se transforma en 0 sin avisar. **Síntoma:** un identificador se repite tras 65 536 eventos y dos registros distintos colisionan. **Causa:** se eligió truncar en silencio en lugar de rechazar o ampliar el ancho. **Corrección:** el contrato define qué hacer fuera de rango (rechazar, ampliar a cuatro bytes con una versión de formato o usar aritmética de secuencia) y los vectores de prueba incluyen 0, 65 535, 65 536 y -1.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

Un encabezado de red fija ancho y orden. El productor que usa orden nativo puede pasar pruebas locales y fallar al interoperar. La solución es contrato explícito y vectores de prueba compartidos, no detectar plataforma en cada extremo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md)) son:

- **conversión aprendida de memoria** — causa: falta modelo posicional. Corrección: reconstruye pesos y suma.
- **overflow no aparece en Python** — causa: entero arbitrario oculta ancho. Corrección: valida rango o usa serialización fija.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Python no muestra este comportamiento porque sus enteros no tienen ancho; para simularlo se impone una máscara. ([SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Base](../b/base.md), [Bit](../b/bit.md), [Byte](../b/byte.md), [Endianess](../e/endianess.md), [Overflow](../o/overflow.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Margen de contribución](./margen-de-contribucion.md) · [Matriz →](./matriz.md)
