# Degradación

## Definición

**Degradación** (en el sentido del programa, *degradación controlada*) es el paso deliberado a un nivel con menos capacidad y más previsibilidad (`SE-599`) cuando algo falta o falla. `SE-030` la usa en su versión mínima: un resultado parcial explícito cuando una capacidad opcional no está disponible. No es «el sistema empeora con el tiempo» ni un fallo: es una respuesta diseñada.

## Por qué importa

Convierte la pregunta binaria «¿funciona?» en «¿qué parte del valor se conserva?» (`SE-321`). Un sistema que solo conoce «todo o nada» cae entero cuando cae una dependencia secundaria. La decisión profesional que cambia es qué funciones son esenciales y cuáles pueden entregarse parciales, antiguas o ausentes, y quién lo decide: `SE-321` subraya que son decisiones de producto, no solo técnicas.

## Cómo funciona

Cuando una dependencia no responde, el sistema devuelve una respuesta **parcial o antigua** en lugar de fallar (`SE-321`). Requiere tres condiciones:

1. detectar el fallo rápido (límites de tiempo, rechazo cuando un grupo se llena);
2. tener un respaldo (caché, datos del día anterior, funcionalidad reducida);
3. **declarar** el estado degradado, para que el consumidor no confunda «desconocido» con «cero» (`SE-030`).

En `SE-321`, el aislamiento por dependencia (mamparas) evita que la lentitud de una agote los recursos de las demás, y el rechazo rápido evita acumular peticiones. En `SE-599`, la degradación aparece como nivel previsible hacia el que un sistema con LLM retrocede cuando falla un componente.

## Ejemplo

Experimento de `SE-321`: 2000 peticiones con una dependencia caída el 40 % del tiempo. Sin degradación, el 60,0 % de las respuestas son útiles; con una caché de 70 % de aciertos como respaldo, el 87,5 %. Corrección aplicada: separar el grupo de recursos por dependencia, limitarlo, rechazar rápido, servir reportes con datos del día anterior y escribir la prueba que simula la lentitud.

## Errores y confusiones comunes

- **Servir datos antiguos sin avisarlo.** El usuario toma decisiones con información obsoleta; la degradación debe ser visible.
- **Degradar sin haber probado el camino degradado.** Solo se descubre que no funciona durante el incidente; `SE-321` exige simular la lentitud en una prueba.
- **Confundir degradación con reintento.** El reintento insiste; la degradación cambia de nivel de servicio.
- **Tratar «desconocido» como cero** (`SE-030`).

## Límites y cuándo no aplica

Las cifras de `SE-321` son de una simulación con parámetros del autor, no una predicción. No toda función admite versión parcial: una transferencia de dinero a medias es peor que un error. Y un respaldo caduco puede ser inaceptable cuando la frescura es el requisito.
