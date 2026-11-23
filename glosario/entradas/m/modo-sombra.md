# Modo sombra

[↑ Glosario](../../README.md) · [← Modo degradado](./modo-degradado.md) · [Modo texto y modo binario →](./modo-texto-y-modo-binario.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Ejecutar el sistema nuevo con tráfico real sin devolver su respuesta, solo para compararla.

Definición de trabajo de [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md).

## Por qué importa

En [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), el tema «Modo sombra» importa porque descubre diferencias antes de que las vea el usuario.

## Cómo funciona

Según [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md):

En el modo sombra, cada petición se envía al sistema antiguo, cuya respuesta se devuelve al usuario, y también al nuevo, cuya respuesta se compara y se descarta. En el experimento se ejecutaron ambos módulos sobre 20 000 peticiones sintéticas: difirieron en 203 (1,01 %). Las causas, clasificadas, fueron 145 por redondeo en el borde (el módulo nuevo trunca los minutos a horas y el antiguo conserva la fracción), 57 por un plazo de extensión que el antiguo concede y el nuevo olvidó, y 1 por un cambio de hora que el antiguo trata con un desplazamiento. Cada divergencia es una pregunta de negocio:

## Ejemplo

Caso medido en la sección «Modo sombra: dos respuestas, una decisión» de [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md):

En el modo sombra, cada petición se envía al sistema antiguo, cuya respuesta se devuelve al usuario, y también al nuevo, cuya respuesta se compara y se descarta. En el experimento se ejecutaron ambos módulos sobre 20 000 peticiones sintéticas: difirieron en 203 (1,01 %). Las causas, clasificadas, fueron 145 por redondeo en el borde (el módulo nuevo trunca los minutos a horas y el antiguo conserva la fracción), 57 por un plazo de extensión que el antiguo concede y el nuevo olvidó, y 1 por un cambio de hora que el antiguo trata con un desplazamiento.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md)) son: Los dos módulos, las tres diferencias, las tasas y las peticiones son construcciones del autor; la detección se calculó por muestreo y por una distribución de Poisson con supuestos declarados. No se migró ningún sistema real ni se midió el costo humano de mantener dos versiones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abstracción de rama](../a/abstraccion-de-rama.md), [Criterio de retroceso](../c/criterio-de-retroceso.md), [Escalón de tráfico](../e/escalon-de-trafico.md), [Estrangulamiento](../e/estrangulamiento.md), [Expandir, migrar y contraer](../e/expandir-migrar-y-contraer.md), [Fachada](../f/fachada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-346 — Evolución y migración entre estilos](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Modo degradado](./modo-degradado.md) · [Modo texto y modo binario →](./modo-texto-y-modo-binario.md)
