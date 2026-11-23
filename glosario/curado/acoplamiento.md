# Acoplamiento

## Definición

El **acoplamiento** es el grado en que un módulo necesita conocer a otro para funcionar o para cambiar (`SE-301`). `SE-317` lo concreta para clases como el grado en que una clase depende de otras. El sentido del programa no es «dependencia mala»: es una propiedad con tres dimensiones que se pueden observar y contar.

## Por qué importa

Cada dependencia es un lugar más por el que un cambio se propaga: cuanto más acoplado está un módulo, más cosas hay que tocar y revisar cuando algo cambia. Por eso `SE-301` lo ata a una pregunta práctica (cuántos lugares hay que editar para una decisión) y no a una opinión sobre el código.

## Cómo funciona

`SE-301` pide mirar tres dimensiones, no solo contar dependencias:

- **Dirección:** quién conoce a quién.
- **Cantidad:** cuántos módulos conoce.
- **Naturaleza:** qué conoce: un nombre, un tipo, un orden de llamadas o una representación interna.

Cuanto más se conoce de la implementación del otro, más cambios se propagan. Un módulo de precio que usa una zona geográfica depende de ella por una razón del dominio: ese acoplamiento no es un defecto. El problema aparece cuando el módulo conoce la representación interna del otro.

Los ciclos de dependencias son el caso extremo: los módulos del ciclo no se pueden entender, probar ni desplegar por separado. `SE-301` observa que aparecen sin mala intención, cuando cada persona añade la dependencia que le conviene, y que una regla de sentido (las capas altas pueden depender de las bajas, nunca al revés) elimina los ciclos por construcción. `SE-317` agrega que el bajo acoplamiento y la alta cohesión tiran en direcciones opuestas y deben leerse juntos.

## Ejemplo

En `SE-301`, un cambio de unidad del peso obliga a tocar muchos archivos porque los clientes leen el dato y calculan por su cuenta: están acoplados a la representación. Exponer comportamiento en vez de datos (`Precio.costo_por_peso()`) esconde la representación y la unidad, y el cambio queda local.

## Errores y confusiones comunes

- **Condenar todo acoplamiento.** Un módulo de precio que usa una zona geográfica depende de ella por una razón del dominio; lo que importa es la dirección, la cantidad y la naturaleza de la dependencia (`SE-301`).
- **Creer que es una opinión de estilo.** Es una propiedad observable en cuántos lugares hay que tocar (`SE-301`).
- **Resolver un ciclo con un parche local.** Sin una regla de sentido, los ciclos reaparecen; la inversión de dependencias que trata `SE-302` es la herramienta cuando una capa baja necesita avisar a una alta.

## Límites y cuándo no aplica

Contar dependencias aproxima el acoplamiento, no lo agota: `SE-301` advierte que el conteo de sitios a editar depende de qué cambio se imagine, y un número bajo puede coexistir con un mal diseño. El acoplamiento por razones del dominio es legítimo. Y los criterios de `SE-317` (bajo acoplamiento, alta cohesión, indirección, variaciones protegidas) se solapan y dos autores pueden agruparlos distinto: son una elección didáctica del curso.
