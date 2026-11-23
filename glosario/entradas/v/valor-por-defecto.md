# Valor por defecto

[↑ Glosario](../../README.md) · [← Valor percibido y cambio](./valor-percibido-y-cambio.md) · [Valor predictivo positivo →](./valor-predictivo-positivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Valor que el lector usa si el campo falta.

Definición de trabajo de [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md).

## Por qué importa

En [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), el tema «Valores por defecto» importa porque permiten añadir campos sin romper.

## Cómo funciona

Según [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md):

La regla del experimento: un lector con esquema `R` lee datos con esquema `W` si, para cada campo de `R`, o el campo está en `W` con un tipo igual o promovible (int a long a float a double), o `R` le da un valor por defecto.

Según [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md):

Depende de quién actualiza primero. Con consumidores que no controlas, prefiere compatibilidad completa y valores por defecto; con un solo consumidor coordinado, basta un sentido. Escríbelo en el contrato.

## Ejemplo

Ejemplo de [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) (sección «Ejemplo mínimo»):

El campo nuevo con valor por defecto es compatible en los dos sentidos; sin valor por defecto, un lector nuevo no puede leer datos viejos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con mil registros escritos con el esquema viejo y un lector con el esquema nuevo, añadir un campo obligatorio sin valor por defecto, renombrar un campo y cambiar el tipo a texto dejaron ilegibles los 1 000. ([SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](./valor.md), [Cambio semántico](../c/cambio-semantico.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Contrato de datos](../c/contrato-de-datos.md), [Expandir, migrar y contraer](../e/expandir-migrar-y-contraer.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (60 clases más lo mencionan; las que más):

[SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Valores por defecto».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Valor percibido y cambio](./valor-percibido-y-cambio.md) · [Valor predictivo positivo →](./valor-predictivo-positivo.md)
