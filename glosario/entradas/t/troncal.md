# Troncal

[↑ Glosario](../../README.md) · [← Trinquete](./trinquete.md) · [Trozo →](./trozo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Línea de desarrollo de la que parte y a la que vuelve el trabajo de todo el equipo.

Definición de trabajo de [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md).

## Por qué importa

La clase donde se define, [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), existe con este propósito: la clase existe para que dejes de tratar la integración continua como un servidor que «corre builds» y la trates como una práctica con consecuencias medibles: cada cuánto se integra el trabajo de varias personas, cuánto cuesta cada integración tardía, cuánto tarda la señal de que algo se rompió y quién actúa cuando aparece.

## Cómo funciona

Según [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md):

Integrar significa combinar el trabajo de varias personas en una línea común y comprobar que el resultado funciona. La integración continua conserva esa definición y cambia la frecuencia y la forma: cada persona integra al menos una vez al día en la troncal, cada integración dispara una verificación automática y una verificación en rojo se corrige antes de seguir añadiendo cambios. Fowler enumera las prácticas que la sostienen: un único repositorio de referencia, una construcción automatizada, pruebas que se ejecutan en esa construcción, integraciones frecuentes, construcción de cada integración en una máquina de integración, construcción rápida, un entorno de prueba parecido al de producción, visibilidad del estado y, en su evolución, despliegue automático.

Según [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md):

El equipo de la API de entregas revisa su historial: las ramas viven nueve días de mediana, el 60 % de las fusiones tiene conflictos y el viernes por la tarde se fusiona todo. Con el modelo de la primera figura estiman que a esa vida casi toda rama choca con algo; con la segunda, que verificar de a diez cambios es razonable porque su tasa de defectos ronda el 4 %.

## Ejemplo

Ejemplo de [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas revisa su historial: las ramas viven nueve días de mediana, el 60 % de las fusiones tiene conflictos y el viernes por la tarde se fusiona todo. Con el modelo de la primera figura estiman que a esa vida casi toda rama choca con algo; con la segunda, que verificar de a diez cambios es razonable porque su tasa de defectos ronda el 4 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Hay un servidor de integración y la troncal pasa días en rojo** — causa: no hay política de reacción ni dueño. Corrección: escribir quién actúa ante un rojo y en cuánto tiempo; revertir primero. ([SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuanto más vive la rama, más cambios acumula la troncal que la rama no ha visto y mayor es la probabilidad de que ambos lados hayan modificado un mismo archivo. ([SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md))
- **una integración semanal que fusiona muchas ramas y deja una troncal roja sin causa evidente**. ([SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](./trabajo.md), [Bisección](../b/biseccion.md), [Cola de integración](../c/cola-de-integracion.md), [Conflicto semántico](../c/conflicto-semantico.md), [Integración continua](../i/integracion-continua.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — prácticas de la integración continua; autoridad: Martin Fowler, texto de referencia del campo.
- [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/) — descripción de las ramas de corta vida y las banderas; autoridad: Paul Hammant, sitio de referencia comunitario.
- [GitHub: gestionar una cola de fusión](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) — funcionamiento de una cola de fusión; autoridad: documentación de GitHub.
- [git bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria del primer cambio defectuoso; autoridad: documentación de git.

---

[↑ Glosario](../../README.md) · [← Trinquete](./trinquete.md) · [Trozo →](./trozo.md)
