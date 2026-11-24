# Composición frente a herencia

[↑ Glosario](../../README.md) · [← Composición](./composicion.md) · [Composición y nivel de abstracción →](./composicion-y-nivel-de-abstraccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

**Composición frente a herencia** es el criterio de diseño que [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) formula así: la **herencia** reutiliza un contrato y un comportamiento bajo una relación de **sustitución** (un subtipo puede usarse donde se espera el tipo base), mientras que la **composición** ensambla **colaboradores**: un objeto contiene a otros y les delega trabajo. No dice «nunca heredar»: dice que heredar solo para compartir código es una mala razón, y que la herencia queda reservada para tipos realmente sustituibles.

## Por qué importa

Quien hereda se acopla a la clase base: a sus métodos protegidos, a su orden de inicialización y a cualquier cambio futuro. Una jerarquía profunda hace que modificar la base afecte a todos sus descendientes, y que entender un método obligue a leer varios niveles. La composición mueve esa dependencia a una interfaz estrecha. La decisión que cambia es cómo se reutiliza código: en lugar de «extiendo la clase que ya hace algo parecido», se pregunta «¿es esto realmente un caso del tipo base, o solo quiero usar su código?».

## Cómo funciona

La prueba de herencia es de **sustitución**: si en cualquier lugar que usa el tipo base se puede poner el subtipo sin que cambie lo que el código espera, la herencia expresa una relación verdadera. Si el subtipo debe rechazar operaciones de la base, o cambiarle el significado, no es sustituible y la herencia miente.

La composición, en cambio, permite:

- **Cambiar el colaborador en ejecución** o por configuración (una política distinta, un repositorio distinto), cosa que una jerarquía fija en compilación.
- **Combinar capacidades** sin explosión de subclases: tres comportamientos independientes son tres colaboradores, no ocho subclases.
- **Probar por separado**, sustituyendo cada colaborador por un doble.

El motor de reglas comparado de [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) hace esto: **compone políticas y repositorios** y reserva la herencia para tipos sustituibles. Un coste de la herencia múltiple, que [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) ilustra, es el orden de resolución: llamar `A.m(self)` en lugar de `super().m()` ejecuta un método de la base dos veces o nunca en un diamante.

## Ejemplo

Se necesita que un servicio de recomendación aplique una política y guarde resultados. Con herencia, se crea `ServicioConPoliticaYRepositorio` extendiendo clases que ya hacen partes de esto. Con composición:

```python
class Servicio:
    def __init__(self, politica, repositorio):
        self.politica = politica
        self.repositorio = repositorio

    def recomendar(self, caso):
        r = self.politica.evaluar(caso)
        self.repositorio.guardar(caso, r)
        return r
```

Cambiar la política o el repositorio no toca `Servicio`. La herencia sigue siendo válida para algo como `ReglaPorUmbral(Regla)` si cualquier `Regla` se puede sustituir por ella sin sorpresas.

## Errores y confusiones comunes

- **Heredar para ahorrar líneas.** Crea acoplamiento a detalles internos de la base y jerarquías frágiles.
- **Creer que composición es «no usar clases base».** Las interfaces o clases abstractas pueden seguir existiendo; lo que cambia es que la reutilización ocurre por delegación.
- **`A.m(self)` en lugar de `super().m()`.** En herencia múltiple, el método de la base se ejecuta dos veces o nunca; hay que usar `super()` en todas las clases del diamante ([SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md)).
- **Confiar en la privacidad por convención.** Un atributo con guion bajo no impide asignarle un valor inválido; hay que validar en el método que escribe o usar una propiedad con setter.

## Límites y cuándo no aplica

Los objetos reducen estados inválidos solo si sus fronteras son reales ([SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md)). La composición no es gratuita: añade indirección y a veces obliga a escribir métodos que solo delegan. Cuando la relación es genuinamente «es un» con sustitución completa y estable, la herencia es más simple y legítima. En lenguajes con interfaces o rasgos, parte de la discusión se resuelve distinto, y en el estilo funcional, la reutilización se hace componiendo funciones y no objetos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Composición](./composicion.md), [Contrato](./contrato.md), [Herencia](../h/herencia.md), [Relación](../r/relacion.md), [Encapsulación como protección](../e/encapsulacion-como-proteccion.md), [Mensajes y despacho](../m/mensajes-y-despacho.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Composición](./composicion.md) · [Composición y nivel de abstracción →](./composicion-y-nivel-de-abstraccion.md)
