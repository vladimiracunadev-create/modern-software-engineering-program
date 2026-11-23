# Cabeza de la cadena

[↑ Glosario](../../README.md) · [← Bytes escaneados](../b/bytes-escaneados.md) · [CAC (costo de adquisición de cliente) →](./cac-costo-de-adquisicion-de-cliente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Resumen de la última entrada, que fija toda la historia.

Definición de trabajo de [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md).

## Por qué importa

La clase donde se define, [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), existe con este propósito: el proyecto existe para que entregues, como lo haría un equipo de plataforma, algo que otra persona pueda ejecutar, atacar y auditar: una plataforma mínima que acepta código ajeno, lo valida antes de ejecutarlo, lo ejecuta con límites, registra cada paso de forma que un cambio posterior se detecte y entrega un informe firmado con una firma que sobreviva a un ordenador cuántico.

## Cómo funciona

Según [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md):

El informe (320 bytes de JSON con la cabeza de la cadena, el número de entradas y las huellas de las reglas aceptadas) se firmó con ML-DSA-65: firma de 3 309 bytes, clave pública de 1 952 bytes, verificación correcta; con un byte distinto en el informe, la verificación falla. Qué demuestra: que el contenido del informe no cambió desde que se firmó con esa clave. Qué no demuestra: que lo que el anfitrión registró sea verdad (si el anfitrión está comprometido, firma mentiras con fidelidad), que la clave privada esté bien guardada, ni que la biblioteca de estudio sea apta para producción.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md)) son: La referencia es una plataforma mínima ejecutada en una máquina: sin autenticación de clientes, sin frontera alrededor del anfitrión, sin hardware seguro, sin almacenamiento durable y con una biblioteca de firma de estudio. Con este proyecto se cierra la [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato de ejecución](./contrato-de-ejecucion.md), [Expediente](../e/expediente.md), [Plataforma de ejecución aislada](../p/plataforma-de-ejecucion-aislada.md), [Política de falla](../p/politica-de-falla.md), [Registro encadenado](../r/registro-encadenado.md), [Tabla amenaza-mecanismo-prueba](../t/tabla-amenaza-mecanismo-prueba.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-288 — Proyecto: plataforma de ejecución aislada con evidencia](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Bytes escaneados](../b/bytes-escaneados.md) · [CAC (costo de adquisición de cliente) →](./cac-costo-de-adquisicion-de-cliente.md)
