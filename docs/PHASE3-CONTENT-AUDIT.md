# Auditoría de contenido de fase 3

## Resultado

La fase 3 está **parcialmente construida**. Su alcance correcto es de 180 clases,
`SE-001`–`SE-180`: las partes 00–01 aportan 24 clases `GUIDED` y las 156 restantes aún
no superan el estándar pedagógico permanente.

Esta auditoría distingue tres hechos:

1. existe la identidad curricular de las 180 clases;
2. existen borradores estructurales, actividades y rúbricas generadas;
3. esos artefactos no equivalen a clases desarrolladas ni aprobadas.

## Evidencia observada el 2026-09-30

| Comprobación | Resultado | Interpretación |
| --- | ---: | --- |
| clases dentro del alcance | 180 | `SE-001`–`SE-180` |
| borradores que repiten el mismo párrafo genérico | 0 | el párrafo señalado en la auditoría anterior ya no aparece |
| clases con sección `Definiciones de trabajo` | 180 | existe una base terminológica inicial |
| clases con sección `Glosario` | 24 | Partes 00–01 reconstruidas; requisito pendiente en las demás partes |
| clases con sección `Preguntas frecuentes` | 180 | existe una capa de aclaración inicial |
| clases con sección `Reto verificable` | 180 | existe una extensión evaluable de la práctica |
| clases aprobadas | 24 | Partes 00–01 aprobadas; las otras 156 permanecen `PLANNED` |

El conteo es evidencia negativa, no un criterio suficiente de calidad. Aunque se
añadieran encabezados, cada clase seguiría necesitando una revisión técnica y
pedagógica integral.

## Defectos cualitativos

- explicaciones intercambiables entre temas distintos;
- conceptos todavía pendientes de validación técnica individual por un revisor;
- ejemplos genéricos que no demuestran el concepto de la clase;
- prácticas sin preparación técnica suficiente ni resultado específico;
- fuentes agrupadas por parte, pero no ligadas a afirmaciones concretas;
- ausencia de un glosario consolidado y de enlaces de fuente por afirmación;
- diagramas formales sin interpretación específica suficiente;
- índices que antes obligaban a recorrer carpetas para localizar una clase.

## Decisión de integridad

- conservar las 180 entradas como borradores públicos para que el defecto sea
  auditable;
- conservar `PLANNED` en toda clase que no haya superado el gate completo;
- no usar `GUIDED` hasta superar
  [`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md);
- reconstruir por parte, con un commit independiente y revisión cualitativa;
- publicar índices con enlaces directos a GitHub y GitHub Pages.

## Avance editorial de la Parte 00

Las doce clases `SE-001`–`SE-012` ya no dependen del generador temático genérico:
sus fuentes canónicas están en `content/part-00/` y el portal publica ese texto
íntegro. Cada clase desarrolla mecanismos propios, ejemplo y contraejemplo,
práctica, fallo controlado, glosario, transferencia, límites y fuentes próximas.
La revisión posterior añadió el caso conductor `Campus Abierto`, una activación
“Antes de empezar” específica, conexiones visibles con la clase anterior y siguiente,
progreso dentro de la parte y mapas conceptuales renderizados con alternativa textual.
El portal fue verificado en escritorio y en un viewport móvil de 390 px sin
desbordamiento horizontal.
Tras revisar enlaces, contenido, publicación y validadores, la Parte 00 superó el
gate y sus doce clases avanzaron a `GUIDED`. Esta promoción no atribuye estados
`EXECUTABLE`, `TESTED` u `OPERABLE` ni se extiende a las demás partes.

## Avance editorial de la Parte 01

Las clases `SE-013`–`SE-024` fueron reemplazadas por fuentes canónicas en
`content/part-01/`. El caso conductor `Pulso` conecta representación, Unicode,
aritmética, CPU, memoria, procesos, traducción, runtime y medición hasta un taller y
un informe reproducible. Cada clase declara mecanismo, entorno, práctica segura,
fallo controlado, errores, fuentes y límites instrumentales. El README completo de la
parte se publica también en Pages. Tras revisión clase por clase y de la progresión
completa, las doce clases avanzaron a `GUIDED`; no se promovieron a estados que exigen
ejecución o evidencia productiva.

## Orden de reconstrucción

La fase se desarrolla en quince entregas: partes 00 a 14. Cada entrega debe incluir
las doce clases de la parte, el README narrativo de la parte, fuentes trazables,
actividades, rúbricas, publicación visual y workflows verdes. No se contabiliza una
parte por archivos creados, sino por clases aprobadas contra el gate.
