# Radio de impacto

[↑ Glosario](../../README.md) · [← Radio de explosión](./radio-de-explosion.md) · [Radio de una filtración →](./radio-de-una-filtracion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

El **radio de impacto** es, en el sentido principal del programa ([SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md)), la fracción de clientes afectada por un fallo. Otras clases lo usan con matices cercanos:

- En [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) (resiliencia): la fracción del sistema o del tráfico que un experimento afecta.
- En [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) (SaaS): el conjunto de clientes afectados por un fallo.
- En [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) (modernización): el número de paquetes que deben cambiar como consecuencia de actualizar uno.

Se parece al radio de explosión; la diferencia que usa el programa es que el radio de impacto se expresa como fracción de clientes y se compara entre arquitecturas.

## Por qué importa

La disponibilidad habitual es un promedio sobre el tiempo y no dice cuántos clientes ven el problema cuando algo falla. Dos sistemas con la misma disponibilidad pueden diferir mucho: uno cae para todos un minuto, otro para el 1 % durante horas. La decisión que cambia es qué se optimiza: acotar cuántos se ven afectados por un único fallo, además de cuánto dura.

## Cómo funciona

[SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) define el radio como la fracción de clientes que quedan sin servicio por un único fallo. En una flota compartida, cualquier fallo que se propague por la flota alcanza al **100 %**. El objetivo de las **celdas** es poner un techo: con ocho celdas y reparto uniforme, un fallo contenido en una celda afecta a una octava parte, el 12,5 %. Ese techo es un escenario de calidad medible, que se puede comprobar inyectando el fallo («un fallo de cualquier inquilino afecta como máximo al 15 % de los inquilinos», en términos de [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)).

La clase compara opciones tras un incidente: ocho celdas dan 12,5 %; fragmentación aleatoria sobre la flota existente da un 3,6 % caído del todo ante una petición venenosa. Pero el costo cuenta: el equipo descarta empezar con celdas completas porque el costo de capacidad del 20 % y la operación de ocho copias superan lo que puede asumir ese año, y elige un camino por etapas (tope de reintentos por inquilino y cortacircuitos, luego fragmentación aleatoria, y celdas solo para el cliente más grande).

En [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), el mismo concepto se aplica a dependencias: antes de actualizar un paquete se calcula el radio de impacto en el grafo, es decir, cuántos otros paquetes deben cambiar.

## Ejemplo

El equipo calcula el radio de impacto de los fallos más probables: una petición venenosa, un despliegue defectuoso, una base saturada, y expresa cada uno como una fracción de clientes. Eso les permite comparar la arquitectura actual con alternativas por una cifra común. Ejercicio de [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

## Errores y confusiones comunes

- **Se actualiza una dependencia y se rompe otra**: no se miró el grafo; se calcula el radio de impacto antes de decidir ([SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md)).
- **Confundirlo con disponibilidad**: no son la misma medida.
- **Calcularlo sin la distribución real de clientes**: un cliente dominante cambia las fracciones.
- **Suponer que el reparto uniforme se cumple**.

## Límites y cuándo no aplica

Las cifras de la clase (8 celdas, 12,5 %, 3,6 %, costo del 20 %) son del escenario construido; en otros sistemas cambian. Acotar el radio tiene un costo (capacidad, operación) que puede no justificarse para cargas pequeñas. Y el radio mide la fracción de clientes afectados, no la gravedad del daño a cada uno.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Consecuencia](../c/consecuencia.md), [Paquete](../p/paquete.md), [Celda](../c/celda.md), [Cola justa](../c/cola-justa.md), [Contexto del inquilino](../c/contexto-del-inquilino.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-410 — Aislamiento multi-inquilino y vecino ruidoso](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-520 — Dependencias obsoletas y riesgo acumulado](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md), [Discord](../../../casos/exito/discord.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Basiri et al., «Chaos Engineering»](https://doi.org/10.1109/MS.2016.60) — experimentación sobre sistemas para ganar confianza; autoridad: IEEE Software, 2016.
- [Principios del caos](https://principlesofchaos.org/) — hipótesis, variación de eventos y radio mínimo; autoridad: comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas de estrés y de recuperación; autoridad: Google, libro de ingeniería de confiabilidad.
- [AWS Well-Architected: probar la fiabilidad](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html) — pruebas de fallo y días de simulacro; autoridad: Amazon Web Services.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de eventos del modelo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Radio de explosión](./radio-de-explosion.md) · [Radio de una filtración →](./radio-de-una-filtracion.md)
