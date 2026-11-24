# Procedencia

## Definición

La **procedencia** (*provenance*) es el registro de quién construyó un artefacto, a partir de qué fuente y con qué materiales y parámetros (`SE-472`). Otras clases la usan con matices: origen, versión, autor, URL, hash y transformación que permiten rastrear un componente (`SE-117`); evidencia sobre origen y cadena de publicación (`SE-032`); información sobre qué construyó un artefacto y con qué proceso (`SE-202`); cadena que permite rastrear evidencia (`SE-024`).

## Por qué importa

Sin procedencia, un binario o un paquete es una caja cerrada: no se sabe de qué código salió ni quién lo produjo. Eso impide verificar que lo que se despliega es lo que se revisó. Cambia qué se exige de una dependencia o de un artefacto propio: no solo un hash, sino de dónde viene.

## Cómo funciona

`SE-472` dice que la procedencia responde cinco preguntas: quién lo construyó (el *constructor*), a partir de qué fuente (repositorio y commit), con qué materiales (dependencias, herramientas), con qué parámetros y cuál es su huella (el *sujeto*). Un marco como SLSA organiza esos campos en niveles según cuánta confianza hay que depositar en el constructor: en los niveles bajos la procedencia existe y la genera el propio *build*; en los altos la genera una plataforma de construcción aislada, de la que el equipo de desarrollo no puede alterar los datos. La diferencia es esencial: una procedencia escrita por quien construye prueba lo que el constructor *dice*; una generada por una plataforma independiente prueba algo mucho más difícil de falsificar.

`SE-117` añade para componentes copiados: registrar cambios y conservar atribución. Y recuerda que un SBOM describe composición pero no certifica que cada dato sea correcto.

## Ejemplo

Un artefacto publicado lleva una declaración con: constructor (la plataforma de CI), repositorio y commit, parámetros del build, y el hash del archivo. El consumidor verifica la declaración contra valores esperados fijados de antemano. Ilustración:

```json
{"sujeto": {"sha256": "..."}, "constructor": "ci.ejemplo", "fuente": "repo@commit", "materiales": ["dep@1.2.3"]}
```

## Errores y confusiones comunes

- **La verificación pasa siempre.** Causa: los valores esperados se tomaron del propio documento; corrección: fijar de antemano constructor, repositorio y rama (`SE-472`).
- **Confundir procedencia con SBOM.** La primera dice cómo se produjo; el segundo, qué contiene (`SE-117`).
- **Creer que firmar equivale a procedencia.** Una firma dice quién firmó, no cómo se construyó.

## Límites y cuándo no aplica

La procedencia demuestra origen, no ausencia de defectos ni de código malicioso en la fuente. Los niveles de SLSA son un marco externo cuyo detalle conviene contrastar con su especificación. Y la procedencia autogenerada por el constructor solo vale si se confía en el constructor.
