# Reproducción

## Definición

**Reproducción** es una palabra con dos familias de sentidos que no deben mezclarse:

- **Volver a producir un resultado o un síntoma** (`SE-289`, `SE-058`, `SE-023`, `SE-035`): que otra persona, con el mismo código y los mismos datos, obtenga un resultado equivalente dentro de una tolerancia declarada (`SE-289`); o el procedimiento que vuelve a mostrar el comportamiento bajo condiciones declaradas (`SE-035`, `SE-058`).
- **Ataque de reproducción** (*replay*, `SE-272`): el reenvío de un mensaje legítimo capturado para que el receptor lo acepte de nuevo.

## Por qué importa

En el primer sentido, sin reproducción no hay diagnóstico ni ciencia: un fallo que no se puede provocar no se puede arreglar con confianza ni comprobar. En el segundo, un mensaje válido y firmado sigue siendo válido cuando lo reenvía un atacante, así que la firma no basta.

## Cómo funciona

**Reproducir un resultado o un fallo:** se declaran las condiciones (versiones, entrada fija, estado inicial), un comando documentado y una verificación de invariantes antes de comparar (`SE-023`). `SE-289` distingue promesas hermanas: la **repetición** falla por estado oculto (una variable de entorno, un archivo sin versionar), la **reproducción** por diferencias numéricas o de dependencias y la **replicación** porque el efecto no existía o dependía de la muestra.

**Ataque de reproducción** (`SE-272`): dos mecanismos lo evitan. Una **ventana de tiempo** acepta mensajes con marca reciente: exige relojes razonablemente sincronizados y deja una ventana en que la reproducción es posible. Un **contador monótono** exige que cada mensaje tenga un número mayor que el anterior: no depende del reloj, pero necesita memoria persistente; si el contador se reinicia con el dispositivo, un mensaje capturado vuelve a ser válido. La elección se documenta con el desfase que tolera y la memoria que exige.

## Ejemplo

```python
def aceptar(msg, ultimo_contador):
    return msg.contador > ultimo_contador and verifica_firma(msg)   # reenviar el mismo mensaje falla
```

En el modelo de `SE-272`, un contador que se reinicia sin memoria persistente acepta una reproducción en el 50,8 % de los casos.

## Errores y confusiones comunes

- **Un mensaje capturado se acepta días después.** Causa: sin anti-reproducción o contador reiniciado; corrección: contador persistente y ventana acotada (`SE-272`).
- **Confundir repetición, reproducción y replicación** (`SE-289`).
- **«Se reproduce en mi máquina» sin condiciones declaradas.** No es una reproducción verificable.

## Límites y cuándo no aplica

Las cifras de `SE-272` son de un modelo con parámetros del autor. Una reproducción exacta puede ser imposible en sistemas no deterministas; entonces se declara la tolerancia. Y la ventana de tiempo requiere relojes sincronizados: con relojes desviados, rechaza mensajes legítimos.
