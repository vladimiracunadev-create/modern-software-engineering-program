# Gate

## Definición

Un **gate** (compuerta) es un punto de la integración continua que bloquea o avisa según un umbral (`SE-432`).

## Por qué importa

Una estrategia de pruebas escrita en un documento que nadie ejecuta no protege nada. El gate es el lugar donde la estrategia se vuelve una decisión automática: si un umbral se supera, el cambio no avanza (bloquea) o alguien se entera (avisa).

## Cómo funciona

`SE-432` propone un paquete estructurado (JSON) con las decisiones: por componente, probabilidad e impacto estimados, clase de fallo, nivel de prueba que la ve, horas asignadas y pruebas; una lista de gates con su umbral y su acción (bloquear o avisar); una lista de exclusiones con razón y caducidad; y los límites. La estructura obliga a que cada riesgo tenga pruebas, cada prueba un riesgo y cada exclusión una fecha, y permite que un programa lo valide en cada cambio.

## Ejemplo

`SE-432`: el equipo versiona `estrategia.json`. El paquete lista nueve componentes probados, tres exclusiones con caducidad a 75 días y dos gates: el **rápido** (diez minutos, bloquea con unitarias, de contrato y de integración por interfaz) y el **nocturno** (90 minutos, avisa con extremo a extremo y carga ligera).

## Errores y confusiones comunes

- **La estrategia es un documento que nadie ejecuta.** No hay validador ni vínculo con la integración continua; paquete estructurado y validado en cada cambio.
- **Un riesgo alto queda sin horas o sin nivel que lo vea.** Faltan reglas de coherencia en el validador.

## Límites y cuándo no aplica

Un gate lento o inestable se esquiva; por eso conviene separar uno rápido que bloquea de otro lento que avisa. Un umbral mal puesto da falsas alarmas o falsa tranquilidad.
