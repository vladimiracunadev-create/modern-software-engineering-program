# Tiempo hasta detectar

[↑ Glosario](../../README.md) · [← Tiempo del evento](./tiempo-del-evento.md) · [Tiempo, plazos y zonas →](./tiempo-plazos-y-zonas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md)

## Definición

Horas entre la falla y la primera alerta.

Definición de trabajo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md).

## Por qué importa

La clase donde se define, [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), existe con este propósito: la clase existe para que decidas cómo llevar una versión nueva a producción de forma que un defecto dañe a pocas personas, se detecte pronto y se pueda deshacer.

## Cómo funciona

Según [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md), en la sección «Tiempo hasta detectar»:

Con 400 solicitudes por segundo, un error de base del 0,5 % y un defecto que lo sube al 1,5 %, se simulan 40 semillas para cinco fracciones de tráfico del canario y una prueba de dos proporciones con z = 3, evaluada cada segundo durante 30 minutos. Se cuentan los errores extra que sufren las personas antes de la detección.

**Cómo leer la figura.** El eje horizontal es la fracción de tráfico del canario y el vertical el tiempo hasta detectar, los dos en escala logarítmica. La línea turquesa es la mediana y la coral el percentil 95. Mira cómo se cierran las dos líneas: con más tráfico la detección es más rápida y la cola se acorta de 268 a 17 segundos. **Dónde deja de valer:** el defecto es un aumento constante y el tráfico llega de forma uniforme; con tráfico en ráfagas, o con un defecto que solo aparece en algunos segmentos o tras un tiempo (una fuga de memoria), el tiempo de detección es otro. Los valores son medianas de 40 semillas y los percentiles altos tienen más incertidumbre.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md):

El equipo de la API de entregas despliega cada versión en cuatro fases: 1 % durante diez minutos, 5 % durante veinte, 25 % durante treinta y 100 % con la versión anterior conservada una hora.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)) son:

- **El despliegue se revierte sin defecto** — causa: umbral de decisión única evaluado repetidamente. Corrección: umbral mayor, mínimo de muestra o prueba secuencial.
- **Un defecto pequeño no se detecta** — causa: canario y ventana insuficientes. Corrección: definir el defecto mínimo relevante y dimensionar para él.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron cuatro simulaciones con semilla fija y tiempo virtual, idénticas en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Blue-green](../b/blue-green.md), [Escalón de tráfico](../e/escalon-de-trafico.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Exposición](../e/exposicion.md), [Falsa alarma](../f/falsa-alarma.md), [Inyección de fallas](../i/inyeccion-de-fallas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CanaryRelease»](https://martinfowler.com/bliki/CanaryRelease.html) — despliegue progresivo; autoridad: autor del texto.
- [Fowler, «BlueGreenDeployment»](https://martinfowler.com/bliki/BlueGreenDeployment.html) — dos entornos y cambio de tráfico; autoridad: autor del texto.
- [Google SRE Workbook: Canarying Releases](https://sre.google/workbook/canarying-releases/) — diseño de un canario; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [Google SRE: Release Engineering](https://sre.google/sre-book/release-engineering/) — entrega y retroceso; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Tiempo del evento](./tiempo-del-evento.md) · [Tiempo, plazos y zonas →](./tiempo-plazos-y-zonas.md)
