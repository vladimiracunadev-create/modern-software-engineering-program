# Integración continua

[↑ Glosario](../../README.md) · [← Instrumento](./instrumento.md) · [Integración frecuente →](./integracion-frecuente.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Práctica de integrar el trabajo de todas las personas en una línea común con frecuencia y verificar automáticamente cada integración.

Definición de trabajo de [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-002 — Historia de la crisis del software a la ingeniería continua](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md): Integrar y verificar cambios con frecuencia.

## Por qué importa

En [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), el tema «Integración continua como práctica» importa porque una herramienta que nadie obedece no integra nada; la práctica define la conducta que la herramienta apoya.

## Cómo funciona

Según [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md):

Integrar significa combinar el trabajo de varias personas en una línea común y comprobar que el resultado funciona. La integración continua conserva esa definición y cambia la frecuencia y la forma: cada persona integra al menos una vez al día en la troncal, cada integración dispara una verificación automática y una verificación en rojo se corrige antes de seguir añadiendo cambios. Fowler enumera las prácticas que la sostienen: un único repositorio de referencia, una construcción automatizada, pruebas que se ejecutan en esa construcción, integraciones frecuentes, construcción de cada integración en una máquina de integración, construcción rápida, un entorno de prueba parecido al de producción, visibilidad del estado y, en su evolución, despliegue automático.

Según [SE-002 — Historia de la crisis del software a la ingeniería continua](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md):

La integración continua reduce el tiempo durante el cual cambios compatibles por separado pueden divergir. Requiere integrar realmente con frecuencia y ejecutar verificaciones útiles: un servidor llamado “CI” que corre una prueba irrelevante una vez por semana no produce el mecanismo. La entrega continua mantiene el producto en estado desplegable; el despliegue continuo además publica cambios que superan el flujo. Ninguno garantiza adopción, valor o recuperación.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md):

El equipo de la API de entregas revisa su historial: las ramas viven nueve días de mediana, el 60 % de las fusiones tiene conflictos y el viernes por la tarde se fusiona todo. Con el modelo de la primera figura estiman que a esa vida casi toda rama choca con algo; con la segunda, que verificar de a diez cambios es razonable porque su tasa de defectos ronda el 4 %.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md)) son:

- **Hay un servidor de integración y la troncal pasa días en rojo** — causa: no hay política de reacción ni dueño. Corrección: escribir quién actúa ante un rojo y en cuánto tiempo; revertir primero.
- **Las fusiones del viernes duran toda la tarde** — causa: ramas largas que se integran en lote. Corrección: acortar ramas, usar banderas para lo inacabado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md)) son: Las definiciones son operativas para la canalización de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Práctica](../p/practica.md), [Trabajo](../t/trabajo.md), [Bisección](../b/biseccion.md), [Cola de integración](../c/cola-de-integracion.md), [Conflicto semántico](../c/conflicto-semantico.md), [Crisis del software](../c/crisis-del-software.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-002 — Historia de la crisis del software a la ingeniería continua](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (98 clases más lo mencionan; las que más):

[SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — prácticas de la integración continua; autoridad: Martin Fowler, texto de referencia del campo.
- [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/) — descripción de las ramas de corta vida y las banderas; autoridad: Paul Hammant, sitio de referencia comunitario.
- [GitHub: gestionar una cola de fusión](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) — funcionamiento de una cola de fusión; autoridad: documentación de GitHub.
- [git bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria del primer cambio defectuoso; autoridad: documentación de git.

---

[↑ Glosario](../../README.md) · [← Instrumento](./instrumento.md) · [Integración frecuente →](./integracion-frecuente.md)
