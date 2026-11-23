# Caso de abuso

[↑ Glosario](../../README.md) · [← Caso coherente](./caso-coherente.md) · [Caso de seguridad →](./caso-de-seguridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Descripción de cómo alguien con mala intención podría usar una funcionalidad prevista para dañar el sistema o a otras personas.

Definición de trabajo de [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

## Por qué importa

En [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), el tema «Casos de abuso» importa porque convierte lo que nadie escribió en un requisito comprobable.

## Cómo funciona

Según [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md):

Una historia de usuario describe el uso previsto («como estudiante, subo una entrega con un adjunto para el curso»). Un **caso de abuso** describe qué haría alguien que quiere dañar el sistema con esa misma funcionalidad. Para la subida de la plataforma: un archivo de tamaño cero o de 20 MB, un nombre con separadores de ruta o NUL, una extensión doble, un tipo MIME que no coincide con la extensión, un identificador de curso ajeno, un adjunto con contenido activo (HTML, script), la misma entrega repetida diez mil veces, un nombre de 10 000 caracteres, una subida concurrente que supera la cuota, una subida después del plazo. Cada abuso se convierte en un **requisito negativo** («el sistema rechaza…») y en una prueba que falla si la defensa se rompe.

Según [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md):

El equipo toma la historia «subir una entrega con un adjunto», escribe doce casos de abuso con otra persona que no la implementó y los convierte en requisitos negativos con pruebas parametrizadas. Mide la suite con una lista de mutantes del validador y exige que la integración continua falle si el número de mutantes vivos sube. Añade las reglas de `ast` que impiden volver a los patrones que ya causaron incidentes (`shell=True`, `yaml.load`, `eval`) con una guía de supresión que exige una razón escrita; mantiene la revisión de cambios con una pregunta de abuso por cambio, no con una casilla. Prueba cada expresión regular que reciba entrada de usuario con una cadena que casi coincide y fija un límite de longitud y de tiempo.

## Ejemplo

Ejemplo de [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) (sección «Ejemplo profesional»):

El equipo toma la historia «subir una entrega con un adjunto», escribe doce casos de abuso con otra persona que no la implementó y los convierte en requisitos negativos con pruebas parametrizadas. Mide la suite con una lista de mutantes del validador y exige que la integración continua falle si el número de mutantes vivos sube. Añade las reglas de `ast` que impiden volver a los patrones que ya causaron incidentes (`shell=True`, `yaml.load`, `eval`) con una guía de supresión que exige una razón escrita; mantiene la revisión de cambios con una pregunta de abuso por cambio, no con una casilla.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los incidentes se repiten** — causa: el aprendizaje no vuelve al catálogo. Corrección: cada incidente añade un caso de abuso y una prueba. ([SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): validador y reglas con cifras idénticas; la medición de la expresión regular es una lectura de reloj de cada equipo. No se usó ninguna herramienta de análisis comercial ni se evaluó el proceso de un equipo; el validador, los mutantes, los fragmentos y las reglas son construcciones del autor y los porcentajes marcan una frontera, no una tasa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intención](../i/intencion.md), [Análisis estático](../a/analisis-estatico.md), [Fuzzing](../f/fuzzing.md), [Mutante equivalente](../m/mutante-equivalente.md), [Requisito negativo](../r/requisito-negativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-464 — Secure SDLC, abuso y pruebas negativas](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) — casos de abuso; autoridad: OWASP.
- [NIST SP 800-218 (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro; autoridad: NIST.
- [OWASP SAMM](https://owaspsamm.org/) — modelo de madurez del software seguro; autoridad: OWASP.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — procedimientos de prueba; autoridad: OWASP.
- [Jia y Harman, 2011](https://doi.org/10.1109/TSE.2010.62) — pruebas de mutación; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Caso coherente](./caso-coherente.md) · [Caso de seguridad →](./caso-de-seguridad.md)
