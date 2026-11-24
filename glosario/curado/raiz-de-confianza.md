# Raíz de confianza

## Definición

La **raíz de confianza** (*root of trust*) es la clave o el dato que el verificador da por bueno sin comprobarlo. Es el sentido de `SE-473` (firmas, checksums y verificación); `SE-283` (hardware seguro: TEE y atestación) lo aplica al hardware: el componente del que se parte sin verificación adicional. Toda cadena de verificación termina en algo así: no existe verificación sin un punto de partida aceptado.

## Por qué importa

La clave fijada es el punto que debe protegerse. Una firma impecable no vale nada si el atacante controla la clave pública con la que se comprueba. Por eso la pregunta útil no es «¿está firmado?» sino «¿de dónde obtuvo el verificador la clave, y quién puede alterarla?».

## Cómo funciona

`SE-473` contrasta dos situaciones:

- **La clave pública llega con el archivo:** la raíz es el sitio de descarga, y el atacante que controla el sitio controla la raíz. La firma no aporta nada.
- **La clave se fija de antemano** (viene en el instalador anterior, en el sistema operativo, en un repositorio de claves independiente, en el propio cliente): el atacante tiene que comprometer esa distribución anterior.

La estrategia es **mover la raíz a un lugar más pequeño, de actualización rara y mejor vigilado**. No se elimina la confianza, se la confina. Por eso los sistemas de actualización robustos distinguen claves por rol (raíz, objetivos, marca de tiempo) y guardan las de mayor valor fuera de línea.

En hardware (`SE-283`), la raíz es un componente, normalmente de silicio, cuyo comportamiento se asume correcto; la atestación demuestra a un tercero que el código arrancó sobre esa raíz.

## Ejemplo

`SE-473` compara con una alternativa que no usa claves de larga vida: se confía en un proveedor de identidad y en un registro público auditable. Eso desplaza el problema: ya no custodias una clave de larga vida, pero confías en el proveedor y en el registro. Cambia la superficie de ataque y la raíz; no las elimina. La recomendación de la clase es evaluar qué raíz es más fácil de proteger en tu caso.

## Errores y confusiones comunes

- **Verificar una firma con una clave obtenida del mismo canal que el archivo.**
- **Creer que firmar elimina la confianza:** solo cambia su ubicación.
- **Una sola clave para todo:** un compromiso lo expone todo; se separan por rol.
- **Confundirla con un certificado de servidor TLS,** que se verifica contra raíces preinstaladas, que son a su vez la raíz.

## Límites y cuándo no aplica

Una raíz fija es difícil de rotar: si se compromete, hay que actualizarla por un canal que ya no es de fiar; por eso se planifica la rotación y la revocación antes de necesitarlas. En hardware, un defecto de la raíz es irreparable sin reemplazar el dispositivo.
