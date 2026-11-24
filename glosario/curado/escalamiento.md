# Escalamiento

## Definición

**Escalamiento** (en el sentido de *escalada*, no de escalar capacidad) es llevar un asunto al nivel siguiente de respuesta o de autoridad cuando el actual no puede o no llega a resolverlo. El programa lo usa en dos contextos:

- **En guardia** (`SE-499`): el paso de una página al siguiente nivel de respuesta cuando el anterior no contesta a tiempo.
- **En gestión** (`SE-529`, `SE-005`): llevar una decisión a quien tiene autoridad sobre ella, con el problema, las opciones y sus costos, como traslado explícito a autoridad capaz de decidir.

No debe confundirse con el escalamiento de capacidad (más recursos), que el programa trata como escalado.

## Por qué importa

Un incidente sin dueño que responda se alarga: cada minuto sin reconocimiento es daño que continúa. Y en la gestión, una decisión atascada en quien no tiene autoridad no avanza. Escalar es una acción profesional que se diseña antes de necesitarla: quién, cuándo, con qué información.

## Cómo funciona

- **Guardia** (`SE-499`): cada nivel tiene un tiempo máximo (cinco minutos es habitual para el reconocimiento) tras el cual la página pasa al siguiente: guardia primaria, secundaria, responsable. Cuenta la independencia de los niveles: con 85 % de respuesta por nivel y fallos independientes, tres niveles atienden el 99,8 % de las páginas en 15 minutos, frente al 84,8 % de un solo nivel. El cálculo es 1 − 0,15³ frente a 0,85 (tres niveles contra uno).
- **Gestión** (`SE-529`): se lleva la decisión con el problema, las opciones y sus costos, no solo una queja; quien tiene autoridad debe poder decidir sin reconstruir el contexto.

## Ejemplo

Una alerta de pago caído llega a la guardia primaria a las 03:00; no hay reconocimiento en cinco minutos y pasa a la secundaria; en otros cinco, al responsable. Ilustración del cálculo:

```python
p = 0.85
uno, tres = p, 1 - (1 - p) ** 3   # 0.85 y 0.996
```

La clase da 99,8 % para tres niveles al incluir reintentos dentro de los 15 minutos; el cálculo mínimo anterior ilustra el principio de niveles independientes.

## Errores y confusiones comunes

- **Un runbook que dice «revisa los servicios».** Causa: pasos sin comando ni salida esperada; corrección: un paso por acción, con comando y resultado esperado (`SE-499`).
- **La guardia es siempre la misma persona.** Causa: equipo pequeño o ausencias sin plan; corrección: calcular la carga y ampliar la rotación o reducir el alcance (`SE-499`).
- **Escalar sin opciones.** Trasladar un problema sin alternativas ni costos devuelve el trabajo de análisis al superior (`SE-529`).

## Límites y cuándo no aplica

Las cifras de `SE-499` suponen fallos independientes: una causa común (por ejemplo, una caída de red que afecta a todos) invalida el cálculo. El escalamiento no corrige un diseño de alertas ruidoso. Y escalar demasiado pronto o por reflejo desgasta a los niveles superiores y reduce la confianza en las páginas.
