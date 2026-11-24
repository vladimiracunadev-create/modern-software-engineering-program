# Metadatos

## Definición

Los **metadatos** son las propiedades de un objeto distintas de su contenido principal (`SE-026`). `SE-367` los define como datos que describen otros datos: dueño, significado, sensibilidad y frescura. Son un mismo concepto en dos escalas: en un sistema de archivos describen cada archivo; en un pipeline de datos describen conjuntos y columnas.

## Por qué importa

Sin metadatos, un dato no se puede gobernar: no se sabe quién es responsable, qué significa, si contiene información personal ni si está al día. Con ellos, se pueden automatizar controles y trazar el origen de un valor. En el sistema de archivos, los metadatos deciden si una operación sobre el archivo se permite o cómo se ordena.

## Cómo funciona

**En archivos** (`SE-026`): el archivo que una aplicación percibe no es «un bloque del disco». El sistema de archivos relaciona nombres con objetos, organiza directorios y conserva metadatos como tipo, tamaño, marcas temporales y permisos. El núcleo traduce operaciones de alto nivel a la implementación montada y, finalmente, al dispositivo o servicio remoto.

**En datos** (`SE-367`): los metadatos del catálogo (dueño, capa, columnas con tipo, sensibilidad, antigüedad máxima) permiten construir el **linaje**, la relación entre columnas de entrada y de salida. El laboratorio de `SE-367` usa un analizador de expresiones regulares sobre seis sentencias `CREATE TABLE ... AS SELECT` para registrar de qué columnas de origen sale cada columna: sirve para el estilo que reconoce y falla en silencio con otro. Un analizador real usa la gramática completa del dialecto y los metadatos del catálogo para expandir comodines.

## Ejemplo

Ilustración en Python sobre archivos:

```python
import os, time
st = os.stat("informe.csv")
print(st.st_size, time.ctime(st.st_mtime), oct(st.st_mode))
```

Aquí el tamaño, la fecha de modificación y los permisos son metadatos; el contenido del CSV no. En un catálogo de datos, el equivalente sería `owner: finanzas`, `pii: false`, `max_age_days: 1`.

## Errores y confusiones comunes

- **El archivo se busca en lugares distintos.** Causa: se confundió directorio del script con directorio de trabajo; corrección: elegir una base explícita y mostrarla en diagnóstico (`SE-026`).
- **Ruta portable construida reemplazando `/`.** Causa: se trataron rutas como cadenas; corrección: biblioteca de rutas y pruebas con raíces, volúmenes y UNC (`SE-026`).
- **Confiar en un analizador que falla en silencio.** Si el estilo no coincide, el linaje queda incompleto sin avisar (`SE-367`).

## Límites y cuándo no aplica

`SE-026` no cubre recuperación forense ni sistemas distribuidos ni todas las garantías de cada sistema de archivos; una ruta resoluble todavía puede estar prohibida por permisos. Los metadatos pueden estar desactualizados o ser incorrectos: un campo «sensibilidad» sin proceso que lo mantenga es una promesa vacía. Y los metadatos también pueden filtrar información (autor, ubicación), de modo que a veces hay que eliminarlos.
