# Verificación

## Definición

La **verificación** es la comprobación de que el sistema, o un artefacto, cumple lo especificado. El programa lo precisa en varios niveles:

- **Conformidad con la especificación** (`SE-003`).
- **Comprobación observable de que un paso dejó el sistema en el estado esperado** (`SE-211`).
- **Comprobación de que la evidencia de un release es coherente con valores esperados fijados de antemano** (`SE-479`).

Contrasta con la **validación** (`SE-145`): verificar es «¿lo hicimos bien?»; validar es «¿es lo correcto?».

## Por qué importa

Sin verificación, un procedimiento «funciona» y nadie sabe si resolvió. En agentes, la diferencia es operativa: un asistente puede declarar terminado un trabajo sin comprobar nada (`SE-577`). Cambia qué se considera «hecho»: no cuando se ejecutó el paso, sino cuando una comprobación observable lo confirma.

## Cómo funciona

El principio de `SE-479`: la verificación compara contra **valores esperados fijados de antemano**; si el valor esperado se toma del propio objeto verificado, la verificación pasa siempre. `SE-211` lo traduce a documentación: tras cada paso de un procedimiento se añade un comando de comprobación con la salida esperada.

En el harness de un agente (`SE-577`), la verificación es una de las decisiones que lo definen, junto con los permisos y la parada: lo que define al harness es qué decide, no qué biblioteca usa. Una configuración sin verificación resuelve tres tareas y declara terminadas las otras tres. La corrección del caso de `SE-577`: restaurar la línea de verificación y añadir una compuerta (`SE-583`) que rechaza la terminación sin pruebas en verde.

## Ejemplo

```bash
./migrar.sh && psql -c "select count(*) from entregas" | grep -q 5231 || { echo "verificación fallida"; exit 1; }
```

El número esperado (5 231) se fijó antes de ejecutar el paso; no se lee del resultado de la propia migración.

## Errores y confusiones comunes

- **El procedimiento «funciona» y nadie sabe si resolvió.** Causa: no hay verificación por paso; corrección: añadir un comando de comprobación con la salida esperada (`SE-211`).
- **Verificación que pasa siempre.** Causa: valores esperados tomados del propio documento; corrección: fijarlos de antemano (`SE-479`).
- **Confundir verificar con validar.** Pasar pruebas no demuestra que se construyó lo necesario.

## Límites y cuándo no aplica

Verificar prueba conformidad con una especificación, no que la especificación sea correcta. Una verificación cubre lo que comprueba: un conjunto de pruebas en verde no implica ausencia de defectos. Y el uso de «verificación» en `SE-479` es el de la cadena de suministro de un release; en otros contextos el término cubre técnicas distintas (inspección, análisis estático, pruebas formales).
