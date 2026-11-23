# Unidad menor

[↑ Glosario](../../README.md) · [← Unidad funcional](./unidad-funcional.md) · [Unificación →](./unificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

La unidad mínima de una moneda en que se expresan los importes enteros, por ejemplo el céntimo.

Definición de trabajo de [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md).

## Por qué importa

La clase donde se define, [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), existe con este propósito: la clase existe para que representes el dinero como un dominio con reglas propias (cantidad entera, moneda, regla de redondeo, doble entrada, idempotencia) y para que sepas qué invariantes comprobar y qué defectos esas invariantes no ven.

## Cómo funciona

Según [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md):

Un importe es una cantidad más una moneda, y la cantidad debe ser exacta. Guardarla como `float` introduce el error de representación binaria que Goldberg describe: 0,10 no tiene representación exacta, y sumarlo un millón de veces da 100 000,000 001 333. Las opciones seguras son un entero de la unidad menor (céntimos) o un tipo decimal con contexto explícito, como `decimal` de Python. Fowler propone unir cantidad y moneda en un valor que no permita sumar pesos con dólares. Cada moneda tiene su número de decimales y su regla de redondeo; no se asume que todas tengan dos.

Según [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md):

Los de la unidad menor de la moneda para el importe final y los que la regla de cálculo exija para los intermedios. No todas las monedas usan dos decimales; la regla debe declararse por moneda.

## Ejemplo

Ejemplo de [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) (sección «Preguntas frecuentes»):

Los de la unidad menor de la moneda para el importe final y los que la regla de cálculo exija para los intermedios. No todas las monedas usan dos decimales; la regla debe declararse por moneda.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md)) son:

- **Totales que difieren en un céntimo entre documentos** — causa: regla de redondeo no declarada o repartida. Corrección: una regla escrita, aplicada en una función con pruebas.
- **Se pierde un céntimo al repartir** — causa: división sin asignar el resto. Corrección: reparto con resto por el método del resto mayor o la regla declarada.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md)) son: Las definiciones son operativas para el cobro de matrículas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún banco, procesador de pagos, red de tarjetas ni dinero real, y no se evaluó ninguna norma fiscal ni de seguridad: las facturas, el IVA, el libro de tres cuentas y las tasas de pérdida son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asiento de doble entrada](../a/asiento-de-doble-entrada.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Invariante](../i/invariante.md), [Oráculo](../o/oraculo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-294 — Fintech, contabilidad e invariantes monetarias](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `decimal`](https://docs.python.org/3/library/decimal.html) — aritmética decimal con modos de redondeo explícitos; autoridad: documentación de Python.
- [Fowler, «Money» (Patterns of Enterprise Application Architecture)](https://martinfowler.com/eaaCatalog/money.html) — patrón de valor para cantidad y moneda; autoridad: autor del catálogo.
- [Goldberg, «What every computer scientist should know about floating-point arithmetic» (ACM Computing Surveys, 1991)](https://doi.org/10.1145/103162.103163) — error de representación y redondeo en coma flotante; autoridad: ACM Computing Surveys.
- [Stripe, «Idempotent requests»](https://docs.stripe.com/api/idempotent_requests) — claves de idempotencia para reintentar peticiones; autoridad: documentación del proveedor.
- [IETF, borrador «The Idempotency-Key HTTP Header Field»](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) — cabecera propuesta para peticiones idempotentes; autoridad: IETF (documento en borrador, no es una norma).

---

[↑ Glosario](../../README.md) · [← Unidad funcional](./unidad-funcional.md) · [Unificación →](./unificacion.md)
