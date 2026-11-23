# Parte 50 — Machine learning en producción y MLOps

La [Parte 30](../part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) trató la plataforma de datos como disciplina propia. Esta parte toma lo que se construye encima: un modelo de aprendizaje automático que decide en producción. La pregunta cambia de «¿qué métrica saca el modelo?» a «¿qué hace el sistema cuando el modelo, los datos o el mundo cambian, y qué evidencia lo demuestra?». Un modelo es una caja pequeña dentro de un sistema grande: datos, etiquetas, características, entrenamiento, evaluación, registro, despliegue, servicio, monitoreo y reentrenamiento, cada uno con dueño y modos de fallo. Esta parte recorre doce eslabones y decisiones (el ciclo de vida y sus fallas, los datos y las etiquetas, el entrenamiento reproducible, la evaluación y el sesgo, la adaptación y su costo, el servicio, el despliegue seguro, el monitoreo y el reentrenamiento, la seguridad, el gobierno y la regulación, un taller de degradación y un proyecto de entrega) y mide cada uno con código. Todo se mide sobre un único caso sintético: **el modelo *Avisos-ML***, que estima la probabilidad de que un estudiante entregue tarde una tarea para decidir a quién se le envía un recordatorio. Es la continuación del servicio *Avisos* de las Partes [26](../part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), [28](../part-28-estilos-arquitectonicos/README.md), [45](../part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) y [48](../part-48-harness-y-agentic-engineering/README.md)–[49](../part-49-patrones-agenticos-y-sistemas-con-llm/README.md).

## Pregunta rectora

> Para este modelo, ¿qué puede fallar en cada eslabón, qué señal lo mostraría y cuánto tarda, qué se hace al respecto con qué costo, y qué evidencia comprobable lo demuestra ante otra persona?

## Antes del recorrido clase por clase

Esta parte no enseña a entrenar el mejor modelo ni defiende una plataforma. Enseña a leer un sistema de aprendizaje automático como un **sistema que se degrada**, y a convertir cada riesgo en una medida: un experimento con semilla, una comprobación que puede fallar, un umbral con un motivo escrito. La primera clase fija el mapa del ciclo de vida con cuatro fallas medidas sobre el mismo modelo y el bucle de realimentación (`SE-601`). Las siguientes miden los eslabones de entrada: los datos, las etiquetas y la fuga de información (`SE-602`) y el entrenamiento que se repite y se compara contra su propio ruido (`SE-603`). Después se evalúa con la pregunta correcta (`SE-604`), se adapta un modelo base con pocos datos y se calcula el costo (`SE-605`) y se mide cuánto cuesta servirlo con lotes y bajo sobrecarga (`SE-606`). El despliegue seguro combina sombra, canary y rollback (`SE-607`) y el monitoreo decide cuándo la deriva importa y cuándo reentrenar (`SE-608`). Siguen la seguridad y la robustez (`SE-609`) y el gobierno de la IA con la regulación (`SE-610`). La parte termina con un taller que degrada y recupera el modelo (`SE-611`) y un proyecto con una puerta de liberación que se ejecuta (`SE-612`).

![Diagrama de flujo con 12 pasos. Recorrido: «Ciclo de vida y fallas»; luego «Datos y etiquetas»; luego «Entrenamiento reproducible»; luego «Evaluación y sesgos»; luego «Adaptación y costo»; luego «Servir: latencia y lotes»; luego «Despliegue seguro»; luego «Monitoreo y reentrenamiento»; luego «Seguridad y robustez»; luego «Gobierno y regulación»; luego «Taller: degradar y recuperar»; luego «Proyecto: sistema operable». Retornos: «Proyecto: sistema operable» lleva a «Ciclo de vida y fallas» (la evidencia reabre el mapa).](../../site/assets/figures/mermaid-78d0132e87.svg)

El diagrama se lee de izquierda a derecha y no es un orden obligatorio de adopción: es el orden en que se explican los costos. El retorno indica que la evidencia del proyecto, o un incidente, vuelve a cambiar el mapa de fallas del primer eslabón.

## Resultados acumulativos

Podrás enumerar los eslabones de un sistema de aprendizaje automático con un dueño y un modo de fallo por eslabón, distinguir y medir cuatro fallas (una unidad distinta, una deriva de covariables, una deriva de concepto y un fallo aguas arriba), mostrar cómo el modelo cambia las etiquetas con las que se reentrena y fijar una línea base de reglas que el modelo debe justificar; medir la fuga de información, el efecto del ruido de las etiquetas, la unión puntual en el tiempo y la divergencia entre entrenamiento y servicio.

Podrás medir la dispersión de una métrica por semilla y por muestra, decidir cuándo una diferencia supera el ruido y estimar el optimismo de elegir el mejor entre muchos candidatos; elegir una métrica según la prevalencia y el costo de cada error, derivar el umbral por costo, medir la calibración y las tasas por grupo y dar un intervalo con el tamaño de muestra; comparar adaptar, entrenar desde cero y no adaptar según los datos disponibles, medir el olvido y calcular parámetros y cómputo de entrenamiento con supuestos explícitos.

Podrás medir el costo por petición según el tamaño del lote, simular un lote dinámico con y sin sobrecarga, comparar la precisión de los pesos y el costo de cargar un modelo; detectar con sombra la regresión de un segmento sin etiquetas, calcular la potencia de un canary por fracción y días, estimar las decisiones expuestas por cada estrategia y probar un rollback exacto; calcular el índice de estabilidad y la prueba de Kolmogorov y Smirnov con sus falsas alarmas, demostrar que una deriva de concepto no se ve en las entradas y comparar cuatro políticas de reentrenamiento.

Podrás medir la evasión, la puerta trasera, la copia de un modelo y la inferencia de pertenencia sobre un modelo propio y diseñar defensas proporcionales; clasificar de forma provisional usos de IA con reglas escritas, medir la completitud de la documentación por área, comparar tasas de error por grupo bajo dos políticas de umbral y construir un registro de decisiones que delata la alteración; y ensayar cuatro fallas inyectadas con cuatro monitores, medir las decisiones expuestas y escribir un postmortem, y entregar un paquete con una puerta de once comprobaciones que lee archivos reales y se prueba con variantes defectuosas.

## Prerrequisitos enlazados

- [Parte 24 — Software especializado y dominios](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-24-software-especializado-y-dominios/): el aprendizaje automático como componente de producto (`SE-291`) y la ingeniería de datos (`SE-290`).
- [Parte 35 — Estrategia y técnicas de prueba](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-35-estrategia-y-tecnicas-de-prueba/): pruebas por riesgo (`SE-421`), datos deterministas (`SE-428`) y mutación y generación de casos (`SE-426`).
- [Parte 36 — Calidad, rendimiento y resiliencia](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-36-calidad-rendimiento-y-resiliencia/): atributos medibles (`SE-433`), latencia y saturación (`SE-436`), tiempos de espera y reintentos (`SE-438`) y degradación (`SE-439`).
- [Parte 38 — Seguridad, privacidad y cumplimiento](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-38-seguridad-privacidad-y-cumplimiento/): modelos de amenaza (`SE-457`), validación de entrada (`SE-460`), privacidad por diseño (`SE-463`) y cumplimiento y evidencia (`SE-466`).
- [Parte 41 — Observabilidad, SRE e incidentes](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-41-observabilidad-sre-e-incidentes/): SLO y alertas (`SE-497`, `SE-498`), runbooks (`SE-499`), incidentes y postmortems (`SE-500`, `SE-501`).
- [Parte 46 — Desarrollo de software asistido por IA](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-46-desarrollo-de-software-asistido-por-ia/): capacidades y límites de los modelos generativos (`SE-553`) y evaluaciones de exactitud, utilidad, costo y latencia (`SE-561`).
- [Parte 49 — Patrones agénticos y sistemas con LLM](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-49-patrones-agenticos-y-sistemas-con-llm/): evaluaciones y LLMOps (`SE-597`) y costo, latencia y seguridad de sistemas con LLM (`SE-598`).
- [Parte 28 — Estilos arquitectónicos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-28-estilos-arquitectonicos/): el contrato de un producto de datos (`SE-343`) y el caso conductor *Avisos*.
- Python 3.11+ y terminal, con numpy 2.4.4 y scikit-learn 1.8.0 (`scripts/requirements-part46.txt`); los experimentos no necesitan GPU y escriben solo en directorios temporales.

## Bloques y progresión

1. **El sistema y sus entradas:** las clases 553 a 555 fijan el mapa del ciclo de vida y miden los datos, las etiquetas y la reproducibilidad del entrenamiento.
2. **Evaluar, adaptar y servir:** las clases 556 a 558 miden la evaluación con costo y por grupo, la adaptación de un modelo y el servicio con lotes y sobrecarga.
3. **Operar y defender:** las clases 559 a 562 miden el despliegue seguro, el monitoreo y el reentrenamiento, la seguridad y la robustez, y la evidencia de gobierno.
4. **Ensayar y entregar:** las clases 563 y 564 degradan y recuperan el modelo, y lo convierten en un paquete con una puerta de liberación que se ejecuta.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan experimentos ejecutados con CPython 3.12.9, numpy 2.4.4 y scikit-learn 1.8.0 en Windows 11; los recuentos y las métricas con semilla fija 46 se repiten idénticos en las mismas versiones y los tiempos de reloj varían entre equipos. **No se invocó ningún modelo de lenguaje, no se usó ninguna GPU, no se ejecutó ninguna herramienta de terceros (MLflow, Feast, Triton, KServe, Evidently, bibliotecas de equidad o de ataque) y no se evaluó ningún sistema real.** Lo que se ejecutó es código propio de la parte con numpy y scikit-learn. La parte se ejecutó solo en Windows; no se repitió en Linux.

Los experimentos son: un boosting de gradiente con cuatro fallas inyectadas en servicio, una regla de base y un bucle de realimentación con un efecto supuesto del recordatorio (`SE-601`); una característica construida con la etiqueta, un barrido de ruido de etiquetas del 0 al 40 %, una unión puntual sobre 5 000 eventos y dos definiciones de una característica (`SE-602`); 40 semillas y 40 muestras de 500 filas, 60 comparaciones pareadas de dos configuraciones, un optimismo de selección con 40 repeticiones por cada uno de cuatro números de candidatos y un registro de corrida con huellas (`SE-603`); una prevalencia baja contra un clasificador trivial, un umbral por costo, la calibración con y sin recalibración isotónica, dos grupos con una brecha de prevalencia, intervalos con bootstrap de 200 repeticiones y una validación aleatoria frente a una temporal (`SE-604`); un modelo base, tres estrategias a cinco tamaños de datos, el olvido, el conteo de parámetros de una adaptación de rango bajo y la aritmética de cómputo con la regla de seis operaciones por parámetro y por token (`SE-605`); una red de tres capas medida para lotes de 1 a 1 024, un lote dinámico simulado con 40 000 llegadas de Poisson con tres cargas, tres precisiones de pesos y la carga de un bosque serializado (`SE-606`).

Siguen un candidato con una anomalía de etiquetado sembrada en un segmento, su ejecución en sombra, la potencia de un canary con 400 repeticiones por celda, una exposición estimada y un rollback por puntero con huellas (`SE-607`); el PSI y la prueba KS con 300 ventanas por celda, una deriva de concepto y cuatro políticas de reentrenamiento durante 44 semanas (`SE-608`); una evasión lineal exacta y de caja negra, una puerta trasera con cinco fracciones de envenenamiento, la copia de un modelo con cuatro presupuestos de consultas, la inferencia de pertenencia contra dos bosques y una validación de entrada (`SE-609`); un triaje con reglas sobre ocho usos inventados, una lista de verificación de 20 elementos en cuatro estados, dos políticas de umbral por grupo y un registro encadenado de 5 000 decisiones (`SE-610`); catorce días simulados con cuatro fallas inyectadas, cuatro monitores y tres mitigaciones (`SE-611`); y un paquete de un proyecto en directorios temporales con once comprobaciones sobre archivos reales y cuatro variantes (`SE-612`).

Los parámetros (las seis características y su generador, las magnitudes de las fallas y de las derivas, el efecto del recordatorio, los candidatos, los costos de cada error, el grupo y su brecha, la anomalía de etiquetado, las llegadas y el tiempo de servicio interpolado, los umbrales de los monitores, las reglas del triaje, la lista de verificación y los umbrales de la puerta) son construcciones del autor. Ninguna cifra es una medición de un sistema de producción: los tiempos son de una CPU de escritorio compartida y varían, y las simulaciones son modelos con supuestos declarados. El precio por hora de `SE-606`, el rendimiento sostenido de 10¹⁴ operaciones por segundo de `SE-605` y las 3 horas de decisión de `SE-611` son supuestos, no hechos.

Lo que **no se hizo**: no se midió ningún equipo, esfuerzo humano ni costo económico de una organización; no se evaluó ninguna plataforma de MLOps, de almacén de características, de servicio de modelos, de monitoreo ni de gobierno; no se entrenó ni se ajustó ningún modelo de lenguaje; no se comprobó que ninguna práctica mejore un sistema real más allá de los mecanismos ejecutados; y las referencias a normas son descripciones por fuente oficial. El triaje de riesgo, la lista de verificación y el expediente de gobierno de `SE-610` no son una clasificación jurídica ni una evaluación de conformidad con el reglamento europeo, con ISO/IEC 42001 o con el marco del NIST. No se reproduce texto protegido de ninguna norma. Una revisión editorial y jurídica humana independiente de la parte sigue pendiente.

## Guía razonada clase por clase

*Avisos-ML* se vuelve un sistema operado mientras cambian las fallas que lo amenazan. Cada clase explica qué eslabón mide, qué experimento lo respalda, qué no demuestra y qué evidencia permitiría abandonar la conclusión.

### Bloque 1 — El sistema y sus entradas

#### SE-601 — Ciclo de vida de ML y por qué falla en producción

Un sistema de aprendizaje automático falla casi siempre fuera del modelo. La clase mapea diez eslabones, mide cuatro fallas con el mismo modelo (una unidad distinta, una deriva de covariables, una deriva de concepto y un historial que llega en cero), compara con una regla de base y muestra cómo las decisiones del modelo contaminan las etiquetas con que se reentrena.

El estudiante entrega el mapa de diez eslabones de un sistema suyo con dueño, modo de fallo y señal, y el diseño de un grupo de control. `SE-602` abre el primer eslabón.

#### SE-602 — Datos de entrenamiento, etiquetas y feature stores

Los datos son un producto con defectos propios. La clase mide una característica construida con la etiqueta (la mejor puntuación fuera de línea, la peor en servicio), el límite que fija el ruido de las etiquetas, una unión puntual en el tiempo frente a una ingenua y la divergencia entre dos implementaciones de la misma característica.

El estudiante entrega el contrato de datos de un modelo con la etiqueta y su retraso, la disponibilidad de cada característica y una prueba de paridad. `SE-603` toma esos datos y entrena.

#### SE-603 — Experimentos y entrenamiento reproducible

Una mejora que cabe en el ruido no es una mejora. La clase fija una corrida con huellas, mide la dispersión por semilla y por muestra con 500 filas, cuenta cuántas veces gana una configuración que en promedio es peor y estima el optimismo de elegir el mejor entre muchos con una validación pequeña.

El estudiante entrega el registro de una corrida y la regla con que declara que una configuración supera a otra. `SE-604` evalúa el modelo elegido.

### Bloque 2 — Evaluar, adaptar y servir

#### SE-604 — Evaluación, sesgos y validación de modelos

La métrica sigue a la decisión. La clase muestra la exactitud que engaña con una prevalencia del 2,8 %, deriva el umbral que minimiza el costo, mide la calibración, desglosa las tasas por grupo, explica por qué las definiciones de equidad compiten y da el ancho del intervalo según el tamaño de la evaluación.

El estudiante entrega el informe de evaluación con costo, umbral, calibración, tasas por grupo e intervalo. `SE-605` adapta el modelo a una población nueva.

#### SE-605 — Ajuste fino, adaptación y costo

Adaptar un modelo no es gratis ni siempre mejor. La clase compara no adaptar, ajustar un modelo base y entrenar desde cero con 50 a 20 000 filas, mide el olvido en la población original, cuenta los parámetros de una adaptación de rango bajo y calcula el cómputo de entrenamiento con una regla publicada y supuestos explícitos.

El estudiante entrega la decisión de adaptación con la línea base, la curva de datos, el olvido y el costo. `SE-606` sirve el modelo elegido.

#### SE-606 — Servir modelos: latencia, lotes y GPU

Un servicio de modelos se dimensiona con mediciones. La clase mide el costo por petición contra el tamaño del lote, simula un lote dinámico con carga normal y con sobrecarga, mide la cuantización y la carga de un modelo, y calcula el costo por millón de predicciones con una fórmula y un precio supuesto.

El estudiante entrega el plan de servicio con la curva de lote, la espera máxima, la política de sobrecarga y el costo. `SE-607` cambia el modelo sin parar el servicio.

### Bloque 3 — Operar y defender

#### SE-607 — Despliegue seguro de modelos: shadow, canary y rollback

El promedio aprueba lo que un segmento sufre. La clase despliega un candidato que mejora el error global y rompe un segmento, lo ve en sombra sin etiquetas, calcula la potencia de un canary según fracción y días, estima las decisiones erróneas expuestas por cada estrategia y mide un rollback que restaura las predicciones exactas.

El estudiante entrega el plan de despliegue con segmentos, guardas, potencia, rollback ensayado y criterios de parada. `SE-608` vigila el modelo desplegado.

#### SE-608 — Monitoreo, deriva y reentrenamiento

Vigilar las entradas no es vigilar la calidad. La clase mide falsas alarmas y sensibilidad del PSI según la ventana, demuestra que una deriva de concepto no se ve en las entradas y compara cuatro políticas de reentrenamiento durante 44 semanas de deriva.

El estudiante entrega el plan de monitoreo con las tres capas de señales, la política de reentrenamiento y la prueba de cada alerta. `SE-609` trata la deriva deliberada.

#### SE-609 — Seguridad y robustez de sistemas de ML

Un modelo preciso no es robusto ni un modelo cerrado es seguro. La clase mide la evasión de un modelo lineal y de uno de caja negra, la puerta trasera implantada con pocas filas, la copia de un modelo preguntando y la señal de pertenencia de un modelo que memoriza, y prueba una validación de entrada.

El estudiante entrega el modelo de amenazas con las cinco amenazas medidas, las defensas y la prueba negativa de cada una. `SE-610` reúne la evidencia bajo marcos de gobierno.

#### SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF

El nivel de obligación depende del uso y la evidencia se construye desde el diseño. La clase aplica un triaje provisional con reglas a ocho usos, mide la completitud de la documentación por área, compara las tasas por grupo con dos políticas de umbral y construye un registro encadenado que delata la alteración, sin sustituir una revisión jurídica.

El estudiante entrega un expediente de gobierno provisional con inventario, triaje, tabla de evidencia con brechas y registro verificable. `SE-611` somete el sistema a un ensayo.

### Bloque 4 — Ensayar y entregar

#### SE-611 — Taller: degradar y recuperar un modelo

Un monitor que nunca se ha disparado es una hipótesis. El taller inyecta cuatro fallas en 14 días simulados, mide cuándo alerta cada uno de cuatro monitores, calcula las decisiones expuestas hasta mitigar y compara tres respuestas a la falla de unidad, con un resultado incómodo: caer a la regla fue peor que el modelo degradado.

El estudiante entrega la matriz falla por monitor, la medida de cada mitigación, el runbook y un postmortem con acciones. `SE-612` convierte todo en una puerta.

#### SE-612 — Proyecto: sistema de ML operable con evidencia

Operable significa comprobable. El proyecto reúne manifiesto, ficha, runbook, canary, modelo anterior y monitor en un paquete con una puerta de once comprobaciones que lee archivos reales, y la prueba con tres variantes defectuosas que debe bloquear con el motivo exacto.

El estudiante entrega su paquete con la puerta, las variantes y la lista de lo que la puerta no ve. Con esta clase se cierra la parte.

## Resumen operativo del recorrido

| Clase | Núcleo profesional | Aporte acumulativo |
|---|---|---|
| [SE-601](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/) | Ciclo de vida de ML y por qué falla en producción | Entrega el mapa de diez eslabones de un sistema suyo con dueño, modo de fallo y señal, y el diseño de un grupo de control |
| [SE-602](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/) | Datos de entrenamiento, etiquetas y feature stores | Entrega el contrato de datos de un modelo con la etiqueta y su retraso, la disponibilidad de cada característica y una prueba de paridad |
| [SE-603](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/) | Experimentos y entrenamiento reproducible | Entrega el registro de una corrida y la regla con que declara que una configuración supera a otra |
| [SE-604](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/) | Evaluación, sesgos y validación de modelos | Entrega el informe de evaluación con costo, umbral, calibración, tasas por grupo e intervalo |
| [SE-605](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/) | Ajuste fino, adaptación y costo | Entrega la decisión de adaptación con la línea base, la curva de datos, el olvido y el costo |
| [SE-606](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/) | Servir modelos: latencia, lotes y GPU | Entrega el plan de servicio con la curva de lote, la espera máxima, la política de sobrecarga y el costo |
| [SE-607](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/) | Despliegue seguro de modelos: shadow, canary y rollback | Entrega el plan de despliegue con segmentos, guardas, potencia, rollback ensayado y criterios de parada |
| [SE-608](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/) | Monitoreo, deriva y reentrenamiento | Entrega el plan de monitoreo con las tres capas de señales, la política de reentrenamiento y la prueba de cada alerta |
| [SE-609](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/) | Seguridad y robustez de sistemas de ML | Entrega el modelo de amenazas con las cinco amenazas medidas, las defensas y la prueba negativa de cada una |
| [SE-610](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/) | Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF | Entrega un expediente de gobierno provisional con inventario, triaje, tabla de evidencia con brechas y registro verificable |
| [SE-611](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/) | Taller: degradar y recuperar un modelo | Entrega la matriz falla por monitor, la medida de cada mitigación, el runbook y un postmortem con acciones |
| [SE-612](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/) | Proyecto: sistema de ML operable con evidencia | Entrega su paquete con la puerta, las variantes y la lista de lo que la puerta no ve |

## Fuentes

- [Sculley et al., «Hidden Technical Debt in Machine Learning Systems»](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), [Breck et al., «The ML Test Score»](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/), [Google, «Rules of Machine Learning»](https://developers.google.com/machine-learning/guides/rules-of-ml) y [Google Cloud, «MLOps»](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — el ciclo de vida, la deuda técnica y la preparación para producción; son descripciones de prácticas, no estudios de resultados.
- [Breck et al., «Data Validation for Machine Learning»](https://mlsys.org/Conferences/2019/doc/2019/167.pdf), [Kapoor y Narayanan sobre fuga de datos](https://arxiv.org/abs/2207.07048), [Northcutt et al. sobre errores de etiqueta](https://arxiv.org/abs/2103.14749) y [Feast, «Point-in-time joins»](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — datos, etiquetas y características.
- [Pineau et al.](https://arxiv.org/abs/2003.12206), [Henderson et al.](https://arxiv.org/abs/1709.06560), [scikit-learn, «Common pitfalls»](https://scikit-learn.org/stable/common_pitfalls.html) y [NumPy, «Random Generator»](https://numpy.org/doc/stable/reference/random/generator.html) — reproducibilidad y azar.
- [scikit-learn: métricas](https://scikit-learn.org/stable/modules/model_evaluation.html), [calibración](https://scikit-learn.org/stable/modules/calibration.html) y [validación cruzada](https://scikit-learn.org/stable/modules/cross_validation.html), [Hardt et al.](https://arxiv.org/abs/1610.02413), [Kleinberg et al.](https://arxiv.org/abs/1609.05807) y [Mitchell et al., «Model Cards»](https://arxiv.org/abs/1810.03993) — evaluación, equidad y documentación.
- [Hu et al., «LoRA»](https://arxiv.org/abs/2106.09685), [Kaplan et al.](https://arxiv.org/abs/2001.08361), [Hoffmann et al.](https://arxiv.org/abs/2203.15556) y [Kirkpatrick et al.](https://arxiv.org/abs/1612.00796) — adaptación, cómputo de entrenamiento y olvido.
- [NVIDIA Triton, «Batchers»](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html), [Kwon et al.](https://arxiv.org/abs/2309.06180), [Frantar et al.](https://arxiv.org/abs/2210.17323), [scikit-learn, «Model persistence»](https://scikit-learn.org/stable/model_persistence.html) y [Google SRE, «Handling Overload»](https://sre.google/sre-book/handling-overload/) — servicio, cuantización y sobrecarga.
- [SRE Workbook, «Canarying Releases»](https://sre.google/workbook/canarying-releases/), [KServe, «Canary Rollout»](https://kserve.github.io/website/latest/modelserving/v1beta1/rollout/canary/), [MLflow, «Model Registry»](https://mlflow.org/docs/latest/model-registry/), [Rabanser et al., «Failing Loudly»](https://arxiv.org/abs/1810.11953) y [SRE Book, «Monitoring Distributed Systems»](https://sre.google/sre-book/monitoring-distributed-systems/) — despliegue, registro y monitoreo.
- [Goodfellow et al.](https://arxiv.org/abs/1412.6572), [Tramèr et al.](https://arxiv.org/abs/1609.02943), [Shokri et al.](https://arxiv.org/abs/1610.05820), [Gu et al., «BadNets»](https://arxiv.org/abs/1708.06733), [NIST AI 100-2](https://csrc.nist.gov/pubs/ai/100/2/e2025/final), [OWASP ML Top 10](https://owasp.org/www-project-machine-learning-security-top-10/) y [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) — seguridad y robustez.
- [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), [Comisión Europea, «AI Act»](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), [Gebru et al., «Datasheets»](https://arxiv.org/abs/1803.09010), [SRE Book, «Postmortem Culture»](https://sre.google/sre-book/postmortem-culture/) y [SRE Workbook, «Incident Response»](https://sre.google/workbook/incident-response/) — gobierno, regulación y operación de incidentes; las normas se citan por su fuente oficial y no se reproduce su texto.

Las fuentes se vinculan también dentro de cada clase. Definen vocabulario y describen prácticas; que una práctica convenga a un sistema se demuestra con el caso, la evidencia medida y la revisión de otra persona, no con la autoridad de la fuente. Algunas son documentación de productos o de proveedores, y las páginas de la Comisión Europea y de las normas ISO cambian con el tiempo: la fecha de consulta de esta parte es noviembre de 2026.

## Criterios de aceptación de la parte

- cada clase conecta mecanismo, medida y límite en una conclusión revisable;
- cada medida puede reproducirse desde un checkout limpio con las mismas semillas y versiones fijadas, salvo las lecturas de reloj, que declaran por qué no;
- ninguna afirmación sobre una organización, una herramienta de terceros, una plataforma o el efecto real de una práctica se apoya en una simulación o en un modelo de juguete;
- ninguna comprobación de la puerta de `SE-612` lee un indicador declarado: cada una abre un archivo y calcula, y se prueba con una variante defectuosa;
- el material de gobierno se declara provisional y no sustituye una revisión jurídica.

[Volver al índice de clases](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md)
