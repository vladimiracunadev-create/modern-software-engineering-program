# Encoding

[↑ Glosario](../../README.md) · [← Encargo](./encargo.md) · [Endianess →](./endianess.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md)

## Definición

Regla entre bytes y caracteres.

Definición de trabajo de [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md).

## Por qué importa

La clase donde se define, [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), existe con este propósito: la clase existe para tratar entrada, salida y serialización como fronteras que validan y preservan significado.

## Cómo funciona

Según [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md):

Un archivo contiene bytes; abrir en modo texto decodifica con un encoding. Declarar UTF-8 evita depender de configuración local. Nueva línea y normalización pueden variar. Un `UnicodeDecodeError` describe una frontera, no un texto «corrupto» universal.

Según [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md):

Guarda un archivo con `Path.write_text('señal', encoding='utf-8')` y léelo con `open(ruta).read()` sin `encoding`. En Linux obtendrás `'señal'`; en Windows, `'seÃ±al'`. Registra la plataforma, `locale.getpreferredencoding(False)` y el resultado de cada lectura. Corrige con `encoding='utf-8'` explícito y añade una prueba que escriba y lea un texto con acentos y una marca fuera de latin-1 (la `✓` de la práctica). Después genera un JSONL con un byte `\xf1` suelto, ejecuta la CLI y comprueba que sale con código 5, con stdout vacío y el error en stderr. Registra por qué rechazar es mejor que reemplazar caracteres.

## Ejemplo

Caso medido en la sección «Texto, bytes y encoding» de [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md):

Un archivo contiene bytes; abrir en modo texto decodifica con un encoding. Declarar UTF-8 evita depender de configuración local. Nueva línea y normalización pueden variar. Un `UnicodeDecodeError` describe una frontera, no un texto «corrupto» universal.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`seÃ±al` en lugar de `señal`** — causa: UTF-8 leído como cp1252/latin-1. Corrección: declarar `encoding='utf-8'` en la lectura. ([SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `open(archivo).read()` sin `encoding` de un archivo guardado en UTF-8 con `señal` devolvió `'seÃ±al'` en Windows y `'señal'` en Linux, con el mismo código. ([SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md))
- Guarda un archivo con `Path.write_text('señal', encoding='utf-8')` y léelo con `open(ruta).read()` sin `encoding`. ([SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Byte](../b/byte.md), [Regla](../r/regla.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Efecto](./efecto.md), [Escritura atómica](./escritura-atomica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial — Input and Output](https://docs.python.org/3/tutorial/inputoutput.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `json` documentation](https://docs.python.org/3/library/json.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `pathlib` documentation](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Encargo](./encargo.md) · [Endianess →](./endianess.md)
