# Matriz de compatibilidad

## Definición

Una **matriz de compatibilidad** es una tabla de combinaciones que se **ejecutan de verdad** para comprobar qué funciona con qué. En el proyecto SDK y CLI de `SE-120` se prueban: la versión **mínima y la máxima** del *runtime*, la instalación desde **wheel y sdist**, un **consumidor anterior con el release nuevo** y un **plugin compatible e incompatible**. En `SE-441` el mismo instrumento se aplica a versiones de un mensaje entre productores y lectores. Lo que define a la matriz es que cada celda es un resultado observado, no una suposición.

## Por qué importa

Afirmar «es compatible con Python 3.9 a 3.12» sin haber ejecutado cada caso es una promesa vacía. La matriz convierte esa promesa en evidencia y, además, delimita su alcance. La decisión que cambia es qué puede decirse en la documentación: `SE-120` establece que **una matriz verde respalda solo las combinaciones ejecutadas; las demás se marcan como no verificadas**. Se declara lo comprobado y se admite lo que no lo está, en lugar de implicar soporte universal.

## Cómo funciona

Se eligen **dimensiones** que importan para el producto y se ejecutan las combinaciones relevantes:

- **Versión del *runtime*:** mínima y máxima soportadas, porque los extremos suelen romperse primero.
- **Forma de instalación:** desde la rueda (*wheel*) y desde el código fuente (*sdist*), que recorren caminos de construcción distintos.
- **Consumidor anterior con release nuevo:** comprueba la compatibilidad hacia atrás.
- **Plugin compatible e incompatible:** el compatible debe funcionar y el incompatible debe **rechazarse con un mensaje claro**, no fallar de forma opaca.

`SE-441` muestra el poder de este método con un experimento: cinco versiones de un mensaje (v1 a v5) y cinco lectores, con los 25 pares ejecutados con mensajes producidos de verdad. Un lector **estricto** (exige exactamente los campos de su versión) es compatible en 7 de 25 pares, y uno **tolerante** (exige solo lo que necesita e ignora el resto) en 9. La tolerancia absorbe cambios **aditivos** (un campo nuevo) pero no los **destructivos** (renombrar un campo o cambiar su tipo rompen con ambos). Los números son de ese experimento sintético, no una regla general.

## Ejemplo

Una matriz mínima para un SDK (ilustración, valores inventados):

```text
                      py3.9   py3.12   consumidor 1.2 + SDK 1.3   plugin v2   plugin v1
wheel                  ok      ok               ok                  ok        rechazado (claro)
sdist                  ok      ok               ok                  ok        rechazado (claro)
py3.8                  no verificado (fuera de soporte declarado)
```

Cada celda es un resultado de ejecución en integración continua. Las combinaciones no ejecutadas aparecen como «no verificado» y no como «ok». Para el caso del mensaje de `SE-441`, un renombrado se evoluciona con el patrón expandir y contraer: durante un periodo el productor emite los dos nombres y los lectores migran antes de quitar el viejo.

## Errores y confusiones comunes

- **Llenar la tabla con supuestos.** Una celda sin ejecución no es «ok».
- **Probar solo la última versión.** Los extremos soportados y el consumidor anterior son donde ocurre la ruptura.
- **Creer que la tolerancia basta.** Absorbe lo aditivo, no lo destructivo; un lector tolerante que ignora en secreto un campo requerido pasaría la matriz sin avisar.
- **No probar el rechazo.** Que lo incompatible falle limpiamente también es parte del contrato.

## Límites y cuándo no aplica

El proyecto acredita un release candidato dentro de su matriz, no disponibilidad, seguridad ni soporte productivo (`SE-120`). Las matrices crecen de forma multiplicativa con cada dimensión; hay que elegir las que importan y no el producto cartesiano completo. En `SE-441`, las versiones son sintéticas con cuatro cambios elegidos: un esquema real tiene campos anidados, valores por defecto, enumeraciones que crecen y consumidores que dependen del orden.
