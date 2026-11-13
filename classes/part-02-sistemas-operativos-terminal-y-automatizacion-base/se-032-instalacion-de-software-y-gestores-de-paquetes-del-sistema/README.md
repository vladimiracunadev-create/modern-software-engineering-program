# SE-032 — Instalación de software y gestores de paquetes del sistema

[← SE-031](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) · [↑ Parte 02](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-033 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.

**Por qué aparece aquí.** Se sitúa después de **Variables de entorno, configuración y secretos** y antes de **Logs del sistema y diagnóstico de fallos**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Mezclar gestores o ejecutar instalaciones sin plan de reversión.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Software-inventory.md con origen, versión, checksum o firma, alcance y rollback. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** La presencia de firma no prueba ausencia de vulnerabilidades.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Microsoft Learn — WinGet](https://learn.microsoft.com/windows/package-manager/winget/) | documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Debian Administrator's Handbook — APT](https://www.debian.org/doc/manuals/debian-handbook/apt.en.html) | delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Homebrew Documentation](https://docs.brew.sh/) | delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Python Packaging User Guide](https://packaging.python.org/en/latest/) | define la semántica y los límites de la API de Python utilizada en el experimento | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

El kit de diagnóstico multiplataforma necesita herramientas auxiliares. “Instala la última versión” parece sencillo hasta que aparecen varios gestores, repositorios, ámbitos y rutas. Instalar modifica estado y añade confianza en publicadores y mecanismos de actualización. La pregunta profesional no es solo cómo instalar, sino qué se instala, desde dónde, para quién y cómo se revierte.

### Resultado de aprendizaje

Al terminar podrás evaluar una instalación por identidad, procedencia, integridad, alcance, resolución de dependencias y camino de desinstalación.

## Prerrequisitos

`SE-031`, un entorno desechable o modo de simulación y permiso explícito para cualquier instalación real. La práctica puede completarse solo con inspección documental si no existe un entorno seguro.

## Problema auténtico

El kit de diagnóstico multiplataforma requiere una herramienta y una guía recomienda “instala el paquete del mismo nombre”. Existen homónimos en varios registros, el comando solicita elevación y ejecuta scripts. La instrucción omite identidad, origen, alcance y reversión.

## Objetivos observables

Podrás describir paquete y grafo de dependencias; verificar procedencia disponible; elegir alcance; revisar un plan antes de aplicar; y demostrar qué revierte y qué permanece tras desinstalar.

## Temas y por qué importan

| Tema | Mecanismo | Decisión habilitada |
| --- | --- | --- |
| Identidad de paquete | combina nombre, ecosistema, origen y versión | evitar homónimos y confusión |
| Resolución | satisface restricciones de un grafo | anticipar cambios transitivos |
| Procedencia | relaciona artefacto con publicador y canal | fundamentar confianza disponible |
| Reversibilidad | inventaría efectos y estado | recuperar sin fingir limpieza total |
## Mapa conceptual

```mermaid
flowchart LR
 M[Manifiesto] --> G[Grafo de dependencias]
 R[Repositorio y publicador] --> G
 G --> P[Plan resuelto]
 P --> V[Verificar origen e integridad]
 V --> A[Aplicar en alcance mínimo]
 A --> T[Probar]
 T --> U[Actualizar, retirar o revertir]
```

La verificación ocurre antes del cambio y la reversión se diseña antes de necesitarla. Un lockfile fija resoluciones, pero no convierte el origen en confiable.

## Conceptos y decisiones

### Un paquete combina artefactos, metadatos y relaciones

Un gestor no descarga únicamente un ejecutable. Interpreta nombre, versión, arquitectura, dependencias, conflictos, scripts y fuente. Luego resuelve un conjunto compatible e instala bajo reglas de alcance. La identidad debe incluir ecosistema y origen; el mismo nombre en otro registro puede no representar el mismo proyecto.

El kit de diagnóstico multiplataforma inventaría cada dependencia con gestor, repositorio, versión solicitada y resuelta, arquitectura, alcance y método de actualización.

### Resolver dependencias es satisfacer restricciones globales

Cada paquete expresa rangos y relaciones. El gestor busca una solución conjunta; actualizar uno puede cambiar otros. Un archivo de bloqueo conserva resoluciones para reproducibilidad, pero no garantiza disponibilidad futura, ausencia de vulnerabilidades ni equivalencia entre plataformas.

```mermaid
flowchart LR
    M[Manifiesto y restricciones] --> R[Resolver grafo]
    I[Índices firmados o metadatos] --> R
    R --> L[Bloqueo o plan]
    L --> V[Verificar procedencia e integridad]
    V --> A[Aplicar en alcance elegido]
    A --> T[Probar]
    T --> U[Actualizar o revertir]
```

Guardar el plan antes de aplicar permite revisar cambios inesperados.

### Procedencia responde quién publicó y por qué confiamos

TLS protege el transporte en cierto tramo, no prueba por sí solo que el paquete sea el esperado. Firmas, hashes, repositorios configurados, identidades de publicador y metadatos verificables aportan señales distintas. Un hash copiado del mismo sitio comprometido tiene un modelo de confianza limitado.

Se prefiere documentación oficial del proyecto y del gestor. Ejecutar directamente un script remoto canalizado al shell reduce la oportunidad de inspección, fijación y auditoría.

### Alcance determina a quién y qué afecta

Una instalación puede ser del sistema, usuario, proyecto o entorno aislado. El alcance global simplifica descubrimiento pero aumenta conflictos y autoridad requerida. Un entorno por proyecto mejora reproducibilidad, aunque consume espacio y aún depende del runtime base.

El kit de diagnóstico multiplataforma prefiere dependencias del proyecto o herramientas ya provistas por el sistema. No eleva privilegios para evitar comprender una ruta.

### Instalar es confiar: scripts de mantenedor, sdist y wheel

Ganchos previos/posteriores y compilación nativa pueden ejecutarse durante la instalación. Revisar el nombre del paquete no basta. En automatización se limita origen, permisos, acceso de red y se conserva log. Para software sensible pueden requerirse artefactos preconstruidos, verificación adicional o entorno aislado.

### Reversibilidad se diseña antes del cambio

Desinstalar un paquete no siempre revierte configuración, servicios, datos o variables. Antes de aplicar se captura estado relevante, se usa modo de simulación cuando existe y se define qué conservar. Un rollback de paquete puede ser incompatible con datos migrados.

Los gestores oficiales —[WinGet](https://learn.microsoft.com/windows/package-manager/winget/), [APT](https://www.debian.org/doc/manuals/debian-handbook/apt.en.html) y [Homebrew](https://docs.brew.sh/)— tienen modelos diferentes. El kit de diagnóstico multiplataforma documenta adaptadores; no presenta comandos como intercambiables.

### Un paquete visto desde el gestor del sistema

Un gestor de paquetes es una base de datos de versiones, relaciones y sumas de verificación. En el Ubuntu 24.04 de prueba, `dpkg -s coreutils` informó el paquete `coreutils`, arquitectura `amd64`, mantenedor «Ubuntu Developers» y versión
`9.4-3ubuntu6`; `apt-cache policy coreutils` mostró que la *versión candidata* era `9.4-3ubuntu6.3`, publicada en `noble-updates`: hay una actualización, y «instalado» no es lo mismo que «el más reciente». `apt-cache depends` listó dependencias previas
(`libacl1`, `libattr1`, `libc6`, `libgmp10`, `libselinux1`) que deben estar presentes antes de instalar. Y `dpkg --verify coreutils` terminó sin salida y con código 0: los archivos instalados coinciden con las sumas de verificación registradas.
El sistema tenía 663 paquetes instalados según `dpkg -l`, y el Python de Windows, unos 350 paquetes de `pip`: cada gestor conoce solo lo suyo.

![Figura 1. Tabla con campos reales de dpkg y apt para el paquete coreutils: versión, candidata, dependencias previas y verificación](../../../content/part-02/figures/se-032-paquete-observado.svg)

**Cómo leer la figura.** Cada fila es una pregunta que el gestor puede responder con evidencia: quién empaqueta, qué versión y arquitectura, si hay una actualización, qué debe existir antes y si los archivos están íntegros. **Dónde deja de valer:** la
verificación con sumas de verificación detecta cambios *accidentales o locales*, pero un atacante con privilegios puede alterar también la base de datos; y los paquetes instalados fuera del gestor (`pip`, descargas manuales, binarios copiados) no aparecen.

### Qué paquete es dueño de una ruta: la respuesta depende de cómo se pregunta

`dpkg -S /bin/ls` respondió `no path found matching pattern /bin/ls`, mientras que `dpkg -S /usr/bin/ls` respondió `coreutils: /usr/bin/ls`. La razón es que en Ubuntu 24.04 `/bin` es un enlace simbólico a `usr/bin`
(`lrwxrwxrwx ... /bin -> usr/bin`), y el gestor registra rutas reales. La misma pregunta con dos rutas equivalentes dio respuestas distintas: la evidencia depende de la *forma* de la consulta. Para obtener resultados fiables se
resuelve la ruta canónica antes de preguntar (`readlink -f`), y se recuerda que un enlace simbólico no es dueño de nada.

![Figura 2. Preguntar a dpkg por /bin/ls no encuentra nada, mientras /usr/bin/ls pertenece a coreutils, porque /bin es un enlace simbólico](../../../content/part-02/figures/se-032-duenos-de-una-ruta.svg)

**Cómo leer la figura.** Las dos cajas de la izquierda son las dos consultas y sus resultados; las de la derecha, la explicación. **Dónde deja de valer:** la fusión de `/bin` en `/usr/bin` es una decisión de la distribución (y de la versión); en otras
distribuciones o versiones, `/bin` puede ser un directorio real. La lección es el método de consulta, no la ruta.

### Instalar puede ejecutar código

Instalar es una operación de confianza porque *puede ejecutar código*. En el sistema de prueba había 624 archivos de scripts de mantenedor (`preinst`, `postinst`, `prerm`, `postrm`) en `/var/lib/dpkg/info`: instalar o quitar un paquete del sistema ejecuta esos
scripts con privilegios de administrador. En Python, instalar una distribución fuente (*sdist*) puede ejecutar código de construcción del paquete; las *ruedas* (*wheels*) son archivos ya construidos y no tienen un paso de ejecución al instalar, aunque el código del paquete se ejecuta cuando se lo
importa. Por eso la decisión de instalar considera la procedencia del repositorio, la firma, el alcance (sistema o usuario) y un plan de reversión antes del cambio.

![Figura 3. Tabla con un hecho observado y dos documentados sobre dónde puede ejecutarse código al instalar: scripts de mantenedor, sdist y wheel](../../../content/part-02/figures/se-032-instalar-ejecuta-codigo.svg)

**Cómo leer la figura.** La primera fila es una observación; las otras dos son afirmaciones de la documentación (no ejecutadas aquí). La columna final traduce cada una en una consecuencia de riesgo. **Dónde deja de valer:** el número 624 depende de qué esté instalado
en el equipo; lo transferible es que los scripts de mantenedor existen y se ejecutan con privilegios. Un paquete firmado por un repositorio legítimo puede aun así contener código con errores; la firma prueba procedencia, no corrección.

## Definiciones de trabajo

- **paquete:** artefactos, metadatos y acciones administradas como una unidad;
- **dependencia transitiva:** componente requerido a través de otra dependencia;
- **procedencia:** evidencia sobre origen y cadena de publicación;
- **alcance:** conjunto de usuarios, proyectos o sistema afectado;
- **reversibilidad:** capacidad demostrada de retirar cambios o volver a un estado definido.

## Caso conductor: el kit de diagnóstico multiplataforma verifica sus dependencias

El kit requiere un runtime con versión mínima y opcionalmente una herramienta de compresión. Antes de sugerir instalación, detecta capacidad y versión. Si falta lo opcional, produce un informe sin comprimir y marca modo degradado. Si falta lo esencial, entrega instrucciones específicas verificadas, pero no instala automáticamente.

El manifiesto fija dependencias de biblioteca; el informe registra resolución y origen sin afirmar que ello certifica seguridad. Una prueba crea un entorno limpio, instala, ejecuta, desinstala y comprueba qué archivos quedan.

## Práctica guiada

1. Elige una dependencia no privilegiada de laboratorio.
2. Localiza su fuente oficial y explica la cadena de confianza disponible.
3. Obtén el plan o simulación antes de instalar.
4. Instala en el alcance más estrecho posible y verifica versión/origen.
5. Desinstala y compara el estado anterior y posterior.
6. Redacta instrucciones alternativas para otra plataforma sin asumir equivalencia.

No agregues repositorios o gestores al sistema real solo para completar la práctica.

## Ejemplo mínimo

Un manifiesto pide `tool >=2,<3` y el gestor resuelve `2.7` más dos dependencias. El informe distingue restricción de versión resuelta y conserva el plan. Copiar solo `2.7` pierde el grafo y origen.

## Ejemplo profesional

Una actualización global rompe dos proyectos. El equipo migra la herramienta a entornos por proyecto, fija resoluciones y prueba desinstalación. Documenta que quedan cachés y datos, en vez de afirmar una reversión perfecta.

## Ejercicios

1. Construye un grafo con dependencia directa, transitiva y conflicto.
2. Evalúa qué prueba una firma, un hash y TLS, y qué no.
3. Compara alcance de sistema, usuario y proyecto para el kit de diagnóstico multiplataforma.

## Reto verificable

Produce un plan de instalación sin aplicarlo: identidad completa, fuentes, dependencias, scripts, alcance, cambios y reversión. Otra persona debe poder rechazarlo antes de ejecutar.

## Preguntas frecuentes

### ¿Estar en un repositorio oficial vuelve seguro un paquete?

No. Aporta una cadena de distribución y controles concretos, no garantía absoluta de comportamiento.

### ¿Un lockfile hace reproducible cualquier instalación?

Fija parte de la resolución; runtime, plataforma, disponibilidad y servicios externos pueden variar.

### ¿Un paquete de un repositorio oficial es seguro?

Tiene una procedencia más confiable y pasó por un proceso de empaquetado, pero «oficial» no significa libre de vulnerabilidades ni de errores. Se mantiene al día con las actualizaciones de seguridad, se minimizan los paquetes instalados y se
revisa qué scripts ejecuta cada uno.

### ¿Un archivo de bloqueo (lockfile) vuelve reproducible cualquier instalación?

Fija las *versiones* (y, si incluye sumas de verificación, el contenido), pero no la plataforma, el compilador ni las dependencias del sistema. Una instalación reproducible exige además declarar el entorno (versión de Python, sistema, arquitectura)
y probarla en él.

### ¿Cómo desinstalo sin romper el sistema?

Se revisa antes qué depende del paquete (`apt-cache rdepends`, `pip show`) y se usa la herramienta que lo instaló. Se prueba el cambio en un entorno desechable cuando es posible, y se conserva el estado previo (lista de paquetes, copia de
configuración) para revertir.
## Fallo controlado y diagnóstico

Usa simulación o un fixture con dos paquetes homónimos de orígenes ficticios. El kit de diagnóstico multiplataforma debe rechazar la identidad ambigua antes de instalar y explicar qué dato falta.


Una segunda práctica explora la propiedad de archivos. En un Ubuntu de práctica elige un binario (por ejemplo, `ls`), obtén su ruta canónica con `readlink -f $(command -v ls)` y pregunta `dpkg -S` con esa ruta y con `/bin/ls`. **Síntoma:** respuestas
distintas para rutas equivalentes. **Causa:** el gestor registra rutas reales y `/bin` es un enlace simbólico. **Corrección:** consultar siempre con la ruta canónica. Repite con un archivo instalado por `pip` en un entorno virtual desechable y comprueba que
`dpkg -S` responde «no path found»: el archivo pertenece a otro gestor. Documenta qué gestor responde por cada archivo y no instales nada con privilegios para hacer la prueba.
## Errores comunes y cómo corregirlos

| Síntoma | Causa conceptual | Corrección |
|---|---|---|
| Se instala un paquete homónimo | Se confió solo en el nombre | Verificar ecosistema, publicador, URL y firma/metadatos |
| Una actualización rompe otro proyecto | Se usó alcance global sin control de resolución | Aislar por proyecto y conservar manifiesto/bloqueo |
| La automatización ejecuta un script remoto | Se priorizó comodidad sobre inspección | Descargar desde fuente verificada, inspeccionar y fijar artefacto |
| Desinstalar deja un servicio activo | Se confundió paquete con todos sus efectos | Inventariar scripts, datos y servicios; probar reversión |
| Un lockfile se presenta como garantía total | Se ignoraron origen, runtime y plataforma | Documentar qué fija y qué permanece variable |

## Entorno y archivos clave

El [laboratorio compartido](https://github.com/vladimiracunadev-create/modern-software-engineering-program/tree/main/labs/part-02-cross-platform-diagnostic-kit) declara Python 3.11+ y biblioteca estándar en lugar de instalar durante la ejecución. Usa esa decisión para completar procedencia, soporte, actualización y retirada del runtime por plataforma.

Entorno virtual o contenedor desechable, `manifest`, `lock`, `install-plan.md` y `reversal-report.md`. No eleva ni agrega fuentes al host.

## Seguridad, ética y accesibilidad

No canalices scripts remotos al shell ni publiques tokens de registro. Presenta el plan en formato textual legible y señala con palabras los cambios de riesgo.

## Puente hacia el trabajo con agentes

Los asistentes proponen instalar paquetes con la misma naturalidad con que sugieren una función, y un agente con una terminal puede ejecutarlo. Es la superficie del ataque de *dependencia falsa* o *typosquatting*: el modelo recomienda un nombre
que no existe, o uno parecido a uno real, y alguien registra el nombre con código malicioso. Las defensas de esta clase se vuelven reglas del harness: instalar solo desde un repositorio y una lista de paquetes aprobados, fijar versiones y sumas de verificación, ejecutar
en un entorno aislado sin privilegios de administrador, y exigir aprobación humana para cualquier instalación nueva. Un agente que «arregla» un error instalando una dependencia debe justificarla y dejarla en el archivo de dependencias, no solo en el entorno. Las partes sobre cadena de suministro y
seguridad agentic desarrollan estas políticas.

## Transferencia

Aplica el análisis a una imagen de contenedor o extensión de editor. Compara identidad, origen, ejecución durante instalación y camino de retiro.

## Evaluación y evidencia

Se exige grafo, plan previo, justificación de procedencia y alcance, prueba de retiro o simulación honesta y estado residual. Instalar correctamente no basta.

## Criterio de cierre

Puedes presentar un plan de instalación verificable, justificar origen y alcance, y demostrar instalación/desinstalación en laboratorio con diferencias remanentes declaradas.

## Límites y siguiente paso

No realizamos auditoría completa de cadena de suministro ni declaramos seguro un paquete por estar firmado. Incluso una instalación correcta puede fallar; la siguiente clase desarrolla logs y observabilidad para reconstruir qué ocurrió.

## Fuentes


- [Microsoft Learn — WinGet](https://learn.microsoft.com/windows/package-manager/winget/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Debian Administrator's Handbook — APT](https://www.debian.org/doc/manuals/debian-handbook/apt.en.html) — delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.
- [Homebrew Documentation](https://docs.brew.sh/) — delimita el contrato técnico que debe cumplirse al distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance.
- [Python Packaging User Guide](https://packaging.python.org/en/latest/) — define la semántica y los límites de la API de Python utilizada en el experimento.

- [dpkg(1)](https://man7.org/linux/man-pages/man1/dpkg.1.html) y la [Guía del mantenedor de paquetes de Debian](https://www.debian.org/doc/manuals/debmake-doc/): estructura de un paquete, scripts de mantenedor y consulta de propiedad de archivos; respaldan las figuras 1 a 3.
- [Python Packaging User Guide](https://packaging.python.org/): diferencia entre distribuciones fuente y ruedas, y cómo se instalan.
## Glosario

- **Dependencia:** componente requerido bajo una relación y restricción declaradas.
- **Lockfile:** registro de resoluciones concretas para repetir una instalación.
- **Procedencia:** evidencia sobre origen y cadena de publicación de un artefacto.
- **Repositorio de paquetes:** servicio e índice desde el que un gestor obtiene metadatos y artefactos.
- **Transacción:** conjunto de cambios tratado como una unidad según garantías del gestor.

---
[← SE-031](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) · [↑ Parte 02](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-033 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md)
