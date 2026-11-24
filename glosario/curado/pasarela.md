# Pasarela

## Definición

Una **pasarela** (*gateway*) es un equipo que conecta dispositivos de una red local con una red mayor, traduciendo protocolos y agregando datos. Es el sentido de `SE-273` (edge, gateways y procesamiento local). No debe confundirse con una pasarela de pagos ni con un API gateway de servicios web, que `SE-341` trata aparte.

## Por qué importa

Concentra confianza, almacenamiento y un punto único de fallo. Un diseño con pasarela decide dónde se toman decisiones y qué sigue funcionando cuando cada nivel cae.

## Cómo funciona

`SE-273`: la pasarela es un punto de concentración de confianza y de fallo. Si cae, todos los nodos de su piso quedan incomunicados; si se compromete, expone todos sus datos. Por eso necesita sus propias actualizaciones, identidad, almacenamiento con política y monitorización. De ello se sigue una regla de diseño: los nodos no deben depender de ella para decisiones críticas, y la pasarela debe poder funcionar sin la nube. La arquitectura se decide por *qué debe seguir funcionando cuando cada nivel cae*.

Funciones típicas: traducir entre el protocolo del nodo y el de la red mayor, agregar y filtrar datos antes de subirlos (ahorra ancho de banda), guardar mientras la nube no responde, y distribuir configuración y umbrales firmados a los nodos.

## Ejemplo

El equipo de la plataforma de `SE-273` asigna cada decisión a un nivel. La alarma de ventilación se decide en el nodo, con un umbral guardado en memoria y un valor seguro por defecto. La pasarela del piso agrupa los 20 nodos, aplica la banda muerta de 0,5 °C a la temperatura y el promedio por minuto al CO₂ más un evento si hay un pico, almacena hasta tres horas por si cae la nube y envía en lotes de 60 muestras en binario comprimido. La nube guarda el histórico y ajusta umbrales, que la pasarela distribuye a los nodos con firma (`SE-272`).

## Errores y confusiones comunes

- **Una pasarela caída silencia un piso:** punto único de fallo. Corrección: redundancia y alarma de silencio de nodos (`SE-273`).
- **Poner decisiones críticas solo en la pasarela.**
- **Tratarla como un equipo sin mantenimiento:** necesita actualizaciones, identidad y monitorización.
- **Confundirla con el borde de la red** en sentido amplio: la pasarela es una pieza del borde.

## Límites y cuándo no aplica

No hace falta cuando los dispositivos hablan directamente con la red mayor y no necesitan traducción ni agregación. Las cifras del ejemplo (20 nodos, tres horas, lotes de 60) son del escenario de la clase. Añadir una pasarela añade un componente que operar y proteger.
