# Reproducibilidad

[↑ Glosario](../../README.md) · [← Reproducción y revisión](./reproduccion-y-revision.md) · [Reproducibilidad entre sistemas →](./reproducibilidad-entre-sistemas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **reproducibilidad** es la capacidad de obtener el mismo resultado con el mismo código y los mismos datos ([SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md)). [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) la presenta como la posibilidad de repetir un método con información suficiente. Es una propiedad que se demuestra, no que se declara: se comprueba haciendo que otra persona, u otro entorno, repita el procedimiento y comparando el resultado.

## Por qué importa

Un resultado que no se puede reproducir no se puede auditar, depurar ni confiar en él. Las comparaciones entre versiones, los benchmarks y los informes dependen de ello. Cambia qué se registra al producir un artefacto: versiones, entradas, orden, codificación y entorno, no solo el código.

## Cómo funciona

La reproducibilidad exige controlar las fuentes de variación. [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) clasifica ocho artefactos comparados: idénticos, diferentes por un defecto de escritura (corregible), diferentes por su naturaleza (por ejemplo, una fecha de generación) y diferentes por diseño. Al pasar de dos ejecuciones en el mismo sistema a Windows frente a Ubuntu, la parte idéntica se reduce: el entorno es una fuente de variación. La parte roja (defectos de escritura) se puede corregir, por ejemplo con escritura determinista.

[SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) indica prácticas concretas: serializar con claves ordenadas y UTF-8 y declarar las versiones, para que la huella no cambie entre sistemas por codificación, orden o versión no declarados. La causa de las diferencias suele ser un valor por defecto del entorno que nadie fijó.

## Ejemplo

```python
import json, hashlib
datos = {"b": 1, "a": 2}
s = json.dumps(datos, sort_keys=True, ensure_ascii=False).encode("utf-8")
print(hashlib.sha256(s).hexdigest())      # igual en Windows y en Linux
```

Sin `sort_keys` ni codificación explícita, la huella puede variar con el orden de inserción o la configuración regional.

## Errores y confusiones comunes

- **La huella cambia entre sistemas.** Causa: codificación, orden o versión no declarados; corrección: serializar con claves ordenadas y UTF-8 y declarar las versiones ([SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)).
- **El validador da 0 problemas y el ejercicio falla.** Causa: solo comprueba existencia y forma; corrección: añadir coincidencias de significado verificables ([SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)).
- **Confundirla con repetición o replicación.** [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md) los separa: repetir, reproducir y replicar fallan por razones distintas.

## Límites y cuándo no aplica

Los resultados de [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) son de dos sistemas en un equipo, con una versión de Python en cada uno: otras versiones, sistemas de archivos o configuraciones regionales podrían cambiarlos. La reproducibilidad byte a byte de un informe con gráficos binarios exige controlar además fechas incrustadas y versiones de bibliotecas. Y no todo debe ser reproducible bit a bit: a veces basta una tolerancia declarada.

## Relación con otros conceptos

- **Prerrequisito:** [Capacidad](../c/capacidad.md).
- **Ver también:** [Resultado](./resultado.md), [Confusor](../c/confusor.md), [Defecto sembrado](../d/defecto-sembrado.md), [Expediente](../e/expediente.md), [Falso negativo](../f/falso-negativo.md), [Falso positivo](../f/falso-positivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (31 clases más lo mencionan; las que más):

[SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng, «Reproducible research in computational science»](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad; autoridad: Science, 2011.
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/) — documentación de SLI, SLO y política; autoridad: Google, SRE Workbook.
- [Google SRE: Managing Incidents](https://sre.google/sre-book/managing-incidents/) — roles y gestión de incidentes; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — postmortems sin culpa y seguimiento; autoridad: libro de ingeniería de confiabilidad de Google.
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planes de contingencia, pruebas y ejercicios; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Reproducción y revisión](./reproduccion-y-revision.md) · [Reproducibilidad entre sistemas →](./reproducibilidad-entre-sistemas.md)
