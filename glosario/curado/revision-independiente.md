# Revisión independiente

## Definición

La **revisión independiente** es una evaluación hecha sin autoría directa ni incentivo dominante (`SE-005`). `SE-468` la concreta como el examen de un paquete por una persona que no lo produjo, y `SE-456` como la revisión por alguien que no desarrolló el sistema. «Independiente» no significa desconocedora ni neutral: significa menos comprometida con la autoría.

## Por qué importa

Quien construye algo ve lo que quiso hacer, no necesariamente lo que hizo. Una persona externa halla fallos que el autor no ve y cuestiona supuestos que el autor da por obvios. A mayor impacto e irreversibilidad, más importante es separar incentivos (`SE-005`). Cambia quién puede aprobar un cambio, una evidencia de seguridad o un caso crítico.

## Cómo funciona

`SE-005` establece las condiciones:

- La persona revisora necesita **contexto** (para entender) y **autoridad** (para cuestionar y detener).
- No significa desconocimiento ni neutralidad absoluta: aporta una perspectiva menos comprometida con la autoría.
- En equipos pequeños, si la misma persona propone y revisa, se **limita el alcance**, se buscan criterios automatizados o revisión externa y se **registra la limitación**.

En sistemas críticos (`SE-456`), la revisión independiente de un caso de seguridad es parte de la práctica: la persona externa aporta escenarios de uso que el equipo desconoce (véase *evidencia*, donde un comité plantea qué ocurre con una carga térmica no considerada). En cumplimiento (`SE-468`), el paquete de evidencia lo examina alguien que no lo produjo, para que «cumple» no sea la palabra del mismo equipo que lo declara.

La cantidad de personas no es lo importante: se necesitan las necesarias para cubrir competencia, autoridad y revisión independiente, no un número fijo; más personas sin interfaz clara añaden espera.

## Ejemplo

Un equipo de tres personas despliega un cambio de permisos. La autora propone; una compañera de otro equipo, con acceso al contexto y autoridad para bloquear, revisa el diff y las pruebas. Registro:

```text
Cambio: ampliar rol "docente" | Autor: A | Revisión: B (otro equipo) | Decisión: aprobado con 1 observación resuelta
```

## Errores y confusiones comunes

- **Todos son «responsables».** Se evitó declarar autoridad; corrección: nombrar quién acepta, detiene y escala cada decisión (`SE-005`).
- **Revisión sin autoridad.** La persona revisora puede opinar pero no detener, y la revisión es decorativa.
- **Confundirla con una segunda firma automática.** Un clic de aprobación sin leer no es una revisión.

## Límites y cuándo no aplica

Para cambios de bajo impacto y fácilmente reversibles, una revisión independiente completa puede costar más de lo que protege; bastan criterios automatizados. En equipos muy pequeños puede no existir una persona independiente, y entonces el límite se declara. Y una revisión independiente no certifica ausencia de defectos: acota el sesgo de autoría, no el alcance de lo revisado.
