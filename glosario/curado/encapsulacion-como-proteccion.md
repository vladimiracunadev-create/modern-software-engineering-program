# Encapsulación como protección

## Definición

**Encapsulación como protección** es el sentido que `SE-075` da a encapsular: impedir **transiciones inválidas** del estado de un objeto y exponer **operaciones del dominio** (como `record_observation` o `close`) en lugar de campos. La clase aclara por qué lo plantea así: encapsular **no significa** esconder campos detrás de *getters* y *setters* equivalentes. Si cada campo privado tiene un acceso público que lo lee y lo escribe sin condiciones, el objeto no protege nada; solo ha movido la sintaxis.

## Por qué importa

Un objeto vale por las garantías que mantiene: un pedido cerrado no admite líneas nuevas, un saldo no baja de cierto límite. Si cualquiera puede reconstruir el estado interno a voluntad, la **invariante** (la regla que siempre debe cumplirse) sigue **fuera del objeto**, repartida entre quienes lo usan, y basta que uno la olvide. La decisión que cambia es dónde vive la regla: dentro del objeto, en un lugar único, o en cada consumidor. Con la primera opción, cambiar la regla es local.

## Cómo funciona

La protección se logra con tres decisiones:

- **Operaciones del dominio, no acceso a campos.** En lugar de `pedido.estado = "cerrado"`, se ofrece `pedido.cerrar()`, que comprueba si es legal cerrarlo y actualiza lo necesario de forma coherente.
- **Validación en el punto de escritura.** Toda vía que cambia el estado pasa por un método que verifica la invariante. En Python, la privacidad por convención (un guion bajo) no impide asignar un valor inválido, como señala `SE-075`; hay que validar en el método que escribe o usar una **propiedad** con *setter* que valide.
- **Sin filtrar estructura mutable.** Devolver la lista interna permite alterarla desde fuera y saltarse la validación; se devuelve una copia o una vista de solo lectura.

La causa de que funcione es que el objeto controla **todas** las rutas por las que su estado cambia. Cada ruta que escapa es un hueco por el que la invariante puede romperse. Por eso la clase condiciona el beneficio: los objetos reducen estados inválidos **solo si sus fronteras son reales**.

## Ejemplo

Una observación en el motor de reglas solo puede registrarse mientras el caso está abierto:

```python
class Caso:
    def __init__(self):
        self._observaciones = []
        self._abierto = True

    def record_observation(self, texto):
        if not self._abierto:
            raise ValueError("el caso está cerrado")
        self._observaciones.append(texto)

    def close(self):
        self._abierto = False

    @property
    def observaciones(self):
        return tuple(self._observaciones)    # copia inmutable
```

Quien use `Caso` no puede registrar en un caso cerrado ni modificar la lista desde fuera. Con un `get_observaciones()` que devolviera la lista interna y un `set_abierto(True)` público, la protección sería solo aparente.

## Errores y confusiones comunes

- **Getters y setters que no validan.** Es acceso directo con otro nombre.
- **Creer que `_atributo` protege.** Es una convención; el lenguaje no lo impide.
- **Devolver colecciones internas.** Permite mutar el estado sin pasar por los métodos.
- **Exponer operaciones técnicas en vez de operaciones del dominio.** Obliga a cada consumidor a conocer el orden correcto de pasos.

## Límites y cuándo no aplica

La protección depende de que las fronteras sean reales (`SE-075`): en un lenguaje sin privacidad aplicada, un consumidor determinado siempre puede saltársela, por lo que sostiene el contrato, no la seguridad. Para estructuras de datos simples sin reglas (un registro de configuración), encapsular cada campo añade código sin proteger nada; un tipo de datos con validación al construirse puede bastar. Y la encapsulación no resuelve invariantes que involucran a varios objetos; eso exige coordinar a nivel de un agregado o de un servicio.
