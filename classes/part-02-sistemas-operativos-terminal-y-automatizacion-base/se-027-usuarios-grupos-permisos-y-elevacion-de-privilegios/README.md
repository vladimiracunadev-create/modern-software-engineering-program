# SE-027 — Usuarios, grupos, permisos y elevación de privilegios

[← SE-026](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) · [↑ Parte 02](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-028 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.

**Por qué aparece aquí.** Se sitúa después de **Sistemas de archivos, rutas, enlaces y metadatos** y antes de **Procesos, señales, servicios y tareas programadas**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Creer que ser propietario implica acceso efectivo o que elevar corrige diseño de permisos.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Access-matrix.md con sujeto, objeto, regla, resultado y recuperación. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** El laboratorio local no modela políticas corporativas completas.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [The Open Group — File Access Permissions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_05) | define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Microsoft Learn — Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) | documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Microsoft Learn — How User Account Control works](https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works) | documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) | delimita el contrato técnico que debe cumplirse al explicar autorización como evaluación de identidad, pertenencia, ACL y elevación | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

El kit de diagnóstico multiplataforma encontró la configuración correcta, pero no puede leerla. Cambiar permisos a “todos” haría desaparecer el síntoma y crearía un problema mayor. El diagnóstico profesional pregunta: ¿qué identidad realiza la operación?, ¿qué autoridad posee?, ¿qué regla se aplicó?, ¿qué mínimo cambio sería suficiente?

### Resultado de aprendizaje

Al terminar podrás razonar sobre autenticación, autorización, propiedad, permisos y elevación sin reducir el problema a “ejecuta como administrador”.

## Prerrequisitos

`SE-026`, una carpeta desechable y una cuenta sin privilegios administrativos para la práctica. Debes poder distinguir ruta, objeto y metadatos.

## Problema auténtico

El kit de diagnóstico multiplataforma recibe “acceso denegado”. Un intento previo abrió permisos para todos y el síntoma desapareció, pero ahora cualquier proceso local puede modificar la configuración. Se reparó disponibilidad destruyendo la política de acceso.

## Objetivos observables

Podrás modelar una decisión como sujeto–acción–objeto–política; interpretar permisos POSIX y ACL de Windows sin traducirlos falsamente; justificar mínimo privilegio; y proponer una corrección reversible con menor autoridad.

## Temas y por qué importan

| Tema | Mecanismo | Decisión habilitada |
| --- | --- | --- |
| Identidad efectiva | acompaña al proceso que solicita | saber quién actúa realmente |
| Autorización | evalúa acción sobre objeto bajo reglas | explicar la denegación |
| ACL y permisos | expresan derechos e herencia | corregir sin acceso universal |
| Elevación | crea un contexto más poderoso | reservarla para una necesidad explícita |
## Mapa conceptual

```mermaid
flowchart LR
 S[Sujeto: proceso e identidad] --> E[Evaluación]
 A[Acción solicitada] --> E
 O[Objeto resuelto] --> E
 P[Permisos, ACL y política] --> E
 E --> D{Permitir o denegar}
 D --> R[Evidencia y corrección mínima]
```

La decisión no vive solo en el archivo. La identidad del proceso, cada directorio padre y reglas adicionales pueden cambiar el resultado; por eso el kit de diagnóstico multiplataforma conserva el conjunto causal.

## Conceptos y decisiones

### Identidad y autoridad no son lo mismo

La autenticación vincula una sesión con una identidad. La autorización decide si esa identidad puede realizar una acción sobre un recurso. Conocer el nombre del usuario no basta: importan grupos, credenciales, token o contexto efectivo, propietario del objeto y política aplicable.

Un proceso hereda un contexto de seguridad al iniciarse. Cambiar de identidad o elevar autoridad crea otro contexto; no corrige la lógica del programa. El kit de diagnóstico multiplataforma registra identidad efectiva y operación fallida sin exponer identificadores más allá de lo necesario.

### El control de acceso evalúa sujeto, acción, objeto y política

Una explicación útil tiene cuatro piezas:

```mermaid
flowchart LR
    S[Sujeto: proceso e identidad] --> P[Motor de autorización]
    A[Acción: leer, escribir, ejecutar] --> P
    O[Objeto: archivo, proceso, servicio] --> P
    R[Reglas: permisos, ACL, política] --> P
    P --> D{Permitir o denegar}
    D --> E[Evidencia y auditoría]
```

El mismo usuario puede leer un archivo y no modificar su directorio. Poder modificar el directorio puede permitir reemplazar una entrada aunque el archivo tenga otros permisos. Por eso “tengo permiso sobre el archivo” es una afirmación incompleta.

### POSIX combina propietario, grupo y otros; las ACL amplían el modelo

Los bits clásicos expresan lectura, escritura y ejecución para propietario, grupo y otros. En un directorio, estos bits tienen semánticas distintas de un archivo: lectura enumera nombres, escritura modifica entradas y ejecución permite atravesar la ruta. Bits especiales y ACL agregan reglas que requieren análisis adicional.

El permiso efectivo puede depender de identidad efectiva, grupos suplementarios, máscara de ACL y de cada directorio padre. `chmod 777` ignora intención y amplía autoridad indiscriminadamente.

### Windows usa tokens, descriptores de seguridad y ACL

En Windows, el proceso opera con un token que representa usuario, grupos y privilegios. Los objetos pueden tener propietarios y listas de control de acceso con entradas de permitir o denegar e herencia. La evaluación no se traduce correctamente a tres dígitos octales.

UAC separa el uso cotidiano de un token elevado; aceptar una elevación amplía la autoridad del proceso completo. La documentación de [Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) detalla el modelo. El kit de diagnóstico multiplataforma evita “traducir” ACL de Windows a permisos POSIX como si fueran equivalentes.

### Mínimo privilegio reduce impacto y mejora el diagnóstico

Un programa debe solicitar solo la autoridad necesaria y durante el tiempo necesario. Si el kit de diagnóstico multiplataforma puede leer estado con permisos normales, no debe ejecutarse elevado “por si acaso”. La elevación también puede cambiar directorio personal, variables, mapeos de red o acceso a la sesión, generando un contexto diferente del fallo original.

Un buen flujo intenta una operación segura, captura la denegación exacta y explica qué capacidad falta. Solo propone elevación si el objetivo la requiere por diseño y ofrece una acción acotada.

### Permiso denegado puede proteger otra frontera

La causa no siempre es el modo del archivo. Puede intervenir una ACL, política de ejecución, sandbox, control de aplicaciones, atributo de procedencia, recurso bloqueado o montaje de solo lectura. La corrección comienza por clasificar la frontera, no por desactivar controles.

### Los secretos exigen permisos y también disciplina de uso

Restringir un archivo no impide que un proceso autorizado imprima su contenido en logs, lo pase como argumento visible o lo herede a un proceso hijo. La protección combina almacenamiento, acceso mínimo, redacción, rotación y ciclo de vida. La clase SE-031 desarrollará esta cadena.

### `chmod` no significa lo mismo en todas partes

El comando y la función `os.chmod` existen en Windows y en Linux, pero hacen cosas distintas. La prueba de esta clase crea un archivo propio, le aplica cuatro modos y comprueba qué se ve
y qué se puede hacer, con una identidad sin privilegios. En Linux (ext4, uid 1000), `0o000` impidió leer y escribir (`PermissionError` en ambos casos), `0o444` permitió leer y
denegó escribir y `0o600` y `0o644` permitieron ambos para el propietario. En Windows, `0o000` terminó como `0o444`: el archivo siguió siendo *legible* y solo se volvió de solo
lectura; `0o600` y `0o644` aparecieron como `0o666`. Para Windows, `chmod` activa o quita el atributo de solo lectura; los permisos de verdad viven en listas de control de acceso (ACL).

![Figura 1. Tabla con el resultado real de cuatro modos en Linux y en Windows: modo que se ve, lectura y escritura](../../../content/part-02/figures/se-027-chmod-en-dos-sistemas.svg)

**Cómo leer la figura.** Cada fila es un modo solicitado. La columna de Linux muestra el modo que se vio, y si la lectura y la escritura funcionaron para el propietario sin privilegios. La de
Windows muestra que el modo se *aproxima*. **Dónde deja de valer:** el resultado de Linux es para un usuario sin privilegios; el administrador (root) puede leer un archivo con `0o000`. Y en
Windows, el control de acceso real se examina con `icacls` o las propiedades de seguridad; esas listas incluyen identificadores de seguridad (SID) que no deben publicarse en un
reporte. Una ficha de permisos documenta la identidad usada y no copia SIDs, nombres de cuenta ni rutas personales.

### Directorios: leer es listar y ejecutar es atravesar

En un directorio, los bits tienen otro significado: `r` permite *listar los nombres*, `w` permite crear y borrar entradas, y `x` permite *atravesarlo* para acceder a lo que contiene. La prueba lo confirma: un
directorio con modo `0o600` (sin `x`) permite `os.listdir` y rechaza `os.stat` sobre un archivo hijo con `PermissionError`. Para alcanzar `/a/b/c.txt` se necesita `x` en `/`, `/a` y `/a/b`, y el permiso del archivo
final. Por eso, un archivo con modo correcto puede ser inalcanzable si algún directorio del camino no concede `x`, y un directorio con `x` pero sin `r` permite acceder a un archivo cuyo nombre ya conoces,
pero no listarlo.

![Figura 2. Un directorio con modo 600: listar los nombres funciona y consultar un hijo falla](../../../content/part-02/figures/se-027-directorio-r-y-x.svg)

**Cómo leer la figura.** El directorio con `rw-` y sin `x` produce dos resultados distintos con la misma identidad: la lectura de nombres funciona y el acceso a los hijos no. **Dónde deja de valer:** es el
modelo clásico de POSIX; las ACL (`getfacl`, `setfacl`), las capacidades y los módulos de seguridad (SELinux, AppArmor) añaden decisiones. En Windows, el modelo es distinto: se evalúan el token del proceso
y la ACL del objeto, y existe un privilegio de «omitir comprobación de recorrido» que muchas cuentas tienen por defecto.

### `umask` y los modos por omisión

Un archivo nuevo no recibe `0o666` ni `0o777`: el sistema resta la máscara `umask`. En el Linux de la prueba, `umask` es `0o022`, de modo que un archivo creado con `0o666` queda en `0o644` (se quita la escritura de grupo y otros). En Windows,
`os.umask` no tiene el mismo efecto (la prueba lo informó como `0o000`). La consecuencia de diseño es que los archivos con secretos no deben depender de la máscara del entorno: se crean con un modo explícito (por ejemplo,
con `os.open(..., 0o600)`) y se verifica, en lugar de confiar en el valor por omisión.

### La denegación como evidencia

Un permiso denegado informa más que un éxito. Dos intentos reales como usuario sin privilegios lo ilustran: `cat /etc/shadow` devolvió `Permission denied` (el archivo es `640` y de `root`), y `sudo -n true`
respondió `a password is required`. En ambos casos el sistema funcionó como debía: el archivo existe, la identidad no tiene el permiso y la elevación exige una autenticación que ese contexto no ofrece. Elevar
privilegios para «ver si funciona» no es una prueba sino una intervención con riesgo; la práctica correcta es identificar sujeto, acción, objeto y política, y pedir el mínimo.

![Figura 3. Tres intentos reales con su resultado y lectura: leer /etc/shadow, sudo sin contraseña e id](../../../content/part-02/figures/se-027-denegacion-es-informacion.svg)

**Cómo leer la figura.** Cada fila combina un intento, el resultado observado y la lectura correcta. La tercera recuerda que la *identidad* (uid 1000, varios grupos) no equivale a
*autoridad*. **Dónde deja de valer:** el mensaje `Permission denied` es el mismo para distintas causas (permisos de archivo, directorio sin `x`, ACL, política). Hace falta una segunda observación (`ls -ld`, `namei -l`, `getfacl`) para
saber cuál.

## Definiciones de trabajo

- **sujeto:** proceso y contexto de identidad que solicita una acción;
- **objeto:** recurso sobre el que se evalúa la solicitud;
- **permiso efectivo:** autoridad resultante después de reglas, grupos, herencia y contexto;
- **elevación:** cambio a un contexto con más autoridad;
- **mínimo privilegio:** autoridad mínima, acotada en acción, alcance y duración.

## Caso conductor: el kit de diagnóstico multiplataforma explica una denegación

El kit de diagnóstico multiplataforma intenta leer la configuración del analizador local de eventos con una operación no destructiva. Ante una denegación registra:

- identidad efectiva y grupos relevantes, redactados si el informe se comparte;
- acción exacta y objeto resuelto;
- propietario, permisos o ACL que sea seguro consultar;
- directorio padre que podría impedir el recorrido;
- hipótesis y prueba mínima siguiente.

No cambia permisos automáticamente. Si el archivo pertenece a otra cuenta, distingue entre un error de instalación y un recurso deliberadamente compartido. Si la corrección propuesta es “cambiar propietario”, declara qué procesos podrían dejar de acceder.

## Práctica guiada

En un directorio de laboratorio:

1. crea un archivo legible y otro restringido;
2. observa identidad real y efectiva;
3. compara permiso de archivo y permisos de sus directorios padre;
4. provoca una denegación y conserva su mensaje/código;
5. propone tres correcciones, ordénalas por autoridad añadida y elige la mínima;
6. revierte todos los cambios y demuestra el estado final.

No uses carpetas del sistema ni datos personales. La reversión es parte de la evidencia.

## Ejemplo mínimo

Un archivo permite lectura al propietario, pero su directorio padre niega atravesar la ruta. Mirar solo el archivo sugiere acceso; evaluar el recorrido completo explica la denegación.

## Ejemplo profesional

Un servicio fue instalado por una cuenta administrativa y su configuración quedó inaccesible a la identidad de servicio. En vez de ejecutar el servicio como administrador, se asigna lectura al sujeto específico sobre el objeto específico y se valida que no obtuvo escritura ni acceso a otros secretos.

## Ejercicios

1. Modela tres operaciones con la cuádrupla sujeto, acción, objeto y política.
2. Explica por qué `chmod 777` y “Control total para Todos” no son diagnósticos.
3. Compara el contexto antes y después de elevar: perfil, entorno, rutas y recursos de sesión.

## Reto verificable

Provoca una denegación en laboratorio y presenta dos correcciones posibles ordenadas por autoridad añadida. Aplica y revierte únicamente la mínima, demostrando el estado final.

## Preguntas frecuentes

### ¿Ser propietario concede siempre todas las acciones?

No. La semántica depende del objeto y plataforma; políticas adicionales o montajes pueden restringir incluso al propietario.

### ¿Elevar confirma que faltaban permisos?

Solo indica que un contexto distinto logró la operación; también pudo cambiar rutas, variables o recursos. Hay que aislar el mecanismo.

### ¿Un archivo con modo 600 es secreto?

Solo protege frente a *otras identidades* del mismo sistema. El propietario, el administrador y los procesos que se ejecutan como ese usuario pueden leerlo, y una copia de seguridad o un registro pueden
exponerlo. Los permisos son una capa; el secreto además se minimiza, se rota y no se escribe en registros.

### ¿Por qué `os.access` y abrir el archivo pueden dar respuestas distintas?

`os.access` pregunta al sistema si el *usuario real* tendría acceso en ese instante; abrir el archivo es la operación definitiva, y entre ambas el estado puede cambiar (condición de carrera). Es mejor intentar la
operación y manejar `PermissionError` que comprobar antes y actuar después.

### ¿Cómo verifico quién puede acceder en Windows?

Con las ACL: `icacls ruta` las lista y las propiedades de seguridad del Explorador las muestran. Los resultados contienen SIDs y cuentas, por lo que una ficha pública debe describirlos de forma genérica (por
ejemplo, «el propietario y el grupo de administradores tienen control total») y no copiarlos.
## Fallo controlado y diagnóstico

Intenta leer un archivo de laboratorio sin permiso y captura el error exacto. Luego comprueba directorios padre y contexto efectivo. Corrige el único derecho necesario y revierte; no desactives controles globales.


Una segunda práctica explora el directorio sin `x`. En un directorio desechable de Linux crea una carpeta con un archivo, quítale `x` (`chmod 600 carpeta`) y comprueba con un script
que `os.listdir` funciona y `os.stat` sobre el hijo falla; restaura `chmod 755` y repite. **Síntoma:** el archivo «existe» (aparece en el listado) pero «no se puede abrir». **Causa:** falta `x`
en el directorio. **Corrección:** conceder el permiso mínimo necesario y registrar con `namei -l` qué directorio del camino lo bloqueaba. Documenta además qué habría ocurrido en Windows (el modelo es distinto) sin ejecutarlo
con credenciales elevadas.
## Errores comunes y cómo corregirlos

| Síntoma | Causa conceptual | Corrección |
|---|---|---|
| “Funciona como administrador” se declara solución | Se ocultó la regla que denegó acceso | Reproducir sin elevar e identificar capacidad mínima |
| Se aplica acceso universal | Se confunde disponibilidad con autorización | Definir quién necesita qué acción y limitar alcance |
| Se revisa solo el archivo | Se ignoran directorios padre, ACL o montaje | Trazar la ruta completa y la política efectiva |
| Un script elevado usa otra configuración | Cambió el contexto de identidad | Registrar identidad, HOME/perfil y ruta antes y después |
| El informe publica usuarios o ACL completas | Se confundió evidencia con exposición | Minimizar y redactar datos sin perder la relación causal |

## Entorno y archivos clave

La negativa ante un marker ajeno del [laboratorio compartido](https://github.com/vladimiracunadev-create/modern-software-engineering-program/tree/main/labs/part-02-cross-platform-diagnostic-kit) es el caso común de autorización: el kit no intenta elevarse ni apropiarse del directorio; devuelve código 3 y conserva el estado para revisión.

`work/SE-027/`, dos archivos ficticios y `access-report.md`. Usa únicamente recursos propios; documenta comandos equivalentes sin forzar una traducción entre ACL y bits POSIX.

## Seguridad, ética y accesibilidad

No practiques sobre cuentas, servicios o datos de terceros. La salida debe explicar la acción negada en texto claro, no solo mediante un código o color.

## Puente hacia el trabajo con agentes

Un agente con acceso a una terminal hereda la identidad del usuario que lo lanzó, y con ella toda su autoridad. La lección de esta clase se traduce en un diseño de permisos: ejecutar al agente con una
identidad *dedicada* y de mínimo privilegio, darle acceso de escritura solo a un directorio de trabajo, y tratar cada `Permission denied` como información, no como un obstáculo que hay que sortear con
`sudo` o `chmod 777`. Un patrón de fallo conocido es que el agente, al encontrar una denegación, «arregla» el problema ampliando permisos; el harness debe impedir la elevación y exigir una aprobación humana para cualquier cambio
de permisos. También conviene que los archivos que el agente crea nazcan con un modo explícito. Las partes de seguridad agentic y de gestión de secretos desarrollan esas políticas.

## Transferencia

Aplica el modelo a una base de datos o repositorio Git. Identifica sujeto, acción, objeto y política aunque el mecanismo no sean permisos de archivo.

## Evaluación y evidencia

Se exige denegación reproducida, explicación efectiva, corrección mínima, verificación negativa y reversión. “Funcionó como administrador” cuenta como síntoma, no como solución.

## Criterio de cierre

Puedes explicar una decisión de acceso como relación entre sujeto, acción, objeto y política; comparar modelos sin falsas equivalencias; y proponer una corrección reversible que no amplíe privilegios innecesariamente.

## Límites y siguiente paso

No cubrimos administración empresarial de identidades, dominios, SELinux, AppArmor ni todos los detalles de ACL. El contexto de seguridad pertenece a un proceso en ejecución. La siguiente clase estudia cómo nacen, se planifican, coordinan y terminan esos procesos.

## Fuentes


- [The Open Group — File Access Permissions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html#tag_04_05) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Access Control](https://learn.microsoft.com/windows/win32/secauthz/access-control) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Microsoft Learn — How User Account Control works](https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) — delimita el contrato técnico que debe cumplirse al explicar autorización como evaluación de identidad, pertenencia, ACL y elevación.

- [chmod(2)](https://man7.org/linux/man-pages/man2/chmod.2.html) y [credentials(7)](https://man7.org/linux/man-pages/man7/credentials.7.html): modos de archivo, identificadores de usuario y grupo y su evaluación en Linux; respaldan las figuras 1 y 2.
- [Python `os`](https://docs.python.org/3/library/os.html): `chmod`, `access`, `umask` y su comportamiento diferente en Windows.
## Glosario

- **ACL:** lista de reglas que asocia identidades o grupos con derechos sobre un objeto.
- **Autenticación:** proceso de establecer una identidad.
- **Autorización:** decisión sobre una acción solicitada por una identidad.
- **Elevación:** ejecución con un contexto de autoridad mayor al habitual.
- **Mínimo privilegio:** principio de conceder la menor autoridad suficiente, con alcance y duración acotados.

---
[← SE-026](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) · [↑ Parte 02](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-028 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)
