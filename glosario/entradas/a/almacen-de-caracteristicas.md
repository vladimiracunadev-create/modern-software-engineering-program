# Almacén de características

[↑ Glosario](../../README.md) · [← Almacén](./almacen.md) · [Almacenamiento temporal →](./almacenamiento-temporal.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Un **almacén de características** (*feature store*) es el sistema que define, versiona y sirve las características (los valores de entrada de un modelo) tanto para entrenar como para decidir en producción. [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) lo presenta como esa pieza de tres funciones; [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) lo usa en su sentido de operación: el servicio que entrega a un modelo en producción los valores con los que predice. Son dos caras del mismo componente: una ve su diseño y la otra, su fallo.

## Por qué importa

La decisión que cambia es dónde vive la definición de cada característica. Si el entrenamiento calcula «compras de los últimos 30 días» con una consulta y el servicio en línea la calcula con otro código, el modelo se entrena con un valor y predice con otro, y ningún error lo avisa. Un almacén bien usado fija la definición una sola vez, y además permite reconstruir qué valores vio una predicción pasada, algo que una auditoría puede exigir. Pero también es otro sistema que operar y otro punto de falla en el camino de cada predicción, así que adoptarlo es una decisión de costo, no un reflejo.

## Cómo funciona

[SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) le asigna tres tareas:

1. **Guardar la definición** de cada característica una sola vez, con su versión.
2. **Servirla fuera de línea**, para construir conjuntos de entrenamiento con uniones puntuales: para cada ejemplo se toma el valor que la característica tenía *en el momento de la decisión*, no el valor actual. Sin esa unión puntual se cuela información del futuro y el modelo parece mejor de lo que será.
3. **Servirla en línea**, con baja latencia, para decidir, y registrar qué versión de cada característica entró en cada predicción.

La causa de que esto importe es la divergencia entre entrenamiento y servicio: dos implementaciones de la misma característica terminan, tarde o temprano, dando valores distintos. El almacén ataca esa causa compartiendo definición, no añadiendo vigilancia.

En operación ([SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md)), el almacén falla de forma parcial: un valor ausente, uno obsoleto, o una lectura lenta que agota su tiempo de espera. El modelo sigue respondiendo con valores por omisión y sus respuestas empeoran sin que ningún error lo señale. [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) cita a Sculley et al. para explicar el riesgo: en sistemas de aprendizaje automático las dependencias de datos y los cambios del mundo externo se agravan cuando los consumidores no están declarados.

## Ejemplo

Un modelo de recomendación usa tres características: antigüedad de la cuenta, compras recientes y categoría favorita. En el almacén, la segunda tiene una versión 1 (ventana de 30 días) y una versión 2 (ventana de 14 días). Cada predicción guarda «compras recientes v1». Cuando se investiga una recomendación rara de hace un mes, se puede reconstruir exactamente qué valor vio el modelo. En el experimento de falla de [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), el almacén deja de responder para una fracción de claves; el modelo recibe el valor por omisión en esas claves, y la señal que detecta el problema no es un error sino la **tasa de valores por omisión** y la distribución de puntuaciones, que se desvían de lo habitual.

## Errores y confusiones comunes

- **«Es obligatorio para hacer aprendizaje automático».** No: [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) dice que con tres características y un solo consumidor, una tabla versionada y una función compartida resuelven lo mismo con menos piezas.
- **El modelo empeora y nadie lo nota.** Causa señalada en [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md): no hay señal de integridad del almacén. Corrección: medir la tasa de valores por omisión y la distribución de puntuaciones.
- **Confundirlo con una base de datos cualquiera.** Lo que lo define no es almacenar, sino la definición única, la unión puntual y el registro de versiones por predicción.
- **Creer que la unión puntual es un detalle.** Es lo que evita la fuga de información del futuro hacia el entrenamiento.

## Límites y cuándo no aplica

Empieza a pagarse cuando varios modelos reutilizan características, cuando calcularlas es costoso o cuando una auditoría exige reconstruir una decisión pasada ([SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md)). Con pocas características y un consumidor, es sobreingeniería. Su camino en línea añade latencia y un punto de falla: si el almacén cae, hay que decidir antes qué hace el modelo (degradar, usar un valor por omisión explícito o rechazar), y eso se prueba con inyección de fallos como la de [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md). Y no resuelve por sí solo la calidad de los datos ni la deriva: solo da el lugar donde medirlas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica](../c/caracteristica.md), [Modelo](../m/modelo.md), [Servicio](../s/servicio.md), [Valor](../v/valor.md), [Escritura confirmada perdida](../e/escritura-confirmada-perdida.md), [Etiqueta](../e/etiqueta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-602 — Datos de entrenamiento, etiquetas y feature stores](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jepsen](https://jepsen.io/) — análisis de seguridad de sistemas distribuidos de datos; autoridad: proyecto de investigación Jepsen.
- [Sculley et al., Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) — riesgos propios de los sistemas de ML; autoridad: artículo de NIPS 2015.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y medir la salida; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas de recuperación e integridad de datos; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Almacén](./almacen.md) · [Almacenamiento temporal →](./almacenamiento-temporal.md)
