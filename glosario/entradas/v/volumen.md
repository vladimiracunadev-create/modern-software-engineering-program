# Volumen

[↑ Glosario](../../README.md) · [← Volatilidad](./volatilidad.md) · [Votación →](./votacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

**Volumen** tiene dos sentidos en el programa:

- **De datos** ([SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md)): el número de filas de una carga o de una partición; la primera comprobación de calidad es si llegaron las filas esperadas.
- **De almacenamiento** ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)): una unidad lógica con un espacio de nombres y un sistema de archivos asociados.

Esta entrada desarrolla el primero y menciona el segundo.

## Por qué importa

Una carga parcial o una tabla vacía son fallos silenciosos: el pipeline termina sin error, la tabla existe, y los paneles muestran la mitad de los datos. Controlar el volumen es la defensa más barata contra esos fallos. [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) cuenta el caso: el lunes, el panel muestra la mitad de las entregas y las alertas de volumen no sonaron; revisar qué comprobaciones existían mostró que la tabla solo tenía validación de esquema.

## Cómo funciona

[SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) lista seis comprobaciones de calidad de datos, cada una con su propia pregunta: **volumen** (¿llegaron las filas esperadas?), **unicidad** (¿hay claves repetidas?), **nulos** (¿falta lo que debería estar?), **integridad referencial** (¿cada clave extranjera apunta a algo?), **frescura** (¿es reciente el dato más nuevo?) y **distribución** (¿se parecen los valores a lo habitual?).

En el laboratorio, una tabla de 5 000 pedidos recibió seis variantes defectuosas. La carga parcial falló el volumen; los duplicados, volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; y los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. La variante limpia no falló ninguna. Ninguna comprobación vio más de dos variantes: su ceguera es tan importante como su vista.

El umbral de volumen se calibra contra lo habitual (por ejemplo, la mediana por día de la semana), no contra un número fijo.

## Ejemplo

```sql
SELECT COUNT(*) AS filas FROM lecturas WHERE dia = :dia;
-- alerta si filas < 0.8 * mediana_mismo_dia_de_semana
```

El equipo de *Avisos* prioriza por impacto: el hecho de lecturas recibe volumen, unicidad, nulos y frescura; el mart ejecutivo, distribución además de volumen. Define que unicidad y volumen detienen la publicación y la distribución publica con una marca.

## Errores y confusiones comunes

- **Solo validar el esquema.** Una tabla con el esquema correcto y la mitad de las filas pasa la validación.
- **Un umbral fijo.** El volumen varía por día de la semana y por temporada; hay que recalibrarlo.
- **Alertas que nadie atiende.** [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) propone una métrica del propio sistema: el porcentaje de alertas que terminaron en una acción; si baja, se recalibra antes de que alguien silencie el canal.

## Límites y cuándo no aplica

El volumen detecta ausencia o exceso, no corrección de los valores: una tabla con el número exacto de filas puede tener todos los importes errados (eso lo ve la distribución). Los umbrales son del equipo y se ajustan con datos reales. Y en el sentido de almacenamiento ([SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md)), un volumen es una unidad lógica de montaje: no tiene relación con el conteo de filas.

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
