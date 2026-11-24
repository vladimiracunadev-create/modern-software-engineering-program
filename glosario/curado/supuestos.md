# Supuestos

## Definición

Un **supuesto** es una creencia sobre personas, mercado, tecnología o negocio que debe ser cierta para que la idea funcione y que aún no ha sido verificada (SE-124). SE-187 lo usa en planificación: algo que damos por cierto para planificar y que puede comprobarse; si es falso, el plan estaba mal desde el principio. SE-450 lo usa en argumentos de seguridad: una condición que se da por cierta y que acota el argumento.

## Por qué importa

Toda idea descansa en creencias no verificadas; hacerlas explícitas es lo único que permite contrastarlas. Un supuesto oculto no se puede probar y falla por sorpresa. Cambia el modo de planificar: se pregunta qué tendría que ser cierto, y se decide qué comprobar primero.

## Cómo funciona

SE-124 dice que un supuesto **no es un defecto**: es la parte de la idea que todavía es creencia. **El defecto es no nombrarlo.** Se encuentran preguntándose, para cada paso de la idea, qué tendría que ser cierto: que las personas tengan el problema, que lo reconozcan, que prefieran esta solución a las alternativas, que puedan usarla, que la institución la autorice. Unos son **observados** (hay 42 tickets al mes) y otros **esperados** (las docentes autorizarán guardar borradores).

SE-187 los distingue del riesgo: un supuesto **no es un evento futuro sino una creencia presente**; si es falsa, el plan estaba mal desde el principio. Ejemplos: «las estudiantes usan navegadores actuales», «el rendimiento será de cinco a ocho elementos por semana». Se registra **con quién lo afirma, qué evidencia tiene y cómo se comprobaría**, y se valida **por orden de coste de fallar y de comprobar**: primero los de gran daño si fallan y barata comprobación.

SE-124 añade la priorización: se ordenan por cuánto mueven el resultado y cuán inciertos son (sensibilidad e incertidumbre), y los críticos se convierten en hipótesis falsables. El mapa de supuestos conserva por cada uno enunciado, tipo, rango, impacto, costo de contrastarlo, hipótesis falsable, umbral, regla de decisión y fecha. Y la regla: ninguna hipótesis cambia de umbral tras observar.

## Ejemplo

Plan de lanzamiento. Supuesto A: «las estudiantes usan navegadores actuales» (afirma: producto; evidencia: estadísticas de acceso del año pasado; se comprobaría mirando el registro de accesos; barato). Supuesto B: «las docentes autorizarán guardar borradores» (esperado; costo de fallar: invalida la idea; se comprueba con cinco entrevistas). Orden de validación: B primero por su alto costo de fallar, A después por ser barato. (Ilustración del criterio de SE-187.)

## Errores y confusiones comunes

- **Dar por hecho sin nombrarlo.**
- **Confundir supuesto con riesgo**: el supuesto es una creencia presente; el riesgo, un evento posible.
- **Supuestos sin responsable ni evidencia.**
- **Comprobar el más cómodo** y no el más sensible.

## Límites y cuándo no aplica

No se pueden enumerar todos los supuestos; se listan los relevantes. Algunos solo se comprueban construyendo. En el sentido de SE-450, un supuesto de un argumento de seguridad debe revisarse cuando cambia el entorno, o el argumento deja de valer.
