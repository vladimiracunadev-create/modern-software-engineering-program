# Reproducibilidad

[↑ Glosario](../../README.md) · [← Reproducción y revisión](./reproduccion-y-revision.md) · [Reproducibilidad entre sistemas →](./reproducibilidad-entre-sistemas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Capacidad de obtener el mismo resultado con el mismo código y los mismos datos.

Definición de trabajo de [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md): Posibilidad de repetir método con información suficiente.

## Por qué importa

En [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), el tema «Reproducibilidad» importa porque un resultado calculado se reproduce; el que toca el sistema difiere.

En [SE-420 — Taller y proyecto integrador: producto SaaS mínimo con evidencia](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md), el tema «Reproducibilidad» importa porque un tercero puede repetir la evidencia.

## Cómo funciona

Según [SE-444 — Proyecto: informe reproducible de calidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md):

**Cómo leer la figura.** Cada barra son los ocho artefactos clasificados para una comparación: en verde los idénticos, en rojo los que difieren por un defecto de escritura, en dorado por su naturaleza y en gris por diseño. Mira primero cuánto se reduce el verde al pasar de dos ejecuciones en el mismo sistema a Windows frente a Ubuntu, y que la parte roja se puede corregir. **Dónde deja de valer:** son dos sistemas en un equipo y una versión de Python en cada uno; otras versiones, otros sistemas de archivos o una configuración regional distinta podrían cambiar el resultado, y la reproducibilidad byte a byte de un informe con gráficos binarios exige controlar además fechas incrustadas y versiones de bibliotecas.

## Ejemplo

Caso medido en la sección «Reproducibilidad entre sistemas» de [SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md):

Un paquete es reproducible si otra persona, con otro equipo, obtiene lo mismo. Los resultados que dependen solo de un generador con semilla fija y de aritmética (los de tiempo virtual) son idénticos en cualquier sistema con la misma versión de Python, y se comprueban con una **huella** (un resumen criptográfico del resultado serializado de forma determinista, con claves ordenadas y codificación explícita). Los que tocan el sistema de archivos, la codificación local o los separadores difieren por diseño, y la tarea no es borrar la diferencia sino declararla.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-504 — Proyecto: operación observable y recuperable](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md)) son:

- **El validador da 0 problemas y el ejercicio falla** — causa: solo comprueba existencia y forma. Corrección: añadir coincidencias de significado verificables y mantener el ejercicio.
- **La huella cambia entre sistemas** — causa: codificación, orden o versión no declarados. Corrección: serializar con claves ordenadas y UTF-8, y declarar las versiones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** son dos sistemas en un equipo y una versión de Python en cada uno; otras versiones, otros sistemas de archivos o una configuración regional distinta podrían cambiar el resultado, y la reproducibilidad byte a byte de un informe con gráficos binarios exige controlar además fechas incrustadas y versiones de bibliotecas. ([SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md))

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
