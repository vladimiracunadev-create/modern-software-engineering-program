# Estado

## Definición

**Estado** es una palabra de dos sentidos en el programa:

- **Estado de infraestructura como código** (`SE-402`): el registro que relaciona cada recurso declarado con el objeto real que lo implementa y guarda sus atributos para poder compararlos (es el sentido de herramientas como Terraform u OpenTofu).
- **Estado de un cómputo** (`SE-057`): un resumen de la historia relevante para el comportamiento futuro.

El primero es el principal de esta entrada; el segundo es la idea general de que un sistema se comporta según lo que «recuerda».

## Por qué importa

Sin estado, una herramienta declarativa no sabría si un recurso ya existe o es nuevo (`SE-402`). El estado decide qué se crea, qué se cambia y qué se destruye; si es erróneo, la herramienta duplica, falla o borra. En el sentido general, entender qué parte de la historia importa permite reducir un sistema a lo necesario.

## Cómo funciona

`SE-402` enumera tres consecuencias prácticas del estado de infraestructura:

1. Es una **fuente de verdad parcial**: queda obsoleta si alguien cambia algo fuera de la herramienta.
2. Puede contener **datos sensibles**, porque guarda los valores de los atributos: se trata como un secreto.
3. Es un **archivo compartido**: necesita almacenamiento común y bloqueo para que dos personas no lo escriban a la vez.

Un plan que solo compara el código con el estado no ve el cambio hecho a mano; uno que antes refresca el estado con la realidad lo ve y propone revertirlo. `SE-057` aplica la idea a un cómputo: el estado es lo mínimo que hay que recordar para decidir qué sigue.

## Ejemplo

Dos personas ejecutan `apply` a la vez sin bloqueo; una escritura del estado se pierde y el siguiente plan crea de nuevo un recurso que ya existe. Corrección de `SE-402`: almacén remoto con bloqueo y versión. Ilustración de configuración:

```hcl
backend "s3" { bucket = "estado-iac"  dynamodb_table = "bloqueo" }
```

## Errores y confusiones comunes

- **Un recurso se crea dos veces o falla por duplicado.** Causa: escritura de estado perdida; corrección: almacén remoto con bloqueo y versión (`SE-402`).
- **Nadie puede aplicar.** Causa: proceso muerto con el bloqueo tomado; corrección: comprobar que nadie escribe y liberar con registro (`SE-402`).
- **El estado aparece en un repositorio público.** Causa: se trató como código; corrección: almacén cifrado con acceso restringido y rotación de lo expuesto (`SE-402`).

## Límites y cuándo no aplica

El estado no es la realidad: sin comparación con ella, no se sabe si sigue siendo cierto (`SE-402`). Los comandos concretos dependen de la herramienta y su versión. En el sentido de `SE-057`, un buen resumen de historia puede ser engañosamente pequeño si omite algo que luego importa.
