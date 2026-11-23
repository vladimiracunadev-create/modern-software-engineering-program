# Caos de seguridad

[↑ Glosario](../../README.md) · [← Canonicalización](./canonicalizacion.md) · [Capa →](./capa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Aplicación del método de la ingeniería del caos a los controles de seguridad.

Definición de trabajo de [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md).

## Por qué importa

En [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), el tema «Caos de seguridad frente a intrusión» importa porque una prueba pregunta si el control funciona; la otra, si alguien puede entrar.

## Cómo funciona

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

El **caos de seguridad** aplica el método (estado estable, hipótesis, falla inyectada, comparación) a los controles de seguridad: la pregunta es «¿el control sigue funcionando cuando algo falla o cambia?». Los ejemplos son concretos: ¿una credencial revocada deja de funcionar?, ¿una regla de red mal puesta se detecta?, ¿el registro de auditoría sigue escribiéndose si su almacén se llena?, ¿qué ocurre si un certificado vence?, ¿el sistema falla cerrado (niega acceso) o abierto (lo permite) cuando el servicio de autorización no responde? Netflix incluyó esa idea desde 2011 con Security Monkey, extensión de Conformity Monkey: busca violaciones de seguridad o vulnerabilidades, como grupos de seguridad mal configurados, termina las instancias que las presentan y comprueba que los certificados SSL y DRM sean válidos y no estén por vencer.

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

No. Una prueba de intrusión explora si alguien puede entrar por caminos que nadie previó; el caos de seguridad comprueba que los controles previstos funcionan cuando cambian las condiciones. Responden preguntas distintas y se complementan.

## Ejemplo

Ejemplo de [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) (sección «Preguntas frecuentes»):

No. Una prueba de intrusión explora si alguien puede entrar por caminos que nadie previó; el caos de seguridad comprueba que los controles previstos funcionan cuando cambian las condiciones. Responden preguntas distintas y se complementan.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md)) son:

- **«Revocación inmediata» no lo es** — causa: caché de autorización sin invalidación. Corrección: medir la exposición y ajustar la vigencia o invalidar.
- **Un control débil aprueba la auditoría** — causa: pocos ensayos. Corrección: fijar ensayos acordes a la cota que se afirma.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes enlazadas. Se ejecutaron tres experimentos con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se atacó, auditó ni revocó nada real; los 30 controles, sus eficacias, los 2 000 clientes, las vigencias de caché y el criterio «cero fallas» son construcciones del autor, y la clase no sustituye una auditoría ni una prueba de intrusión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ingeniería del caos](../i/ingenieria-del-caos.md), [Ingeniería](../i/ingenieria.md), [Seguridad](../s/seguridad.md), [Criterio de aceptación](./criterio-de-aceptacion.md), [Ensayo](../e/ensayo.md), [Evidencia de cumplimiento](../e/evidencia-de-cumplimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — Security Monkey y verificación de certificados; autoridad: blog de ingeniería de Netflix.
- [Reglamento (UE) 2022/2554 sobre resiliencia operativa digital del sector financiero](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — pruebas de resiliencia como requisito regulatorio; autoridad: Diario Oficial de la Unión Europea.
- [NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planificación, prueba y mantenimiento de contingencias; autoridad: National Institute of Standards and Technology.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y medir la salida; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [IETF RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) — validez temporal de los certificados X.509; autoridad: Internet Engineering Task Force.

---

[↑ Glosario](../../README.md) · [← Canonicalización](./canonicalizacion.md) · [Capa →](./capa.md)
