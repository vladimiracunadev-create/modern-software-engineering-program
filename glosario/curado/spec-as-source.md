# Spec-as-source

## Definición

**Spec-as-source** es el uso de la especificación como único artefacto editable del que se genera el código (SE-165, SE-548). Es el tercer nivel de uso de una especificación, después de spec-first (guía y se archiva) y spec-anchored (se mantiene anclada al código).

## Por qué importa

La especificación es lo que se edita; el código se genera y no se toca a mano. La deriva entre especificación y código desaparece por construcción, y cambiar un contrato es editar un archivo. Cambia dónde se trabaja: se edita la fuente y se regenera.

## Cómo funciona

En spec-as-source el humano **no toca el código generado**. Se edita la especificación y se regenera; editar el código a mano está desaconsejado y se marca con un comentario («GENERADO; no editar»). SE-548 menciona a Tessl como la herramienta que, según Böckeler, explora este nivel, con una correspondencia de uno a uno entre un archivo de especificación y un archivo de código.

Los **costes** son reales, según SE-165: hay que **confiar en el generador** (y revisar lo que produce), la especificación debe ser **lo bastante expresiva** para cubrir el comportamiento deseado (si no lo es, la gente edita el código y rompe el modelo) y, con modelos generativos, la regeneración puede no ser determinista. De ahí que la generación determinista sea una condición: un generador que ordena toda su salida y **marca la región generada**, más una comprobación que regenera y compara huellas, y falla si hay diferencias.

La práctica en la plataforma de entregas: los clientes de la API se generan desde el documento OpenAPI (spec-as-source), con un generador determinista, mientras el contrato mismo es spec-anchored y el documento de arquitectura es spec-first. Cada artefacto declara su nivel. Un fallo previsto: la regeneración borra trabajo manual porque se editó dentro de lo generado; se corrige delimitando la región generada y moviendo lo manual fuera.

## Ejemplo

El equipo edita `entregas.openapi.yaml` para añadir el campo opcional `comentario`. Ejecuta el generador: el cliente en TypeScript y el servidor de esqueleto se regeneran, con los archivos marcados «GENERADO; no editar». Una comprobación en CI regenera de nuevo y compara huellas con lo comprometido; si alguien editó a mano un archivo generado, la comparación falla. (Ilustración del flujo descrito en SE-165.)

## Errores y confusiones comunes

- **Editar a mano el código generado**: se pierde en la próxima regeneración.
- **La regeneración borra trabajo manual**: ediciones dentro de lo generado.
- **Generador no determinista** que produce diffs ruidosos.
- **Confundirlo con spec-anchored**: allí el código se escribe aparte y se compara.

## Límites y cuándo no aplica

Solo sirve donde la especificación puede expresar todo lo necesario; la lógica compleja suele escribirse a mano en código no generado. Con generadores de IA, el resultado puede variar y exige revisión. El costo de montar el generador solo se justifica para artefactos que cambian a menudo y se repiten (clientes, esqueletos).
