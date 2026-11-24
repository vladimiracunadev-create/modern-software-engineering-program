# Journey de desarrollador

## Definición

El **journey de desarrollador** es el recorrido completo que una persona hace con una biblioteca, SDK o API, y que `SE-118` descompone en ocho etapas: **descubrir, evaluar, instalar, lograr el primer éxito, integrar, depurar, actualizar y abandonar**. Es una aplicación del mapa de recorrido de usuario al producto técnico: quien consume una biblioteca es un usuario con tareas, tiempos y frustraciones. El término *DX* (*developer experience*, experiencia de desarrollo) designa la calidad de ese recorrido.

## Por qué importa

Es habitual optimizar solo el inicio: un *quickstart* brillante que consigue el primer éxito en cinco minutos. Pero la mayor parte de la vida con una biblioteca ocurre después: integrar con el código propio, diagnosticar errores, actualizar de versión, y, a veces, dejarla. `SE-118` lo dice así: **optimizar solo el quickstart oculta el mantenimiento**. La decisión que cambia es dónde se invierte el esfuerzo de diseño: en las etapas donde las personas pasan más tiempo o abandonan, que no siempre son las primeras.

## Cómo funciona

Cada etapa tiene cuatro elementos que `SE-118` pide registrar: la **tarea** que la persona intenta, el **tiempo** que le toma, el **error** más probable y la **evidencia** de que funciona. Recorridas con alguien que no conoce el producto, aparecen las fricciones:

- **Descubrir y evaluar:** ¿se entiende qué hace y si sirve para mi caso? La documentación y los ejemplos deciden.
- **Instalar y primer éxito:** ¿cuántos pasos y requisitos ocultos hasta ver un resultado? El síntoma documentado es que los usuarios abandonan antes de la primera llamada por demasiados pasos o requisitos previos ocultos; se corrige midiendo el recorrido con alguien nuevo, eliminando pasos o dando valores por defecto.
- **Integrar y depurar:** ¿los errores dicen qué faltó y cómo arreglarlo? Si los reportes son «no funciona» sin datos, el mensaje no ayudó; se diseña una excepción propia con causa, solución y atributos estructurados.
- **Actualizar:** ¿hay política de versiones, changelog y guía de migración?
- **Abandonar:** ¿se puede salir sin quedar atrapado (formatos abiertos, exportación)?

La causa de que el modelo sirva es que reemplaza opiniones («nuestra API es intuitiva») con observaciones por etapa.

## Ejemplo

Para el SDK del programa, una tabla de recorrido (ilustración, valores inventados):

```text
etapa            tarea                    tiempo   error probable             evidencia
instalar         pip install              1 min    versión de Python antigua  mensaje con versión requerida
primer éxito     choose_next(casos)       4 min    casos con campo faltante   error con campo y ejemplo
actualizar       1.2 -> 1.3               10 min   opción renombrada          guía de migración + aviso
```

Una persona nueva la recorre y se anotan los bloqueos. Esa observación alimenta mejoras concretas: un valor por defecto, un mensaje mejor, una nota de migración.

## Errores y confusiones comunes

- **Medir solo el primer éxito.** Oculta el costo de mantener la integración.
- **Evaluar por autoevaluación.** El equipo que construyó el producto no ve sus propias fricciones.
- **Ignorar la etapa de abandono.** La dependencia sin salida es un riesgo para quien adopta.
- **Tratar la documentación como etapa aparte.** Atraviesa todas las etapas.

## Límites y cuándo no aplica

Una evaluación interna de DX no sustituye investigación diversa ni soporte real (`SE-118`): personas con otros entornos, experiencia o idioma encuentran fricciones que el equipo no ve. El modelo de ocho etapas es una guía, no un estándar; un producto con un solo consumidor interno puede no necesitar tanto formalismo. Y el recorrido no reemplaza datos de uso reales (abandonos, tickets) cuando existen.
