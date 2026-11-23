# Vista

[↑ Glosario](../../README.md) · [← Visited](./visited.md) · [Vista arquitectónica →](./vista-arquitectonica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Presentación de un hecho o de un procedimiento adaptada a una audiencia, que cita su fuente y no la contradice.

Definición de trabajo de [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).

## Por qué importa

En [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), el tema «Vistas de una misma verdad» importa porque permite que estudiante, docente y mantenimiento lean cosas distintas sin contradecirse.

## Cómo funciona

Según [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md):

La regla de penalización es una sola; sus vistas son varias. La estudiante necesita saber cuánto pierde y cómo evitarlo; el docente, cómo conceder una prórroga; la secretaría, cómo se registra en el acta; mantenimiento, qué función la calcula y qué contrato tiene. Cada vista selecciona y reformula, pero ninguna debe inventar. La forma barata de mantener la coherencia es que cada vista cite o incluya el dato desde un único lugar; la forma cara es copiarlo y confiar en la disciplina. El experimento de coherencia calcula qué pasa en la segunda: la probabilidad de que todas las copias coincidan tras tres cambios cae del 62,6 % con una copia al 5,3 % con seis.

Según [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md):

El portal documental de la plataforma de entregas tiene un inventario de tareas por audiencia en `audiencias.md`: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga, corregir una nota), secretaría (exportar el acta con la nota final), mantenimiento (depurar el cálculo, cambiar el tope). La regla vive en `politica/penalizacion.md`, versionada, con responsable y fecha de revisión. Las cuatro vistas enlazan esa fuente con una frase de contexto cada una. Cuando la política cambia el tope al 30 %, el cambio es un único commit en la fuente y una lista de verificación señala las cuatro vistas para revisar.

## Ejemplo

Ejemplo de [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sección «Ejemplo profesional»):

El portal documental de la plataforma de entregas tiene un inventario de tareas por audiencia en `audiencias.md`: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga, corregir una nota), secretaría (exportar el acta con la nota final), mantenimiento (depurar el cálculo, cambiar el tope). La regla vive en `politica/penalizacion.md`, versionada, con responsable y fecha de revisión. Las cuatro vistas enlazan esa fuente con una frase de contexto cada una. Cuando la política cambia el tope al 30 %, el cambio es un único commit en la fuente y una lista de verificación señala las cuatro vistas para revisar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md)) son:

- **Nadie encuentra «cómo cambiar el plazo» aunque existe la página** — causa: el título usa el nombre del componente («Módulo de calendario») y no la tarea. Corrección: reescribir el título con verbo y resultado y añadirla al índice de tareas.
- **Dos páginas dan topes de penalización distintos** — causa: el dato se copió en lugar de enlazarse. Corrección: elegir una fuente, enlazar desde las demás y añadir un comprobador de enlaces.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Crea cuatro vistas que repitan el tope de penalización, cambia la política y actualiza solo dos. ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Audiencia](../a/audiencia.md), [Hecho](../h/hecho.md), [Fuente única](../f/fuente-unica.md), [Prueba de recorrido](../p/prueba-de-recorrido.md), [Tarea](../t/tarea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (114 clases más lo mencionan; las que más):

[SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [TSB Bank](../../../casos/fallo/tsb.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Diátaxis](https://diataxis.fr/) — cuatro necesidades de quien usa documentación y las formas que les corresponden; autoridad: proyecto Diátaxis.
- [Diátaxis: guías prácticas](https://diataxis.fr/how-to-guides/) — define una guía por su orientación a un objetivo y no a un componente; autoridad: proyecto Diátaxis.
- [Google, Technical Writing One](https://developers.google.com/tech-writing/one) — curso con una unidad sobre audiencia; autoridad: Google for Developers.
- [Digital.gov, guías de lenguaje claro](https://www.plainlanguage.gov/) — escribir y probar el contenido para su audiencia; autoridad: Digital.gov.
- [Barrio-Cantalejo et al., «Validación de la Escala INFLESZ» (Anales del Sistema Sanitario de Navarra, 2008)](https://doi.org/10.4321/S1137-66272008000300004) — interpretación de un índice de legibilidad para español en textos para pacientes; autoridad: Anales del Sistema Sanitario de Navarra.

---

[↑ Glosario](../../README.md) · [← Visited](./visited.md) · [Vista arquitectónica →](./vista-arquitectonica.md)
