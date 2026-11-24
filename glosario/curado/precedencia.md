# Precedencia

## Definición

La **precedencia** es el orden en que se consultan las fuentes de configuración cuando hay más de una para el mismo valor (`SE-219`). `SE-031` lo precisa como el orden que determina qué fuente gana por campo. En el trabajo con asistentes de IA, `SE-560` usa la palabra para la regla que establece cuál de dos instrucciones en conflicto prevalece. El sentido común: ante dos respuestas, cuál manda.

## Por qué importa

Sin precedencia declarada, la misma configuración produce comportamientos distintos según quién lance el programa, y nadie sabe por qué. «Cambié el archivo y no pasó nada» es el síntoma típico: otra fuente de mayor precedencia seguía activa. La decisión que cambia es dónde se permite configurar y quién gana.

## Cómo funciona

`SE-219` identifica quién decide cada fuente: el valor por defecto lo decide quien escribe la herramienta; el archivo, el equipo que la despliega o quien la usa; la variable de entorno, quien lanza el proceso (un guion, un contenedor, un planificador); el *flag*, quien escribe esa invocación concreta. La precedencia habitual (flag, entorno, archivo, valor por defecto) sigue una idea: lo más cercano a la invocación manda sobre lo más general.

Pero es una convención de diseño, no un hecho: algunas herramientas ponen el archivo del sistema por encima del de usuario, o permiten fijar valores que ningún flag puede cambiar (política de seguridad). Lo importante es decidirlo y escribirlo. Para que sea operable se muestra la **configuración efectiva y su procedencia** (qué fuente dio cada valor), y se documenta la precedencia por campo (`SE-031`). Con asistentes (`SE-560`), reglas contradictorias hacen que el asistente alterne entre estilos: se detectan los pares y se escribe una precedencia.

## Ejemplo

Tabla de precedencia con casos de borde (`SE-219`): el caso normal, un entorno vacío, un `--limite 0` y un archivo con BOM. Ilustración:

```text
limite: flag --limite  >  env APP_LIMITE  >  archivo config.toml  >  default 100
efectivo: 0 (origen: flag)          # 0 es un valor válido, no «ausente»
```

La configuración es apropiada cuando esos casos tienen una fila; es peligrosa cuando solo se probó «todo ausente» y «todo definido».

## Errores y confusiones comunes

- **Cambiar el archivo no cambia la ejecución.** Causa: una variable de mayor precedencia sigue activa; corrección: mostrar configuración efectiva y procedencia (`SE-031`).
- **Cada opción puede venir de cualquier fuente.** Causa: no se controló la superficie operativa; corrección: limitar fuentes y documentar precedencia por campo (`SE-031`).
- **Tratar `0` o cadena vacía como ausente.** Confunde un valor válido con la falta de valor.

## Límites y cuándo no aplica

La precedencia flag-entorno-archivo-defecto es una convención: no todas las herramientas la siguen. En políticas de seguridad, el orden puede invertirse deliberadamente. Y con instrucciones en lenguaje natural (`SE-560`), una precedencia escrita reduce el conflicto pero no lo garantiza, porque el asistente la interpreta.
