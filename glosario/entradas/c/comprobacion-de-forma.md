# Comprobación de forma

[↑ Glosario](../../README.md) · [← Comprobación de calidad](./comprobacion-de-calidad.md) · [Comprobación inestable →](./comprobacion-inestable.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Verificación mecánica de una propiedad del paquete que no depende del sentido del cambio.

Definición de trabajo de [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

## Por qué importa

En [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), el tema «Comprobaciones de forma» importa porque liberan a la revisora de lo mecánico y deben ser independientes.

## Cómo funciona

Según [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), en la sección «Comprobaciones de forma»:

Doce comprobaciones cubren la forma: mensajes convencionales, commits atómicos (≤ 6 archivos y ≤ 120 líneas), cada commit pasa las pruebas, pasan en la punta, cabecera de licencia en archivos nuevos, issue enlazado, sin secretos, commits firmados, `Signed-off-by`, tamaño del PR (≤ 400 líneas), revisores de los propietarios pedidos y «si cambia el código cambia una prueba». Los umbrales son una decisión del equipo y deben revisarse con los casos que se escapan.

## Ejemplo

Caso medido en la sección «Comprobaciones de forma» de [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md):

Doce comprobaciones cubren la forma: mensajes convencionales, commits atómicos (≤ 6 archivos y ≤ 120 líneas), cada commit pasa las pruebas, pasan en la punta, cabecera de licencia en archivos nuevos, issue enlazado, sin secretos, commits firmados, `Signed-off-by`, tamaño del PR (≤ 400 líneas), revisores de los propietarios pedidos y «si cambia el código cambia una prueba». Los umbrales son una decisión del equipo y deben revisarse con los casos que se escapan.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md)) son:

- **El validador pasa y el comportamiento es erróneo** — causa: una prueba vacía o débil. Corrección: añadir una mutación o una lectura humana de las pruebas.
- **Una rama tiene un commit que no compila** — causa: se empujó un intermedio roto. Corrección: reordenar la rama para que cada commit pase las pruebas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La forma no ve el sentido: un test que afirma `True` pasa todas las comprobaciones de forma, y un cambio de una regla de negocio sin prueba que la ejercite solo se ve si una regla exige tocar una prueba. ([SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md))
- Traslada el paquete a otra contribución de naturaleza distinta (por ejemplo, un cambio de infraestructura como código o una modificación de un conjunto de datos): decide qué comprobaciones de forma seguirían valiendo, cuáles no y qué quedaría para una persona. ([SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Paquete](../p/paquete.md), [Propiedad](../p/propiedad.md), [Verificación](../v/verificacion.md), [Contribución revisable](./contribucion-revisable.md), [Mutación](../m/mutacion.md), [Signed-off-by](../s/signed-off-by.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Comprobaciones de forma».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Pro Git: Contributing to a Project](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) — preparación de contribuciones; autoridad: Pro Git.
- [Developer Certificate of Origin](https://developercertificate.org/) — declaración de origen de un cambio; autoridad: Linux Foundation.
- [REUSE specification](https://reuse.software/spec/) — licencia y titularidad por archivo; autoridad: REUSE.
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — formato de mensajes; autoridad: especificación de la convención.
- [git-commit](https://git-scm.com/docs/git-commit) — firma y `--signoff`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Comprobación de calidad](./comprobacion-de-calidad.md) · [Comprobación inestable →](./comprobacion-inestable.md)
