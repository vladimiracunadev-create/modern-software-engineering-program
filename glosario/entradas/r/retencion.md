# Retención

[↑ Glosario](../../README.md) · [← Retardo de replicación](./retardo-de-replicacion.md) · [Retención bruta y neta →](./retencion-bruta-y-neta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Plazo durante el cual se conserva cada tipo de dato.

Definición de trabajo de [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md): Plazo máximo durante el que se conserva un dato.
- En [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md): Plazo de conservación, con su costo en TB-mes.
- En [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md): Tiempo durante el que se conserva un tipo de dato y fundamento de ese plazo.
- En [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md): Política que decide qué artefactos se conservan y durante cuánto tiempo.

## Por qué importa

En [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), el tema «Retención» importa porque un plazo sin purga programada convierte el dato en pasivo.

En [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md), el tema «Retención» importa porque conservar es un costo y un riesgo.

En [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), el tema «Retención» importa porque decide si lo gastado en conseguir un cliente se recupera.

## Cómo funciona

Según [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), en la sección «Retención»:

La **retención** fija cuánto tiempo se conserva cada tipo de dato, según su finalidad y las obligaciones aplicables, que decide la institución con asesoría y no el equipo técnico solo. Una retención sin ejecución es un deseo: hace falta un trabajo programado que purgue lo vencido, una medida de cuánto hay vencido y un plazo para cada copia. Un registro de accesos que se conserva «por si acaso» crece sin límite, aumenta el daño de una filtración y puede dejar de tener base para conservarse. El plazo también cubre los respaldos: una copia con datos vencidos los conserva hasta que ella misma expira.

## Ejemplo

Ejemplo de [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) (sección «Caso conductor»):

La capa de datos de la plataforma de entregas sigue siendo el caso conductor. Esta clase deja el décimo artefacto: el inventario de datos personales con su retención, su procedimiento de borrado y su política de anonimización. `SE-359` pone a prueba lo aprendido sobre migraciones con un taller. Cambia después una sola decisión, el plazo de retención de los eventos de acceso, y observa qué cambia en el volumen, en el riesgo y en las copias.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La tabla de eventos crece sin parar** — causa: retención sin purga programada. Corrección: trabajo de purga con medida de lo vencido. ([SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md))
- **Se borran actas que debían conservarse** — causa: corte único de retención. Corrección: reglas por tipo con fundamento y retención legal. ([SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md))
- **Se guardan datos personales de hace diez años** — causa: no hay retención ni disposición. Corrección: tabla de retención y proceso de borrado verificado. ([SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **retención** fija cuánto tiempo se conserva cada tipo de dato, según su finalidad y las obligaciones aplicables, que decide la institución con asesoría y no el equipo técnico solo. ([SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md))
- Traslada el análisis a otro tipo de artefacto (un paquete de biblioteca publicado en un índice, una aplicación móvil enviada a una tienda): cambia el almacén y conserva el procedimiento de identificar por contenido, promover sin reconstruir, guardar el estado como metadatos y justificar la retención con la profundidad de los retrocesos. ([SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Costo](../c/costo.md), [Plazo](../p/plazo.md), [Registro](./registro.md), [Ciclo](../c/ciclo.md), [Consulta recursiva](../c/consulta-recursiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-369 — Gobierno, privacidad y retención de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-470 — Artefactos, repositorios y promoción](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-525 — Retiro, archivado y disposición de sistemas](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (90 clases más lo mencionan; las que más):

[SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — principios de minimización, limitación del plazo y supresión; autoridad: texto oficial de la Unión Europea.
- [NIST SP 800-88 Rev. 1](https://csrc.nist.gov/pubs/sp/800/88/r1/final) — saneamiento de medios; autoridad: NIST.
- [SQLite: PRAGMA](https://www.sqlite.org/pragma.html) — `secure_delete`; autoridad: documentación oficial de SQLite.
- [SQLite: VACUUM](https://www.sqlite.org/lang_vacuum.html) — reconstrucción del archivo; autoridad: documentación oficial de SQLite.
- [Sweeney, «k-anonymity»](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: artículo original (2002).

---

[↑ Glosario](../../README.md) · [← Retardo de replicación](./retardo-de-replicacion.md) · [Retención bruta y neta →](./retencion-bruta-y-neta.md)
