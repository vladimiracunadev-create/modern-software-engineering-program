# Comprobación de forma

## Definición

Una **comprobación de forma** es una verificación mecánica de una propiedad del paquete de un cambio que no depende del sentido del cambio: el formato del mensaje, el tamaño, la licencia, las firmas. Es el término de `SE-204`, el proyecto de contribución revisable de extremo a extremo. Se opone a la revisión de fondo: la forma se puede automatizar; el sentido necesita a una persona.

## Por qué importa

Libera a la revisora de lo mecánico. Si el tamaño del PR, el formato de los commits o la cabecera de licencia los comprueba una máquina, la atención humana se dedica a lo que solo ella puede ver: si el cambio resuelve el problema y si es correcto. `SE-204` añade que estas comprobaciones deben ser independientes entre sí, para que un fallo señale una causa concreta.

## Cómo funciona

`SE-204` enumera doce comprobaciones de forma: mensajes convencionales; commits atómicos (≤ 6 archivos y ≤ 120 líneas); cada commit pasa las pruebas; las pruebas pasan en la punta; cabecera de licencia en archivos nuevos; issue enlazado; sin secretos; commits firmados; `Signed-off-by`; tamaño del PR (≤ 400 líneas); revisores de los propietarios pedidos; y «si cambia el código cambia una prueba».

Los umbrales son una decisión del equipo y deben revisarse con los casos que se escapan: si un cambio pequeño rompe algo que la regla no vio, se ajusta. La regla «si cambia el código cambia una prueba» es el ejemplo de cómo se acerca la forma al sentido sin entrar en él: no valora la prueba, solo exige que exista.

## Ejemplo

Una contribución a la plataforma de entregas pasa las doce comprobaciones: cada commit compila, el PR tiene 210 líneas, hay `Signed-off-by` e issue enlazado. Aun así, puede contener una prueba que afirma `True` y un cambio de una regla de negocio sin prueba real. Las comprobaciones de forma no lo ven; lo ve una lectura humana o una mutación que modifique el código y compruebe que alguna prueba falla.

## Errores y confusiones comunes

- **El validador pasa y el comportamiento es erróneo.** Una prueba vacía o débil; corrección de `SE-204`: añadir una mutación o una lectura humana de las pruebas.
- **Una rama tiene un commit que no compila.** Se empujó un intermedio roto; reordenar la rama para que cada commit pase.
- **Tratar el verde como aprobación.** Las comprobaciones dicen que el paquete está bien formado, no que sea correcto.
- **Umbrales intocables.** Se fijan y no se revisan con lo que se escapa.

## Límites y cuándo no aplica

La forma no ve el sentido (`SE-204`): un test que afirma `True` las pasa todas, y un cambio de regla de negocio solo se detecta si una regla exige tocar una prueba. Al trasladar el paquete a otro tipo de contribución, como infraestructura como código o un conjunto de datos, algunas comprobaciones dejan de valer y otras hay que inventarlas; la clase propone justamente decidir cuáles siguen valiendo y qué queda para una persona.
