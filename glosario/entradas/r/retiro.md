# Retiro

[↑ Glosario](../../README.md) · [← Retirar del reparto](./retirar-del-reparto.md) · [Retorno →](./retorno.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

El **retiro** es la eliminación controlada de una capacidad, de sus dependencias y de sus datos ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md)). Es la última etapa del ciclo de vida del software, no un apagado. [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) usa el término en arquitectura de procesadores con otro sentido, el compromiso de los resultados de una instrucción al estado arquitectónico; esa acepción es distinta y no se trata aquí.

## Por qué importa

Un sistema que se apaga sin plan deja consumidores rotos, datos huérfanos, credenciales vivas y obligaciones sin cumplir. Pensar el retiro desde el diseño tiene un efecto inverso: [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) señala que una dificultad de retiro revela una decisión de diseño pendiente y devuelve a la concepción el criterio de no construir y la exportabilidad.

## Cómo funciona

[SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) trata el ciclo de vida con bucles, no como cascada: la operación informa nuevos requisitos y el retiro reabre decisiones. El error típico es entender «retiro» como apagar infraestructura; omite consumidores y obligaciones. Un retiro completo:

- **inventaría** dependencias, datos, accesos y comunicación;
- **avisa** a quienes dependen, con alternativa y plazo (véase *obsolescencia*);
- **decide la conservación** de los datos (qué se exporta, qué se borra, qué se retiene por obligación);
- **revoca** credenciales y accesos;
- **deja evidencia de cierre**.

Cada función involucrada tiene su rol: en el cambio de proveedor de correo de [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), producto define la experiencia, ingeniería adapta el contrato, seguridad revisa secretos, soporte comunica, operaciones observa y legal decide la conservación; el retiro revoca las credenciales antiguas.

## Ejemplo

Lista de cierre para retirar un servicio de avisos:

```text
[ ] consumidores identificados y avisados (fecha de corte: 2026-06-30)
[ ] datos exportados / eliminados según política de retención
[ ] credenciales y secretos revocados
[ ] registros DNS, colas y alertas eliminados
[ ] documentación marcada como retirada, con enlace a la alternativa
```

## Errores y confusiones comunes

- **El ciclo termina en despliegue.** Causa: se definió entrega como final del producto; corrección: añadir operación, evolución, conservación y retiro con responsables ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md)).
- **Retiro equivale a apagar infraestructura.** Causa: se omitieron consumidores y obligaciones; corrección: inventariar dependencias, datos, accesos, comunicación y evidencia de cierre ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md)).
- **Borrar datos sin decidir la conservación.** Puede incumplir una obligación o perder información necesaria.

## Límites y cuándo no aplica

En prototipos y software desechable, el retiro se reduce a borrar. Las obligaciones de conservación dependen de la jurisdicción y del dominio; la decisión corresponde a quien tiene autoridad, no al equipo técnico solo. Y retirar no es lo mismo que migrar: la migración mantiene la capacidad en otro lugar.

## Relación con otros conceptos

- **Prerrequisito:** [Capacidad](../c/capacidad.md).
- **Ver también:** [Compromiso](../c/compromiso.md), [Dependencia](../d/dependencia.md), [Estado](../e/estado.md), [Resultado](./resultado.md), [Excepción](../e/excepcion.md), [Instrucción](../i/instruccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (29 clases más lo mencionan; las que más):

[SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Retirar del reparto](./retirar-del-reparto.md) · [Retorno →](./retorno.md)
