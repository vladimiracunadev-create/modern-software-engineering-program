# Validador de paquete

[↑ Glosario](../../README.md) · [← Validador de forma](./validador-de-forma.md) · [Validador de presencia →](./validador-de-presencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Programa que comprueba la estructura y la coherencia del paquete sin juzgar si la evidencia prueba el requisito.

Definición de trabajo de [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md).

## Por qué importa

La clase donde se define, [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), existe con este propósito: el proyecto existe para que entregues un producto cuya seguridad otra persona pueda comprobar sin creerte: requisitos de verificación elegidos con un criterio, cada uno con su prueba, su evidencia con fecha y huella, un validador que revisa el paquete y una lista honesta de lo que ninguna comprobación ve.

## Cómo funciona

[SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md):

El equipo selecciona 30 requisitos por amenaza, genera el paquete en cada versión, ejecuta el validador en la integración continua en Windows y Ubuntu, compara las huellas canónicas y publica `LIMITES.md`. Una persona ajena revisa por muestreo estratificado (`SE-466`) y en especial las evidencias que el validador no puede juzgar. En el modelo de la clase el validador completo detecta 195 de 210 mutaciones.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md)) son:

- **La huella cambia entre sistemas** — causa: orden, finales de línea o separadores. Corrección: huella canónica.
- **Tres requisitos con la misma evidencia** — causa: evidencia copiada. Corrección: regla de huellas repetidas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron dos experimentos en Windows y Ubuntu (WSL2): el validador con cifras idénticas y la huella con diferencias por diseño. Los requisitos, mutaciones y validadores son del autor; no se evaluó ningún producto real. La [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md) pasa a build, release y cadena de suministro.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Evidencia](../e/evidencia.md), [Paquete](../p/paquete.md), [Excepción](../e/excepcion.md), [Huella canónica](../h/huella-canonica.md), [Paquete de evidencia](../p/paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) — requisitos de verificación; autoridad: OWASP.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.
- [Reproducible Builds](https://reproducible-builds.org/) — verificación independiente; autoridad: proyecto Reproducible Builds.
- [OWASP SAMM](https://owaspsamm.org/) — madurez; autoridad: OWASP.
- [Jia y Harman, 2011](https://doi.org/10.1109/TSE.2010.62) — mutación; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Validador de forma](./validador-de-forma.md) · [Validador de presencia →](./validador-de-presencia.md)
