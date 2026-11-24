# Servicio

## Definición

**Servicio** tiene dos sentidos en el programa:

- **Componente de arquitectura** (`SE-327`): un componente que se despliega y escala de forma independiente y se comunica por red.
- **Proceso de larga duración** (`SE-028`, `SE-222`): un proceso gestionado por un supervisor y una política de ciclo de vida, que atiende peticiones o ejecuta trabajo sin un usuario interactivo (en Unix, *daemon*).

Comparten la idea de algo que está disponible para otros, pero operan en niveles distintos.

## Por qué importa

Elegir servicios como unidad de despliegue cambia qué se gana y qué se paga. `SE-327` lo pone en la misma tabla: se gana autonomía (un equipo publica sin coordinar, un componente pesado se escala sin escalar el resto) y se paga operación, latencia de red, fallos parciales y consistencia. Y para el proceso de larga duración, entender el ciclo de vida evita reinicios en bucle y despliegues que fallan.

## Cómo funciona

**Arquitectura** (`SE-327`): al separar servicios, una transacción que los cruza deja de ser atómica y se convierte en una saga con compensaciones. Fowler y Lewis describen esos costos junto a las ventajas. Para muchos sistemas el destino correcto es un monolito bien organizado: da orden y pruebas rápidas sin el costo de operar muchos servicios.

**Proceso** (`SE-028`, `SE-222`): un supervisor lo arranca, lo vigila y lo reinicia según una política. Una recuperación sana clasifica el fallo, aplica espera creciente y corta el bucle; si no, un servicio que cae al arrancar se reinicia sin límite. Tras un despliegue, el tráfico solo debe llegar cuando una sonda de preparación comprueba lo mismo que hará el cliente. En parada, el cierre ordenado (vaciar, escribir en archivo temporal y renombrar) evita archivos truncados.

## Ejemplo

```text
saga "matricular":  reservar_cupo -> cobrar -> emitir_constancia
si cobrar falla:    compensar -> liberar_cupo     (no hay transacción atómica entre servicios)
```

## Errores y confusiones comunes

- **Quedan datos a medias entre servicios.** Causa: transacción entre servicios sin compensación; corrección: diseñar y probar compensaciones o evitar la operación cruzada (`SE-327`).
- **El servicio reinicia sin límite.** Causa: se sustituyó recuperación por repetición; corrección: clasificar fallo, aplicar espera creciente y cortar el bucle (`SE-028`).
- **Fallan peticiones tras cada despliegue.** Causa: tráfico antes de que el servicio esté preparado; corrección: sonda de preparación que prueba lo mismo que el cliente (`SE-222`).

## Límites y cuándo no aplica

Separar en servicios no es mejor en sí: para equipos pequeños o dominios poco definidos suele costar más de lo que da (`SE-327`). Y el sentido de arquitectura no implica el de proceso: un servicio de arquitectura puede ejecutarse en muchos procesos y un *daemon* no es necesariamente un servicio independiente de negocio.
