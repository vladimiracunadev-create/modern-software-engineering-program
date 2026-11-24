# Reintentos

## Definición

Los **reintentos** consisten en repetir una llamada fallida con la esperanza de que una falla transitoria no se repita. El programa lo trata en varios contextos: en pruebas (`SE-430`, flakiness), en códigos de salida y errores (`SE-220`) y en ejecución durable (`SE-596`). La palabra no implica por sí sola ninguna política: cuántas veces, con qué espera y para qué errores son las decisiones que importan.

## Por qué importa

Es la primera defensa contra fallos transitorios, y también una fuente de problemas: reintentar lo permanente gasta recursos y retrasa el aviso (`SE-220`); reintentar sin retroceso aleatorio daña al servicio (`SE-596`); y reintentar una prueba silencia el defecto real intermitente (`SE-430`).

## Cómo funciona

`SE-430` da los números del costo en pruebas. Para una prueba con 2 % de fallo espurio, un reintento la deja en verde el 99,96 % de las veces: el ruido desaparece. Pero un defecto real que ocurre en el 30 % de las ejecuciones también termina en verde el 91,2 % de las veces con un reintento y el 97,3 % con dos. El reintento no distingue entre los dos. Si se reintenta, se registra cada reintento y se revisa la tasa.

Para llamadas a servicios, la política mínima es:

1. **Reintentar solo errores transitorios** (tiempo agotado, servicio no disponible), no los permanentes (petición inválida, no autorizado).
2. **Limitar intentos** y tiempo total.
3. **Espera creciente con dispersión** (retroceso exponencial con jitter), para no sincronizar a los clientes.
4. **Idempotencia** de lo que se repite, porque un reintento puede duplicar un efecto.

## Ejemplo

El equipo de `SE-430` guarda el historial de cada prueba y calcula cada semana la tasa de fallo espurio por prueba y suite. Una prueba con más de 0,1 % de fallo espurio entra en cuarentena: sigue ejecutándose pero no bloquea, con responsable, fecha de revisión a 14 días y criterio de salida de 300 ejecuciones sin fallo tras la corrección. Los reintentos están desactivados para no esconder defectos reales.

## Errores y confusiones comunes

- **Reintentar errores permanentes.**
- **Reintentar sin dispersión,** provocando oleadas sincronizadas.
- **Reintentar operaciones no idempotentes** (cobros, envíos).
- **Usar el reintento de pruebas como solución a la inestabilidad,** en lugar de diagnosticarla.

## Límites y cuándo no aplica

No ayuda cuando la dependencia está caída por un periodo largo: ahí actúa el circuit breaker. Multiplica la carga sobre un servicio ya saturado. Los porcentajes de `SE-430` suponen intentos independientes; si la causa es persistente, el reintento no ayuda.
