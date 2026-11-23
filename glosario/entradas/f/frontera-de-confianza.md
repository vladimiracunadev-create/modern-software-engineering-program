# Frontera de confianza

[↑ Glosario](../../README.md) · [← Frontera de aislamiento](./frontera-de-aislamiento.md) · [Frontera de confirmación →](./frontera-de-confirmacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Línea de un diagrama de flujo de datos donde cambia quién controla el dato o el proceso, de modo que lo que cruza debe tratarse como no confiable.

Definición de trabajo de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md).

## Por qué importa

La clase donde se define, [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), existe con este propósito: la clase existe para que dejes de pensar la seguridad como una lista de controles y empieces a pensarla como una pregunta que se puede responder con evidencia: qué se protege, de quién, por qué camino y a qué costo para quien ataca.

## Cómo funciona

Según [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

El diagrama de flujo de datos es la representación más pequeña que sirve para razonar: actores externos (estudiante, docente, sistema de correo), procesos (la API de entregas, el servicio de calificación), almacenes (la base de datos, el almacenamiento de archivos) y flujos entre ellos. Sobre ese dibujo se trazan las **fronteras de confianza**: líneas que atraviesan los flujos donde cambia quién controla qué. La frontera entre el navegador y la API es la más importante y la más malentendida: todo lo que cruza de izquierda a derecha, incluso un campo oculto, una cabecera o un identificador, lo decide quien está del lado del cliente y por tanto puede ser cualquier cosa.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

El equipo de la plataforma dibuja el diagrama con cuatro procesos (API, servicio de calificación, trabajador de archivos y notificador), dos almacenes, tres actores y cinco fronteras. En el cruce navegador-API enumera por STRIDE nueve amenazas, descarta tres con razón escrita y deja seis; al ponerles costo descubre que la más barata es la elevación de privilegios por el campo de rol del registro.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)) son:

- **Se arregla lo grave y nada mejora** — causa: se prioriza por gravedad, no por camino. Corrección: calcular el camino más barato y recalcularlo tras cada decisión.
- **El modelo es una lista de 80 amenazas sin dueño** — causa: se enumera sin descartar ni decidir. Corrección: una fila por amenaza con elemento, respuesta y supuesto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El 9 % cruza una frontera de confianza (24 cambios: un endpoint nuevo, un almacén nuevo, un proveedor externo nuevo). ([SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Diagrama](../d/diagrama.md), [Flujo](./flujo.md), [Proceso](../p/proceso.md), [Activo](../a/activo.md), [Grafo de ataque](../g/grafo-de-ataque.md), [Modelo de amenazas](../m/modelo-de-amenazas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — principios de diseño de la protección; autoridad: Proceedings of the IEEE.
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) — valores y principios del modelado de amenazas; autoridad: comunidad de profesionales de seguridad.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — proceso práctico de modelado; autoridad: OWASP.
- [Microsoft: amenazas STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — categorías por elemento; autoridad: documentación de Microsoft.
- [Schneier, «Attack Trees»](https://www.schneier.com/academic/archives/1999/12/attack_trees/) — árboles de ataque con costos; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Frontera de aislamiento](./frontera-de-aislamiento.md) · [Frontera de confirmación →](./frontera-de-confirmacion.md)
