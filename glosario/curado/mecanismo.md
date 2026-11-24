# Mecanismo

## Definición

Un **mecanismo** es la explicación de *cómo* algo produce su efecto: qué entrada produce qué transición, paso a paso (`SE-037`). En el programa no es sinónimo de «técnica» ni de «herramienta»: es la cadena causal que se puede seguir, comprobar y trasladar a otro caso. Por eso las clases piden «el mecanismo» y no solo la receta.

## Por qué importa

Quien conoce el mecanismo puede diagnosticar y adaptar; quien solo conoce los comandos repite pasos mecánicamente y falla cuando cambia el entorno. `SE-038` lo formula como diferencia profesional: la decisión conecta requisito, mecanismo, señal, riesgo y recuperación, y el equipo puede cambiar de herramienta sin perder el razonamiento. Eso es trazabilidad del razonamiento, no solo del código.

## Cómo funciona

Entender un mecanismo implica nombrar:

- **la entrada** (qué ocurre o se envía);
- **la transición** (qué cambia de estado y dónde);
- **la señal observable** (cómo se distingue que ocurrió);
- **los supuestos** (qué hace falta para que valga: topología, dirección, política).

Las clases de redes (`SE-037` a `SE-045`) lo practican: en cada tema se pide trasladar el mecanismo a una segunda red o protocolo sin repetir comandos mecánicamente. Se conserva la pregunta y el criterio de evidencia; cambian los supuestos de dirección, intermediación y política. Y se escribe qué observación seguiría siendo válida y cuál depende de la topología original. La causa de que esto funcione es que lo que se traslada es la estructura del argumento, no los nombres del caso original.

## Ejemplo

`SE-038` describe un síntoma: «las transferencias grandes se cuelgan pero conectar funciona». El mecanismo: un tramo con MTU menor descarta paquetes con la marca DF (no fragmentar), y los avisos ICMP de «fragmentación necesaria» se filtran, de modo que el emisor nunca ajusta el tamaño. Corrección: probar el MTU de la ruta, permitir ese ICMP y ajustar el MSS. Ilustración:

```bash
ping -M do -s 1472 destino   # prueba un paquete de 1500 bytes sin fragmentar (Linux)
```

## Errores y confusiones comunes

- **Medir el rendimiento en loopback y extrapolarlo.** Causa: el loopback no usa ningún medio; corrección: medir sobre la interfaz y la ruta reales (`SE-038`).
- **Aprender comandos sin mecanismo.** Funciona hasta que el entorno cambia.
- **Confundir mecanismo con causa raíz.** El mecanismo explica el camino; la causa raíz es dónde conviene intervenir.

## Límites y cuándo no aplica

Un mecanismo vale bajo sus supuestos: trasladarlo a otra topología exige revisarlos (`SE-038`, `SE-045`). Un mecanismo plausible no es un mecanismo comprobado: requiere una observación que lo respalde. Y hay fenómenos emergentes de sistemas grandes donde el mecanismo detallado no se conoce y se trabaja con regularidades medidas.
