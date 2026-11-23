# Política como código

[↑ Glosario](../../README.md) · [← Polisemia](./polisemia.md) · [Política de acceso →](./politica-de-acceso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md)

## Definición

Regla de configuración escrita de forma que una herramienta pueda comprobarla de manera automática.

Definición de trabajo de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md): Regla ejecutable evaluada sobre datos de entrada que produce una decisión auditable.

## Por qué importa

En [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), el tema «Políticas como código» importa porque comprobar el resultado no depende de quién lo creó.

En [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), el tema «Políticas como código» importa porque convierte un criterio en una regla verificable, con sus falsas alarmas.

## Cómo funciona

Según [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), en la sección «Políticas como código»:

Un verificador de políticas lee un descriptor de servicio (qué imagen, con qué usuario, qué límites) y comprueba reglas escritas como código: debe tener dueño, límites, una imagen con versión fija, un usuario sin privilegios. Es independiente del origen: un servicio de la plantilla y uno hecho a mano pasan por la misma puerta. Herramientas como Open Policy Agent ofrecen un lenguaje para escribir esas reglas. Su límite es que comprueban forma, no sentido: un límite de CPU de mil núcleos cumple la regla «tiene límite» y es absurdo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md):

El equipo de plataforma de la plataforma de entregas escribe la historia de su usuario principal: un equipo de producto que necesita un servicio nuevo en producción en un día, de forma segura. Reduce los 23 pasos a 5: una plantilla crea el repositorio, la cuenta y la red; otra, el despliegue con límites y sondas; otra, las alarmas; el equipo escribe el código y revisa un plan.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md)) son:

- **Los equipos no usan el camino** — causa: es más difícil que lo manual o no cubre su caso. Corrección: medir pasos y excepciones y mejorarlo.
- **El equipo de plataforma está saturado de solicitudes** — causa: baja adopción y servicios hechos a mano. Corrección: reducir pasos del camino y atender primero las excepciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **política como código** es una regla escrita en un lenguaje ejecutable que se evalúa sobre datos de entrada (la configuración de infraestructura, un archivo de flujo de trabajo, una lista de dependencias) y produce una decisión. ([SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Regla](../r/regla.md), [Sobre](../s/sobre.md), [Camino dorado](../c/camino-dorado.md), [Carga cognitiva](../c/carga-cognitiva.md), [Compuerta](../c/compuerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-406 — Plataformas internas y golden paths](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-483 — Tests, seguridad y políticas como gates](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Políticas como código».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/) — políticas como código; autoridad: documentación del proyecto.
- [Open Policy Agent](https://www.openpolicyagent.org/docs) — políticas como código; autoridad: documentación del proyecto.
- [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) — qué es una plataforma interna y qué ofrece; autoridad: CNCF TAG App Delivery.
- [Team Topologies](https://teamtopologies.com/) — equipos de plataforma y carga cognitiva; autoridad: sitio de los autores del libro.
- [DORA](https://dora.dev/) — investigación sobre desempeño de entrega de software; autoridad: programa de investigación DORA.

---

[↑ Glosario](../../README.md) · [← Polisemia](./polisemia.md) · [Política de acceso →](./politica-de-acceso.md)
