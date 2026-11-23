# Extracción

[↑ Glosario](../../README.md) · [← Extensión](./extension.md) · [Extractor →](./extractor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Copia del comportamiento de un modelo mediante consultas.

Definición de trabajo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md): Modelo en el que el agente que despliega lee el repositorio desde dentro del entorno, en lugar de recibir órdenes desde fuera.

## Por qué importa

En [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), el tema «Extracción» importa porque las respuestas permiten copiar el modelo.

En [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), el tema «Extracción» importa porque una copia periódica y un registro de cambios ven cosas distintas.

## Cómo funciona

Según [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md):

El equipo de *Avisos-ML* escribe su modelo de amenazas. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz. Para cada uno, un atacante y una prueba. Evasión: se mide la fracción de marcados que evaden con las tres características autodeclaradas y se decide aceptar el riesgo, documentado, porque el costo es un recordatorio no enviado; se retira la tasa de lectura declarada del modelo y se reemplaza por una medida del sistema. Extracción: se limita a 1 000 consultas por cuenta y por día y se devuelve una clasificación en lugar de la probabilidad. Envenenamiento: los datos de proveedores externos pasan por una revisión de procedencia y una prueba de disparadores sobre un conjunto de combinaciones raras.

Según [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md):

Una columna `status = 'delivered'` puede significar «el mensajero marcó entregado» en la base operacional y «el cliente confirmó» en el informe de ventas. Las columnas conservan nombre y tipo mientras cambian de sentido. Hay tres puntos donde ocurre: la extracción (qué filas entran, cuáles se omiten), la transformación (cómo se redondea, qué zona horaria se aplica, qué se descarta) y el consumo (cuál es la definición de «activo»). La defensa es escribir la definición junto con la columna, con un ejemplo, y comprobarla; las clases siguientes dan las herramientas (`SE-365`, `SE-366`).

## Ejemplo

Ejemplo de [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* escribe su modelo de amenazas. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz. Para cada uno, un atacante y una prueba. Evasión: se mide la fracción de marcados que evaden con las tres características autodeclaradas y se decide aceptar el riesgo, documentado, porque el costo es un recordatorio no enviado; se retira la tasa de lectura declarada del modelo y se reemplaza por una medida del sistema. Extracción: se limita a 1 000 consultas por cuenta y por día y se devuelve una clasificación en lugar de la probabilidad.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La diferencia de seguridad es concreta: en extracción la canalización de integración no necesita credenciales del clúster (basta con que publique un artefacto y actualice un manifiesto), de modo que comprometer la integración no entrega el control de producción, y el agente solo necesita leer el repositorio. ([SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Entorno](./entorno.md), [Modelo](../m/modelo.md), [Capa](../c/capa.md), [Carga analítica](../c/carga-analitica.md), [Carga operacional](../c/carga-operacional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-361 — Del dato operacional al analítico](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-487 — GitOps y reconciliación](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-609 — Seguridad y robustez de sistemas de ML](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-086](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenGitOps: principios](https://opengitops.dev/) — cuatro principios de GitOps; autoridad: proyecto OpenGitOps de la CNCF.
- [Argo CD: opciones de sincronización](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/) — poda y protección de recursos; autoridad: documentación de Argo CD.
- [Argo CD: diferencias](https://argo-cd.readthedocs.io/en/stable/user-guide/diffing/) — campos ignorados en la comparación; autoridad: documentación de Argo CD.
- [Flux: conceptos](https://fluxcd.io/flux/concepts/) — reconciliación e intervalos; autoridad: documentación de Flux.
- [Kubernetes: controladores](https://kubernetes.io/docs/concepts/architecture/controller/) — bucle de control y estado deseado; autoridad: documentación de Kubernetes.

---

[↑ Glosario](../../README.md) · [← Extensión](./extension.md) · [Extractor →](./extractor.md)
