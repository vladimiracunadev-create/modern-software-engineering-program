# Vigencia de la caché

[↑ Glosario](../../README.md) · [← Vigencia](./vigencia.md) · [Virtualización de lista →](./virtualizacion-de-lista.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

La **vigencia de la caché** (TTL, *time to live*) es el tiempo máximo durante el cual un dato guardado puede reutilizarse sin comprobarse de nuevo. El programa la aplica en contextos distintos:

- **Registros DNS** ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)): tiempo máximo indicado para reutilizar un dato en caché.
- **Respuestas HTTP** ([SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md)): tiempo durante el cual una respuesta guardada se considera fresca.
- **Valores de aplicación** ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)): tiempo máximo que un valor puede servirse desde la caché sin comprobarse.
- **Decisiones de autorización** ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md)): tiempo durante el cual un cliente reutiliza una decisión sin consultarla.
- **Recursos temporales** ([SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md)): tiempo máximo de vida de un recurso tras el cual se destruye salvo que se renueve.

## Por qué importa

La vigencia es la cuantificación de «cuánto aceptamos estar desactualizados» a cambio de velocidad y menor carga. Es una decisión de producto además de técnica: determina cuánto tarda en notarse un cambio y, en seguridad, cuánto tiempo sigue siendo válida una decisión revocada.

## Cómo funciona

Durante la vigencia, quien tiene la copia no pregunta al origen; al expirar, vuelve a consultar. De ahí se derivan consecuencias medibles:

- **Exposición tras revocación** ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md)): si la revocación ocurre en un instante cualquiera, cada cliente conserva el acceso hasta que expire su entrada, a una distancia uniforme entre 0 y TTL; la exposición media es TTL/2 y la máxima, TTL. El experimento de la clase calcula, con 2 000 clientes que hacen 0,5 peticiones por segundo, las exposiciones y las peticiones autorizadas para cinco vigencias.
- **Propagación** ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)): TTL limita cuánto tiempo puede reutilizarse un registro; no fija una hora universal de propagación. Las respuestas negativas también pueden almacenarse.
- **Expiraciones simultáneas** ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)): tras un despliegue con caché fría, todas las entradas expiran a la vez y la base se satura.

## Ejemplo

Antes de migrar un servicio, bajar el TTL del registro DNS de 3600 s a 60 s con anticipación. Así, cuando se cambia el destino, las cachés de resolvedores que respetan la política expiran pronto. Ilustración de cálculo de [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

```python
ttl = 300
exposicion_media = ttl / 2    # 150 s
exposicion_maxima = ttl       # 300 s
```

## Errores y confusiones comunes

- **Cambiar un registro y esperar efecto inmediato.** Causa: el TTL anterior y las cachés demoran la propagación; corrección: bajar el TTL antes del cambio y esperar su expiración ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)).
- **Los docentes ven notas viejas.** Causa: TTL largo en datos que cambian; corrección: TTL corto o invalidación al cambiar, y revalidación condicional ([SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md)).
- **La base se satura tras un despliegue.** Causa: caché fría y expiraciones simultáneas; corrección: variar el TTL, precalentar escalonadamente y recarga única ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)).

## Límites y cuándo no aplica

Reducir el TTL antes de una migración reduce la persistencia futura, pero no invalida copias ya almacenadas ni clientes que incumplen la política ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)). En autorización, un TTL corto no equivale a revocación inmediata. Y la vigencia aplica a copias; si el dato debe ser siempre el más reciente, no corresponde una caché sin validación.

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
