# Propietario de código

## Definición

Un **propietario de código** es la persona o el equipo responsable de una ruta del repositorio y a quien se pide revisión cuando cambia (SE-199). Se declara en un archivo `CODEOWNERS` que asocia patrones de ruta con personas o equipos. No debe confundirse con el propietario de un campo de datos ni con la propiedad de archivos en el sentido de permisos del sistema operativo.

## Por qué importa

Decide quién debe ver cada cambio. Sin propietarios declarados, la revisión depende de quién esté disponible o de quién se acuerde; un hueco deja un cambio sin revisión con dueño. Cambia el flujo de revisión: la plataforma pide revisión a la persona correcta de forma automática.

## Cómo funciona

Un archivo CODEOWNERS contiene reglas de la forma «patrón de ruta → propietarios». Cuando un pull request toca una ruta, la plataforma **pide revisión** a los propietarios correspondientes y, si la **protección de rama** lo exige, **requiere su aprobación** antes de fusionar. SE-199 subraya que un propietario es **una responsabilidad, no un privilegio**: debe ser alguien que pueda revisar y que exista (una cuenta o equipo real, activo).

Dos propiedades del archivo causan fallos clásicos. Primera, **el orden importa**: cuando varias reglas coinciden con una ruta, gana la última, de modo que lo específico va después de lo general. Si una regla posterior más amplia cubre la ruta, el PR no pide revisión a quien debería. Segunda, **las rutas sin regla no tienen propietario**: la solución es una regla `*` al principio que asigne un propietario por defecto, de modo que ninguna ruta quede sin dueño.

En la plataforma de entregas, el archivo tiene un comentario por regla con su motivo, la regla `*` al comienzo y reglas específicas al final (por ejemplo, el equipo dueño de `migraciones/` revisa siempre las migraciones). Un trabajo de integración continua carga el archivo, lo evalúa sobre las rutas del repositorio y **falla** si hay una ruta sin propietario, una regla que nunca gana o un propietario que no existe. Así el archivo deja de ser documentación y se comprueba.

## Ejemplo

```text
# propietario por defecto
*                 @equipo-plataforma
# las migraciones las revisa quien mantiene los datos
migraciones/      @equipo-datos
# la regla de penalización exige una segunda mirada
src/penal.py      @coordinacion-academica
```

Un PR que toca `migraciones/0007.sql` pide revisión a `@equipo-datos`; uno que toca `README.md` cae en la regla `*`. (Sintaxis estándar de CODEOWNERS; nombres ilustrativos.)

## Errores y confusiones comunes

- **Un PR no pide revisión a quien debería**: una regla posterior cubre la ruta; corrección: lo específico después de lo general y probar rutas clave.
- **Rutas sin propietario**: falta la regla `*`.
- **Propietarios que ya no existen** o están de baja.
- **Confundirlo con un privilegio de bloqueo** en vez de una responsabilidad.

## Límites y cuándo no aplica

SE-199 declara que su modelo de coincidencia simplifica el de una plataforma real y que las rutas y equipos son del autor. Si hay un único propietario para todo, el archivo no aporta. Con muy poca gente, exigir aprobación de propietarios puede bloquear el flujo; se combina con relevos y con un indicador de cuántas personas conocen cada ruta.
