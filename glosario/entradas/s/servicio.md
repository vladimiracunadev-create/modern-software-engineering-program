# Servicio

[↑ Glosario](../../README.md) · [← Service worker](./service-worker.md) · [Servicio de apoyo →](./servicio-de-apoyo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

**Servicio** tiene dos sentidos en el programa:

- **Componente de arquitectura** ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)): un componente que se despliega y escala de forma independiente y se comunica por red.
- **Proceso de larga duración** ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)): un proceso gestionado por un supervisor y una política de ciclo de vida, que atiende peticiones o ejecuta trabajo sin un usuario interactivo (en Unix, *daemon*).

Comparten la idea de algo que está disponible para otros, pero operan en niveles distintos.

## Por qué importa

Elegir servicios como unidad de despliegue cambia qué se gana y qué se paga. [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) lo pone en la misma tabla: se gana autonomía (un equipo publica sin coordinar, un componente pesado se escala sin escalar el resto) y se paga operación, latencia de red, fallos parciales y consistencia. Y para el proceso de larga duración, entender el ciclo de vida evita reinicios en bucle y despliegues que fallan.

## Cómo funciona

**Arquitectura** ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)): al separar servicios, una transacción que los cruza deja de ser atómica y se convierte en una saga con compensaciones. Fowler y Lewis describen esos costos junto a las ventajas. Para muchos sistemas el destino correcto es un monolito bien organizado: da orden y pruebas rápidas sin el costo de operar muchos servicios.

**Proceso** ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)): un supervisor lo arranca, lo vigila y lo reinicia según una política. Una recuperación sana clasifica el fallo, aplica espera creciente y corta el bucle; si no, un servicio que cae al arrancar se reinicia sin límite. Tras un despliegue, el tráfico solo debe llegar cuando una sonda de preparación comprueba lo mismo que hará el cliente. En parada, el cierre ordenado (vaciar, escribir en archivo temporal y renombrar) evita archivos truncados.

## Ejemplo

```text
saga "matricular":  reservar_cupo -> cobrar -> emitir_constancia
si cobrar falla:    compensar -> liberar_cupo     (no hay transacción atómica entre servicios)
```

## Errores y confusiones comunes

- **Quedan datos a medias entre servicios.** Causa: transacción entre servicios sin compensación; corrección: diseñar y probar compensaciones o evitar la operación cruzada ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)).
- **El servicio reinicia sin límite.** Causa: se sustituyó recuperación por repetición; corrección: clasificar fallo, aplicar espera creciente y cortar el bucle ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)).
- **Fallan peticiones tras cada despliegue.** Causa: tráfico antes de que el servicio esté preparado; corrección: sonda de preparación que prueba lo mismo que el cliente ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)).

## Límites y cuándo no aplica

Separar en servicios no es mejor en sí: para equipos pequeños o dominios poco definidos suele costar más de lo que da ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)). Y el sentido de arquitectura no implica el de proceso: un servicio de arquitectura puede ejecutarse en muchos procesos y un *daemon* no es necesariamente un servicio independiente de negocio.

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
