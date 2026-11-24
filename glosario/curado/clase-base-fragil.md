# Clase base frágil

## Definición

La **clase base frágil** es la situación en que un cambio interno de la clase base, sin cambiar su interfaz, rompe a sus subclases (`SE-303`). El defecto no está en la base ni en la subclase por separado: está en que la subclase depende de un detalle de implementación que la base nunca prometió.

## Por qué importa

La herencia parece gratis: se reutiliza código y se redefine solo lo distinto. Pero quien hereda asume el compromiso de seguir a la base durante toda su vida. La decisión que cambia este concepto es cuándo heredar y cuándo componer: si la base puede evolucionar sin avisar, cada subclase es un cliente que conoce demasiado de ella, una forma de acoplamiento a la implementación y no solo a la interfaz.

## Cómo funciona

`SE-303` lo muestra con un caso clásico. Una colección implementa `agregar_todos` llamando internamente a su propio `agregar`. Una subclase que cuenta los elementos sobrescribe `agregar` y también `agregar_todos`, y suma en ambos. Con esa base, cada elemento se cuenta dos veces: una en `agregar_todos` y otra cuando este llama a `agregar`. Si la base cambia a un `extend` interno que ya no pasa por `agregar`, la subclase pasa a contar bien. Ninguna de las dos versiones de la base viola su documentación; la subclase simplemente dependía de **cómo** la base se llama a sí misma.

La causa es que al sobrescribir, el método de la subclase se convierte en parte del flujo interno de la base: la llamada `self.agregar` despacha a la versión de la subclase. La interfaz pública no dice qué métodos se invocan entre sí, así que ese orden es un detalle invisible que sostiene el comportamiento de las subclases. La salida que enseña `SE-303` es **componer y reenviar solo lo prometido**: mantener la base como atributo y delegar únicamente en su interfaz documentada.

## Ejemplo

Una clase `ContadorLista` hereda de la colección y cuenta en `agregar` y en `agregar_todos`. Con la base original suma el doble; tras el cambio interno de la base suma lo correcto, sin que nadie tocara la subclase. Con composición, `ContadorLista` guarda una colección interna, cuenta una sola vez en sus propios métodos y reenvía; el cambio interno de la base ya no la afecta. Es el experimento de `SE-303` con clases de Python y datos sintéticos.

## Errores y confusiones comunes

- **Un contador cuenta doble tras un cambio interno de la base**: herencia que sobrescribe métodos que la base también usa; se corrige componiendo.
- **Cada nueva opción duplica las subclases**: herencia por combinación; se corrige con decoradores o con una lista de recargos.
- **Creer que si la interfaz no cambia, nada se rompe**: la fragilidad existe justo cuando la interfaz no cambia.
- **Pensar que toda herencia es mala**: lo frágil es sobrescribir métodos que la base usa internamente.

## Límites y cuándo no aplica

`SE-303` aclara que sus análisis usan clases reales de Python con datos sintéticos; las colecciones, los recargos y las jerarquías aleatorias son construcciones del autor, no una medición de código real. El problema afecta sobre todo a jerarquías donde la base y las subclases evolucionan por separado; si la base es del mismo equipo, pequeña y cambia junto con sus subclases, el riesgo baja. Una base diseñada y documentada para extensión, con los puntos de enganche prometidos, deja de ser frágil en esos puntos.
