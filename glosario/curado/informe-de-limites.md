# Informe de límites

## Definición

Un **informe de límites** es el apartado de un entregable que declara lo que se hizo, lo que no se hizo y lo que ningún validador detecta. Es la definición de trabajo de `SE-516`; `SE-588` lo precisa como la declaración de lo no probado, lo no cubierto y lo no medido. No es una disculpa ni un descargo: es información técnica que permite a quien recibe el trabajo saber hasta dónde puede apoyarse en él.

## Por qué importa

Un resultado sin límites se lee como más general de lo que es. Quien recibe un paquete de experimentos o un informe de un agente decide según lo que cree que cubre. `SE-588` lo resume así: «un informe sin límites es un anuncio». El informe de límites cambia la decisión del lector de «¿me convence?» a «¿para qué sirve y para qué no?», y de paso protege a quien lo escribe de que se le atribuya una garantía que nunca dio.

## Cómo funciona

El informe tiene un contenido reconocible, que `SE-588` ilustra con un informe de un agente que debe responder a un comité tres preguntas: qué puede tocar, cómo se detiene y cómo se verifica. Y declara cuatro tipos de límite:

1. **Lo que no se probó:** un adversario adaptativo, un modelo real.
2. **Lo que el confinamiento no cubre:** procesos hijos, red.
3. **Lo que la verificación no ve:** un error que ninguna prueba ejerce, o una prueba que replica el error.
4. **Lo que no se midió:** productividad, costo.

En `SE-516` el informe forma parte de un **paquete** de experimentos junto con el catálogo, y su función es que otra persona pueda entenderlo sin ayuda. La causa de su utilidad es que ningún validador automático detecta lo que *falta*: las pruebas confirman lo que se probó; el informe nombra lo que quedó fuera.

## Ejemplo

Un paquete de experimentos de caos sobre la API de entregas incluye un informe con tres líneas de límites: «los experimentos usaron tiempo virtual y semillas fijas, no producción»; «la dependencia de 8 hilos y el tráfico son construcciones del autor»; «no se probó una falla de red parcial con pérdida de paquetes». Quien lo revisa sabe de inmediato que no puede concluir nada sobre producción ni sobre ese tipo de falla. (Ilustración basada en los límites que las clases declaran para sus propios experimentos.)

## Errores y confusiones comunes

- **El paquete no lo entiende nadie más.** Falta el informe de límites y el catálogo (`SE-516`); corrección: revisión por otra persona sin ayuda del autor.
- **Escribirlo como lista de excusas.** El límite útil dice qué conclusión *no* se puede sacar y por qué.
- **Declarar solo límites obvios.** Los valiosos son los que el lector no adivinaría: qué no ve la verificación, qué no se midió.
- **Dejarlo para el final sin datos.** Se escribe mientras se hace el trabajo, cuando se sabe qué se omitió.

## Límites y cuándo no aplica

Declarar límites no sustituye a hacer el trabajo: un informe honesto de un trabajo débil sigue siendo débil. Y un informe de límites no es exhaustivo: siempre hay límites que el autor ignora. Es una práctica de comunicación, no una garantía de rigor; tiene efecto cuando alguien lo lee, así que conviene colocarlo donde el lector lo vea antes de las conclusiones.
