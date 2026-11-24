# Comprobación automática

## Definición

Una **comprobación automática** es una verificación ejecutada por una máquina antes o durante la revisión humana (SE-196). Incluye compilación, pruebas, análisis estático, formato, licencias y búsqueda de secretos. Se distingue de la revisión humana, que juzga el sentido del cambio.

## Por qué importa

Libera a la persona de lo que una máquina comprueba y deja para ella el sentido: ¿es esta la regla correcta?, ¿se probó el caso límite? Una revisora que gasta su atención en señalar un espacio de más tiene menos para detectar una regla mal aplicada. Cambia el orden del proceso: las comprobaciones se ejecutan **antes** de pedir revisión humana.

## Cómo funciona

El flujo de integración continua ejecuta las comprobaciones sobre cada cambio y devuelve un resultado objetivo. SE-196 las ubica antes de la asignación de revisora: formato, pruebas, análisis estático y búsqueda de secretos. Si alguna falla, el autor corrige sin consumir tiempo ajeno.

Su virtud es la repetibilidad: la máquina aplica la misma regla a todos los cambios, sin cansarse ni preferencias. Su límite es el que la clase destaca: **detecta forma y no intención**. Una comprobación puede asegurar que el código compila, que el formato es el acordado o que no hay secretos, pero no sabe si la regla de negocio está bien, si faltan casos o si la prueba verifica algo. Por eso no sustituye la lectura de los archivos de mayor riesgo.

Las comprobaciones se combinan con el triaje por riesgo (qué leer primero) y con las comprobaciones de forma de un paquete (mensajes convencionales, commits atómicos, tamaño del PR): lo mecánico se automatiza; lo que exige juicio queda para la persona. Una comprobación que nadie hace cumplir se degrada en pocas semanas, por eso se ejecutan como requisito de integración y no como recomendación.

En la plataforma de entregas, el CODEOWNERS añade como revisor obligatorio al equipo dueño de las migraciones cuando un PR toca `migraciones/`; es una comprobación automática de que la revisión correcta ocurre.

## Ejemplo

Un PR cambia la fórmula de penalización. Las comprobaciones automáticas pasan: compila, las pruebas existentes pasan, el análisis estático no encuentra alertas y no hay secretos. Pero la regla de negocio nueva redondea mal en el empate y ninguna prueba cubre ese caso: lo detecta la revisora al leer el cambio, no la máquina. (Ilustración del límite que enseña SE-196.)

## Errores y confusiones comunes

- **Comentarios de estilo y defectos que se escapan**: se revisa a mano lo que una máquina haría; corrección: automatizar el estilo.
- **Creer que verde significa correcto.**
- **Comprobaciones lentas o inestables** que la gente aprende a ignorar.
- **Ejecutarlas después de la revisión**: la persona revisa un cambio que luego debe cambiar.

## Límites y cuándo no aplica

No detectan lo que no se escribió como regla ni la intención del cambio. En proyectos muy pequeños, mantenerlas cuesta más que el beneficio. Un conjunto de comprobaciones muy amplio puede dar falsa confianza si las pruebas son débiles.
