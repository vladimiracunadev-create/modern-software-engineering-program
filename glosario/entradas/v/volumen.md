# Volumen

[↑ Glosario](../../README.md) · [← Volatilidad](./volatilidad.md) · [Votación →](./votacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Número de filas de una carga o partición.

Definición de trabajo de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md): Unidad lógica con espacio de nombres y sistema de archivos asociados.

## Por qué importa

En [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), el tema «Volumen» importa porque detecta cargas parciales, duplicados y ausencias.

## Cómo funciona

Según [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

Volumen: ¿llegaron las filas esperadas? Unicidad: ¿hay claves repetidas? Nulos: ¿falta lo que debería estar? Integridad referencial: ¿cada clave extranjera apunta a algo? Frescura: ¿es reciente el dato más nuevo? Distribución: ¿se parecen los valores a lo habitual? En el laboratorio, una tabla de 5 000 pedidos recibió seis variantes defectuosas. La carga parcial falló el volumen; los duplicados fallaron volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. La variante limpia no falló ninguna. Ninguna comprobación vio más de dos variantes: su ceguera es tan importante como su vista.

Según [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

El equipo de *Avisos* levanta una tabla con sus diez conjuntos de datos más consultados y, para cada uno, anota qué comprobaciones tiene. Encuentra que tres tienen solo validación de esquema. Prioriza por impacto: el hecho de lecturas recibe volumen, unicidad, nulos y frescura; el mart ejecutivo, distribución además de volumen. Define la política: unicidad y volumen detienen la publicación; la distribución publica con una marca. Fija una métrica del propio sistema: el porcentaje de alertas que terminaron en una acción (corregir, ajustar umbral, aceptar con anotación). A los dos meses, la métrica baja del 30 % al 12 % de acciones y el equipo recalibra la mediana por día de la semana en tres conjuntos antes de que alguien silencie el canal.

## Ejemplo

Ejemplo de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) (sección «Ejemplo mínimo»):

Una comprobación de volumen con estacionalidad:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La carga parcial falló el volumen; los duplicados fallaron volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. ([SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md))
- **Fallo.** El lunes, el panel muestra la mitad de las entregas y las alertas de volumen no sonaron. ([SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espacio de nombres](../e/espacio-de-nombres.md), [Partición](../p/particion.md), [Comprobación de calidad](../c/comprobacion-de-calidad.md), [Deriva de distribución](../d/deriva-de-distribucion.md), [Directorio de trabajo](../d/directorio-de-trabajo.md), [Enlace simbólico](../e/enlace-simbolico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-026 — Sistemas de archivos, rutas, enlaces y metadatos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (72 clases más lo mencionan; las que más):

[SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_16) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Naming Files, Paths, and Namespaces](https://learn.microsoft.com/windows/win32/fileio/naming-a-file) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Python documentation — pathlib](https://docs.python.org/3/library/pathlib.html) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Apple Platform Deployment — File system basics](https://support.apple.com/guide/deployment/intro-to-file-system-apd0b895e8e1/web) — delimita el contrato técnico que debe cumplirse al razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución.

---

[↑ Glosario](../../README.md) · [← Volatilidad](./volatilidad.md) · [Votación →](./votacion.md)
