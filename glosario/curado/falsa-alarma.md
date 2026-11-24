# Falsa alarma

## Definición

Una **falsa alarma** es la activación de un aviso, regla o disparador cuando el problema que debía detectar no existe. El programa la usa con un núcleo común y matices por clase: en SE-192, la activación de un disparador sin que el plan haya dejado de valer; en SE-332, el aviso de una función cuando la propiedad se cumple; en SE-578, el bloqueo de un cambio que no infringe la regla; en SE-512, el fallo de una suite sobre una configuración sana; en SE-306, el código que una regla señala y que, mirado en su contexto, no es un problema; en SE-476, la reversión de un canario sin defecto real.

## Por qué importa

Cada falsa alarma cuesta atención y credibilidad. Una regla que alarma casi siempre acaba ignorada, y entonces la alarma verdadera pasa desapercibida. Cambia el diseño de umbrales y ventanas: no se trata solo de detectar, sino de detectar sin alarmar de más.

## Cómo funciona

La causa estructural es el compromiso entre dos errores. SE-476 lo explica con el canario: el umbral fija el equilibrio entre ambos; **bajo, y se revierte sin defecto (falsa alarma); alto, y tarda más en declararse un defecto real**. Con ruido, el umbral decide cuántas falsas alarmas se producen.

La cuenta que sorprende es la de **evaluaciones repetidas**. En SE-476, sin ningún defecto (error del 0,5 % en ambas versiones), se evalúa la prueba cada segundo durante 30 minutos con un canario del 5 % y se cuenta cuántos de 200 episodios terminan en reversión según el umbral. Con un umbral del 5 % para una sola decisión, se revierte el 47 % de los episodios, porque se evalúa 1.800 veces. Las evaluaciones consecutivas están correlacionadas (no son 1.800 pruebas independientes), pero el efecto es grande. Es el mismo problema de mirar los resultados repetidamente.

SE-192 lo aplica a los disparadores: si cada semana hay una probabilidad independiente de 5 % de activarse sin motivo, en 20 semanas la probabilidad de al menos una falsa alarma es 1 − 0,95²⁰ ≈ 64 %. Las defensas son las mismas: exigir **avisos seguidos** (ventana), ampliar la ventana, subir el umbral y **medir las falsas alarmas** para ajustarlas.

## Ejemplo

Un canario del 5 % se evalúa cada segundo con un umbral del 5 % por decisión. Aunque las dos versiones sean idénticas, al cabo de 30 minutos casi la mitad de los episodios termina en reversión. Con un umbral más estricto y la exigencia de varias evaluaciones consecutivas, las reversiones innecesarias caen a una fracción pequeña, a costa de tardar más en detectar un defecto real. (Resultado de SE-476, expresado con las cifras de la clase.)

## Errores y confusiones comunes

- **Nadie reacciona a la alarma de replanificación**: regla sin ventana que alarma casi siempre; corrección: exigir avisos seguidos, ampliar la ventana y medir falsas alarmas.
- **Tratar cada falsa alarma como un fallo del equipo** en lugar de un parámetro de la regla.
- **Evaluar sin corregir por múltiples miradas.**
- **Confundirla con un falso positivo estadístico**: es el mismo concepto aplicado a una regla operativa.

## Límites y cuándo no aplica

Eliminar las falsas alarmas del todo exige dejar pasar defectos reales. El nivel aceptable depende del costo de actuar sin necesidad frente al de no actuar a tiempo. Las cifras de SE-476 son de una simulación con supuestos del autor.
