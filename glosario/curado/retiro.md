# Retiro

## Definición

El **retiro** es la eliminación controlada de una capacidad, de sus dependencias y de sus datos (`SE-003`). Es la última etapa del ciclo de vida del software, no un apagado. `SE-017` usa el término en arquitectura de procesadores con otro sentido, el compromiso de los resultados de una instrucción al estado arquitectónico; esa acepción es distinta y no se trata aquí.

## Por qué importa

Un sistema que se apaga sin plan deja consumidores rotos, datos huérfanos, credenciales vivas y obligaciones sin cumplir. Pensar el retiro desde el diseño tiene un efecto inverso: `SE-003` señala que una dificultad de retiro revela una decisión de diseño pendiente y devuelve a la concepción el criterio de no construir y la exportabilidad.

## Cómo funciona

`SE-003` trata el ciclo de vida con bucles, no como cascada: la operación informa nuevos requisitos y el retiro reabre decisiones. El error típico es entender «retiro» como apagar infraestructura; omite consumidores y obligaciones. Un retiro completo:

- **inventaría** dependencias, datos, accesos y comunicación;
- **avisa** a quienes dependen, con alternativa y plazo (véase *obsolescencia*);
- **decide la conservación** de los datos (qué se exporta, qué se borra, qué se retiene por obligación);
- **revoca** credenciales y accesos;
- **deja evidencia de cierre**.

Cada función involucrada tiene su rol: en el cambio de proveedor de correo de `SE-003`, producto define la experiencia, ingeniería adapta el contrato, seguridad revisa secretos, soporte comunica, operaciones observa y legal decide la conservación; el retiro revoca las credenciales antiguas.

## Ejemplo

Lista de cierre para retirar un servicio de avisos:

```text
[ ] consumidores identificados y avisados (fecha de corte: 2026-06-30)
[ ] datos exportados / eliminados según política de retención
[ ] credenciales y secretos revocados
[ ] registros DNS, colas y alertas eliminados
[ ] documentación marcada como retirada, con enlace a la alternativa
```

## Errores y confusiones comunes

- **El ciclo termina en despliegue.** Causa: se definió entrega como final del producto; corrección: añadir operación, evolución, conservación y retiro con responsables (`SE-003`).
- **Retiro equivale a apagar infraestructura.** Causa: se omitieron consumidores y obligaciones; corrección: inventariar dependencias, datos, accesos, comunicación y evidencia de cierre (`SE-003`).
- **Borrar datos sin decidir la conservación.** Puede incumplir una obligación o perder información necesaria.

## Límites y cuándo no aplica

En prototipos y software desechable, el retiro se reduce a borrar. Las obligaciones de conservación dependen de la jurisdicción y del dominio; la decisión corresponde a quien tiene autoridad, no al equipo técnico solo. Y retirar no es lo mismo que migrar: la migración mantiene la capacidad en otro lugar.
