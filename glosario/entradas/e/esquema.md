# Esquema

[↑ Glosario](../../README.md) · [← Espiral de la muerte](./espiral-de-la-muerte.md) · [Esquema abierto →](./esquema-abierto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Restricciones de forma y campos.

Definición de trabajo de [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md): Contrato de nombres, tipos, restricciones y sensibilidad.

## Por qué importa

La clase donde se define, [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), existe con este propósito: la clase existe para tratar entrada, salida y serialización como fronteras que validan y preservan significado.

## Cómo funciona

Según [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md):

Una entrada hostil puede ser un problema de tamaño o de forma: `json.loads('[' * 100000 + ']' * 100000)` lanzó `RecursionError`. De ahí que el laboratorio limite la entrada a 1 MB, valide el esquema campo a campo y devuelva códigos de error estables en lugar de dejar pasar una excepción. En la salida conviene lo contrario: ordenar las claves (`sort_keys=True`), un formato estable y un `schema_version` explícito, para que un consumidor pueda detectar un cambio.

Según [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md):

No sin validarlo: límites de tamaño y profundidad, esquema y tipos estrictos, rechazo de `NaN` y de claves duplicadas si el contrato lo exige.

## Ejemplo

Ejemplo de [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) (sección «Preguntas frecuentes»):

No sin validarlo: límites de tamaño y profundidad, esquema y tipos estrictos, rechazo de `NaN` y de claves duplicadas si el contrato lo exige.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md)) son:

- **`seÃ±al` en lugar de `señal`** — causa: UTF-8 leído como cp1252/latin-1. Corrección: declarar `encoding='utf-8'` en la lectura.
- **`UnicodeEncodeError` al imprimir** — causa: la consola no puede codificar el carácter. Corrección: salida ASCII escapada o configurar la codificación de salida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No sin validarlo: límites de tamaño y profundidad, esquema y tipos estrictos, rechazo de `NaN` y de claves duplicadas si el contrato lo exige. ([SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Contrato](../c/contrato.md).
- **Ver también:** [Restricciones](../r/restricciones.md), [Sensibilidad](../s/sensibilidad.md), [Tipo](../t/tipo.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Contrato](../c/contrato.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-067 — Entrada, salida y serialización](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (148 clases más lo mencionan; las que más):

[SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Tutorial — Input and Output](https://docs.python.org/3/tutorial/inputoutput.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `json` documentation](https://docs.python.org/3/library/json.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python `pathlib` documentation](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Microsoft Learn — about_Environment_Variables](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_environment_variables) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Espiral de la muerte](./espiral-de-la-muerte.md) · [Esquema abierto →](./esquema-abierto.md)
