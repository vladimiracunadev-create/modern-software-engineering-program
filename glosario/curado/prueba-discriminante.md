# Prueba discriminante

## Definición

Una **prueba discriminante** es un experimento (`SE-047`) u observación (`SE-035`) cuyo resultado separa hipótesis: da un resultado distinto según cuál sea cierta. No es cualquier prueba: una que pasa igual con las dos explicaciones no discrimina nada.

## Por qué importa

En diagnóstico, es común acumular datos compatibles con todas las hipótesis y sentir que se avanza. La prueba discriminante es la que realmente reduce el espacio: tras ella, al menos una hipótesis sale. Cambia cómo se decide el siguiente paso: no «qué puedo medir», sino «qué medición separa mis dos mejores explicaciones».

## Cómo funciona

`SE-047` presenta el método: después de la traza normal, se introduce un **único** fallo. La prueba debe producir un cambio **predicho**: un *override* de DNS, un puerto cerrado o una caché controlada. Si cambian varias señales, se vuelve a reducir antes de concluir. La estructura lógica es la de `SE-050`: «si H entonces O»; observar no-O refuta H (*modus tollens*), mientras observar O no prueba H (afirmar el consecuente es una falacia).

Los pasos prácticos:

1. Escribir dos o más hipótesis rivales.
2. Elegir un cambio mínimo (una sola variable).
3. **Predecir** el resultado bajo cada hipótesis, antes de ejecutar.
4. Ejecutar y comparar.

La causa de su valor es que fuerza a que la hipótesis pueda fallar; una explicación que no predice nada observable no se puede discriminar.

## Ejemplo

Síntoma: «la página no carga». Hipótesis A: falla la resolución DNS. Hipótesis B: falla la conexión al puerto. Prueba discriminante: conectar directamente a la IP (saltando DNS). Si carga, A se sostiene y B se descarta; si no carga, B sigue en pie. Ilustración:

```bash
curl --resolve ejemplo.com:443:203.0.113.10 https://ejemplo.com/    # fija la IP y salta DNS
```

## Errores y confusiones comunes

- **Informe con una lista de errores sin ordenar.** Causa: no se identificó la primera divergencia; corrección: comparar con el caso sano y señalar la primera fase que difiere (`SE-047`).
- **Eventos de componentes que no se pueden unir.** Causa: falta un identificador propagado; corrección: generarlo en el borde, propagarlo y registrarlo en cada capa (`SE-047`).
- **Cambiar varias cosas a la vez.** Si cambian varias señales, no se sabe cuál separó las hipótesis.

## Límites y cuándo no aplica

El taller de `SE-047` no garantiza visibilidad dentro de redes de terceros, y no deben recolectarse tokens ni cuerpos personales. Una prueba discriminante supone que las hipótesis son exhaustivas: si la causa real no estaba entre ellas, la prueba puede «confirmar» la menos mala. Y en sistemas con fallos intermitentes, una sola ejecución no discrimina: hay que repetir.
