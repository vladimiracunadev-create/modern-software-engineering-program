# Defensa por profundidad

## Definición

En este programa, la **defensa por profundidad** es la secuencia de preguntas cada vez más específicas sobre un mismo trabajo para descubrir hasta dónde llega la comprensión de quien lo hizo. Es la definición de `SE-538`, en la parte de gestión y práctica profesional, y se refiere a defender un trabajo ante una persona evaluadora (portafolio, entrevista, comité).

**Atención a la homonimia:** en seguridad, «defensa en profundidad» (*defense in depth*) designa otra cosa, la superposición de controles para que el fallo de uno no exponga el sistema. El programa usa aquí el sentido de `SE-538`, el de las preguntas escalonadas; para el otro, véase mínimo privilegio y los controles de las clases de seguridad.

## Por qué importa

Cambia cómo se prepara y cómo se presenta el trabajo. Quien lo hizo conoce los primeros niveles de memoria; a cierto punto se topa con lo que no probó o no entendió. La decisión es qué hacer en ese punto, y la clase la formula como dos estrategias con consecuencias distintas.

## Cómo funciona

Una defensa profesional sigue una escalera: *qué hiciste → por qué esa opción → qué pasa si falla → cómo lo probaste → qué cambiarías*. Cada nivel exige más precisión que el anterior y deja menos espacio para respuestas de memoria.

En el límite de lo que se sabe hay dos estrategias (`SE-538`):

- **Defender con seguridad.** A veces se acierta por intuición; cuando falla, la persona evaluadora lo detecta y el daño no queda en esa pregunta: contagia las anteriores («¿qué más fue invención?»).- **Declarar el límite y proponer cómo comprobarlo.** Por ejemplo: «eso no lo probé; lo comprobaría repitiendo la entrega dos veces y mirando los duplicados».

La causa de que la segunda gane es que preserva la credibilidad de todo lo respondido antes: una frontera honesta da valor a lo que sí se afirmó.

## Ejemplo

Se presenta una entrada de portafolio sobre una cola de entregas. Pregunta 1: ¿qué hiciste? Respuesta con comando y datos sintéticos. Pregunta 3: ¿qué pasa si el trabajador muere a mitad de procesar? Aquí la persona no lo probó. Defender con seguridad sería afirmar que «se reintenta sin problema». La respuesta de `SE-538` sería: «no lo probé; lo comprobaría matando el proceso a mitad, repitiendo la entrega y contando los duplicados». Esa respuesta convierte un hueco en un plan verificable. (El ejemplo es ilustrativo; la clase usa una entrada de portafolio comprobable y un verificador sobre cuatro entradas del autor.)

## Errores y confusiones comunes

- **Nadie puede reproducir mis resultados.** Faltan comando, versión o datos; corrección de `SE-538`: incluir comando, entorno y datos sintéticos.
- **El comité duda de mi alcance.** Se describe participación en lugar de autoría; hay que atribuir con precisión qué se decidió y qué se hizo.
- **Confundirla con la defensa en profundidad de seguridad.** Son conceptos distintos (véase arriba).
- **Memorizar respuestas.** Funciona en los primeros niveles y se rompe en los profundos.

## Límites y cuándo no aplica

`SE-538` usa datos sintéticos y un verificador sobre cuatro entradas escritas por el autor, y sus definiciones son operativas para el equipo de plataforma educativa; no mide el comportamiento de personas evaluadoras reales. Declarar un límite no compensa un trabajo sin sustancia: solo es valioso si el resto es sólido. Y depende del contexto: algunas evaluaciones esperan respuesta inmediata y no admiten «lo comprobaría».
