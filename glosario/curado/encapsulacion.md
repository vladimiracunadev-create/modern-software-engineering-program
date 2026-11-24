# Encapsulación

## Definición

**Encapsular**, en diseño (`SE-301`), es esconder una decisión detrás de una interfaz de modo que cambiarla no obligue a cambiar a los clientes. Parnas lo formuló como ocultar la decisión que probablemente cambie. En redes, `SE-037` usa la misma palabra con otro sentido: añadir información de control (cabeceras) alrededor de los datos de una capa superior. Son usos distintos; esta entrada trata el de diseño y señala el de redes al final.

## Por qué importa

Cada decisión visible es un compromiso con todos los clientes. Una representación expuesta se convierte en parte del contrato, y cambiarla obliga a tocar a todos. Encapsular reduce el número de lugares que hay que editar cuando algo cambia, que es la pregunta práctica con la que `SE-301` mide el acoplamiento.

## Cómo funciona

`SE-301` distingue niveles de ocultación:

- un **campo público** no esconde nada;
- un *getter* esconde el nombre pero no el significado: el cliente sigue multiplicando kilos;
- un método que responde la pregunta que el cliente realmente tiene (`costo_por_peso`) esconde la representación y la unidad.

La causa de que funcione es que el cliente depende de una promesa («costo por peso») y no de un detalle («el peso se guarda en kilos como `float`»). La decisión escondida puede cambiar sin tocar a los clientes. La clase propone comprobarlo contra un cambio previsto y con medidas como LCOM4 para detectar clases que mezclan responsabilidades con distinto motivo de cambio.

## Ejemplo

En `SE-301`, un cambio de unidad del peso toca decenas de archivos porque los clientes leen el dato y calculan por su cuenta. Con encapsulación:

```python
class Precio:
    def costo_por_peso(self, tarifa): return self._kilos * tarifa
```

La unidad queda dentro; un cambio a libras es local.

## Errores y confusiones comunes

- **Cambiar una plantilla obliga a releer el cálculo del costo.** Causa: una clase mezcla responsabilidades con distinto motivo de cambio; corrección: separar por decisión y comprobar con LCOM4 y con el cambio previsto (`SE-301`).
- **Un cambio de unidad toca decenas de archivos.** Causa: los clientes leen el dato y calculan por su cuenta; corrección: exponer comportamiento en vez de datos (`SE-301`).
- **Creer que `private` más getters basta.** Esconde el nombre, no la decisión.

## Límites y cuándo no aplica

Encapsular todo añade indirección sin beneficio: solo vale esconder lo que probablemente cambie. Las medidas de `SE-301` se calcularon sobre código de ejemplo y datos sintéticos; no se midió ningún proyecto real ni se evaluó si predicen defectos. Y el sentido de `SE-037` (cabeceras de protocolo) no es el principio de ocultación de información.
