# Retroceso

## Definición

El **retroceso** (*rollback*) es el conjunto de acciones que devuelve el sistema al estado anterior a un paso (`SE-211`). Según la clase, es la vuelta a la versión anterior tras detectar un defecto (`SE-225`, `SE-476`), a una versión anterior ya validada (`SE-607`) o la operación que restituye el sistema al estado previo a la inyección de una falla y cuyo tiempo se mide (`SE-506`). Tiene un sentido distinto en algoritmos (*backtracking*, retroceder ante un conflicto, como hace el resolvedor de `SE-111`); esta entrada trata el retroceso operativo.

## Por qué importa

Un cambio solo es seguro si se puede deshacer rápido. Cuánto tarda el retroceso acota el daño de un despliegue o de un experimento. Cambia lo que se exige antes de cambiar algo en producción: un camino de vuelta probado.

## Cómo funciona

`SE-506` (ingeniería del caos) lo trata con precisión: abortar un experimento significa que algo deja de inyectar; si la falla es una regla de red, un proceso detenido o una configuración modificada, el retroceso es una operación que **puede fallar**: la regla no se elimina, el proceso no reinicia, la configuración vieja ya no existe. Por eso el retroceso:

- se **prueba antes**;
- se ejecuta con **un solo comando**;
- **no depende** del componente que se está dañando;
- se **mide**: cuánto tarda en volver el indicador a su banda.

En despliegues (`SE-476`), el *blue-green* mantiene dos entornos completos y el retroceso es redirigir el tráfico; pero el cambio expone a todas las personas a la vez y el costo es doble infraestructura. Otras estrategias (canario, bandera) trazan otros compromisos. En ML (`SE-607`), retroceder es volver a un modelo ya validado.

## Ejemplo

`SE-506`, como caso hipotético: la especificación del experimento «almacenamiento con 20 % de errores» define un radio de 2 % del tráfico durante 10 minutos, aborto si el grupo experimental falla más de 50 % en 10 s o si el servicio global baja de 99,5 % en 30 s, y reversión «quitar la regla del proxy», probada la víspera con un tiempo de 4 s.

```bash
./quitar_toxico.sh && ./verificar_indicador.sh --espera 10
```

## Errores y confusiones comunes

- **La falla no se detiene al abortar.** Causa: reversión no probada o dependiente del componente dañado; corrección: probar la reversión antes y ejecutarla desde fuera (`SE-506`).
- **Suponer que siempre se puede retroceder.** Un cambio de esquema que borra columnas o una migración de datos pueden no ser reversibles.
- **Confundir retroceso con retiro.** El retroceso vuelve a un estado anterior; el retiro elimina una capacidad.

## Límites y cuándo no aplica

El retroceso solo restituye lo que el cambio tocó: los efectos externos (mensajes enviados, cobros) no se deshacen. Los datos escritos por la versión nueva pueden ser ilegibles para la anterior; por eso se prefieren cambios compatibles hacia atrás. Y un retroceso que nunca se ensayó es una esperanza.
