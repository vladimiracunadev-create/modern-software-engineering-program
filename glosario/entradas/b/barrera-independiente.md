# Barrera independiente

[↑ Glosario](../../README.md) · [← Bandera de funcionalidad](./bandera-de-funcionalidad.md) · [Barrera independiente de la consulta →](./barrera-independiente-de-la-consulta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Defensa que no falla por la misma causa que la defendida.

Definición de trabajo de [SE-455 — Taller: analizar un fallo real frente a las normas](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md).

## Por qué importa

En [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), el tema «Barrera independiente» importa porque quita la responsabilidad de cada consulta.

## Cómo funciona

Según [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md):

Si cada función recibe `tenant_id` como argumento, cada función puede olvidarlo. Si el contexto del inquilino se establece una vez al entrar la petición (a partir del token validado, como se vio en `SE-341`) y la capa de datos lo aplica sin que el código de negocio lo escriba, el error de olvido deja de ser posible en ese código. Es la misma idea de las barreras independientes: mover la responsabilidad de «recordar» a un lugar donde se escribe una vez.

Según [SE-455 — Taller: analizar un fallo real frente a las normas](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md):

Cuando una protección depende de un único componente, un solo defecto basta. Es la idea de `SE-446` (independencia de los canales, causa común) aplicada a una arquitectura completa: tras retirar interbloqueos de hardware, la protección de seguridad era la misma pieza que producía el fallo. La medida de control es de arquitectura: una barrera independiente (hardware, otro principio) que no pueda ser anulada por el mismo error. En el modelo del laboratorio, un enclavamiento de hardware con una probabilidad de falla del autor del 1 % reduce las exposiciones peligrosas de 5 705 a 58 por 100 000 tratamientos, un 99 %, sin tocar la causa de las inconsistencias, que sigue produciendo 5 627.

## Ejemplo

Ejemplo de [SE-455 — Taller: analizar un fallo real frente a las normas](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) (sección «Preguntas frecuentes»):

Porque el modelo permite comparar controles y ver la sensibilidad (cuánto pesa la ventana, cuánto la barrera independiente) y porque entrenar la traducción de un caso a un modelo es la habilidad que se aplicará a un sistema que todavía no falló.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se probó una barrera independiente: al abrir la conexión de cada solicitud, se crea una vista temporal con el nombre de la tabla que oculta la real y solo muestra las filas del inquilino (`CREATE TEMP VIEW deliveries AS SELECT * FROM deliveries_all WHERE tenant_id = N`). ([SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aislamiento de datos](../a/aislamiento-de-datos.md), [Alarma rutinaria](../a/alarma-rutinaria.md), [Análisis retrospectivo](../a/analisis-retrospectivo.md), [Barrera independiente de la consulta](./barrera-independiente-de-la-consulta.md), [Condición de carrera](../c/condicion-de-carrera.md), [Envoltura de un byte](../e/envoltura-de-un-byte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-455 — Taller: analizar un fallo real frente a las normas](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Bandera de funcionalidad](./bandera-de-funcionalidad.md) · [Barrera independiente de la consulta →](./barrera-independiente-de-la-consulta.md)
