# Terminación

[↑ Glosario](../../README.md) · [← Tenant](./tenant.md) · [Terminación cooperativa →](./terminacion-cooperativa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

La **terminación** es la propiedad de finalizar para toda entrada del dominio ([SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)). Un algoritmo cuya ejecución puede no acabar para alguna entrada no termina, aunque casi siempre lo haga. En operación ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)), la palabra tiene un segundo sentido: cómo se detiene un proceso o un servicio, ordenada o forzosamente.

## Por qué importa

Un programa que no termina consume recursos indefinidamente o bloquea a quien lo espera. Un timeout detiene una ejecución, pero no demuestra que el algoritmo termine para cualquier entrada ([SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)). Importa distinguir ambas cosas: parar un proceso es una decisión operativa; demostrar que termina es una propiedad del algoritmo. Y en producción, la forma de terminar decide si se pierden datos.

## Cómo funciona

**Del algoritmo** ([SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)): se demuestra con una **variante**, una cantidad que toma valores en un orden bien fundado (por ejemplo, enteros no negativos) y disminuye estrictamente en cada iteración. Si `b` decrece en cada paso y no baja de 0, el bucle termina; su **corrección** viene de un invariante (una igualdad que se conserva) junto con esa terminación. `pendientes` puede servir como variante si ningún paso vuelve a insertar indefinidamente. En recorridos de grafos con ciclos, el conjunto de visitados garantiza que los nodos pendientes decrecen ([SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md)).

**Operativa** ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)): terminar un servicio puede ser ordenado (el proceso recibe una señal, vacía lo pendiente, escribe en un archivo temporal y renombra) o forzado (se corta sin limpieza). La terminación forzada puede dejar un archivo truncado; en Windows, `terminate()` equivale a una terminación forzada, por lo que se usa `CTRL_BREAK_EVENT` o un canal de cierre propio.

## Ejemplo

```python
def mcd(a, b):
    while b:                    # variante: b decrece estrictamente y es >= 0
        a, b = b, a % b         # invariante: mcd(a, b) no cambia
    return a
```

Como `a % b < b`, el valor de `b` baja en cada paso: termina para cualquier par de enteros no negativos.

## Errores y confusiones comunes

- **Un archivo queda truncado al detener el servicio.** Causa: terminación forzada o manejador que no vació; corrección: cierre ordenado y escritura en archivo temporal ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)).
- **`terminate()` no limpia en Windows.** Causa: equivale a terminación forzada; corrección: `CTRL_BREAK_EVENT` o un canal de cierre propio ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)).
- **Creer que un timeout prueba terminación.** Solo corta una ejecución concreta ([SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)).

## Límites y cuándo no aplica

La terminación no es decidible en general para programas arbitrarios (problema de la parada); se demuestra caso a caso con una variante. Para servicios que por diseño no terminan, la propiedad relevante es la de cada petición, no la del proceso. Y una demostración de terminación no acota el tiempo: un programa puede terminar tras un tiempo inaceptable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Propiedad](../p/propiedad.md), [Algoritmo](../a/algoritmo.md), [Código de salida](../c/codigo-de-salida.md), [Corrección parcial](../c/correccion-parcial.md), [Corrección total](../c/correccion-total.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (40 clases más lo mencionan; las que más):

[SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [The Open Group — Process Concepts](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Processes and Threads](https://learn.microsoft.com/windows/win32/procthread/processes-and-threads) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Tenant](./tenant.md) · [Terminación cooperativa →](./terminacion-cooperativa.md)
