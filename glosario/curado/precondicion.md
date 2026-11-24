# Precondición

## Definición

Una **precondición** es la condición que debe cumplirse al invocar una operación; su incumplimiento es un defecto del cliente (`SE-159`). `SE-052` la define como la propiedad requerida al iniciar una operación; `SE-547` como lo que debe cumplirse al llamar a una rutina, responsabilidad de quien llama; `SE-242` aplica la idea a HTTP: una condición sobre el estado del recurso que debe cumplirse para que una solicitud se aplique.

## Por qué importa

Reparte la culpa: si la precondición falla, el defecto es del cliente y el proveedor no tiene por qué comportarse bien (`SE-159`). Esa precisión evita código defensivo repetido en cada capa y obliga a decidir quién valida la entrada. Cambia cómo se diseña la interfaz: qué se rechaza, dónde y con qué error.

## Cómo funciona

Una precondición dice qué debe ser cierto al llamar: `calificar` exige que la calificación no esté publicada; `dar_prórroga` exige horas positivas (`SE-159`). Debe poder decidirse antes de ejecutar: `destino autorizado` o `presupuesto > costo_estimado` son comprobables; una «esperanza escondida» no (`SE-052`). Si el consumidor puede violarla, la interfaz valida y produce un error observable.

La calibración importa: una precondición demasiado débil traslada al proveedor casos que debería rechazar; una demasiado fuerte hace inutilizable la operación. En herencia, la regla de sustitución dice que una subclase debe aceptar al menos lo mismo (no reforzar la precondición) y garantizar al menos lo mismo (no debilitar la poscondición). En HTTP (`SE-242`), las solicitudes condicionales (por ejemplo con `If-Match` y una etiqueta de versión) permiten que el servidor aplique el cambio solo si el recurso sigue en el estado que el cliente vio.

## Ejemplo

```python
def dar_prorroga(entrega, horas):
    assert horas > 0                 # precondición: responsabilidad de quien llama
    entrega.limite += timedelta(hours=horas)
```

```text
PUT /entregas/12   If-Match: "v7"    -> 412 Precondition Failed si el recurso ya está en "v8"
```

## Errores y confusiones comunes

- **Una subclase rompe a los clientes de la base pese a compilar.** Causa: reforzó una precondición o debilitó una poscondición; corrección: aceptar al menos lo mismo y garantizar al menos lo mismo (`SE-159`).
- **Validar la misma precondición en tres capas.** Causa: no se acordó quién valida; corrección: un responsable, el resto como afirmaciones internas (`SE-159`).
- **Función que falla sin decir quién se equivocó.** Causa: contrato implícito (`SE-052`).

## Límites y cuándo no aplica

No se aplica a entradas de fuera del sistema: la validación de formularios y mensajes debe responder con un error amable; la precondición expresa lo que un componente interno da por hecho (`SE-159`). Y una precondición solo es un contrato si está escrita y se comprueba en algún momento; si no, es una creencia.
