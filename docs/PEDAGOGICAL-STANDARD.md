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

Una clase que se presente como desarrollada debe integrar, como mínimo:

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
crear estructura y comprobaciones, pero no demuestra profundidad pedagógica.

## Contrato de una parte

Cada parte debe explicar:

- propósito, problemas profesionales y audiencia;
- resultados de aprendizaje acumulativos;
- prerrequisitos enlazados;
- bloques temáticos y progresión;
- recorrido clase por clase: qué enseña, por qué aparece allí y qué evidencia produce;
- proyecto integrador, criterios de salida y pregunta de control por bloque;
- fuentes de la parte y relación explícita con sus clases.

## Contrato de continuidad y experiencia visual

La clase no se presenta como un archivo aislado. Antes del contenido principal debe
activar lo aprendido, explicar por qué aparece ahora, anticipar qué evidencia se
construirá y declarar cómo esa evidencia alimenta la clase siguiente. Cada parte debe
mantener un caso conductor, proyecto o pregunta profesional que permita revisitar el
mismo sistema con lentes progresivamente más exigentes.

El portal debe ayudar a orientarse y razonar, no limitarse a decorar Markdown:

- muestra parte, posición, clase anterior, capacidad actual y conexión siguiente;
- diferencia visualmente explicación, práctica, evidencia, fuentes y límites;
- transforma diagramas en una representación legible y conserva una alternativa
  textual o notación fuente accesible;
- interpreta cada visual dentro del texto: qué relación muestra, por qué importa y
  dónde deja de ser válida;
- usa tablas, mapas, secuencias o comparaciones solo cuando reducen carga cognitiva;
- evita imágenes ornamentales, iconos ambiguos y color como único portador de sentido;
- conserva lectura cómoda en móvil, teclado, zoom y movimiento reducido;
- mantiene el contenido íntegro disponible sin depender de JavaScript externo.

Una estética consistente debe reforzar jerarquía, continuidad y atención. No compensa
contenido superficial, pero una presentación descuidada sí puede impedir aprender de
contenido correcto.

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

## Revisión para publicación

La aprobación se realiza clase por clase y luego parte por parte:

1. cobertura de todos los temas;
2. revisión técnica y pedagógica contra este documento;
3. práctica y criterio de aceptación reproducibles;
4. fuentes y enlaces verificados;
5. ausencia de frases genéricas repetidas entre clases;
6. contenido íntegro visible en GitHub Pages;
7. recorrido, diagramas y navegación comprobados en escritorio y móvil;
8. validadores, pruebas, encoding y workflows verdes;
9. commit independiente para la parte.

Solo entonces puede describirse como desarrollada. Si se afirma que una práctica fue
ejecutada, probada, integrada u operada, esa afirmación debe acompañarse de evidencia
adicional definida en la arquitectura.

## Alcance corregido de fase 3

La fase 3 comprende **180 clases consecutivas**, de `SE-001` a `SE-180`, agrupadas
en las partes 00–14. Las Partes 00–02 están desarrolladas; las partes 03–14 conservan
borradores que deben superar la revisión completa antes de presentarse como clases
terminadas.

## Alcance de fase 4

La fase 4 comprende **180 clases consecutivas**, de `SE-181` a `SE-360`, agrupadas
en las partes 15–29. Aplica la misma revisión cualitativa: disponer de guía, actividad,
rúbrica, fuentes y publicación no demuestra por sí solo que la clase esté terminada.
