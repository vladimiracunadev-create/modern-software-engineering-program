# Encapsulación

[↑ Glosario](../../README.md) · [← Encadenado](./encadenado.md) · [Encapsulación como protección →](./encapsulacion-como-proteccion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Ocultar una decisión detrás de una interfaz, de modo que cambiarla no obligue a cambiar a los clientes.

Definición de trabajo de [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-037 — Modelos OSI y TCP/IP como herramientas de diagnóstico](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md): Adición de información de control alrededor de datos de una capa superior.

## Por qué importa

En [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), el tema «Encapsulación» importa porque lo que un módulo no expone no puede romperse desde fuera.

## Cómo funciona

Según [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), en la sección «Encapsulación»:

Encapsular es esconder una decisión detrás de una interfaz, de modo que cambiar la decisión no obligue a cambiar a los clientes. Un campo público esconde nada; un getter esconde el nombre, pero no el significado (el cliente sigue multiplicando kilos); un método que responde la pregunta que el cliente realmente tiene (`costo_por_peso`) esconde la representación y la unidad. Parnas lo formuló como ocultar la decisión que probablemente cambie.

## Ejemplo

Ejemplo de [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) (sección «Preguntas frecuentes»):

Esconde el nombre del campo, no su significado: los treinta clientes seguían multiplicando kilos. Es mejor que un campo público, y la encapsulación completa llega cuando el módulo responde la pregunta del cliente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)) son:

- **Cambiar una plantilla obliga a releer el cálculo del costo** — causa: una clase mezcla responsabilidades con distinto motivo de cambio. Corrección: separar por decisión y comprobar con LCOM4 y con el cambio previsto.
- **Un cambio de unidad toca decenas de archivos** — causa: los clientes leen el dato y calculan por su cuenta. Corrección: exponer comportamiento en vez de datos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con código de ejemplo y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proyecto real ni se evaluó si las métricas predicen defectos; las clases, los treinta clientes y los grafos son construcciones del autor. La siguiente clase examina los principios que guían estas separaciones y dónde dejan de valer.

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
