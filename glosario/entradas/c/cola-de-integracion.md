# Cola de integración

[↑ Glosario](../../README.md) · [← Cola de fusión](./cola-de-fusion.md) · [Cola de mensajes fallidos →](./cola-de-mensajes-fallidos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Mecanismo que verifica cada cambio combinado con los que lo preceden antes de integrarlo.

Definición de trabajo de [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md).

## Por qué importa

En [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), el tema «Choques semánticos y cola de integración» importa porque dos cambios correctos por separado pueden fallar juntos; probar contra una base vieja no lo ve.

## Cómo funciona

Según [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md):

Un conflicto de fusión es lo que git detecta; un **choque semántico** es lo que git no puede detectar: dos cambios que tocan archivos distintos y juntos rompen una suposición compartida (uno renombra un campo que el otro empieza a leer). Cada cambio pasó su verificación contra la base en la que nació; ninguno fue probado contra el resultado de integrar ambos. La defensa es probar la combinación: una **cola de integración** toma cada cambio aprobado, lo combina virtualmente con los que están por delante y solo lo integra si esa combinación pasa. No elimina el choque: lo transforma en un rechazo al entrar, antes de que la troncal quede en rojo para todos.

Según [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md):

El equipo de la API de entregas revisa su historial: las ramas viven nueve días de mediana, el 60 % de las fusiones tiene conflictos y el viernes por la tarde se fusiona todo. Con el modelo de la primera figura estiman que a esa vida casi toda rama choca con algo; con la segunda, que verificar de a diez cambios es razonable porque su tasa de defectos ronda el 4 %.

## Ejemplo

Ejemplo de [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas revisa su historial: las ramas viven nueve días de mediana, el 60 % de las fusiones tiene conflictos y el viernes por la tarde se fusiona todo. Con el modelo de la primera figura estiman que a esa vida casi toda rama choca con algo; con la segunda, que verificar de a diez cambios es razonable porque su tasa de defectos ronda el 4 %.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md)) son:

- **Hay un servidor de integración y la troncal pasa días en rojo** — causa: no hay política de reacción ni dueño. Corrección: escribir quién actúa ante un rojo y en cuánto tiempo; revertir primero.
- **Las fusiones del viernes duran toda la tarde** — causa: ramas largas que se integran en lote. Corrección: acortar ramas, usar banderas para lo inacabado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La defensa es probar la combinación: una **cola de integración** toma cada cambio aprobado, lo combina virtualmente con los que están por delante y solo lo integra si esa combinación pasa. ([SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-480](../../../classes/part-39-build-release-y-cadena-de-suministro/se-480-proyecto-release-firmado-y-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [Bisección](../b/biseccion.md), [Conflicto semántico](./conflicto-semantico.md), [Integración continua](../i/integracion-continua.md), [Troncal](../t/troncal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — prácticas de la integración continua; autoridad: Martin Fowler, texto de referencia del campo.
- [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/) — descripción de las ramas de corta vida y las banderas; autoridad: Paul Hammant, sitio de referencia comunitario.
- [GitHub: gestionar una cola de fusión](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) — funcionamiento de una cola de fusión; autoridad: documentación de GitHub.
- [git bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria del primer cambio defectuoso; autoridad: documentación de git.

---

[↑ Glosario](../../README.md) · [← Cola de fusión](./cola-de-fusion.md) · [Cola de mensajes fallidos →](./cola-de-mensajes-fallidos.md)
