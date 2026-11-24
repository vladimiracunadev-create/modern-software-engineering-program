# Segmentación por necesidad

## Definición

La **segmentación por necesidad** agrupa a las personas que comparten un trabajo, un contexto y resultados insatisfechos, y que justifican una decisión de producto distinta de la del resto (SE-126). Se opone a segmentar por rasgos de superficie como edad, cargo o región.

## Por qué importa

Un segmento útil se distingue por lo que necesita y hace, y **cambia qué se construye**. Segmentar por edad o cargo es fácil de medir y casi nunca cambia el producto: dos personas del mismo cargo pueden tener necesidades opuestas, y dos de cargos distintos, la misma. Cambia a quién se le diseña, cómo se llega a esa gente y cuánto está dispuesta a esforzarse.

## Cómo funciona

SE-126 plantea una prueba de utilidad con dos preguntas: ¿el segmento cambia una decisión (qué se construye, cómo se llega a él, cuánto está dispuesto a esforzarse)? ¿El equipo puede **reconocer** a una persona como parte de él? Un segmento que nadie puede identificar no se puede alcanzar ni validar. Un ejemplo de la clase: quienes entregan desde móvil con conexión débil. Lo define el contexto y el trabajo, no un dato demográfico.

El mapa de segmentos de la plataforma de entregas conserva, por segmento: el criterio de definición, los trabajos, los contextos, los resultados insatisfechos, el tamaño como rango con método y supuestos, el canal de acceso y las alternativas con los trabajos que cubren. Dos reglas del contrato: ningún segmento se declara sin decir cómo se reconocería a una persona de él, y ninguna cifra de mercado se publica sin su rango.

Cuando los segmentos se derivan con un algoritmo de agrupamiento, hay que añadir dos controles: la **estabilidad** (el agrupamiento debe reproducirse con otra semilla o submuestra, y compararse con la estabilidad sobre ruido) y el **significado** (los grupos deben diferir en comportamiento o necesidad). Un agrupamiento estable pero sin significado de negocio no es un segmento.

## Ejemplo

Segmentación por cargo: «docentes». Segmentación por necesidad: «docentes que corrigen en el móvil entre clases y necesitan ver quién entregó sin abrir cada entrega», «docentes que gestionan cursos de 200 estudiantes y necesitan correcciones por lote». El primero se resuelve con un panel compacto; el segundo, con flujos de lote. Dos decisiones de producto distintas dentro del mismo cargo. (Ejemplo ilustrativo apoyado en el patrón de SE-126.)

## Errores y confusiones comunes

- **Segmentos que cambian al repetir el análisis**: agrupamiento inestable.
- **Segmentos estables que nadie reconoce**: estabilidad sobre ruido o variables sin sentido de negocio.
- **Segmentar por lo que es fácil de medir.**
- **Publicar el tamaño de mercado como cifra única.**

## Límites y cuándo no aplica

Cuando hay un solo trabajo y un contexto homogéneo, segmentar no aporta. Los segmentos por necesidad exigen investigación cualitativa, que es costosa y se hace con pocas personas: son hipótesis con incertidumbre. Un segmento puede mezclar necesidades que solo se separan al construir. Y los segmentos cambian cuando cambia el contexto.
