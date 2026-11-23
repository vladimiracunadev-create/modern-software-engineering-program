# Dependencia

[↑ Glosario](../../README.md) · [← Denegación por defecto](./denegacion-por-defecto.md) · [Dependencia alucinada →](./dependencia-alucinada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

**Dependencia** es una palabra con varios sentidos en el programa, todos con la idea de «algo que necesita de otra cosa». Las clases distinguen:

- **De software instalable** ([SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md)): un componente requerido bajo una relación y una restricción declaradas (por ejemplo, una versión).
- **Entre componentes** ([SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md)): el conocimiento de un componente sobre otro; es el acoplamiento visto como relación.
- **De orden de trabajo** ([SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)): una relación por la cual un elemento no puede empezar o terminar hasta que otro llegue a cierto estado.
- **Entre requisitos** ([SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)): una relación por la cual un requisito no puede entregarse, probarse o usarse sin otro.

El sentido común es una relación dirigida: A depende de B. Al leer la palabra hay que confirmar qué clase de relación es.

## Por qué importa

Una dependencia ignorada produce planes que no se pueden cumplir o sistemas que se rompen al cambiar una pieza. [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) lo muestra en la planificación: ordenar por valor sin comprobar dependencias produce planes que prometen lo que no se puede construir con lo comprometido. [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) lo muestra en la entrega: si el camino crítico pasa por una dependencia externa, todo el equipo espera la misma entrega.

## Cómo funciona

[SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) modela las dependencias entre requisitos como un grafo dirigido. Si hay un ciclo, los requisitos implicados son en realidad uno solo o están mal separados. Un conjunto es **entregable** si está cerrado bajo las dependencias: si contiene un requisito, contiene también todo aquello de lo que depende; por eso se verifica el cierre antes de aprobar un plan. [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) trata las dependencias externas con una práctica: acordar con cada proveedor una fecha de aviso y un doble (una alternativa o un contrato que permita avanzar sin la entrega), y revisar el diagrama de dependencias en cada ciclo con el avance real. [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) lo aplica al orden: se enumera o resuelve el orden con las dependencias, y no se hace primero lo de mayor valor propio.

## Ejemplo

En [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), un requisito de alto valor nunca se hace porque su dependencia está fuera del presupuesto; la corrección es hacer visible la dependencia y decidir si se incluye o se retira el requisito. En [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), todo el equipo espera la misma entrega externa porque el camino crítico pasa por ella; se divide el trabajo para que avance sin ella, con un contrato o un doble.

## Errores y confusiones comunes

- **El plan aprobado no se puede construir.** Se ordenó por valor sin comprobar dependencias; corrección ([SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)): verificar el cierre del conjunto.
- **Una dependencia «casi lista» que llega tarde.** No se pidió fecha de aviso ni alternativa ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)).
- **Un diagrama de dependencias desactualizado.** Se dibujó una vez; hay que revisarlo cada ciclo.

## Límites y cuándo no aplica

Un grafo de dependencias solo contiene las relaciones que alguien declaró: las no declaradas aparecen como sorpresas. Las clases tratan las dependencias de requisitos ([SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md)) y de plan ([SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md)) en contextos de planificación con ejemplos sintéticos, y las de software y de componentes en otros contextos; no se pueden trasladar sus reglas de un sentido a otro sin comprobar que la relación es la misma.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Estado](../e/estado.md), [Relación](../r/relacion.md), [Restricciones](../r/restricciones.md), [Adaptador](../a/adaptador.md), [Alcance](../a/alcance.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-032 — Instalación de software y gestores de paquetes del sistema](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-068 — Módulos, interfaces y separación de responsabilidades](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-150 — Priorización, dependencias y negociación](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-186 — Planificación de entregas y gestión de dependencias](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (396 clases más lo mencionan; las que más):

[SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Dependencias», «dependencias».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — identificar y priorizar riesgos de proyecto, incluidas las dependencias; autoridad: IEEE Software.
- [Karlsson y Ryan: A cost-value approach for prioritizing requirements (1997)](https://doi.org/10.1109/52.605933) — comparación por pares de valor y costo; autoridad: IEEE Software.
- [Stanford Encyclopedia of Philosophy: Voting Methods](https://plato.stanford.edu/entries/voting-methods/) — paradoja de Condorcet y métodos de votación; autoridad: Stanford University.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — atributos de un conjunto de requisitos, incluida la priorización; autoridad: ISO, IEC e IEEE.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — priorización y negociación de requisitos; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Denegación por defecto](./denegacion-por-defecto.md) · [Dependencia alucinada →](./dependencia-alucinada.md)
