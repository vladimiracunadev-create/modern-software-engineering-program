# Huella canónica

[↑ Glosario](../../README.md) · [← Huella (resumen) SHA-256](./huella-resumen-sha-256.md) · [Huella de bloque →](./huella-de-bloque.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Resumen criptográfico calculado sobre una representación con orden, codificación y finales de línea fijados.

Definición de trabajo de [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md).

## Por qué importa

La clase donde se define, [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), existe con este propósito: el proyecto existe para que entregues un producto cuya seguridad otra persona pueda comprobar sin creerte: requisitos de verificación elegidos con un criterio, cada uno con su prueba, su evidencia con fecha y huella, un validador que revisa el paquete y una lista honesta de lo que ninguna comprobación ve.

## Cómo funciona

Según [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md):

Una huella que depende del orden de `os.listdir`, de los finales de línea o del separador de ruta cambia entre sistemas aunque el contenido sea el mismo. La huella canónica ordena las rutas, usa separador `/`, normaliza `\r\n` a `\n` y fija la codificación. Es la misma idea de reproducibilidad que defiende Reproducible Builds para los binarios.

Según [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md):

El equipo selecciona 30 requisitos por amenaza, genera el paquete en cada versión, ejecuta el validador en la integración continua en Windows y Ubuntu, compara las huellas canónicas y publica `LIMITES.md`. Una persona ajena revisa por muestreo estratificado (`SE-466`) y en especial las evidencias que el validador no puede juzgar. En el modelo de la clase el validador completo detecta 195 de 210 mutaciones.

## Ejemplo

Ejemplo de [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) (sección «Ejemplo profesional»):

El equipo selecciona 30 requisitos por amenaza, genera el paquete en cada versión, ejecuta el validador en la integración continua en Windows y Ubuntu, compara las huellas canónicas y publica `LIMITES.md`. Una persona ajena revisa por muestreo estratificado (`SE-466`) y en especial las evidencias que el validador no puede juzgar. En el modelo de la clase el validador completo detecta 195 de 210 mutaciones.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La huella cambia entre sistemas** — causa: orden, finales de línea o separadores. Corrección: huella canónica. ([SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Aplica el proyecto a otro producto (por ejemplo, la aplicación de citas de un taller): cambia los requisitos y conserva la selección por amenaza, el validador medido, la huella canónica y los límites. ([SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Codificación](../c/codificacion.md), [Huella](./huella.md), [Representación](../r/representacion.md), [Sobre](../s/sobre.md), [Excepción](../e/excepcion.md), [Paquete de evidencia](../p/paquete-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md).

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

[↑ Glosario](../../README.md) · [← Huella (resumen) SHA-256](./huella-resumen-sha-256.md) · [Huella de bloque →](./huella-de-bloque.md)
