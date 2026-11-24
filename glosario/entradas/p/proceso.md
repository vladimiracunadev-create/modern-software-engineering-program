# Proceso

[↑ Glosario](../../README.md) · [← Procedimientos de verificación](./procedimientos-de-verificacion.md) · [Proceso sin estado →](./proceso-sin-estado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Un **proceso** es una instancia en ejecución de un programa, con espacio de direcciones propio, identificador, credenciales, descriptores o manejadores, entorno y estado planificable ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)). [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) lo precisa para aplicaciones móviles y de escritorio: la unidad de ejecución que el sistema operativo crea y puede terminar; contiene la memoria de la aplicación y no equivale a una ventana. Un *programa* es la descripción en un archivo; el proceso es su ejecución.

## Por qué importa

Es la unidad de aislamiento y de administración del sistema operativo: se lanza, se mide, se limita, se señala y se termina. Entenderlo evita errores concretos, como creer que cerrar una ventana cierra la aplicación o que guardar estado solo en memoria sobrevive a que el sistema termine el proceso. También es la base de contenedores, servicios y concurrencia.

## Cómo funciona

Un archivo de programa puede originar múltiples procesos. Cada uno posee espacio de direcciones virtual, identificador, recursos y estado administrado por el sistema ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)). El aislamiento limita el acceso accidental a la memoria de otro, pero no es una frontera de seguridad absoluta sin permisos y controles. Un proceso puede contener varios hilos que comparten su memoria. Termina con un código de salida que comunica el resultado al proceso padre ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)).

En plataformas móviles ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md)), el sistema puede terminar procesos en segundo plano para recuperar memoria sin aviso. Por eso lo que importa debe guardarse en disco al pasar a segundo plano y restaurarse en el arranque.

## Ejemplo

```python
import subprocess, sys
r = subprocess.run([sys.executable, "-c", "print('hola')"], capture_output=True, text=True)
print(r.returncode, r.stdout)   # proceso hijo con su propia memoria y su propio código de salida
```

En [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), el texto de un borrador desaparece al volver a la aplicación porque el estado vivía solo en memoria y el sistema terminó el proceso.

## Errores y confusiones comunes

- **Programa igual a proceso.** Causa: se confunde archivo con ejecución; corrección: distinguir descripción e instancia ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)).
- **El texto del borrador desaparece al volver a la aplicación.** Causa: el estado vivía solo en memoria; corrección: guardar en disco al pasar a segundo plano y restaurar al arrancar ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md)).
- **Medir CPU como si fuera espera.** El tiempo de CPU aproxima el trabajo ejecutado por el proceso, no la espera externa ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)).

## Límites y cuándo no aplica

El aislamiento entre procesos no equivale a seguridad: un proceso con los mismos permisos puede afectar a otro. Los procesos son más costosos que los hilos y su comunicación requiere mecanismos explícitos. Y en entornos con contenedores o máquinas virtuales, lo que «parece» un proceso aislado depende de la configuración del anfitrión.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](../s/sistema-operativo.md), [Contextos](../c/contextos.md), [Instancia](../i/instancia.md), [Recurso](../r/recurso.md), [Código de salida](../c/codigo-de-salida.md), [Concurrencia](../c/concurrencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (309 clases más lo mencionan; las que más):

[SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Process Concepts](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Android Developers, «Application fundamentals»](https://developer.android.com/guide/components/fundamentals) — procesos, sandbox y componentes de una aplicación Android; autoridad: Google.
- [Electron, «Process Model»](https://www.electronjs.org/docs/latest/tutorial/process-model) — proceso principal y procesos de interfaz de una aplicación de escritorio; autoridad: OpenJS Foundation.
- [Microsoft Learn — Processes and Threads](https://learn.microsoft.com/windows/win32/procthread/processes-and-threads) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.

---

[↑ Glosario](../../README.md) · [← Procedimientos de verificación](./procedimientos-de-verificacion.md) · [Proceso sin estado →](./proceso-sin-estado.md)
