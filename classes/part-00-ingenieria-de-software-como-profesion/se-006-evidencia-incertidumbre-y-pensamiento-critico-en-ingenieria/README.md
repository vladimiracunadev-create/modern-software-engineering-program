# SE-006 — Evidencia, incertidumbre y pensamiento crítico en ingeniería

[← SE-005](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) · [↑ Parte 00](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-00-ingenieria-de-software-como-profesion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [SE-007 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md)


## Antes de empezar

Campus Abierto ya tiene responsables y canales de colaboración, pero varias personas
explican el incidente de forma distinta. Una muestra pequeña culpa a la base de datos;
otra observación apunta al proveedor de identidad. Tener roles claros no elimina la
incertidumbre ni convierte una métrica en conclusión.

Esta clase introduce el ciclo pregunta → hipótesis → prueba → observación → decisión
provisional. Crearás un registro que permita a otra persona refutar tu interpretación.
En `SE-007` usarás esa disciplina para evitar que “calidad” sea una opinión o una
colección de indicadores cómodos.

## Prerrequisitos

Poder formular decisiones y reconocer perspectivas de `SE-001`–`SE-005`.

## Problema auténtico

Tras optimizar una consulta, un benchmark muestra 40% menos tiempo. ¿El cambio es mejor? Puede medir caché caliente, pocos datos o una máquina distinta. El número es observación; la conclusión necesita modelo e incertidumbre.

## Objetivos observables

Separarás hecho, inferencia e hipótesis; diseñarás comprobaciones que puedan refutarte; estimarás incertidumbre práctica y decidirás cuándo obtener más evidencia.

## Temas y por qué importan

| Elemento | Pregunta |
| --- | --- |
| Observación | ¿qué ocurrió y cómo se midió? |
| Inferencia | ¿qué explicación conecta datos y conclusión? |
| Incertidumbre | ¿qué no sabemos y cuánto cambia la decisión? |
| Falsación | ¿qué resultado demostraría que estamos equivocados? |

## Mapa conceptual

```mermaid
flowchart LR
 Q[Pregunta] --> H[Hipótesis]
 H --> T[Prueba]
 T --> O[Observación]
 O --> I[Interpretación]
 I --> D[Decisión provisional]
 D --> Q
```

La decisión es provisional: nueva evidencia puede cambiarla.

## Conceptos y decisiones

### 1. Separar lo observado de la historia que contamos

Una **observación** registra qué ocurrió mediante un método: “el p95 fue 480 ms en
estas solicitudes, intervalo y entorno”. Una **inferencia** conecta observaciones con
una conclusión: “la dependencia contribuyó a la demora”. Una **hipótesis** formula una
explicación contrastable: “si la dependencia es la causa dominante, aislarla reducirá
la cola”. Un **supuesto** es una condición aceptada provisionalmente, como considerar
representativa la carga de prueba.

Mezclarlos impide aprender. “La base de datos estuvo lenta” parece un hecho, pero ya
atribuye causa. Puede haber esperado conexiones o bloqueo de aplicación. El registro
debe permitir que otra persona acepte la observación y dispute la inferencia sin negar
los datos.

![Figura 1. Una afirmación vaga se descompone en observación, inferencia, hipótesis y supuesto, cada uno con su pregunta de control](../../../content/part-00/figures/se-006-observacion-a-supuesto.svg)

**Cómo leer la figura.** La caja roja es la frase habitual: parece un dato pero ya contiene
una causa. Debajo se separa en cuatro tipos de enunciado y cada uno recibe una pregunta
distinta. Una persona escéptica puede aceptar la observación (el p95 subió, con ese método),
discutir la inferencia (¿fue la dependencia Y?) y exigir que la hipótesis diga qué la
refutaría. **Dónde deja de valer:** la frontera entre observación e inferencia no es absoluta.
Todo instrumento incorpora supuestos (qué se cuenta como solicitud, cómo se agrega el tiempo),
así que la «observación» es siempre relativa a un método que debe declararse.

### 2. La fuerza de la evidencia depende de la decisión

No existe evidencia “alta” por su formato. Una prueba unitaria es fuerte para un caso
determinista y débil para experiencia de uso. Un testimonio puede revelar un modo de
fallo que una métrica agregada oculta, aunque no estime su frecuencia. Evalúa al menos:

- **relevancia:** responde la pregunta que cambia la decisión;
- **validez:** el método mide razonablemente el fenómeno declarado;
- **fiabilidad:** condiciones semejantes producen observaciones compatibles;
- **representatividad:** casos y entorno cubren la población pertinente;
- **trazabilidad:** se conservan origen, configuración, tiempo y transformaciones.

Una prueba que siempre pasa, una captura sin fecha o un promedio sin población pueden
ser datos auténticos y aun así aportar poca discriminación entre opciones. Calidad de
evidencia no es cantidad de archivos.

### 3. Predicción, causalidad y mecanismos

Una correlación puede ayudar a anticipar, pero no demuestra qué ocurrirá al intervenir.
Si latencia y concurrencia crecen juntas, limitar concurrencia podría ayudar o solo
ocultar una dependencia saturada. Una explicación causal combina temporalidad,
mecanismo plausible, predicciones y exclusión razonada de alternativas.

En ingeniería rara vez se controla todo. Se puede comparar antes y después, aislar una
dependencia, variar un parámetro, reproducir con una carga sintética y revisar trazas.
Cuando no es posible experimentar —por riesgo o costo— se triangulan métodos y se
reduce la fuerza de la conclusión. “Compatible con” es a veces la afirmación más
honesta.

Los **confusores** cambian junto con la variable estudiada. Un benchmark después de
optimizar también puede usar caché caliente, menos datos o hardware distinto. Mantener
condiciones, aleatorizar orden o registrar diferencias reduce la confusión; no la
elimina automáticamente.

### 4. Diseñar la posibilidad de estar equivocados

Una hipótesis útil produce una predicción cuya ausencia la debilita. “El sistema está
lento por muchas razones” puede ser cierto, pero no orienta una prueba. “El pool de
conexiones es el cuello de botella; al aumentar temporalmente su capacidad bajará la
espera sin trasladarla a la base” crea observaciones que pueden contradecirla.

Buscar solo confirmación es fácil: elegir el intervalo que coincide, descartar outliers
sin regla o consultar únicamente a quien adoptó el producto. La defensa es escribir
antes qué resultado cuenta contra la hipótesis, comparar explicaciones rivales y pedir
que una revisión intente refutar, no solo aprobar.

### 5. Decidir con incertidumbre y costo de información

La incertidumbre puede expresarse con rangos, escenarios, sensibilidad o confianza
argumentada. Una cifra con decimales no es más honesta si el método no permite esa
precisión. Conviene preguntar si cambiar un supuesto cambia la opción preferida. Si no
la cambia, quizá investigar más no aporte valor; si invierte una decisión irreversible,
la evidencia adicional puede ser esencial.

En un cambio reversible y de bajo impacto, una exposición pequeña y observada puede
ser el experimento adecuado. Ante consecuencias graves, el umbral de evidencia y
revisión aumenta. La decisión incluye siempre señales de parada y revisión: reconocer
incertidumbre no es paralizarse, sino gobernar lo que todavía no se sabe.

![Figura 3. Cuadrícula de reversibilidad por impacto con la forma de actuar ante la incertidumbre en cada cuadrante](../../../content/part-00/figures/se-006-incertidumbre.svg)

**Cómo leer la figura.** El esfuerzo de evidencia no es una constante: crece cuando equivocarse
es grave o irreversible. Abajo se muestra la pregunta que evita gastar de más: si cambiar un
supuesto no cambia la opción preferida, otro dato no vale su costo. **Dónde deja de valer:**
«reversible» e «impacto» no son atributos fijos de una decisión; dependen de quién la sufre.
Un cambio reversible para el sistema puede ser irreversible para una persona (una
confirmación de matrícula perdida), y esa asimetría debe decidir en qué cuadrante se coloca.

## Caso conductor: cuatro explicaciones para la latencia

Campus Abierto registra demoras después de un despliegue. Compiten cuatro hipótesis:
consulta más costosa, pool agotado, proveedor de identidad lento o mezcla de tráfico
distinta. Se construye una matriz antes de tocar producción:

| Hipótesis | Predicción discriminante | Prueba segura | Resultado que la debilita |
| --- | --- | --- | --- |
| consulta costosa | tiempo de DB crece en la ruta afectada | reproducir con conjunto representativo | DB estable mientras aumenta espera previa |
| pool agotado | cola de conexión precede a latencia | observar y variar en entorno controlado | conexiones disponibles durante el pico |
| identidad externa | trazas concentran demora en esa llamada | usar stub y comparar | la cola persiste sin dependencia |
| mezcla de tráfico | cambian rutas y tamaños de solicitud | segmentar por ruta y cohorte | misma mezcla con distinta latencia |

La decisión provisional puede ser limitar exposición mientras se ejecuta la prueba de
mayor valor informativo. El log conserva configuración y observaciones; no reemplaza
la incertidumbre por una causa conveniente.

![Figura 2. Barras apiladas con datos sintéticos: antes 220 ms; tres escenarios con 480 ms cuya causa está en tramos distintos](../../../content/part-00/figures/se-006-latencia-desglose.svg)

**Cómo leer la figura.** Los tres escenarios tienen el mismo p95 de 480 ms, pero la demora
vive en un tramo distinto: la espera del pool, la base de datos o la identidad externa. Una
métrica total no puede distinguirlos; el desglose sí, y cada hipótesis de la tabla del caso
conductor predice cuál tramo debería crecer. Por eso la prueba más valiosa no es la más
barata sino la que más separa las explicaciones. **Dónde deja de valer:** son datos sintéticos
y los tramos suman limpiamente. En un sistema real los tramos se solapan, hay colas
compartidas y una dependencia lenta puede *causar* espera de pool; entonces hay más de una
causa verdadera, y una sola prueba no las aísla.

## Definiciones de trabajo

- **hecho observado:** registro producido por un método declarado;
- **inferencia:** conclusión derivada de observaciones y supuestos;
- **hipótesis:** explicación contrastable;
- **confusor:** variable que altera relación aparente;
- **reproducibilidad:** posibilidad de repetir método con información suficiente.

## Glosario

**Base rate** es frecuencia previa relevante. **Proxy** es medida indirecta. **Intervalo** expresa rango compatible con método y datos, no promesa absoluta.

## Ejemplo mínimo

«La API estuvo lenta» mezcla observación e interpretación. Mejor: p95 subió de 220 a 480 ms durante 15 minutos en región A; coincidió con despliegue X; faltan datos de dependencia Y.

## Ejemplo profesional

El benchmark de consulta se repite con datos fríos y calientes, mismos recursos y múltiples corridas. La mediana mejora, pero la cola empeora con alta concurrencia. La decisión cambia de «adoptar» a «probar bajo carga representativa».

## Práctica guiada

Escribe `evidence-log.md` con afirmación, observación, método, supuesto y contraevidencia. Diseña dos pruebas que podrían cambiar la decisión y priorízalas por costo de información.

## Ejercicios

1. Reescribe cinco afirmaciones absolutas como hipótesis.
2. Encuentra un proxy que pueda incentivar conducta indeseada.
3. Decide con evidencia incompleta y declara condición de revisión.

## Reto verificable

Otra persona reproduce una medición y obtiene resultado compatible o explica la diferencia. Debe existir un resultado que refute tu hipótesis.

## Preguntas frecuentes

### ¿Más datos siempre reducen incertidumbre?
No; datos sesgados o irrelevantes pueden reforzar una conclusión incorrecta.

### ¿Sin certeza no se decide?
Se decide con riesgo explícito, reversibilidad y señales de revisión.

### ¿Qué significa que algo sea «estadísticamente significativo»?

Que, bajo ciertos supuestos del modelo, un resultado así sería poco probable si no hubiera
efecto. No dice que el efecto sea grande, importante ni causal. Esta clase no es un curso
de estadística: lo útil aquí es preguntar qué incertidumbre queda y si cambia la decisión.

### ¿Una sola ejecución de la prueba basta si pasa?

Depende de qué demuestre. Una prueba determinista que pasa una vez sobre una entrada
específica demuestra ese caso, no otros. Una prueba intermitente que pasa una vez no
demuestra nada sobre su causa de intermitencia. Cuanto más ruido tenga el fenómeno, más
repeticiones y más control del entorno necesitas.

### ¿Cómo evito el sesgo de confirmación en equipo?

Escribe antes qué resultado contaría en contra, pide a alguien que intente refutar y compara
explicaciones rivales en vez de aceptar la primera plausible. El sesgo no desaparece por ser
consciente de él; se mitiga con procesos que lo hacen visible.

## Fallo controlado y diagnóstico

En Python, compara dos formas de buscar un elemento (por ejemplo, una lista frente a un
conjunto) con `time.perf_counter` o con el módulo `timeit`. **Primera medición:** una sola
ejecución, con la caché fría de la primera llamada; concluye cuál es «más rápida». **Segunda
medición:** repite al menos treinta veces, alterna el orden de las dos variantes, descarta
solo con una regla escrita de antemano y registra mediana, dispersión y versión del entorno.
**Síntoma esperado:** la conclusión de la primera medición puede invertirse o volverse
indecidible. **Causa:** ruido de arranque, caché, orden de ejecución y un único punto. Anota
además qué resultado habría refutado tu hipótesis *antes* de medir, y un supuesto que tus datos
no controlan (por ejemplo, el tamaño de la entrada). Usa solo datos sintéticos.

## Errores comunes y cómo corregirlos

| Síntoma | Causa | Corrección |
| --- | --- | --- |
| una métrica se presenta como conclusión | se omitieron inferencia y supuestos | separa registro, interpretación y alternativa rival |
| benchmark sin configuración | se perdió trazabilidad | fija datos, entorno, versiones, orden y múltiples corridas |
| hipótesis imposible de refutar | se formuló una explicación elástica | escribe predicción y resultado que obligaría a cambiarla |
| promedio único | se ocultaron distribución y contexto | segmenta, observa colas y declara población |
| “necesitamos más datos” sin decisión | no se evaluó valor de información | indica qué dato puede cambiar qué opción y a qué costo |

## Entorno y archivos clave

Datos sintéticos, reloj monotónico cuando midas tiempo: `evidence-log.md`, `experiment.md`, `decision.md`.

## Seguridad, ética y accesibilidad

No recolectes datos personales «por si acaso». Documenta exclusiones de muestra y evita presentar promedios como experiencia universal.

## Puente hacia el trabajo con agentes

La distinción entre observación e inferencia se vuelve crítica con IA, porque un modelo
puede afirmar con fluidez «las pruebas pasan» sin haberlas ejecutado. Una afirmación del
agente es una *inferencia* o un informe, no una observación, hasta que existe un registro de
ejecución con comando, versión y salida que otra persona pueda reproducir. Del mismo modo,
sus resultados pueden variar entre ejecuciones: evaluar un flujo asistido exige repetir,
registrar configuración y definir de antemano el criterio de refutación, como en la figura 2.
El agente puede proponer hipótesis rivales y pruebas, lo cual es útil; la decisión sobre qué
evidencia basta sigue dependiendo de la figura 3, es decir, de reversibilidad e impacto.

## Transferencia

Aplica el método a rendimiento, usabilidad y seguridad; compara qué evidencia puede producirse sin causar daño.

## Evaluación y evidencia

Se exige trazabilidad, método reproducible, contraevidencia e incertidumbre que cambie la decisión.

## Fuentes

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), revisiones y criterios de éxito.
- [SWEBOK v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4), medición y práctica profesional.
- [ACM Code of Ethics](https://www.acm.org/code-of-ethics), honestidad y evaluaciones exhaustivas.
- [Documentación de `time.perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter) y [`timeit`](https://docs.python.org/3/library/timeit.html): reloj monotónico y método de medición repetida usados en el fallo controlado.
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/): por qué importan percentiles y colas además del promedio; respalda la figura 2.

## Límites y siguiente paso

No es un curso de estadística. `SE-007` usa esta disciplina para distinguir perspectivas de calidad.

---

[← SE-005](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) · [↑ Parte 00](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-00-ingenieria-de-software-como-profesion/README.md) · [SE-007 →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md)
