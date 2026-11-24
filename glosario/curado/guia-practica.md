# Guía práctica

## Definición

Una **guía práctica** (*how-to guide*) es, en SE-206, una página orientada a un objetivo de trabajo concreto que supone competencia previa y admite bifurcaciones. Es uno de los cuatro tipos de documentación que distingue la clase: tutorial, guía práctica, referencia y explicación. No debe confundirse con el uso coloquial de «guía» como manual general.

## Por qué importa

Resuelve un problema de quien ya sabe lo básico y necesita hacer algo específico. Si se mezcla con un tutorial, quien tiene prisa debe leer lecciones; si se mezcla con una explicación, el procedimiento se pierde entre justificaciones. Cambia la decisión de qué entra en la página: solo lo que lleva de la situación inicial al objetivo.

## Cómo funciona

Una guía responde a un objetivo del trabajo («cambiar el tope de penalización de un curso»), da por sentado que quien la lee sabe lo básico y evita enseñar. Es una receta con **precondiciones**, **pasos** y una **forma de comprobar** que funcionó. Se distingue del tutorial porque admite bifurcaciones («si el curso tiene prórrogas activas, antes haz esto») y porque no garantiza que sea la primera vez de nadie: el tutorial guía a un principiante por un camino único y seguro.

El error típico que describe SE-206 es que la guía **crece**: se le añaden definiciones, el porqué del tope, una tabla de parámetros, y deja de ser una guía. La regla es que lo que sobra se enlaza: las definiciones y el porqué van a la explicación y los parámetros a la referencia. Empezar la guía con la historia de la política es la mezcla de contexto con procedimiento, y se corrige moviendo esa historia a la explicación y enlazándola desde el primer párrafo.

## Ejemplo

En la plataforma de entregas, la guía «Cambiar el tope de penalización de un curso» lista las precondiciones (permiso de administración del curso), los pasos, la comprobación (una entrega de prueba con retraso muestra el nuevo descuento) y una bifurcación para cursos con prórrogas. Enlaza al tutorial, a la referencia «Parámetros de penalización» y a la explicación «Por qué la penalización es diaria y con tope» en una línea cada una. La clase añade que la guía se ejecuta en integración continua, de modo que si el procedimiento deja de funcionar, la compilación lo detecta.

## Errores y confusiones comunes

- **Empezar con la historia de la política**: mezcla de contexto y procedimiento.
- **Convertirla en tutorial**: explicar lo básico a quien ya lo sabe.
- **Sin comprobación de éxito**: la lectora no sabe si terminó.
- **Dejarla sin ejecutar**: una guía que nadie prueba se desactualiza.

## Límites y cuándo no aplica

No sirve a quien aún no sabe lo básico (necesita un tutorial) ni a quien quiere entender por qué (necesita una explicación). Para tareas muy simples, una línea en la referencia puede bastar. Una guía solo es fiable mientras el sistema no cambie; por eso conviene que sea comprobable automáticamente o tenga fecha de revisión.
