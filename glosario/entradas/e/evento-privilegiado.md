# Evento privilegiado

[↑ Glosario](../../README.md) · [← Evento de uso](./evento-de-uso.md) · [Evento tardío →](./evento-tardio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Un **evento privilegiado** es un evento de activación de un flujo de integración continua cuyo flujo se ejecuta con secretos y permisos de escritura aunque lo origine un tercero. Es la definición de trabajo de [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), que lo ejemplifica con `pull_request_target` de GitHub Actions. Es un concepto de seguridad de la cadena de entrega: lo peligroso no es el evento por sí mismo, sino el privilegio con el que corre.

## Por qué importa

Cambia una decisión de configuración de CI aparentemente inocente: «¿qué evento dispara este flujo?». Un flujo disparado por una solicitud de cambio de una bifurcación externa puede ejecutarse con los secretos del repositorio. Si además ejecuta el código del cambio, un tercero cualquiera consigue ejecutar código propio con esos secretos y permisos de escritura. [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) llama a ese patrón «solicitud pwn».

## Cómo funciona

[SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) contrasta dos eventos:

- **`pull_request`**: ejecuta el flujo *del cambio*, con permisos reducidos y sin secretos cuando viene de una bifurcación. Es seguro por diseño porque el código no revisado corre sin credenciales.
- **`pull_request_target`**: ejecuta el flujo de la **rama base**, con acceso a secretos y permisos de escritura. Está pensado para tareas como etiquetar o comentar, que necesitan escribir.

El peligro aparece al **combinar** el evento privilegiado con una descarga del código del cambio (por ejemplo, `ref` apuntando al SHA de la cabeza de la solicitud) y ejecutarlo: código no revisado se ejecuta con privilegios completos. La causa es la confusión de dos propiedades que normalmente van juntas: «qué flujo corre» (el de la base, de confianza) y «qué código procesa» (el de un tercero, no confiable).

Defensas de la clase: no descargar ni ejecutar código del cambio en un evento privilegiado, o **dividir el trabajo en dos flujos**: uno sin privilegios que construye y prueba, y otro privilegiado que solo consume el resultado como datos, nunca como código.

## Ejemplo

Un flujo se dispara con `pull_request_target` para comentar el resultado de las pruebas. Para ello descarga el código de la solicitud y ejecuta las pruebas. Una persona externa abre una solicitud cuyo script de pruebas lee las credenciales del entorno y las envía fuera. Como el flujo corre con secretos, la fuga funciona. Corregido: un primer flujo con `pull_request` construye y prueba sin secretos y guarda el resultado como artefacto; un segundo flujo privilegiado lee ese resultado *como datos* y publica el comentario. (Ilustración construida a partir del patrón de [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).)

## Errores y confusiones comunes

- **Una solicitud externa accede a secretos.** Causa: evento privilegiado más código del cambio; corrección ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md)): `pull_request` o dos flujos separados.
- **Creer que «corre el flujo de la base, luego es seguro».** Lo es solo mientras no procese código del tercero.
- **Tratar el resultado del flujo no privilegiado como confiable.** Se consume como datos: se valida, no se ejecuta ni se interpola en comandos.
- **Dar permisos amplios por defecto.** Reducir los permisos del flujo al mínimo necesario limita el daño si algo falla.

## Límites y cuándo no aplica

Es un término de la clase de CI/CD y del modelo de GitHub Actions; otras plataformas tienen eventos equivalentes con otros nombres, y el principio (separar el privilegio del código no confiable) se traslada, pero el detalle no. Dentro de un repositorio privado con colaboradores de confianza el riesgo baja, pero no desaparece: una dependencia o una rama comprometidas tienen el mismo efecto. Dividir en dos flujos reduce el riesgo, no lo elimina si el segundo flujo trata los datos como comandos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activación](../a/activacion.md), [Evento](./evento.md), [Flujo](../f/flujo.md), [Permiso](../p/permiso.md), [Fijar por SHA](../f/fijar-por-sha.md), [Hallazgo](../h/hallazgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Eventos privilegiados».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — fijar acciones, variables intermedias y permisos; autoridad: documentación de GitHub.
- [GitHub Security Lab: preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/) — riesgo de `pull_request_target` con código del cambio; autoridad: GitHub Security Lab.
- [GitHub Actions: eventos que activan flujos](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) — contexto de ejecución de cada evento; autoridad: documentación de GitHub.
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) — catálogo de riesgos de canalizaciones; autoridad: OWASP.
- [OpenSSF Scorecard](https://github.com/ossf/scorecard) — auditoría automática de prácticas de seguridad de repositorios; autoridad: OpenSSF.

---

[↑ Glosario](../../README.md) · [← Evento de uso](./evento-de-uso.md) · [Evento tardío →](./evento-tardio.md)
