# Retiro

[↑ Glosario](../../README.md) · [← Retirar del reparto](./retirar-del-reparto.md) · [Retorno →](./retorno.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Eliminación controlada de capacidad, dependencias y datos.

Definición de trabajo de [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md): Compromiso de resultados al estado arquitectónico.

## Por qué importa

En [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), el tema «Retiro» importa porque exportación, conservación y eliminación

## Cómo funciona

Según [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md):

Confundir ciclo de vida con cascada produce dos errores. El primero es rechazar actividades necesarias —requisitos, validación o retiro— porque se asocian a una metodología. El segundo es tratarlas como handoffs irreversibles: “análisis terminó, ya no puede aprender”. Un ciclo profesional conserva bucles; la operación informa nuevos requisitos y una dificultad de retiro revela una decisión de diseño pendiente.

Según [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md):

Al cambiar proveedor de correo, producto define experiencia; ingeniería adapta contrato; seguridad revisa secretos; soporte comunica; operaciones observa; legal decide conservación. El retiro revoca credenciales antiguas.

## Ejemplo

Ejemplo de [SE-003 — Ciclo de vida completo y responsabilidades profesionales](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md) (sección «Ejemplo profesional»):

Al cambiar proveedor de correo, producto define experiencia; ingeniería adapta contrato; seguridad revisa secretos; soporte comunica; operaciones observa; legal decide conservación. El retiro revoca credenciales antiguas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **el ciclo termina en despliegue** — causa: se definió entrega como final del producto. Corrección: añade operación, evolución, conservación y retiro con responsables. ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md))
- **retiro equivale a apagar infraestructura** — causa: se omitieron consumidores y obligaciones. Corrección: inventaría dependencias, datos, accesos, comunicación y evidencia de cierre. ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** La fila central es la secuencia de momentos; las flechas rojas continuas son los bucles que impiden leerla como cascada: lo que se aprende al operar corrige requisitos, el mantenimiento reabre decisiones de diseño y pruebas, y el retiro devuelve a la concepción el criterio de no construir y la exportabilidad. ([SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md))

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
