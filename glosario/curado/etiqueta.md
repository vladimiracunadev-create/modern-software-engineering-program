# Etiqueta

## Definición

El programa usa **etiqueta** con dos sentidos distintos. En la cadena de entrega (`SE-470`), una etiqueta es un nombre legible que apunta a una huella y que normalmente se puede reasignar (por ejemplo, `api:1.4.0`). En aprendizaje automático (`SE-602`), la etiqueta es el valor que el modelo debe predecir, con su fuente, su ventana y su retraso. Esta entrada desarrolla ambos y avisa de que no son lo mismo.

## Por qué importa

En entrega, confundir etiqueta con huella permite que «la misma versión» sea contenido distinto en dos momentos. En aprendizaje automático, una etiqueta sin su retraso invita a calcular métricas sobre decisiones que todavía no tienen respuesta y a presentarlas como resultados (`SE-602`).

## Cómo funciona

**Sentido de entrega.** Un artefacto es la salida inmutable de un build; su huella es el resultado de aplicarle una función hash, de modo que un solo byte distinto produce otra huella. Un registro de contenedores permite referirse a una imagen por etiqueta (`api:1.4.0`) o por resumen (`api@sha256:…`); solo la segunda es inmutable. La etiqueta es un puntero que alguien puede mover.

**Sentido de datos.** La etiqueta tiene una fuente (de dónde sale la verdad), una ventana (en qué intervalo se observa) y un retraso (cuánto tarda en conocerse).

## Ejemplo

`SE-470`: el repositorio de la API de entregas acepta etiquetas de versión una sola vez; integración y preproducción prueban contra la huella, y el despliegue recibe la huella y la configuración por separado.

## Errores y confusiones comunes

- **Un defecto aparece solo en producción.** Se reconstruyó o se movió una etiqueta; corrección (`SE-470`): desplegar por huella y promover sin reconstruir.
- **Métricas sobre etiquetas que aún no existen.** Se ignora el retraso de la etiqueta.

## Límites y cuándo no aplica

Una etiqueta inmutable por política (aceptada una sola vez) reduce el riesgo, pero la garantía fuerte sigue siendo la huella. En datos, ninguna etiqueta es verdad absoluta: tiene ruido y retraso de su fuente.
