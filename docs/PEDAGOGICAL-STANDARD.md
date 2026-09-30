# Estándar permanente de desarrollo pedagógico

## Principio central

El repositorio es un programa profesional de aprendizaje. Cada clase debe permitir
comprender, razonar, practicar y verificar el tema sin depender de conocimiento
implícito. Una estructura completa no compensa contenido superficial.

La referencia de calidad es la Parte 6 de
[`modern-cybersecurity-program`](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/tree/main/classes/parte-6-analisis-de-malware):
explicación fluida desde primeros principios, conceptos desarrollados en contexto,
diagramas interpretados, práctica coherente y fuentes que respaldan afirmaciones.
No se copia su contenido ni se usa su extensión como plantilla.

## Contrato cualitativo de una clase

Una clase candidata a `GUIDED` debe integrar, como mínimo:

1. objetivo que explique capacidad, propósito y límite;
2. resultados de aprendizaje observables;
3. tabla de temas donde cada fila explique por qué importa;
4. explicación en profundidad de **todos** los temas anunciados;
5. causas, mecanismos, decisiones, consecuencias y relaciones con clases previas;
6. ejemplos razonados y contraejemplos que cambien la conclusión;
7. definiciones técnicas en contexto y glosario no circular;
8. diagrama específico interpretado dentro del texto;
9. herramientas, versiones, entorno, archivos clave, preparación y recuperación;
10. laboratorio o práctica reproducible, segura y adecuada al tipo de clase;
11. ejercicios graduados y reto con criterio de aceptación verificable;
12. errores comunes expresados como síntoma → causa → solución;
13. preguntas frecuentes auténticas que resuelvan ambigüedades;
14. seguridad, privacidad, accesibilidad, ética y licencias aplicables;
15. fuentes primarias u oficiales vinculadas a afirmaciones concretas;
16. navegación a prerrequisitos, clase anterior y siguiente;
17. límites honestos: qué no se ejecutó, midió o validó.

Una tabla, un enlace o una lista no sustituyen la explicación. Un generador puede
crear estructura y comprobaciones, pero no otorga madurez pedagógica.

## Contrato de una parte

Cada parte debe explicar:

- propósito, problemas profesionales y audiencia;
- resultados de aprendizaje acumulativos;
- prerrequisitos enlazados;
- bloques temáticos y progresión;
- recorrido clase por clase: qué enseña, por qué aparece allí y qué evidencia produce;
- proyecto integrador, criterios de salida y pregunta de control por bloque;
- fuentes de la parte y relación explícita con sus clases.

## Profundidad y estilo

- La extensión depende del tema; se prohíben cuotas uniformes de palabras.
- Evita párrafos intercambiables, frases robóticas y ejemplos ornamentales.
- Explica primero principios y mecanismos; las herramientas vienen después.
- Distingue hechos documentados, inferencias pedagógicas, ejemplos hipotéticos y
  decisiones dependientes del contexto.
- Una clase conceptual debe producir evidencia verificable; no necesita código falso.
- Una clase técnica debe declarar compatibilidad, versiones, limpieza y recuperación.

## Fuentes y vigencia

- Prioriza estándares, especificaciones, documentación oficial, proyectos primarios,
  libros con ISBN y artículos con DOI.
- Registra título, autoridad, localizador, estado y fecha de verificación.
- Explica qué afirmación o concepto respalda cada fuente.
- Marca fuentes retiradas o superadas y su reemplazo.
- No reproduzcas material protegido ni uses una bibliografía como decoración.

## Gate de aprobación

La aprobación se realiza clase por clase y luego parte por parte:

1. cobertura de todos los temas;
2. revisión técnica y pedagógica contra este documento;
3. práctica y criterio de aceptación reproducibles;
4. fuentes y enlaces verificados;
5. ausencia de frases genéricas repetidas entre clases;
6. contenido íntegro visible en GitHub Pages;
7. validadores, pruebas, encoding y workflows verdes;
8. commit independiente para la parte.

Solo entonces se cambia `PLANNED` a `GUIDED`. Los estados `EXECUTABLE`, `TESTED`,
`INTEGRATED` y `OPERABLE` requieren evidencia adicional definida en la arquitectura.

## Alcance corregido de fase 3

La fase 3 comprende **180 clases consecutivas**, de `SE-001` a `SE-180`, agrupadas
en las partes 00–14. Mientras una clase no supere el gate, permanece `PLANNED` aunque
exista un borrador público.
