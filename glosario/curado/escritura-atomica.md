# Escritura atómica

## Definición

La **escritura atómica** es un guardado que deja **siempre el estado anterior o el nuevo completos, nunca uno parcial**. El programa la define desde varios ángulos que coinciden: en `SE-256` es el guardado que deja uno de los dos estados completos; en `SE-224`, la publicación de un archivo de modo que un lector ve el contenido anterior o el nuevo completo, nunca una mezcla; en `SE-067`, un reemplazo observado como cambio indivisible **bajo supuestos del sistema**. Se logra con un patrón: escribir un archivo temporal, forzar su sincronización y reemplazar el original de una vez.

## Por qué importa

Escribir directamente sobre el archivo y ser interrumpido (un corte de energía, un cierre forzado, un proceso terminado) deja un archivo a medias, y el estado queda corrupto «justo cuando más hace falta» (`SE-254`): la aplicación se suspende y el guardado no termina. La decisión que cambia es cómo se persiste lo que importa: no se sobrescribe in situ; se prepara el estado nuevo aparte y se intercambia. Además, en automatizaciones, oculta el trabajo a medias a los lectores (`SE-224`): quien lee ve lo anterior hasta que lo nuevo está completo.

## Cómo funciona

El patrón tiene cuatro pasos y cada uno cubre un modo de fallo:

1. **Escribir en un archivo temporal** en el mismo directorio (y por tanto en el mismo sistema de archivos). El original no se toca.
2. **Sincronizar** el temporal (`flush` y `fsync` o equivalente), para que el contenido haya llegado al medio de almacenamiento y no quede solo en memoria del sistema.
3. **Reemplazar** el original con el temporal mediante una operación de renombrado que el sistema ofrece como indivisible (`os.replace` en Python). Mientras no ocurre, el estado anterior sigue válido.
4. **Opcionalmente sincronizar el directorio**, para fijar el cambio de nombre.

Si el proceso muere antes del paso 3, queda un temporal huérfano y el original intacto; si muere después, queda el nuevo. No existe un instante en que un lector encuentre un archivo mezclado. El reemplazo es atómico **bajo supuestos del sistema** (`SE-067`): mismo volumen, sistema de archivos que lo garantice. El costo crece con el tamaño del estado, y ese costo decide qué cabe en un gancho de pausa y qué debe guardarse antes.

## Ejemplo

La herramienta `notas` de `SE-224` publica de forma nocturna con claves por fila, escritura atómica y reanudación verificada. `SE-225` aplica la misma técnica a una actualización de binarios: descargar a un temporal, verificar y reemplazar. Esquema mínimo (ilustración):

```python
import os, tempfile

def guardar_atomico(ruta, datos):
    dirn = os.path.dirname(ruta) or "."
    with tempfile.NamedTemporaryFile("w", dir=dirn, delete=False) as f:
        f.write(datos)
        f.flush()
        os.fsync(f.fileno())
    os.replace(f.name, ruta)      # indivisible bajo los supuestos del sistema
```

Cambiar el tamaño del lote de 20 a 200 filas, como hace la clase, se prueba con una matriz de caídas que confirma que los resultados siguen igual.

## Errores y confusiones comunes

- **Sobrescribir in situ.** Una interrupción deja el archivo parcial.
- **Temporal en otro volumen.** El renombrado deja de ser atómico y se convierte en copia.
- **Omitir la sincronización.** El renombrado puede persistir antes que el contenido y, tras un corte, quedar un archivo vacío.
- **Guardar solo en un evento de cierre.** El borrador vuelve vacío si ese evento no se entregó; se guarda al pasar a segundo plano y de forma periódica (`SE-254`).
- **Estado de una versión que la siguiente rechaza.** Se resuelve con versión en el archivo y migraciones.

## Límites y cuándo no aplica

Garantiza que el archivo no queda a medias, no que el contenido sea correcto ni que dos escritores concurrentes no se pisen; para eso se necesitan bloqueos o una base de datos con transacciones. Las medidas de `SE-254` fueron con datos sintéticos en Windows y Ubuntu (WSL2): no se midió ningún dispositivo móvil ni el plazo real de ningún gancho. En archivos enormes, copiar todo el estado en cada guardado puede ser prohibitivo y conviene un registro de cambios.
