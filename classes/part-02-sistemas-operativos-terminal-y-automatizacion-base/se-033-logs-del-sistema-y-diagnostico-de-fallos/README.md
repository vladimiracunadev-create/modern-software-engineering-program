# SE-033 — Logs del sistema y diagnóstico de fallos

[← SE-032](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) · [↑ Parte 02](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-034 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.

**Por qué aparece aquí.** Se sitúa después de **Instalación de software y gestores de paquetes del sistema** y antes de **Virtualización, WSL y aislamiento local**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Buscar una cadena y declarar causa sin línea temporal ni evidencia rival.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Incident-timeline.md con evento, fuente, reloj, hipótesis y dato ausente. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Los logs pueden omitir, retrasar o redactar hechos.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Microsoft Learn — Event Logging](https://learn.microsoft.com/windows/win32/eventlog/event-logging) | documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [systemd — journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) | define ciclo de vida, supervisión o consulta de eventos en systemd | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Apple Developer — Logging](https://developer.apple.com/documentation/os/logging) | delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [OpenTelemetry — Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) | delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Cuando el analizador local de eventos falla, un archivo de log puede contener miles de líneas y aun no responder qué ocurrió. Registrar más no equivale a observar mejor. El kit de diagnóstico multiplataforma necesita relacionar evento, contexto y resultado sin capturar secretos ni convertir una coincidencia temporal en causa.

### Resultado de aprendizaje

Al terminar podrás diseñar eventos útiles, correlacionar evidencia de varias fuentes y producir un paquete diagnóstico minimizado que separa hechos, inferencias y acciones.

## Prerrequisitos

`SE-031` para redacción, `SE-028` para ciclo de proceso y una ejecución local del analizador local de eventos/el kit de diagnóstico multiplataforma. Usa únicamente eventos sintéticos o propios.

## Problema auténtico

El analizador local de eventos falla y existen miles de líneas de log. No hay identificador de operación, los relojes difieren y una ruta personal aparece junto a un token. El volumen aumentó; la capacidad de explicar disminuyó.

## Objetivos observables

Podrás diseñar eventos estructurados; distinguir logs, métricas y trazas; correlacionar con incertidumbre temporal; separar hecho e inferencia; y exportar evidencia minimizada sin el secreto centinela.

## Temas y por qué importan

| Tema | Mecanismo | Decisión habilitada |
| --- | --- | --- |
| Evento estructurado | conserva código, tiempo, componente y campos | consultar sin parsear frases |
| Correlación | relaciona señales de una operación | reconstruir una línea temporal |
| Tiempo | separa marca de pared y duración monótona | evitar órdenes y duraciones falsas |
| Minimización | selecciona y redacta antes de persistir | compartir evidencia con menor riesgo |
## Mapa conceptual

```mermaid
flowchart LR
 O[Operación] --> L[Logs estructurados]
 O --> M[Métricas]
 O --> X[Estado y stderr]
 C[Contexto de plataforma] --> T[Línea temporal]
 L --> T
 M --> T
 X --> T
 T --> H[Hipótesis rivales]
 H --> P[Prueba discriminante]
```

Las señales convergen en una hipótesis, no en una certeza automática. La prueba siguiente debe poder cambiar la conclusión.

## Conceptos y decisiones

### Observabilidad permite inferir estado desde salidas

Un sistema es más observable cuando sus señales permiten responder preguntas sobre su comportamiento. Logs describen eventos; métricas agregan medidas; trazas relacionan pasos de una operación. En un diagnóstico local también importan códigos de salida, configuración efectiva, versión y estado del sistema.

Ninguna señal aislada es verdad completa. Un log registra lo que el programa alcanzó a emitir; un cierre abrupto puede dejar eventos pendientes.

### Un evento útil tiene estructura y propósito

Un registro profesional incluye tiempo con zona o referencia inequívoca, severidad, componente, evento estable, correlación y campos relevantes. El mensaje humano complementa, no sustituye, la estructura.

```mermaid
flowchart LR
    O[Operación del analizador local de eventos] --> A[Eventos de aplicación]
    O --> M[Métricas locales]
    O --> X[Código y stderr]
    S[Contexto del sistema] --> C[Correlación temporal]
    A --> C
    M --> C
    X --> C
    C --> H[Hipótesis contrastables]
    H --> P[Prueba mínima siguiente]
```

La correlación aproxima relaciones; no demuestra causalidad por sí sola. Un identificador de operación une eventos mejor que buscar textos parecidos.

### Severidad representa impacto operativo, no emoción

`DEBUG`, `INFO`, `WARN` y `ERROR` solo son útiles si el equipo define cuándo aplican. Un error recuperado puede ser advertencia para la operación global; una precondición ausente puede ser error sin excepción interna. Todo marcado como error crea fatiga y oculta señales.

El kit de diagnóstico multiplataforma conserva un evento estable como `config.read.denied` y una explicación localizada. Las automatizaciones dependen del código, no de frases traducidas.

### Tiempo y orden exigen cautela

Relojes pueden diferir, cambiar o tener distinta precisión. El tiempo de pared sirve para ubicar un evento; un reloj monótono es mejor para duraciones dentro de un proceso. En concurrencia, el orden de escritura no necesariamente reproduce el orden causal.

El kit de diagnóstico multiplataforma registra inicio, fin y duración con mecanismo apropiado, además de zona para marcas compartidas. Si combina fuentes, declara la incertidumbre de sincronización.

### La captura debe minimizar datos sensibles

Logs pueden revelar rutas personales, argumentos, nombres de usuario, tokens o contenido. La política define campos permitidos, redacción, retención, acceso y eliminación. Recolectar todo “por si acaso” aumenta riesgo y ruido.

La redacción debe ocurrir antes de serializar. Los valores secretos centinela de SE-031 vuelven a usarse para probar que no aparecen en eventos ni archivos comprimidos.

### Diagnosticar es iterar hipótesis, no buscar una línea roja

El flujo profesional define el síntoma, construye una línea temporal, formula causas alternativas y elige una prueba que las distinga. La bitácora conserva resultados negativos porque reducen el espacio de búsqueda.

Los sistemas ofrecen almacenes diferentes: Windows Event Log, journal de `systemd`, Unified Logging de Apple y archivos de aplicación. Sus filtros y permisos no son equivalentes. Se consulta documentación oficial como [Windows Event Log](https://learn.microsoft.com/windows/win32/eventlog/event-logging), [`journalctl`](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) y [Apple Unified Logging](https://developer.apple.com/documentation/os/logging).

### Anatomía de un evento: estructura sobre texto libre

Un buen registro tiene campos. Tres eventos reales del registro *Application* de Windows (leídos con `Get-WinEvent`, sin privilegios de administrador) muestran los cuatro campos mínimos: la hora de creación, un identificador numérico (8224, 8302), un nivel
(«Información») y el proveedor que lo emitió («VSS», «Microsoft-Windows-System-Restore»). El registro es *circular*: cuando se llena, los eventos más antiguos se sobrescriben, por lo que la evidencia de un incidente se exporta antes de que se pierda.
En Linux con `systemd`, `journalctl` entrega campos parecidos con otra forma: una marca de tiempo ISO 8601 con desfase, el nombre del equipo, la unidad y el mensaje.

![Figura 1. Tabla con tres eventos reales del registro Application de Windows y sus campos: hora, identificador, nivel y proveedor](../../../content/part-02/figures/se-033-anatomia-de-un-evento.svg)

**Cómo leer la figura.** Cada fila es un evento y cada columna, un campo. El identificador y el proveedor permiten buscar y agrupar sin leer el mensaje; el nivel prioriza. **Dónde deja de valer:** los identificadores son específicos de cada proveedor (el 8224 de VSS no
significa nada para otro proveedor), y el texto del mensaje depende del idioma del sistema; un análisis automático se apoya en proveedor e identificador, no en el texto. El ejemplo no contiene datos personales: los nombres del equipo se omiten.

### Tiempo y orden: el mismo instante en dos escrituras

Ordenar eventos exige un tiempo comparable. Una entrada del journal con la marca `2026-11-13T11:38:54-03:00` y la salida de `date -u` en ese momento, `2026-11-13T14:38:54Z`, son *el mismo instante* (11 h con desfase de -3 equivalen a 14 h en UTC). Sin el desfase explícito, dos registros de
equipos en zonas horarias distintas no se pueden ordenar. Hay además dos relojes: el *reloj de pared* (`time.time()`) puede ajustarse hacia atrás o adelante (por sincronización o cambio de hora), y un reloj *monotónico* (`time.monotonic()`) solo avanza; para medir duraciones se usa el segundo. En una prueba de 0,2 s, ambos
midieron 0,203 s porque no hubo ajuste: la diferencia aparece cuando lo hay.

![Figura 2. Una misma hora escrita en local con desfase y en UTC, y la distinción entre reloj de pared y reloj monotónico](../../../content/part-02/figures/se-033-hora-local-y-utc.svg)

**Cómo leer la figura.** Las dos cajas superiores son la misma hora; las inferiores recuerdan que el reloj de pared no es una base fiable para medir duraciones y que el orden de llegada de las líneas no es el orden de ocurrencia. **Dónde deja de valer:** aun con UTC,
los relojes de equipos distintos pueden tener un desfase de milisegundos a segundos; para ordenar eventos entre sistemas se declara la fuente de sincronización y la tolerancia, y se usan identificadores de correlación.

### Registros estructurados y correlación

Un registro estructurado emite una línea por evento con campos fijos, normalmente JSON. Con un formateador de `logging` de pocas líneas, la salida es, por ejemplo, `{"ts": "2026-11-13T14:46:09Z", "nivel": "ERROR", "evento": "integridad invalida", "cid": "a1"}`: una marca de tiempo en
UTC, un nivel, un evento con nombre estable y un *identificador de correlación* (`cid`) que une todas las líneas de una misma operación. Con eso, reconstruir una línea temporal es filtrar por `cid` y ordenar por `ts`, en vez de leer texto libre. El diseño del evento incluye qué *no* se registra: no
datos personales ni secretos, y no más detalle del necesario.

### Diagnosticar es iterar hipótesis

El caso de la Figura 3 muestra el método con un fallo común de servicios: `systemd` registra `Main process exited, code=exited, status=200/CHDIR`, un código que, según su documentación, indica que no se pudo cambiar al directorio de trabajo configurado. La lectura precisa excluye las hipótesis sobre el
programa (ni siquiera llegó a ejecutarse) y señala la configuración (`WorkingDirectory`). Se comprueba la ruta con `ls -ld` y `namei -l`, se corrige y se verifica que el servicio queda activo. El ejemplo es genérico: omite deliberadamente el nombre de la unidad y de la ruta.

![Figura 3. Cuatro pasos de diagnóstico para un servicio que falla con 200/CHDIR: observar, formular hipótesis, probar y corregir](../../../content/part-02/figures/se-033-diagnostico-por-hipotesis.svg)

**Cómo leer la figura.** Los cuatro pasos son un bucle: si la verificación falla, la nueva evidencia reformula las hipótesis. **Dónde deja de valer:** la «línea roja» más visible no siempre es la causa; a menudo es una consecuencia (un reintento fallido tras el primer error). Se busca el *primer* evento anómalo y se
comprueba que la corrección cambia el resultado, para no confundir correlación con causa.

## Definiciones de trabajo

- **evento:** observación estructurada con significado estable;
- **correlación:** relación explícita entre señales de una operación;
- **hecho:** observación respaldada por una fuente identificable;
- **inferencia:** explicación compatible con hechos, aún contrastable;
- **paquete diagnóstico:** evidencia seleccionada, contextualizada y minimizada para revisión.

## Caso conductor: el kit de diagnóstico multiplataforma construye una línea temporal

El analizador local de eventos devuelve código `3`: configuración ausente. El kit de diagnóstico multiplataforma recoge versión, configuración efectiva redactada, metadatos de la ruta y eventos con el mismo identificador. Descubre que la ruta provino de una variable heredada, no del archivo esperado. Esa relación ya está explicada por la precedencia de SE-031.

El informe separa:

- **hechos:** variable presente, ruta resuelta, archivo ausente, código 3;
- **inferencia:** la variable probablemente desvió la búsqueda;
- **prueba:** ejecutar en un entorno mínimo sin esa variable;
- **resultado:** el analizador local de eventos usa el archivo correcto;
- **corrección:** eliminar la configuración obsoleta en su ámbito, no codificar otra ruta.

## Práctica guiada

1. Instrumenta tres etapas del kit de diagnóstico multiplataforma con eventos estructurados y correlación.
2. Induce dos fallos que compartan un síntoma superficial.
3. Construye una línea temporal con hechos y fuentes.
4. Formula una prueba que discrimine las causas.
5. Exporta solo la evidencia necesaria y busca el secreto centinela.
6. Pide a otra persona reconstruir tu conclusión desde el paquete.

## Ejemplo mínimo

Dos eventos comparten `operation_id=abc`: inicio y `config.read.denied`. Ordenarlos por tiempo y código permite afirmar que pertenecen a la operación; no demuestra todavía que la ACL sea la causa.

## Ejemplo profesional

Un servicio presenta latencia y errores coincidentes con presión de disco. El equipo compara operaciones con y sin presión y conserva una hipótesis rival de dependencia externa. La correlación orienta el experimento; no se publica como causalidad cerrada.

## Ejercicios

1. Convierte tres mensajes libres en eventos con código estable y campos mínimos.
2. Distingue hechos e inferencias en una línea temporal dada.
3. Diseña una política de severidad, retención y redacción para el kit de diagnóstico multiplataforma.

## Reto verificable

Entrega un paquete con dos causas superficiales iguales pero evidencia discriminante. Otra persona debe identificar la causa correcta y no encontrar el secreto centinela.

## Preguntas frecuentes

### ¿Más detalle de log siempre ayuda?

No. Puede aumentar ruido, costo y exposición. Cada campo debe responder una pregunta operacional.

### ¿El evento inmediatamente anterior causó el fallo?

No necesariamente. Proximidad temporal es evidencia para explorar, no prueba causal.

### ¿Más detalle de registro siempre ayuda?

No. Más volumen aumenta el costo, ahoga la señal y arriesga datos sensibles. Se registra lo que permite responder preguntas concretas (qué ocurrió, a quién, cuándo, con qué resultado) y se ajusta el nivel de detalle por componente y por situación.

### ¿El evento inmediatamente anterior a un fallo lo causó?

No necesariamente. Puede ser una consecuencia, una coincidencia o un síntoma de la misma causa previa. La correlación temporal es una pista; la causa se establece con una hipótesis y una prueba que podría refutarla.

### ¿Cómo comparto un registro sin exponer datos personales?

Con una copia minimizada: se recortan los campos necesarios, se sustituyen identificadores por seudónimos estables y se revisa a mano antes de compartir. Los nombres de equipo, usuarios, rutas personales y direcciones no suelen ser necesarios para diagnosticar.
## Fallo controlado y diagnóstico

Emite eventos sin correlación para dos ejecuciones simultáneas y demuestra la ambigüedad. Añade un identificador por operación, repite y documenta qué preguntas ahora sí pueden responderse.


Una segunda práctica construye una línea temporal con registros estructurados. Escribe un programa que emita tres eventos con el mismo `cid` (inicio, advertencia, error) como líneas JSON, y otro `cid` interleaved con otra operación. **Síntoma:** al leer el archivo en
orden de llegada, las operaciones se mezclan. **Causa:** el orden de llegada no es el orden de las operaciones. **Corrección:** filtrar por `cid` y ordenar por `ts`; añade un test que verifique que cada `cid` reconstruye su secuencia. Convierte después una marca local con desfase
a UTC con `datetime` y comprueba que dos escrituras del mismo instante coinciden.
## Errores comunes y cómo corregirlos

| Síntoma | Causa conceptual | Corrección |
|---|---|---|
| Hay mucho log pero no se relacionan eventos | Faltan identificadores y estructura | Añadir eventos estables y correlación por operación |
| Se culpa al evento anterior | Se confundió proximidad con causalidad | Formular alternativas y diseñar una prueba discriminante |
| Un archivo compartido expone rutas y tokens | Se recolectó sin política | Minimizar, redactar antes de escribir y revisar el paquete final |
| Duraciones negativas o extrañas | Se usó reloj de pared para medir intervalos | Usar reloj monótono para duración |
| El diagnóstico depende de buscar texto traducido | No hay códigos estables | Separar identificador estructurado y mensaje humano |

## Entorno y archivos clave

Trata el JSON de `inspect` del [laboratorio compartido](https://github.com/vladimiracunadev-create/modern-software-engineering-program/tree/main/labs/part-02-cross-platform-diagnostic-kit) como evento estructurado: correlaciona ejecución sana y configuración corrupta, conserva la primera divergencia y comprueba redacción antes de compartir.

`work/SE-033/events.jsonl`, `timeline.md`, `diagnostic-package/` y política de redacción. El paquete usa datos ficticios y tamaño limitado.

## Seguridad, ética y accesibilidad

Recoge solo señales autorizadas y propias. Redacta antes de escribir, define retención y acompaña gráficos o severidades con texto y códigos estables.

## Puente hacia el trabajo con agentes

Un agente que ejecuta herramientas produce una traza, y su calidad determina si se puede depurar. Los principios de esta clase se aplican directamente: eventos estructurados con nombre estable, marca de tiempo en UTC, un identificador de correlación por tarea y por llamada a una
herramienta, y niveles que distingan la decisión del agente del resultado de la herramienta. Esa traza es la evidencia que permite reconstruir *por qué* el agente hizo algo y detectar un bucle o una acción no autorizada. Además, el registro debe omitir secretos y datos personales, incluidas las entradas del
usuario que no hagan falta. Las partes de observabilidad, evaluación y auditoría de agentes retoman estos formatos con OpenTelemetry y registros de auditoría.

## Transferencia

Aplica la bitácora a una investigación de fallo de red sin inspeccionar contenido personal. Indica qué nueva señal solicitarías y con qué autoridad.

## Evaluación y evidencia

Se exige esquema de evento, línea temporal, dos hipótesis, prueba discriminante, redacción comprobada y límite temporal. Buscar una palabra “error” no constituye diagnóstico.

## Criterio de cierre

Puedes producir una línea temporal reproducible, distinguir hecho de inferencia, y entregar evidencia suficiente para contrastar una hipótesis sin revelar el secreto centinela.

## Límites y siguiente paso

No implementamos una plataforma distribuida de observabilidad ni demostramos causalidad completa. En entornos virtualizados o WSL, una señal puede provenir de otra capa. La siguiente clase delimita qué está aislado y qué sigue compartido.

## Fuentes


- [Microsoft Learn — Event Logging](https://learn.microsoft.com/windows/win32/eventlog/event-logging) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd — journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Apple Developer — Logging](https://developer.apple.com/documentation/os/logging) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.
- [OpenTelemetry — Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.

- [journalctl(1)](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) y [systemd.exec(5)](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html): campos del journal y códigos de salida de servicios como `200/CHDIR`.
- [Get-WinEvent (PowerShell)](https://learn.microsoft.com/powershell/module/microsoft.powershell.diagnostics/get-winevent) y [Python `logging`](https://docs.python.org/3/library/logging.html): lectura de registros de Windows y registros estructurados en Python.
- [RFC 3339, Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339): perfil de ISO 8601 con desfase o `Z` usado para ordenar eventos.
## Glosario

- **Correlación:** atributo que permite relacionar señales de una misma operación.
- **Evento:** registro estructurado de algo observado en un momento.
- **Métrica:** medida numérica agregable a lo largo del tiempo.
- **Observabilidad:** capacidad de inferir estado interno a partir de salidas disponibles.
- **Traza:** representación del recorrido de una operación por etapas relacionadas.

---
[← SE-032](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md) · [↑ Parte 02](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-034 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md)
