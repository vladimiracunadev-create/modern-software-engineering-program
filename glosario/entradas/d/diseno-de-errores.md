# Diseño de errores

[↑ Glosario](../../README.md) · [← Directorio de trabajo](./directorio-de-trabajo.md) · [Diseño desde consumidor →](./diseno-desde-consumidor.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md)

## Definición

El **diseño de errores** es la práctica de decidir, antes de que ocurran, qué comunica un fallo a quien consume una biblioteca, un SDK o una CLI. [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) lo resume en cuatro componentes de un error útil: **qué falló**, **contexto seguro**, **acción** que puede tomar quien lo recibe y una **referencia estable**. El error se trata como parte de la API pública y de la experiencia de quien desarrolla con el producto, no como un detalle interno que aparece al final.

## Por qué importa

Un error es, muchas veces, la primera «documentación» que alguien lee de verdad. Si dice solo «no funciona» o vuelca una traza interna, el consumidor abre una incidencia sin datos o abandona el producto. [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) documenta ese síntoma: los reportes de error son «no funciona» sin datos, porque el mensaje no dice qué faltó ni cómo arreglarlo. La decisión que cambia es quién paga el costo del diagnóstico: con un error diseñado lo paga el autor una vez, al escribirlo; sin él, lo paga cada consumidor, cada vez.

## Cómo funciona

Cada componente tiene una razón:

- **Qué falló:** el nombre del problema en términos del dominio, no del código interno («configuración ausente», no «KeyError»).
- **Contexto seguro:** los datos que ayudan a entenderlo (clave que faltó, valor esperado, versión) **sin filtrar secretos**: ni tokens ni rutas personales.
- **Acción:** qué hacer a continuación («defina `CLIENTE_ID` o pase `--cliente`»).
- **Referencia estable:** un código o identificador que no cambia aunque cambie el texto, para buscar documentación o filtrar registros. [SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) advierte que no se debe obligar a **buscar texto cambiante**: si el contrato es el texto del mensaje, cualquier mejora de redacción rompe a quien lo analizaba.

Además, tipos de excepción, códigos de salida y documentación deben **contar la misma clasificación**. Si la API lanza `ErrorDeConfiguracion`, la CLI sale con un código asociado y la documentación lista el mismo nombre, el consumidor puede tratar el fallo de manera uniforme. La corrección que propone la clase es una **excepción propia con causa, solución y atributos estructurados**.

## Ejemplo

Un SDK que lee credenciales de un archivo. Un error pobre:

```python
raise Exception("error")
```

Un error diseñado, siguiendo los cuatro componentes (ilustración):

```python
class ErrorDeConfiguracion(Exception):
    codigo = "SDK-CFG-001"
    def __init__(self, clave, archivo):
        self.clave, self.archivo = clave, archivo
        super().__init__(
            f"[{self.codigo}] Falta la clave '{clave}' en '{archivo}'. "
            f"Agréguela o defina la variable de entorno {clave.upper()}."
        )
```

La referencia `SDK-CFG-001` es estable, el atributo `clave` permite programarla, y el mensaje no contiene valores sensibles. En la CLI, la misma clasificación se traduce a un código de salida concreto.

## Errores y confusiones comunes

- **Mensaje sin acción.** Dice qué pasó pero no qué hacer.
- **Incluir el valor del secreto.** «Token inválido: abc...» termina en registros y capturas.
- **Depender del texto.** Los consumidores analizan el mensaje y una mejora de redacción los rompe.
- **Clasificaciones distintas por capa.** La API, la CLI y la documentación nombran el mismo fallo de maneras diferentes.

## Límites y cuándo no aplica

Una evaluación interna de la experiencia de desarrollo no sustituye investigación diversa ni soporte real ([SE-118](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md)): un error que parece claro a su autor puede no serlo para otras personas. Los mensajes muy detallados pueden revelar demasiado sobre el sistema cuando el consumidor no es de confianza (un servicio público); allí se devuelve una referencia y el detalle queda en registros internos. No todo error merece diseño: en código interno de vida corta, una excepción estándar con mensaje claro basta.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contextos](../c/contextos.md), [Referencia](../r/referencia.md), [Documentación ejecutable](./documentacion-ejecutable.md), [Feedback, telemetría y privacidad](../f/feedback-telemetria-y-privacidad.md), [Journey de desarrollador](../j/journey-de-desarrollador.md), [Time to first success](../t/time-to-first-success.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-118 — Diseño de experiencia para desarrolladores](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.

---

[↑ Glosario](../../README.md) · [← Directorio de trabajo](./directorio-de-trabajo.md) · [Diseño desde consumidor →](./diseno-desde-consumidor.md)
