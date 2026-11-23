# Criterio de retroceso

[↑ Glosario](../../README.md) · [← Criterio de parada](./criterio-de-parada.md) · [Criterio de salida →](./criterio-de-salida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Condición medible que devuelve el tráfico al sistema antiguo.

Definición de trabajo de [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md).

## Por qué importa

La clase donde se define, [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), existe con este propósito: la clase existe para que puedas cambiar la arquitectura de un sistema que está en producción sin detenerlo y sin apostar el negocio a una fecha de corte.

## Cómo funciona

Según [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md):

El equipo de *Avisos* descarta el fin de semana de corte y propone una migración con tres pasos y un criterio por paso. Primero, una interfaz `CalculadoraDeAvisos` con la implementación heredada detrás. Segundo, el módulo nuevo en sombra durante dos ciclos de entrega completos, con un informe diario de divergencias por causa; el primer informe muestra el 1 % de diferencias, y el tercero tiene cero tras decidir con las docentes los tres comportamientos en disputa y escribirlos como pruebas. Tercero, escalones del 1, 5, 25 y 100 % con un criterio de retroceso: si la tasa de errores del nuevo supera en un 0,2 % absoluto la del antiguo en un escalón, el tráfico vuelve.

## Ejemplo

Ejemplo de [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* descarta el fin de semana de corte y propone una migración con tres pasos y un criterio por paso. Primero, una interfaz `CalculadoraDeAvisos` con la implementación heredada detrás. Segundo, el módulo nuevo en sombra durante dos ciclos de entrega completos, con un informe diario de divergencias por causa; el primer informe muestra el 1 % de diferencias, y el tercero tiene cero tras decidir con las docentes los tres comportamientos en disputa y escribirlos como pruebas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md)) son: Los dos módulos, las tres diferencias, las tasas y las peticiones son construcciones del autor; la detección se calculó por muestreo y por una distribución de Poisson con supuestos declarados. No se migró ningún sistema real ni se midió el costo humano de mantener dos versiones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Abstracción de rama](../a/abstraccion-de-rama.md), [Escalón de tráfico](../e/escalon-de-trafico.md), [Estrangulamiento](../e/estrangulamiento.md), [Expandir, migrar y contraer](../e/expandir-migrar-y-contraer.md), [Fachada](../f/fachada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Criterio de parada](./criterio-de-parada.md) · [Criterio de salida →](./criterio-de-salida.md)
