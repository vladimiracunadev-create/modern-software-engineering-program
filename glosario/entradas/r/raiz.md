# Raíz

[↑ Glosario](../../README.md) · [← Ráfaga](./rafaga.md) · [Raíz de confianza →](./raiz-de-confianza.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Referencia inicial para un trazado de alcanzabilidad.

Definición de trabajo de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md).

## Por qué importa

La clase donde se define, [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), existe con este propósito: la clase existe para razonar sobre carga, memoria y recolección separando especificación de estrategia del runtime.

## Cómo funciona

Según [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

Conteo de referencias recupera cuando el conteo llega a cero, pero ciclos requieren otro mecanismo. Un recolector por trazado parte de raíces y marca alcanzables; los demás pueden recuperarse. Hipótesis generacionales usan el patrón de que muchos objetos mueren jóvenes. Cada estrategia intercambia pausas, memoria, CPU y complejidad.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

Un servicio guarda respuestas en una caché sin límite. Los objetos son alcanzables; no es fallo del GC. Se define tamaño, expiración, métrica y comportamiento al saturarse.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md)) son:

- **toda memoria creciente = fuga GC** — causa: causas no separadas. Corrección: inspecciona alcanzabilidad, caché y memoria nativa.
- **`del` = liberación física** — causa: niveles confundidos. Corrección: habla de referencias y política del runtime.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El recolector de ciclos (C) parte de las raíces, no encuentra esos objetos y los libera. ([SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcanzabilidad](../a/alcanzabilidad.md), [Referencia](./referencia.md), [Finalización](../f/finalizacion.md), [Máquina virtual](../m/maquina-virtual.md), [Objeto alcanzable](../o/objeto-alcanzable.md), [Runtime](./runtime.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (58 clases más lo mencionan; las que más):

[SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-473](../../../classes/part-39-build-release-y-cadena-de-suministro/se-473-firmas-checksums-y-verificacion/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ráfaga](./rafaga.md) · [Raíz de confianza →](./raiz-de-confianza.md)
