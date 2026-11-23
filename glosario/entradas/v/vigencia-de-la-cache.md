# Vigencia de la caché

[↑ Glosario](../../README.md) · [← Vigencia](./vigencia.md) · [Virtualización de lista →](./virtualizacion-de-lista.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Tiempo durante el cual un cliente reutiliza una decisión de autorización sin consultarla.

Definición de trabajo de [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md): Tiempo máximo indicado para reutilizar un dato en caché.
- En [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md): Tiempo durante el cual una respuesta guardada se considera fresca.
- En [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md): Tiempo máximo que un valor puede servirse desde la caché sin comprobarse.
- En [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md): Tiempo máximo de vida de un recurso tras el cual se destruye salvo que se renueve.

## Por qué importa

La clase donde se define, [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), existe con este propósito: la clase trata el aprendizaje que deja un experimento (cuántos ensayos sostienen una conclusión, cómo se clasifican los hallazgos y qué evidencia queda), usando como dominio los controles de seguridad y de cumplimiento.

## Cómo funciona

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

Una afirmación clásica de política es «el acceso se revoca de inmediato». Se mide con un experimento: se revoca una credencial y se comprueba cuánto tiempo y cuántas peticiones siguen siendo autorizadas. El mecanismo que lo alarga es la **caché de autorización**: cada cliente guarda la decisión durante una vigencia (TTL) y la revisa al expirar. Si la revocación ocurre en un instante cualquiera, cada cliente conserva el acceso hasta que expire su entrada, que está a una distancia uniforme entre 0 y TTL; la exposición media es TTL/2 y la máxima, TTL. Con 2 000 clientes que hacen 0,5 peticiones por segundo, se calculan las exposiciones y las peticiones autorizadas para cinco vigencias.

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

TTL limita cuánto tiempo puede reutilizarse un registro, no fija una hora universal de propagación. Respuestas negativas también pueden almacenarse. Reducir TTL antes de una migración reduce cierta persistencia futura, pero no invalida copias ya almacenadas ni clientes que incumplen la política.

## Ejemplo

Ejemplo de [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) (sección «Caso conductor»):

El acceso a la API de entregas sigue siendo el caso conductor. Esta clase deja el décimo artefacto: criterios de aceptación de controles con su evidencia. `SE-515` ejecuta un experimento acotado con criterio de aborto y `SE-516` reúne todo en un programa con validador y huella. Cambia después un solo dato, la vigencia de la caché, y observa cuántas peticiones siguen autorizadas tras una revocación.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Cambiar un registro y esperar efecto inmediato** — causa: el TTL anterior y las cachés demoran la propagación. Corrección: bajar el TTL antes del cambio y esperar su expiración. ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md))
- **Los docentes ven notas viejas** — causa: TTL largo en datos que cambian. Corrección: TTL corto o invalidación al cambiar; revalidación condicional. ([SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md))
- **La base se satura tras un despliegue** — causa: caché fría y expiraciones simultáneas. Corrección: variar el TTL, precalentar escalonadamente y recarga única. ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- TTL limita cuánto tiempo puede reutilizarse un registro, no fija una hora universal de propagación. ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md))
- Añade en un dominio de laboratorio un registro con destino incorrecto y TTL corto, o usa un nombre reservado. ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Autorización](../a/autorizacion.md), [Recurso](../r/recurso.md), [Valor](./valor.md), [429](../0-9/429.md), [Alcance](../a/alcance.md), [Autoritativo](../a/autoritativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-488 — Entornos preview y datos seguros](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.
- [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «TTL».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — Security Monkey y verificación de certificados; autoridad: blog de ingeniería de Netflix.
- [Reglamento (UE) 2022/2554 sobre resiliencia operativa digital del sector financiero](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — pruebas de resiliencia como requisito regulatorio; autoridad: Diario Oficial de la Unión Europea.
- [NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planificación, prueba y mantenimiento de contingencias; autoridad: National Institute of Standards and Technology.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y medir la salida; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [IETF RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) — validez temporal de los certificados X.509; autoridad: Internet Engineering Task Force.

---

[↑ Glosario](../../README.md) · [← Vigencia](./vigencia.md) · [Virtualización de lista →](./virtualizacion-de-lista.md)
