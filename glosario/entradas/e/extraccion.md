# Extracción

[↑ Glosario](../../README.md) · [← Extensión](./extension.md) · [Extractor →](./extractor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

En el sentido principal del programa ([SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md)), la **extracción** es la copia del comportamiento de un modelo mediante consultas: un atacante hace muchas preguntas y usa las respuestas para entrenar su propia réplica. El término tiene otros sentidos en el programa, que conviene no confundir:

- En [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md) (ingeniería de datos): el paso de un proceso de datos en que se decide qué filas entran y cuáles se omiten.
- En [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md) (CI/CD): un modelo de despliegue en que el agente que despliega lee el repositorio desde dentro del entorno, en lugar de recibir órdenes desde fuera.

Esta entrada desarrolla el primero y resume los otros dos.

## Por qué importa

Un modelo expuesto por una interfaz es un activo que se puede copiar sin acceso a su código ni a sus datos: basta con consultarlo. La decisión que cambia es qué se expone y a qué ritmo: la interfaz del modelo es parte de su superficie de ataque, y limitarla es una defensa de seguridad, no solo de capacidad.

## Cómo funciona

[SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) incluye la extracción en el modelo de amenazas del equipo de *Avisos-ML*. Activos: el modelo, los datos de comportamiento de estudiantes, las etiquetas, el registro y la interfaz; para cada uno, un atacante y una prueba. Frente a la extracción, la defensa elegida es doble: limitar a 1 000 consultas por cuenta y por día, y devolver una clasificación en lugar de la probabilidad. La razón es de información: cada respuesta es una pista sobre la frontera de decisión del modelo; cuantas menos respuestas y menos informativas, más cuesta reconstruirlo. Una probabilidad revela más que una etiqueta.

En [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), la extracción de datos es uno de tres puntos donde una columna cambia de sentido sin cambiar de nombre (junto con la transformación y el consumo): qué filas entran y cuáles se omiten define lo que el dato significa aguas abajo. La defensa es escribir la definición junto con la columna y comprobarla.

En [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), la extracción en CI/CD tiene una ventaja de seguridad concreta: la canalización de integración no necesita credenciales del clúster (basta con que publique un artefacto y actualice un manifiesto), de modo que comprometer la integración no entrega el control de producción.

## Ejemplo

El modelo de marcados de *Avisos-ML* se expone con una interfaz que devuelve una probabilidad. Un atacante la consulta decenas de miles de veces y entrena una copia. La mitigación del equipo: tope de 1 000 consultas por cuenta y por día, y respuesta en forma de clasificación. No impide del todo la copia, pero la encarece.

## Errores y confusiones comunes

- **Confundirla con la evasión o el envenenamiento**: la evasión engaña a un modelo existente; el envenenamiento corrompe sus datos; la extracción lo copia.
- **Devolver siempre la probabilidad por comodidad**: entrega más información de la necesaria.
- **Mezclar sentidos**: la extracción de un proceso de datos no tiene relación con el robo de un modelo.
- **Tratar el límite de consultas como defensa completa**: las cuentas múltiples pueden eludirlo.

## Límites y cuándo no aplica

Las medidas de [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md) forman parte de un modelo de amenazas del ejemplo, con aceptación documentada de ciertos riesgos; no son una garantía contra la copia. Si el modelo no está expuesto fuera de la organización, o su valor no justifica el costo de protegerlo, la extracción puede no ser un riesgo prioritario.

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
