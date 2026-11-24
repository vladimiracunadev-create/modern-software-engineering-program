# Escalera de degradación

## Definición

Una **escalera de degradación** es la secuencia ordenada de estados de menor servicio que adopta un sistema ante un fallo, cada uno con su límite declarado (`SE-396`). `SE-599` la usa en el sentido más amplio de secuencia ordenada de niveles de servicio, aplicada a sistemas con modelos de lenguaje.

## Por qué importa

Cuando una dependencia cae, entre «todo funciona» y «error 500» hay peldaños intermedios. Sin escalera, el sistema salta del servicio completo al fallo. La decisión que cambia es que la degradación se diseña de antemano, con límites y mensajes honestos, en vez de improvisarse durante el incidente. Y es una decisión de producto, no un interruptor técnico.

## Cómo funciona

`SE-396` describe tres peldaños:

1. **Servir lecturas obsoletas** de una caché, con una antigüedad máxima declarada y una etiqueta visible.
2. **Encolar las escrituras** localmente y reenviarlas al volver la dependencia, con un tamaño máximo de cola y una promesa honesta («tu entrega está recibida y se confirmará en unos minutos»).
3. **Rechazar** con un mensaje claro.

Cada peldaño cambia un fallo visible por un estado que hay que **declarar, vigilar y limitar**. Por eso cada nivel lleva su límite: cuánto tiempo, cuántos elementos, qué se promete. Sin límite, un nivel degradado se convierte en un fallo silencioso: la cola crece sin tope o la caché sirve datos arbitrariamente viejos.

La parte delicada es la promesa. Aceptar una entrega que aún no está en la base obliga a poder cumplirla. Por eso la clase distingue estados de garantía («recibida» y «guardada»): un acuse emitido al encolar sin distinguir estados genera estudiantes con acuse y sin entrega.

## Ejemplo

La base de entregas cae durante 60 s. Peldaño 1: la lista de entregas se sirve desde caché con una etiqueta «datos de hace 90 s». Peldaño 2: las nuevas entregas se encolan hasta un máximo de elementos y se responde «recibida». Si la cola se llena, peldaño 3: se rechaza con un mensaje claro. Escenario sintético de `SE-396` (la caída de 60 s es una construcción del autor).

## Errores y confusiones comunes

- **El servicio tarda más que el plazo sin que nadie falle**: tiempos límite que se suman por capa; se corrige con un presupuesto de tiempo comprobado con una prueba.
- **Un estudiante tiene acuse y no entrega**: acuse emitido al encolar sin distinguir estados.
- **Degradar sin declarar el límite**: el nivel intermedio se vuelve indefinido.
- **Tratarla como detalle técnico**: aceptar trabajo bajo degradación es una promesa de producto.

## Límites y cuándo no aplica

`SE-396` indica que sus experimentos son deterministas, sin servicio desplegado ni carga real: la caída de 60 s, la sobrecarga del 50 %, la proporción 30/70 y las mutaciones del paquete son construcciones del autor, y el validador se escribió conociendo las mutaciones. La escalera exige que la degradación sea aceptable para el negocio; donde no lo es (por ejemplo, ciertos datos que no pueden estar obsoletos), el único peldaño válido es rechazar.
