# Trazas comparables

## Definición

Las **trazas comparables** son, en el taller de `SE-083`, registros del razonamiento de un programa que tienen **la misma forma en todas las implementaciones** y por eso pueden contrastarse: se registra la **entrada normalizada, las reglas consideradas, la decisión, el error y los efectos**. Una traza responde a «¿cómo llegó el programa a este resultado?»; que sea *comparable* significa que las cinco versiones de la regla (en cinco paradigmas) la producen con el mismo esquema, aunque la calculen de maneras distintas.

## Por qué importa

Dos implementaciones pueden devolver el mismo resultado final por razones distintas, o coincidir **por accidente**. Si solo se compara la salida, esas coincidencias parecen equivalencias. `SE-083` lo dice: **comparar solo el resultado final oculta por qué dos programas coinciden por accidente**. La decisión que cambia es qué se compara: el resultado y el camino. Con trazas comparables, una divergencia aparece en la regla exacta donde las implementaciones empiezan a diferir, en lugar de solo en el resultado, donde puede ya ser tarde para entenderla.

## Cómo funciona

El diseño de una traza útil tiene condiciones:

- **Contenido definido:** la **entrada normalizada** (cómo se interpretó), las **reglas consideradas** (cuáles se evaluaron y con qué resultado), la **decisión**, el **error** si lo hubo y los **efectos** (qué se escribió, qué se envió).
- **Estable:** el mismo caso produce la misma traza; sin marcas de tiempo variables, identificadores aleatorios ni orden no determinista.
- **Sin detalles internos irrelevantes:** no debe revelar cómo está implementado cada paradigma (nombres de clases, estructuras internas), porque eso impediría compararlas y acoplaría la prueba a la implementación.

Las trazas dan valor en dos usos. En la **comparación**, se ejecutan los mismos casos del fixture en cada versión y se comparan las trazas campo a campo. En el **diagnóstico**, una traza permite disputar una decisión incorrecta: qué reglas se consideraron y por qué ganó una. Esto conecta con el requisito del motor de reglas del programa: quién puede producir una decisión, qué estado observa, cómo falla y qué rastro permite disputarla.

## Ejemplo

Una traza con la misma forma en todas las versiones (ilustración):

```json
{
  "entrada": {"id": "c-17", "monto": 1500, "autorizado": true},
  "reglas": [
    {"regla": "autorizacion", "resultado": "ok"},
    {"regla": "umbral_monto", "resultado": "supera"}
  ],
  "decision": "revisar",
  "error": null,
  "efectos": []
}
```

Si la versión de objetos produce `"reglas"` en otro orden o la versión funcional omite `umbral_monto` porque la evalúa de forma perezosa, la comparación lo muestra, aunque ambas lleguen a `"revisar"`. Dos fallos documentados en la clase se descubren con este instrumento: las pruebas pasan pero un defecto plantado sobrevive (falta el caso que ejercita esa regla), y dos versiones divergen solo con ciertos tipos (el contrato no definía los inválidos).

## Errores y confusiones comunes

- **Comparar solo el resultado final.** Oculta coincidencias accidentales.
- **Trazas inestables.** Marcas de tiempo o identificadores aleatorios hacen imposible compararlas.
- **Trazas que filtran la implementación.** Acoplan la comparación a detalles internos.
- **Omitir los efectos.** Dos versiones pueden decidir igual y actuar distinto.

## Límites y cuándo no aplica

El taller compara un cambio y una carga pequeña; no demuestra mantenibilidad a largo plazo (`SE-083`). Registrar trazas tiene costo (tiempo, espacio y posible exposición de datos); en producción deben revisarse por privacidad. Para reglas triviales de un solo paso, la traza es redundante con la decisión. Y las trazas muestran qué pasó, no si la regla era la correcta: eso lo da el fixture con resultados esperados.
