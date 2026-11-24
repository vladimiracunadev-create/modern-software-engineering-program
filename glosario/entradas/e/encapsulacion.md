# Encapsulación

[↑ Glosario](../../README.md) · [← Encadenado](./encadenado.md) · [Encapsulación como protección →](./encapsulacion-como-proteccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

**Encapsular**, en diseño ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)), es esconder una decisión detrás de una interfaz de modo que cambiarla no obligue a cambiar a los clientes. Parnas lo formuló como ocultar la decisión que probablemente cambie. En redes, [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) usa la misma palabra con otro sentido: añadir información de control (cabeceras) alrededor de los datos de una capa superior. Son usos distintos; esta entrada trata el de diseño y señala el de redes al final.

## Por qué importa

Cada decisión visible es un compromiso con todos los clientes. Una representación expuesta se convierte en parte del contrato, y cambiarla obliga a tocar a todos. Encapsular reduce el número de lugares que hay que editar cuando algo cambia, que es la pregunta práctica con la que [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) mide el acoplamiento.

## Cómo funciona

[SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) distingue niveles de ocultación:

- un **campo público** no esconde nada;
- un *getter* esconde el nombre pero no el significado: el cliente sigue multiplicando kilos;
- un método que responde la pregunta que el cliente realmente tiene (`costo_por_peso`) esconde la representación y la unidad.

La causa de que funcione es que el cliente depende de una promesa («costo por peso») y no de un detalle («el peso se guarda en kilos como `float`»). La decisión escondida puede cambiar sin tocar a los clientes. La clase propone comprobarlo contra un cambio previsto y con medidas como LCOM4 para detectar clases que mezclan responsabilidades con distinto motivo de cambio.

## Ejemplo

En [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), un cambio de unidad del peso toca decenas de archivos porque los clientes leen el dato y calculan por su cuenta. Con encapsulación:

```python
class Precio:
    def costo_por_peso(self, tarifa): return self._kilos * tarifa
```

La unidad queda dentro; un cambio a libras es local.

## Errores y confusiones comunes

- **Cambiar una plantilla obliga a releer el cálculo del costo.** Causa: una clase mezcla responsabilidades con distinto motivo de cambio; corrección: separar por decisión y comprobar con LCOM4 y con el cambio previsto ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).
- **Un cambio de unidad toca decenas de archivos.** Causa: los clientes leen el dato y calculan por su cuenta; corrección: exponer comportamiento en vez de datos ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).
- **Creer que `private` más getters basta.** Esconde el nombre, no la decisión.

## Límites y cuándo no aplica

Encapsular todo añade indirección sin beneficio: solo vale esconder lo que probablemente cambie. Las medidas de [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) se calcularon sobre código de ejemplo y datos sintéticos; no se midió ningún proyecto real ni se evaluó si predicen defectos. Y el sentido de [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) (cabeceras de protocolo) no es el principio de ocultación de información.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Control](../c/control.md), [Interfaz](../i/interfaz.md), [Acoplamiento](../a/acoplamiento.md), [Alcance](../a/alcance.md), [Ciclo de dependencias](../c/ciclo-de-dependencias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — descomposición por decisiones ocultas; autoridad: Communications of the ACM.
- [Stevens, Myers y Constantine, «Structured design» (IBM Systems Journal, 1974)](https://doi.org/10.1147/sj.132.0115) — cohesión y acoplamiento; autoridad: IBM Systems Journal.
- [Chidamber y Kemerer, «A metrics suite for object oriented design» (IEEE TSE, 1994)](https://doi.org/10.1109/32.295895) — métricas de cohesión y acoplamiento; autoridad: IEEE Transactions on Software Engineering.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis del árbol sintáctico usado para medir; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Encadenado](./encadenado.md) · [Encapsulación como protección →](./encapsulacion-como-proteccion.md)
