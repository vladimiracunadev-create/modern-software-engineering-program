# Frontera

[↑ Glosario](../../README.md) · [← Frontend/backend](./frontend-backend.md) · [Frontera de aislamiento →](./frontera-de-aislamiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Punto donde cambian autoridad, semántica, rendimiento o propiedad.

Definición de trabajo de [SE-034 — Virtualización, WSL y aislamiento local](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-422 — Pruebas unitarias y diseño testable](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md): Valor de entrada donde cambia la clase de comportamiento; allí la comparación (`<` o `<=`) decide.

## Por qué importa

En [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), el tema «Frontera» importa porque decide qué se modela y quién responde

## Cómo funciona

Según [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md):

Una **frontera de análisis** declara qué elementos se modelan con detalle y cuáles se tratan como entorno. Es útil cuando permite explicar la capacidad sin volver el modelo inmanejable. Debe acompañarse de interfaces y supuestos, porque el entorno sigue condicionando el resultado. Externalizar pagos cambia quién opera el procesador; no externaliza el deber de informar un cobro incierto, reconciliarlo ni ofrecer reparación.

Según [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md):

Las necesarias para responder preguntas distintas, normalmente entre dos y cuatro. Una sola frontera obliga a mezclar preguntas incompatibles; ocho producen un mapa que nadie mantiene. Un criterio práctico: si dos fronteras darían las mismas respuestas y las mismas responsabilidades, sobra una.

## Ejemplo

Ejemplo de [SE-001 — Software, sistemas y productos: fronteras de la disciplina](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) (sección «Ejemplo mínimo»):

Una calculadora tributaria contiene software. El sistema relevante incluye reglas, datos introducidos, navegador y persona que interpreta el resultado. Si el producto promete una declaración correcta, debe gestionar vigencia normativa y casos no cubiertos. El mismo código, con otra frontera, cambia de responsabilidad.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **la frontera coincide exactamente con el organigrama** — causa: se modeló autoridad formal, no causalidad. Corrección: sigue una solicitud real y mueve la frontera según la pregunta que necesitas responder. ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md))
- **“Está aislado porque está en un contenedor”** — causa: se ignoraron kernel, montajes y privilegios compartidos. Corrección: enumerar fronteras y capacidades efectivas. ([SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md))
- **La cobertura es 100 % y un cambio de operador no rompe ninguna prueba** — causa: casos típicos sin valores en las fronteras. Corrección: tabla de fronteras y medida con mutantes. ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una frontera excesiva tiene el problema opuesto: incorpora toda la universidad, pierde responsables concretos y no permite verificar nada. ([SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md))
- Los que cubran cada clase de comportamiento y cada frontera, no una cantidad fija. ([SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md))

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
