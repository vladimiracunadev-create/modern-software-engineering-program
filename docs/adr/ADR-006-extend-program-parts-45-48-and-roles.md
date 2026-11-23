# ADR-006 — Ampliar el programa con las Partes 45–48 y tres roles nuevos

> [!NOTE]
> **Documento histórico.** Los identificadores `SE-nnn` y los números de parte de este texto usan la
> numeración vigente cuando se escribió (antes del 2026-11-23). Los enlaces apuntan a la clase migrada. Para
> traducir un identificador, consulta [`ID-MIGRATION.md`](../ID-MIGRATION.md) ([ADR-007](ADR-007-pedagogical-renumbering-and-new-parts.md)).

- Estado: aceptada el 2026-11-17.
- Contexto: tras publicar las Partes 00–44 ([ADR-004](ADR-004-expand-to-540-class-scope.md) y
  [ADR-005](ADR-005-publish-parts-40-44-from-content.md)), una revisión entre las promesas de
  las guías de rol y el contenido publicado encontró dos tipos de brecha:
  1. **Promesas de rol sin contenido propio.** Las guías de Data Engineer, Safety-Critical
     Software Engineer, Embedded & IoT Engineer, Green Software Engineer y Open Source &
     InnerSource Engineer prometen ingeniería de datos como disciplina, normas de seguridad
     funcional (IEC 61508, ISO 26262, DO-178C, IEC 62304), RTOS y planificación de tiempo real,
     software verde y contribución interna. El programa los trata de forma dispersa en las
     Partes 22, 23, 26 y 31, sin una parte que los desarrolle con mecanismos, normas y
     evidencia.
  2. **Temas modernos ausentes.** No existe cobertura de MLOps y ML en producción, ajuste fino
     y GPU, WebAssembly, eBPF, computación cuántica y criptografía poscuántica, confianza
     cero, regulación de IA (EU AI Act, ISO/IEC 42001, NIST AI RMF) ni de CRDT y consenso
     como sistemas operados.
- Decisión:
  1. **Cuatro partes nuevas al final, sin renumerar nada.** Cada una con doce clases
     (diez de núcleo, un taller y un proyecto) y el mismo contrato que las demás:
     - Parte 45 · Ingeniería de datos y plataformas de datos — `SE-541`–`SE-552`.
     - Parte 46 · Machine learning en producción y MLOps — `SE-553`–`SE-564`.
     - Parte 47 · Sistemas críticos, tiempo real y normas de seguridad — `SE-565`–`SE-576`.
     - Parte 48 · Runtimes y plataformas modernas — `SE-577`–`SE-588`.
     El alcance planificado pasa a **49 partes, 588 clases y 2.646 horas**. Los 540 IDs
     existentes no cambian.
  2. **Estado derivado, como en ADR-005.** Las cuatro partes nacen *planificadas*: no tienen
     carpeta en `classes/`, ni página en `site/`, ni enlaces en las guías de rol. Pasan a
     *desarrolladas* cuando existen `content/part-NN/README.md` y los doce
     `SE-NNN.md`. Los contadores («N clases desarrolladas, M planificadas») los calcula
     `scripts/program_state.py`; no hay cifras editadas a mano.
  3. **Tres roles nuevos y actualización de ocho existentes.** Roles nuevos:
     `MLOps / ML Platform Engineer`, `AI Governance & Responsible AI Engineer` y
     `Runtime & Systems Engineer`. Se actualizan con filas de ampliación para las partes
     nuevas Data Engineer, Safety-Critical Software Engineer, Embedded & IoT Engineer,
     Green Software Engineer, Open Source & InnerSource Engineer, Security Engineer,
     AI Systems Engineer y Distributed Systems Engineer (y las demás guías a las que cada
     parte aporta de forma directa). Las guías nuevas siguen el mismo esquema, longitud
     (más de 2.200 palabras), identidad visual y dos gráficos interpretables que las
     existentes.
  4. **Temas transversales dentro de partes y no como partes aparte.** Software verde se
     integra como criterio de costo y operación en las Partes 45, 46 y 48; InnerSource se
     apoya en las Partes 16 y 41 y en el contrato de datos de la 45; CRDT y consenso se
     tratan como ampliación de las Partes 28 y 21 y como caso de contraste en la 45, sin
     parte propia; tolerancia a fallos y seguridad de ML se integran en la 46. Una ampliación
     de clases existentes se hace dentro del número fijo de cada parte, sin renumerar.
- Por qué al final y no intercaladas: insertar partes en el medio obligaría a renumerar
  `SE-NNN`, rutas de `classes/`, enlaces del portal, figuras, fuentes y referencias de
  roles. [ADR-003](ADR-003-reconcile-480-baseline-with-progressive-expansion.md) prohíbe
  renumerar. El orden de lectura recomendado se resuelve con la guía de cada rol y con los
  prerrequisitos de cada clase, no con la numeración.
- Por qué doce clases por parte: es el contrato de la infraestructura (`CLASSES_PER_PART`),
  mantiene una carga comparable y evita cuotas por tema. No es una promesa de que cada tema
  reciba la misma extensión.
- Consecuencias:
  - Los validadores, generadores y pruebas dejan de asumir 45 partes y 540 clases y leen el
    estado de `program_state.py`. «Fin del programa» pasa a significar «última clase
    desarrollada»; cuando se publique `SE-541`, la navegación de `SE-540` se regenera sola.
  - README, ROADMAP, STATUS, portal, catálogo, About de GitHub y `docs/PROGRAM-ARCHITECTURE.md`
    distinguen «540 desarrolladas» de «588 planificadas» y no presentan las partes 45–48
    como disponibles.
  - Cada parte nueva se escribe en su propia sesión con el procedimiento de
    [`../ADDING-A-PART.md`](../ADDING-A-PART.md); las guías de rol enlazan sus clases en
    cuanto la parte existe.
- Fuera de alcance: no se añaden partes entre la 00 y la 44, no se cambia el contrato de
  clase (dieciséis secciones) y no se publica ninguna clase de las Partes 45–48 en este
  commit.
