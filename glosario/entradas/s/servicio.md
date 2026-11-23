# Servicio

[↑ Glosario](../../README.md) · [← Service worker](./service-worker.md) · [Servicio de apoyo →](./servicio-de-apoyo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Componente que se despliega y escala de forma independiente y se comunica por red.

Definición de trabajo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md): Proceso gestionado por un supervisor y una política de ciclo de vida.
- En [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md): Proceso de larga duración que atiende peticiones o ejecuta trabajo sin un usuario interactivo.

## Por qué importa

En [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), el tema «Servicios» importa porque despliegue y escalado independientes a cambio de red, consistencia y operación.

## Cómo funciona

Según [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), en la sección «Servicios»:

Los **servicios** se despliegan y escalan por separado y se comunican por red. Lo que se gana es autonomía: un equipo puede publicar su servicio sin coordinar con otros, y un componente pesado se escala sin escalar el resto. Lo que se paga es operación (varios despliegues, versiones, monitoreo), latencia de red, fallos parciales y consistencia: una transacción que cruza servicios deja de ser atómica y se convierte en una saga con compensaciones. Fowler y Lewis describen esos costes junto a las ventajas; la decisión honesta los pone en la misma tabla.

## Ejemplo

Ejemplo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma mantiene el sistema como monolito modular y añade al CI un comprobador de fronteras que falla si un módulo importa algo que no sea la `api` de otro, y otro que prohíbe `importlib` y `__import__` con nombres de módulos internos. Mide que la operación «calificar» hace 14 llamadas entre `notas` y `entregas` y decide que, si algún día se separan, esas dos son una sola frontera mal puesta: primero deberían fusionarse o reducir las llamadas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Quedan datos a medias entre servicios** — causa: transacción entre servicios sin compensación. Corrección: diseñar y probar compensaciones o evitar la operación cruzada. ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md))
- **El servicio reinicia sin límite** — causa: se sustituyó recuperación por repetición. Corrección: clasificar fallo, aplicar espera creciente y cortar el bucle. ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md))
- **Fallan peticiones tras cada despliegue** — causa: se envía tráfico antes de que el servicio esté preparado. Corrección: sonda de preparación que prueba lo mismo que el cliente. ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que se gana es autonomía: un equipo puede publicar su servicio sin coordinar con otros, y un componente pesado se escala sin escalar el resto. ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md))
- Para muchos sistemas es el destino: da orden y pruebas rápidas sin el coste de operar muchos servicios. ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Proceso](../p/proceso.md).
- **Ver también:** [Ciclo de vida](../c/ciclo-de-vida.md), [Ciclo](../c/ciclo.md), [Componente](../c/componente.md), [Trabajo](../t/trabajo.md), [Código de salida](../c/codigo-de-salida.md), [Daemon/servicio](../d/daemon-servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (373 clases más lo mencionan; las que más):

[SE-286](../../../classes/part-23-runtimes-y-plataformas-modernas/se-286-confianza-cero-en-la-practica/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «daemon», «Servicios».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler y Lewis, «Microservices»](https://martinfowler.com/articles/microservices.html) — características, ventajas y costes de los servicios; autoridad: Martin Fowler y James Lewis.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — tipos de servicio, reinicio y plazos de parada; autoridad: proyecto systemd.
- [Microsoft: Services](https://learn.microsoft.com/en-us/windows/win32/services/services) — servicios de Windows y su control; autoridad: Microsoft Learn.
- [Fowler, «MonolithFirst»](https://martinfowler.com/bliki/MonolithFirst.html) — empezar por un monolito modular; autoridad: Martin Fowler.
- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — ocultación de información como criterio de descomposición; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Service worker](./service-worker.md) · [Servicio de apoyo →](./servicio-de-apoyo.md)
