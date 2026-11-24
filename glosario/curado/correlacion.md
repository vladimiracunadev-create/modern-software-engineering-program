# Correlación

## Definición

En el programa, **correlación** es la relación explícita entre señales de una operación (`SE-033`): lo que permite unir líneas de registro, métricas y trazas que pertenecen al mismo evento. `SE-046` la matiza como el vínculo entre señales que podrían pertenecer al mismo evento. Es distinta de la correlación estadística y, sobre todo, no es causalidad.

## Por qué importa

Un sistema distribuido produce mucho registro, pero sin un identificador común nadie sabe qué líneas pertenecen a qué petición. El diagnóstico se vuelve adivinanza, y con dos ejecuciones simultáneas la ambigüedad es total (`SE-033`). Cambia la decisión de qué se registra: eventos estables con un identificador de operación, no frases libres.

## Cómo funciona

Según `SE-494`, una petición de entrega atraviesa la pasarela, la API, la cola, un trabajador y el almacenamiento, y cada uno escribe sus líneas. Para unirlas, cada servicio debe:

1. **recibir** el identificador en la petición entrante;
2. **incluirlo** en todas las líneas que escriba;
3. **copiarlo** a toda llamada saliente (cabecera HTTP o propiedad del mensaje en la cola).

El estándar `traceparent` de W3C Trace Context fija un formato para esto y las bibliotecas de trazado lo hacen solas en HTTP; en una cola o un grupo de hilos hay que hacerlo explícitamente, y es donde se rompe. Cuando falta el identificador, `SE-046` recuerda la trampa contraria: agrupar señales por coincidencia temporal y atribuirles causa.

## Ejemplo

Dos entregas simultáneas escriben «guardado» y «error de red». Sin identificador, no se sabe qué error corresponde a qué entrega. Con él:

```json
{"evento": "guardado", "operacion": "a1b2", "t": "12:00:01"}
{"evento": "error_red", "operacion": "c3d4", "t": "12:00:01"}
```

## Errores y confusiones comunes

- **Mucho registro sin relacionar eventos.** Causa: faltan identificadores y estructura; corrección: eventos estables y correlación por operación (`SE-033`).
- **Atribuir causa por coincidencia temporal.** Causa: la correlación no es causalidad; corrección: plantear una hipótesis con predicción y una intervención (`SE-046`).
- **Perder el identificador en el salto asíncrono.** Cola o pool de hilos que no lo propagan (`SE-494`).

## Límites y cuándo no aplica

La correlación aproxima relaciones; no demuestra causalidad por sí sola (`SE-033`). Un identificador único une señales de una operación, pero no explica por qué falló. En sistemas sin red ni concurrencia, un registro secuencial basta. Y el estándar `traceparent` resuelve el formato, no la disciplina de propagarlo en cada salto.
