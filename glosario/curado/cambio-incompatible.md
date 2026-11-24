# Cambio incompatible

## Definición

Un **cambio incompatible** es el que puede hacer fallar o cambiar el resultado de un cliente que seguía el contrato (`SE-474`).

## Por qué importa

Quien publica una biblioteca o una API promete a quien depende de ella; el versionado semántico es la forma de expresar esa promesa. Saber si un cambio es incompatible decide qué número de versión sube y cuánto aviso hay que dar.

## Cómo funciona

`SE-474`: el **versionado semántico** asigna significado a los tres números: el **mayor** sube cuando hay cambios incompatibles de la API pública, el **menor** cuando se añade funcionalidad compatible y el **parche** cuando se corrige un error sin cambiar la API. Quien depende puede escribir rangos (`>=1.4,<2`) y automatizar actualizaciones menores. Su debilidad: la compatibilidad se declara, no se comprueba, y un cambio de comportamiento con la firma intacta rompe clientes sin que el número lo anuncie.

## Ejemplo

Una función que antes devolvía una lista vacía ante «sin resultados» y ahora lanza una excepción mantiene su firma, pero rompe a los clientes que no la capturaban: es un cambio incompatible aunque el tipo no haya cambiado.

## Errores y confusiones comunes

- **Un cliente se rompe tras un cambio menor.** Cambio de comportamiento con la firma intacta; pruebas de contrato y revisión del comportamiento observable.
- **El número de versión no dice nada.** API pública no definida; declarar la API pública y lo que no se promete.

## Límites y cuándo no aplica

La compatibilidad es relativa a lo que el contrato promete; por eso hay que definir qué es API pública. El versionado semántico no se aplica igual a aplicaciones finales, que no tienen clientes programáticos.
