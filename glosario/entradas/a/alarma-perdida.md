# Alarma perdida

[↑ Glosario](../../README.md) · [← Al menos una vez](./al-menos-una-vez.md) · [Alarma rutinaria →](./alarma-rutinaria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Ausencia de aviso cuando la propiedad se ha degradado.

Definición de trabajo de [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md).

## Por qué importa

La clase donde se define, [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), existe con este propósito: la clase existe para que conviertas una decisión de arquitectura en una prueba automática que la defienda a lo largo del tiempo, y para que sepas elegir su umbral y su frecuencia sin que falle al azar ni deje pasar el deterioro.

## Cómo funciona

Según [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md):

Las propiedades de ejecución (latencia, uso de memoria) son aleatorias. Una prueba que compara una medición con un umbral falla por el ruido aunque nada haya cambiado (falsa alarma) o pasa aunque haya empeorado (alarma perdida). Ambos errores dependen del umbral relativo al ruido y del número de muestras: más muestras estrechan la distribución del estadístico y permiten un umbral más cercano al valor esperado. Un margen holgado casi elimina las falsas alarmas y deja pasar regresiones considerables. La elección es una decisión estadística y de coste: cuántas muestras puedo pagar por ejecución.

Según [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md):

Traslada el análisis a otro sistema (por ejemplo, una biblioteca con una API pública): cambia las propiedades (compatibilidad, tamaño) y conserva el procedimiento de elegir frecuencia, calibrar el umbral contra el ruido y comparar alarmas. La transferencia está lograda cuando puedes decir qué error cuesta más en tu caso (falsa alarma o alarma perdida), no cuando el catálogo se parece.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md):

El equipo de la plataforma escribe un catálogo de siete funciones de aptitud: cuatro atómicas en cada commit (dominio sin importaciones de infraestructura, sin ciclos entre módulos, tamaño máximo del paquete, endpoints sin cambios incompatibles) y tres holísticas nocturnas (p95 del recorrido de entrega bajo 800 ms con 5 peticiones por segundo, capacidad en el pico, y tiempo de restauración).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md)) son:

- **Se descubren violaciones meses después** — causa: revisión infrecuente. Corrección: funciones atómicas baratas en cada commit.
- **La prueba de rendimiento falla al azar y se ignora** — causa: umbral cerca del valor esperado con pocas muestras. Corrección: más muestras o margen calibrado con la variabilidad.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se mide la fracción de ejecuciones sin cambio que fallan (falsas alarmas) y la de ejecuciones con una regresión del 20 % que no fallan (alarmas perdidas), con 2000 ejecuciones por celda. ([SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md))
- La transferencia está lograda cuando puedes decir qué error cuesta más en tu caso (falsa alarma o alarma perdida), no cuando el catálogo se parece. ([SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Erosión arquitectónica](../e/erosion-arquitectonica.md), [Falsa alarma](../f/falsa-alarma.md), [Función de aptitud arquitectónica](../f/funcion-de-aptitud-arquitectonica.md), [Trinquete](../t/trinquete.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-332 — Fitness functions y arquitectura evolutiva](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Ford, Parsons y Kua, «Building Evolutionary Architectures» (O'Reilly)](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — funciones de aptitud y arquitectura evolutiva; autoridad: O'Reilly Media.
- [Thoughtworks Technology Radar, «Architectural fitness function»](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) — técnica de funciones de aptitud en la entrega; autoridad: Thoughtworks.
- [Google SRE, «Service Level Objectives»](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y percentiles; autoridad: Google SRE.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis de importaciones del ejemplo mínimo; autoridad: documentación de Python.
- [Python: `statistics`](https://docs.python.org/3/library/statistics.html) — mediana y cuantiles; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Al menos una vez](./al-menos-una-vez.md) · [Alarma rutinaria →](./alarma-rutinaria.md)
