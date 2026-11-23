# STRIDE

[↑ Glosario](../../README.md) · [← Strategy con registro](./strategy-con-registro.md) · [Subagente →](./subagente.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Lista de seis categorías de amenaza (suplantación, manipulación, repudio, divulgación de información, denegación de servicio y elevación de privilegios) usada como guía de preguntas por elemento.

Definición de trabajo de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md).

## Por qué importa

En [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), el tema «Enumeración con STRIDE» importa porque convierte «qué puede salir mal» en seis preguntas por elemento.

## Cómo funciona

Según [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

STRIDE es un acrónimo de seis categorías: suplantación (Spoofing), manipulación (Tampering), repudio (Repudiation), divulgación de información (Information disclosure), denegación de servicio (Denial of service) y elevación de privilegios (Elevation of privilege). Sirve como lista de preguntas por elemento del diagrama, no como clasificación definitiva. Un actor externo puede ser suplantado o repudiar una acción; un proceso puede sufrir las seis; un almacén puede ser manipulado, divulgado o inaccesible, y si guarda registros, puede permitir el repudio si alguien altera el registro; un flujo de datos puede ser manipulado, observado o interrumpido. Aplicado a la frontera navegador-API: el cliente puede enviar un identificador de otra persona (suplantación), alterar un campo de rol (elevación), repetir una petición con otro cuerpo (manipulación) o negar haber enviado una entrega que luego perjudica (repudio).

Según [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md):

El equipo de la plataforma dibuja el diagrama con cuatro procesos (API, servicio de calificación, trabajador de archivos y notificador), dos almacenes, tres actores y cinco fronteras. En el cruce navegador-API enumera por STRIDE nueve amenazas, descarta tres con razón escrita y deja seis; al ponerles costo descubre que la más barata es la elevación de privilegios por el campo de rol del registro. La decisión: la API ignora el rol del cliente y lo asigna por la invitación del curso; se añade una prueba negativa que intenta registrarse con `rol=docente` y exige que el rol resultante sea estudiante. El modelo se guarda en el repositorio junto al diagrama y registra tres supuestos con dueño y fecha.

## Ejemplo

Ejemplo de [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma dibuja el diagrama con cuatro procesos (API, servicio de calificación, trabajador de archivos y notificador), dos almacenes, tres actores y cinco fronteras. En el cruce navegador-API enumera por STRIDE nueve amenazas, descarta tres con razón escrita y deja seis; al ponerles costo descubre que la más barata es la elevación de privilegios por el campo de rol del registro. La decisión: la API ignora el rol del cliente y lo asigna por la invitación del curso; se añade una prueba negativa que intenta registrarse con `rol=docente` y exige que el rol resultante sea estudiante.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)) son:

- **Se arregla lo grave y nada mejora** — causa: se prioriza por gravedad, no por camino. Corrección: calcular el camino más barato y recalcularlo tras cada decisión.
- **El modelo es una lista de 80 amenazas sin dueño** — causa: se enumera sin descartar ni decidir. Corrección: una fila por amenaza con elemento, respuesta y supuesto.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se modeló un atacante real, ningún sistema en producción ni ningún incidente; los costos de las aristas, el ruido de los revisores, las tasas de cambio y la sensibilidad de la regla son construcciones del autor, y el análisis de la plataforma de entregas es un ejercicio sobre un diseño ficticio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Elevación](../e/elevacion.md), [Servicio](./servicio.md), [Activo](../a/activo.md), [Frontera de confianza](../f/frontera-de-confianza.md), [Grafo de ataque](../g/grafo-de-ataque.md), [Modelo de amenazas](../m/modelo-de-amenazas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft: amenazas STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) — categorías por elemento; autoridad: documentación de Microsoft.
- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — principios de diseño de la protección; autoridad: Proceedings of the IEEE.
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) — valores y principios del modelado de amenazas; autoridad: comunidad de profesionales de seguridad.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — proceso práctico de modelado; autoridad: OWASP.
- [Schneier, «Attack Trees»](https://www.schneier.com/academic/archives/1999/12/attack_trees/) — árboles de ataque con costos; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Strategy con registro](./strategy-con-registro.md) · [Subagente →](./subagente.md)
