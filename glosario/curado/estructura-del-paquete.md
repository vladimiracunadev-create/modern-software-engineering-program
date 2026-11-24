# Estructura del paquete

## Definición

La **estructura del paquete** es la forma declarada de un paquete de trabajo: qué tipos de artefacto contiene, cómo se identifican y qué enlaces entre ellos son válidos. En `SE-168` (paquete de especificaciones trazables) se compone de cinco tipos de artefacto (intención, requisito, contrato, ejemplo y prueba) con identificadores estables (`INT-1`, `REQ-4`, `CON-4`, `EJE-7`, `TST-3`). `SE-468` y `SE-456` aplican la misma idea a un paquete de seguridad verificable y a uno de aseguramiento de un controlador.

## Por qué importa

Cambia si el paquete se puede comprobar con una máquina y recorrer sin ayuda. Un paquete con tipos de artefacto y de enlace definidos permite comprobaciones mecánicas (`SE-168`); sin campos obligatorios, faltan eslabones (`SE-468`); con estructura clara, otra persona lo recorre sin que su autor esté presente (`SE-456`).

## Cómo funciona

Los enlaces apuntan hacia el origen: un requisito enlaza a una intención, un contrato a un requisito, un ejemplo y una prueba a un contrato, y una prueba también a un ejemplo. Los **tipos de enlace permitidos están declarados**, de modo que un enlace no previsto (por ejemplo, una prueba directamente a una intención) se rechaza. Los identificadores son **estables**: no dependen del título, así que renombrar un artefacto no rompe enlaces.

Con esa estructura, un validador puede comprobar presencia, enlaces colgantes y cobertura en ambos sentidos (cada cláusula del contrato tiene ejemplo, cada ejemplo respalda una cláusula), y puede correrse en integración continua. En el paquete de seguridad de `SE-468`, cada requisito añade estado (cumple, no aplica, excepción), control, prueba, evidencia, fecha, alcance y dueño: «no aplica» exige justificación y una excepción exige dueño y fecha de vencimiento. La evidencia es el resultado ejecutable de una prueba, no una captura.

## Ejemplo

En la plataforma de entregas de `SE-168`, el requisito `REQ-4` enlaza a `INT-1`; el contrato `CON-4` enlaza a `REQ-4`; el ejemplo `EJE-7` y la prueba `TST-3` enlazan a `CON-4`, y la prueba también a `EJE-7`. Si alguien renombra el título del requisito, el identificador no cambia y ningún enlace se rompe; si añade una prueba sin contrato, el validador la señala.

## Errores y confusiones comunes

- **Un revisor no sabe qué ejemplo respalda una cláusula.** Faltan enlaces entre contrato y ejemplo; exigir cobertura en ambos sentidos y comprobarla en integración continua.
- **Al renombrar se rompen enlaces.** Los identificadores dependen del título; usar identificadores estables y comprobar enlaces colgantes.
- **Confundir estructura con calidad.** Un paquete bien enlazado puede tener requisitos malos.
- **Evidencia como captura de pantalla.** Debe ser el resultado ejecutable de una prueba.

## Límites y cuándo no aplica

La estructura garantiza que los enlaces existen, no que sean ciertos: un validador que solo comprueba forma deja pasar un enlace erróneo. Los experimentos de `SE-168` usan datos sintéticos, y el alcance de sus mutaciones es el de la clase. Para un cambio pequeño, un paquete de cinco tipos puede ser más costo que beneficio.
