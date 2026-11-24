# Inferencia

## Definición

Una **inferencia** es una conclusión derivada de observaciones y supuestos (`SE-006`). `SE-033` la usa como explicación compatible con los hechos pero aún contrastable; `SE-050` como la derivación de una conclusión desde premisas. En los tres usos, la inferencia es un paso que *va más allá* de lo observado, y por eso puede equivocarse aunque la observación sea correcta.

## Por qué importa

Gran parte de los errores de diagnóstico no vienen de medir mal sino de saltar de lo medido a la causa sin decirlo. `SE-006` pide separar cuatro cosas que suelen presentarse mezcladas: observación, inferencia, hipótesis y supuesto. Esa separación cambia lo que se firma: se afirma el dato, y se argumenta la conclusión.

## Cómo funciona

`SE-006` define cada pieza:

- **Observación:** registra qué ocurrió con un método: «el p95 fue 480 ms en estas solicitudes, intervalo y entorno».
- **Inferencia:** conecta observaciones con una conclusión: «la dependencia contribuyó a la demora».
- **Hipótesis:** una explicación contrastable: «si la dependencia es la causa dominante, aislarla reducirá la cola».
- **Supuesto:** una condición aceptada provisionalmente, como considerar representativa la carga de prueba.

En lógica (`SE-050`), una inferencia es válida si la conclusión se sigue de las premisas; un `para todo` exige cubrir el dominio declarado y un `existe` se demuestra con un testigo. En registro y diagnóstico (`SE-033`), una inferencia es una explicación que se somete a una prueba que podría refutarla. La causa del error típico es que la inferencia hereda los supuestos de las observaciones: si la carga de prueba no era representativa, la conclusión tampoco lo es.

## Ejemplo

Observación: «tras desplegar, el p95 pasó de 300 a 480 ms». Inferencia: «el despliegue causó la demora». Alternativa rival: «coincidió con el pico de matrícula». Contraste: revertir el despliegue en un entorno equivalente y comprobar si el p95 baja. Ilustración:

```text
obs: p95 480ms (n=2000, entorno X) -> inf: dependencia D contribuye -> prueba: aislar D, esperar p95 < 350ms
```

## Errores y confusiones comunes

- **Una métrica se presenta como conclusión.** Causa: se omitieron inferencia y supuestos; corrección: separar registro, interpretación y alternativa rival (`SE-006`).
- **Tomar la inferencia por hecho.** Un hecho se verifica observando; una inferencia se contrasta.
- **Confundir correlación con causa** (`SE-033`).

## Límites y cuándo no aplica

Una inferencia correcta formalmente puede ser falsa si las premisas lo son. En dominios infinitos, la verificación por enumeración no alcanza (`SE-050`). Y la separación observación/inferencia es una disciplina de comunicación del programa: no elimina la incertidumbre, solo la hace visible.
