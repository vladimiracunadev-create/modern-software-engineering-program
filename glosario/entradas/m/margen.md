# Margen

[↑ Glosario](../../README.md) · [← Marca de agua](./marca-de-agua.md) · [Margen de contribución →](./margen-de-contribucion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Diferencia de puntaje entre el primero y el segundo.

Definición de trabajo de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

## Por qué importa

En [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), el tema «Margen y ruido» importa porque una diferencia pequeña no decide.

## Cómo funciona

Según [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

El segundo resultado es el margen: en el sistema crítico la arquitectura celular gana por 0,20 puntos sobre los microservicios, y en el equipo de seis el monolito modular gana por 0,35 sobre el monolito en capas. Una valoración de 1 a 5 tiene un error de al menos un punto en alguna celda, y un punto en una celda con peso 0,25 mueve el total en 0,25. Para cuantificarlo se perturbó cada celda en más o menos un punto con probabilidad 0,2 y se repitió 2 000 veces: el ganador del equipo de seis se mantuvo en el 92,7 % de las repeticiones, el de doce equipos en el 84,8 %, el de la plataforma en el 98,3 % y el del sistema crítico en el 77,2 %.

Según [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

El equipo de *Avisos* recibe las tres propuestas del problema auténtico. En lugar de votar, la líder pide un escenario por propuesta. La del microservicio queda como «el cálculo de avisos escala a 2 000 solicitudes por segundo sin degradar el resto de la plataforma»; la de complementos, como «una universidad añade su canal en una semana sin tocar el núcleo»; la de celdas, como «un cliente defectuoso afecta como máximo al 15 % de los inquilinos». Con los escenarios escritos aparece algo que no se veía: hoy el tráfico es de 80 solicitudes por segundo, de modo que el primer escenario no está en riesgo; el segundo ya ocurrió dos veces; el tercero ocurrió la semana pasada.

## Ejemplo

Ejemplo de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* recibe las tres propuestas del problema auténtico. En lugar de votar, la líder pide un escenario por propuesta. La del microservicio queda como «el cálculo de avisos escala a 2 000 solicitudes por segundo sin degradar el resto de la plataforma»; la de complementos, como «una universidad añade su canal en una semana sin tocar el núcleo»; la de celdas, como «un cliente defectuoso afecta como máximo al 15 % de los inquilinos».

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se usa para hacer visible el razonamiento, medir el margen y probar la sensibilidad; no para producir un número que decida solo. ([SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario de calidad](../e/escenario-de-calidad.md), [Estilo arquitectónico](../e/estilo-arquitectonico.md), [Matriz de decisión](./matriz-de-decision.md), [Punto de compromiso](../p/punto-de-compromiso.md), [Punto de sensibilidad](../p/punto-de-sensibilidad.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (75 clases más lo mencionan; las que más):

[SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Marca de agua](./marca-de-agua.md) · [Margen de contribución →](./margen-de-contribucion.md)
