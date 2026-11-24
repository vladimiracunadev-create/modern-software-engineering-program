# Arranque en frío

## Definición

**Arranque en frío** es la creación de un entorno de ejecución para atender una petición cuando no hay uno disponible. Es el sentido principal de `SE-400` (serverless y ejecución gestionada). El programa lo usa en cuatro contextos relacionados por la misma idea («parte de cero»): en `SE-253`, arranque de una aplicación sin proceso ni estado en memoria; en `SE-331`, latencia añadida al crear un entorno inexistente; en `SE-606`, tiempo desde que se pide una réplica hasta que sirve; y en `SE-416`, el problema distinto de las plataformas de dos lados que no llegan sin masa en el otro lado.

## Por qué importa

La primera petición tras un silencio paga el costo de crear el entorno. Eso no es una falla: según `SE-400`, es el precio de pagar solo cuando hay uso. La decisión que cambia es si ese costo es tolerable para el escenario de latencia, y qué hacer si no lo es.

## Cómo funciona

En serverless (`SE-400`), para atender una petición la plataforma necesita un entorno con el código cargado. Si hay uno libre y vigente lo reutiliza (arranque caliente); si no, crea uno: reserva recursos, descarga o monta el código, inicia el proceso y ejecuta la inicialización. Los entornos pueden reutilizarse, pero la documentación de Lambda no promete cuánto se conservan inactivos. Resultado: mayor latencia tras un silencio y en cada pico que supera las instancias existentes.

En aplicaciones de teléfono y escritorio (`SE-253`) el arranque en frío parte sin proceso; en caliente encuentra el proceso vivo. La fracción de arranques fríos depende de la presión de memoria y del tiempo fuera, y el equipo no la controla; por eso restaurar el estado desde disco debe ser parte normal del arranque.

En servir modelos (`SE-606`), es el tiempo hasta que una réplica nueva sirve, lo que limita cuán rápido puede reaccionar el escalado.

## Ejemplo

`SE-331`: la revisión antivirus pasa a funciones bajo demanda con 10 instancias provisionadas durante la ventana de cierre, porque el 11,1 % de arranques en frío al inicio del pico era inaceptable. Con una función de 512 MB y 0,15 s, el equilibrio de costo es de 7,8 peticiones por segundo; como el tráfico medio ronda 2,5 por segundo, gana el pago por uso. Los números son del patrón simulado de la clase.

## Errores y confusiones comunes

- **Primera petición lenta tras un silencio:** causa, inicialización pesada; corrección, reducir dependencias de arranque y medir (`SE-400`).
- **Lentitud solo en los primeros segundos de un pico:** arranque concentrado; se aprovisionan instancias en la ventana crítica (`SE-331`).
- **Confundirlo con el calentamiento:** el arranque en frío es crear el entorno; el calentamiento es llenar cachés y conexiones de uno ya creado.

## Límites y cuándo no aplica

Con tráfico sostenido y alto el costo de arranque se amortiza y deja de ser relevante. Los tiempos de `SE-331` son construcciones del autor, no mediciones de un proveedor. Y el sentido de `SE-416` es de mercado, no técnico: no se resuelve con instancias aprovisionadas.
