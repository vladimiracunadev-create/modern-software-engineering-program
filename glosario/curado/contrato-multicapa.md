# Contrato multicapa

## Definición

Un **contrato multicapa** es, en el proyecto de `SE-120`, la publicación conjunta de varias superficies públicas de un mismo producto, con **versiones y errores alineados**: la **API de Python**, la **CLI** y el **protocolo de plugin**. Cada capa tiene sus propios consumidores y su propia compatibilidad, pero se gobiernan con un único documento que enumera lo público. El término lo introduce el programa para este proyecto; no es un nombre estándar.

## Por qué importa

Un producto reutilizable rara vez tiene una sola puerta. Quien programa usa la API; quien automatiza usa la CLI; quien extiende usa el protocolo de plugins. Cada puerta tiene dependientes distintos, y romper una sin avisar rompe a un grupo que quizá no lee las notas de las otras. La decisión que cambia es **cuándo se clasifica un cambio**: `SE-120` pide que un documento enumere la superficie pública *antes*, para que el equipo no clasifique los cambios *después* de haber roto algo, cuando la clasificación se vuelve una justificación.

## Cómo funciona

El contrato se construye con tres decisiones:

1. **Enumerar capas y superficie.** Para cada una, qué es público: funciones exportadas en la API, comandos y opciones en la CLI, mensajes y registro en el protocolo de plugin. Un `__all__` o una lista pública acota lo que se compara.
2. **Alinear versiones y errores.** Una versión del producto que significa lo mismo en todas las capas, y errores coherentes: un fallo de configuración se manifiesta como excepción en la API, como código de salida y mensaje en la CLI, y como respuesta definida en el protocolo.
3. **Verificar cada capa desde su consumidor.** Pruebas de contrato escritas desde quien consume, no desde quien implementa, cubren cada puerta; el comparador de API solo mira lo declarado público.

La causa de que el documento sea necesario es la asimetría: es fácil romper una capa creyendo que se tocó «solo código interno», porque otra capa dependía del comportamiento.

## Ejemplo

En el producto SDK+CLI de `SE-120`, la API Python expone `choose_next`, la CLI invoca lo mismo con códigos de salida definidos, y el plugin se registra con un protocolo versionado. Un cambio «interno» que rompe a un consumidor sin que ninguna prueba falle tiene como causa que la promesa no estaba escrita como prueba de contrato; la corrección es escribir la prueba desde el consumidor. Un esquema del documento (ilustración):

```text
Capa      Superficie pública                 Compatibilidad
API       engineering_sdk.__all__            semver de paquete
CLI       comandos y opciones documentados   semver + códigos de salida
Plugin    protocolo v2 (registro, hooks)     versión de protocolo propia
```

## Errores y confusiones comunes

- **Versionar una sola capa.** La CLI cambia de formato de salida y nadie sube la versión porque la API no cambió.
- **Comparar toda la superficie.** El comparador marca cambios que no importan; se define lo público y se compara solo eso.
- **Errores incoherentes entre capas.** El mismo fallo se describe de tres formas y los consumidores no pueden tratarlo de modo uniforme.
- **Clasificar el cambio al final.** Se rompe y luego se decide si «contaba».

## Límites y cuándo no aplica

El proyecto acredita un release candidato dentro de su matriz, no disponibilidad, seguridad ni soporte productivo (`SE-120`). Un contrato multicapa tiene un costo de mantenimiento real: más documentos, más pruebas, más decisiones de versión. Si el producto tiene una sola capa o un único consumidor controlado, el esfuerzo no compensa; basta una API pública bien definida.
