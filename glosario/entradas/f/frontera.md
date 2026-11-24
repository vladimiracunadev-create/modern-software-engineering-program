# Frontera

[↑ Glosario](../../README.md) · [← Frontend/backend](./frontend-backend.md) · [Frontera de aislamiento →](./frontera-de-aislamiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Una **frontera** es el punto donde cambian la autoridad, la semántica, el rendimiento o la propiedad ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)). El programa usa la palabra en tres lugares:

- **Frontera de análisis** ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)): declara qué elementos de un sistema se modelan con detalle y cuáles se tratan como entorno.
- **Frontera de aislamiento** ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)): hasta dónde un proceso, contenedor o máquina separa lo que ve y comparte con el anfitrión.
- **Valor de frontera** ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)): el valor de entrada donde cambia la clase de comportamiento; allí la comparación (`<` o `<=`) decide.

## Por qué importa

Casi todo error serio vive en una frontera: donde dos autoridades se pasan un dato, donde un umbral cambia el comportamiento, donde se supone un aislamiento que no existe. Trazar la frontera correcta decide qué se analiza, qué se aísla y qué se prueba.

## Cómo funciona

- **Análisis** ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)): se declara qué se modela con detalle y qué es entorno, y se acompaña de interfaces y supuestos, porque el entorno sigue condicionando el resultado. Externalizar pagos cambia quién opera el procesador; no externaliza el deber de informar un cobro incierto, reconciliarlo ni ofrecer reparación. Se necesitan las fronteras para responder preguntas distintas, normalmente entre dos y cuatro: una sola mezcla preguntas incompatibles; ocho producen un mapa que nadie mantiene.
- **Aislamiento** ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)): se enumeran las fronteras y las capacidades efectivas; compartir núcleo, montajes y privilegios debilita la frontera.
- **Valores** ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)): las clases de equivalencia terminan en fronteras, y los errores `<` contra `<=` solo aparecen probando justo en ellas y alrededor.

## Ejemplo

[SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md): la regla «descuento si el pedido es ≥ 100» se prueba con 99, 100 y 101. Una cobertura del 100 % con casos típicos (50 y 500) no rompe si alguien cambia `>=` por `>`; una tabla de fronteras y la medida con mutantes sí lo detecta. Ilustración:

```python
assert descuento(99) == 0 and descuento(100) > 0 and descuento(101) > 0
```

## Errores y confusiones comunes

- **La frontera coincide con el organigrama.** Causa: se modeló autoridad formal, no causalidad; corrección: seguir una solicitud real y mover la frontera según la pregunta ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)).
- **«Está aislado porque está en un contenedor».** Causa: se ignoraron kernel, montajes y privilegios compartidos; corrección: enumerar fronteras y capacidades efectivas ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)).
- **Cobertura del 100 % sin valores de frontera.** Causa: casos típicos únicamente; corrección: tabla de fronteras y medida con mutantes ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md)).

## Límites y cuándo no aplica

Una frontera excesiva tiene el problema opuesto: incorpora toda la universidad, pierde responsables concretos y no permite verificar nada ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md)). Los casos de prueba deben cubrir cada clase de comportamiento y cada frontera, no una cantidad fija. Y los tres sentidos no son intercambiables: una frontera de análisis no aísla nada.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Propiedad](../p/propiedad.md), [Rendimiento](../r/rendimiento.md), [Semántica](../s/semantica.md), [Valor](../v/valor.md), [Anfitrión](../a/anfitrion.md), [Bind mount](../b/bind-mount.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (196 clases más lo mencionan; las que más):

[SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Linux kernel — namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Linux kernel — cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Docker documentation — storage](https://docs.docker.com/engine/storage/) — delimita el contrato técnico que debe cumplirse al distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan.
- [Microsoft Learn — WSL documentation](https://learn.microsoft.com/windows/wsl/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Documentación de unittest](https://docs.python.org/3/library/unittest.html) — organización de pruebas; autoridad: documentación oficial de Python.

---

[↑ Glosario](../../README.md) · [← Frontend/backend](./frontend-backend.md) · [Frontera de aislamiento →](./frontera-de-aislamiento.md)
