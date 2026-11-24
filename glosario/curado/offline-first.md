# Offline-first

## Definición

**Offline-first** es un estilo de diseño en el que el cliente lee y escribe en su almacenamiento local y la red solo reconcilia las copias. Es el sentido de `SE-260` (offline-first y resolución de conflictos). No significa «funciona sin conexión como extra»: significa que el caso sin conexión es el normal y que la conexión es una optimización.

## Por qué importa

Invierte el diseño habitual, donde la red es la fuente de verdad y la caché una ayuda. La aplicación responde sin esperar a la red, y funciona en un tren, en una sala sin cobertura o con una red inestable. El costo es que dos copias pueden divergir, y alguien debe decidir qué hacer cuando lo hacen.

## Cómo funciona

`SE-260`: un cliente offline-first lee y escribe en su almacenamiento local y sincroniza en segundo plano. La red solo reconcilia. Kleppmann y colaboradores, citados por la clase, describen la propuesta y sus dificultades abiertas.

De eso se siguen tres decisiones:

1. **Dónde vive el estado** (local primero) y cómo se guarda.
2. **Cómo se registra el cambio:** como operaciones (un registro de lo hecho) y no solo como estado final, para poder fusionar.
3. **Qué política de conflicto aplica a cada tipo de dato.**

La política es por tipo de dato, no global.

## Ejemplo

El equipo del cliente en `SE-260` documenta una política de conflicto por tipo de dato. Los comentarios son un conjunto con marcas únicas: nunca se pierde uno añadido, a costa de que una baja concurrente a un alta no gane. El título del borrador usa último escritor con un contador por réplica para decidir, y guarda la versión descartada 30 días con un aviso. El contador de revisiones se calcula a partir del registro de operaciones, no se sincroniza como número.

## Errores y confusiones comunes

- **Un comentario añadido sin conexión desaparece:** se copió el estado de la última réplica en llegar. Corrección: fusionar operaciones y usar una estructura que conserve los añadidos (`SE-260`).
- **Una política única de «gana el último»** para todo.
- **Confundirlo con una caché sin conexión,** que solo sirve lecturas viejas.
- **Sincronizar contadores como números,** que pierde incrementos concurrentes.

## Límites y cuándo no aplica

No conviene cuando los datos exigen consistencia fuerte inmediata (un saldo, un cupo único): ahí dos copias divergentes son inaceptables. Las dificultades abiertas que cita la clase siguen vigentes: no existe solución general sin decidir políticas por dominio. Añade complejidad de almacenamiento local, migraciones del estado guardado y avisos al usuario.
