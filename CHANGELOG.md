# Changelog

## 2026-11-13 — Parte 26 desarrollada y profundizada con experimentos sintéticos reproducibles de datos, persistencia y recuperación

- las clases `SE-313`–`SE-324` pasan de borradores genéricos a clases completas sobre la capa de datos de la plataforma de entregas de tareas: modelado conceptual, lógico y físico, modelos relacional, documental, de clave-valor y de grafos, transacciones y aislamiento, restricciones e invariantes, consultas e índices,
  migraciones compatibles, replicación y partición, cachés entre capas, backups y pruebas de recuperación, privacidad, retención y ciclo de vida del dato, un taller de migración peligrosa y un paquete de capa de datos recuperable; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos de datos sintéticos y semilla fija, la mayoría sobre SQLite real: anomalías de una tabla plana, tamaño de la clave primaria y falsos positivos de una lista en una columna; filas frente a documentos, búsqueda por clave y consultas recursivas con ciclo; actualización perdida en 90 intercalaciones, cortes de una transferencia y sesgo de escritura;
  filas inválidas por capa de restricciones, comprobar y luego insertar y borrado con la clave foránea apagada; pasos con y sin índice, orden de un índice compuesto y costo de escritura; compatibilidad entre versiones, lotes de relleno y migraciones revertidas; lecturas obsoletas y cuórum, claves movidas por un anillo de hash y claves calientes;
  políticas de caché, estampida y carrera de relleno; pérdida por intervalo de copia, copia en caliente y niveles de verificación; restos tras borrar, retención y personas únicas; analizador de migraciones, ensayo en tres entornos y cortes de una migración; y validador de paquetes, un mes con dos incidentes y costo de retener copias;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los doce experimentos se ejecutaron en Windows (Python 3.12.9, SQLite 3.45.3) y en Ubuntu bajo WSL2 (3.12.3, SQLite 3.45.1) con cifras idénticas salvo los pasos de la máquina virtual del relleno por lotes (un 7 % mayores en Ubuntu con la misma proporción) y los bytes comprimidos con zlib (menos de un 1 % de diferencia); los datos son sintéticos, los parámetros son supuestos del autor,
  los dos validadores se afinaron con los mismos casos que los evalúan, el modelo de niveles de aislamiento, el cuórum, las cachés y la bitácora del mes simulado son modelos y no motores, y no se usó ningún servidor de bases de datos, base distribuida, caché real ni nube, ni se midió tiempo de reloj, de restauración ni cumplimiento legal; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: leer-sumar-escribir acierta en 6 de 90 intercalaciones de tres clientes; una lista de identificadores en una columna devuelve 33 099 resultados cuando los correctos son 7 408; con una restricción `UNIQUE` los duplicados dejan de colarse y el motor rechaza 108 inserciones; con las claves foráneas apagadas, que es el valor por defecto de SQLite, borrar un curso deja 50 entregas huérfanas sin error;
  un índice sobre una columna con el 90 % de las filas iguales ahorra un 3 %; el reparto por módulo mueve el 79,9 % de las claves al añadir un quinto nodo frente al 21,1 % de un anillo con 128 puntos; copiar el archivo de una base en uso da `integrity_check` en ok y una suma 197 unidades menor; los niveles de verificación estructurales ven 88 de 200 copias alteradas y todos los niveles 180;
  tras borrar la mitad de las filas siguen 2 087 de 2 090 ocurrencias de un valor en el archivo; tres atributos aparentemente inofensivos dejan únicas a 3 094 de 5 000 personas y un hash de correo sin clave se invierte por completo con un diccionario; un analizador de texto ve 141 de 200 mutaciones de una migración y ninguna de las que dañan los datos sin romper la sintaxis.

## 2026-11-13 — Parte 24 desarrollada y profundizada con análisis de código y simulaciones reproducibles

- las clases `SE-289`–`SE-300` pasan de borradores genéricos a clases completas sobre el componente `tarifas` de una plataforma de entregas: cohesión, acoplamiento y encapsulación, SOLID y sus límites, composición, herencia y delegación, patrones creacionales, estructurales y conductuales, patrones funcionales, reactivos y concurrentes, code smells y diagnóstico contextual, refactorización segura apoyada por pruebas, diseño para cambio, prueba y operación, complejidad accidental y esencial, deuda técnica, interés y opciones, un taller de refactorización de una función heredada y un proyecto de evolución compatible de un componente; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con código analizado con `ast` y simulaciones de semilla fija: LCOM4, sitios de edición y primer ciclo de dependencias; reglas añadidas, violaciones de Liskov e interfaces anchas; clase base frágil, orden de decoradores y herencia múltiple al azar; singleton y orden de pruebas, aislamiento de observadores y similitud entre patrones; detección de impureza, contrapresión e intercalaciones de dos hilos; umbrales de olores sobre código real fijado por commit, duplicación frente a parámetros y envidia de características; mutación, cobertura frente a mutantes y tamaño del paso de un refactor; módulos tocados por cambio, reloj real e inyectado y correlación de registros; la misma regla en dos formas, cobertura por pares y complejidad ciclomática y cognitiva; políticas de pago de deuda, refactorizar ahora o después y puntos calientes; maestro dorado por pasos, mutantes y caminos según las entradas; y firma frente a comportamiento, ventana de deprecación y contratos de consumidor;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- los experimentos usan solo la biblioteca estándar y se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas idénticas; los parámetros son supuestos del autor, el análisis de `SE-294` se fija al commit `4dafaa63` y no se midió ningún proyecto de producción, ningún reloj real, ningún hilo ni ningún consumidor real; el contenido sigue pendiente de revisión humana independiente.

## 2026-11-13 — Parte 23 desarrollada y profundizada con simulaciones sintéticas reproducibles

- las clases `SE-277`–`SE-288` pasan de borradores genéricos a clases completas sobre una plataforma educativa ficticia que incorpora una pieza de un dominio especializado en cada una: software científico y
  reproducibilidad, ingeniería de datos y procesamiento analítico, aprendizaje automático como componente de producto, videojuegos y simulación, gráficos, audio y realidad extendida, fintech e invariantes
  monetarias, salud y datos sensibles, cadenas de bloques y contratos inteligentes, sistemas geoespaciales y temporales, low-code y automatización visual, un taller de comparación de riesgos entre dominios
  y un proyecto de diseño profundo de un dominio elegido; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: orden de la suma, dispersión entre semillas y horizonte del caos; reintentos con duplicados, eventos tardíos y asimetría de claves; fuga de la
  etiqueta, prevalencia y alarmas de deriva; paso de tiempo fijo, atravesar una pared y espiral de la muerte; latencia y subcargas de audio, aliasing y fotogramas fuera de presupuesto; dinero con coma flotante,
  mutantes de un libro mayor y cobros duplicados; anonimización por generalización, fusión de fichas y fatiga de alarmas; prueba de trabajo, doble gasto y reentrada; distancia en grados, un año de reloj e índice
  de rejilla; caminos frente a pares, eventos duplicados y automatizaciones huérfanas; estabilidad de un ranking, acuerdo entre evaluadores y cobertura de controles; y mutaciones de un dosier, sensibilidad de
  supuestos y huella del paquete;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un puente hacia el trabajo con agentes;
- las simulaciones se ejecutaron con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas idénticas (salvo el orden de listado de elementos empatados en `SE-287`); los parámetros son supuestos
  del autor y las puntuaciones de riesgo de `SE-287` son un juicio ilustrativo; no se usó ningún código científico real, motor de procesamiento, modelo de aprendizaje automático, motor de juego, dato clínico,
  procesador de pagos ni red de cadena de bloques, no se midió confort ni percepción y no se evaluó ninguna norma;
- el alcance (480 clases publicadas, 540 planificadas) y los textos globales no cambian en esta entrada.


## 2026-11-13 — Guías por rol alineadas con el alcance de 540 clases: 42 guías

- dos guías nuevas, de más de 2.200 palabras cada una y con la misma estructura, generador y contrato que las demás: `Agentic Harness Engineer` (harness, contexto, herramientas, bucles, evaluación y recuperación de agentes) y `Domain & Methodology Engineer` (TDD, BDD, ATDD, DDD, contratos y SDD como práctica de equipo); el programa pasa de 40 a 42 guías profesionales;
- cada guía, el mapa del README y `roles/README.md` incorporan el estado real de cada parte (00–22 desarrolladas, 23–29 borradores, 30–39 estructura), una sección «Clases ya desarrolladas que sostienen la ruta hoy» con clases de las Partes 00–22 verificadas contra `curriculum.yaml` y una sección «Ampliación planificada» con las Partes 40–44 (`SE-481`–`SE-540`) por rol, sin enlaces porque esas clases no existen;
- las guías `ai-augmented-software-engineer`, `ai-systems-engineer`, `qa-test-engineer` y `software-architect` delimitan su frontera con las dos nuevas para evitar solapamiento;
- la tabla de cuerpos de conocimiento del README añade referencias a TDD, BDD, Gherkin, Specification by Example, DDD, Pact, GoF, POSA, PoEAA, Enterprise Integration Patterns, patrones cloud, ISO/IEC/IEEE 42010, estilos arquitectónicos, patrones agénticos, sistemas con LLM, evaluación de agentes, A2A, ISO/IEC 42001, Spec Kit y AGENTS.md; cada URL se comprobó con `curl` (las páginas de ISO responden 403 a clientes automatizados);
- «Cobertura disponible hoy» se corrige con los conteos reales (276 desarrolladas, 84 borradores, 120 con estructura y 60 planificadas); `STATUS.md`, `validate_repository.py` y `tests/test_roles.py` pasan a exigir 42 guías y a comprobar que ninguna guía enlace una parte planificada;
- los conteos generados del programa (480 clases publicadas, 40 partes) no cambian.

## 2026-11-13 — Documentación alineada con las Partes 00–22 y el alcance de 540 clases

- el estado publicado pasa de «Partes 00–05» a «Partes 00–22 (`SE-001`–`SE-276`) desarrolladas»; las páginas de las clases 73 a 276 dejan de marcarse como «contenido en revisión» y la revisión editorial humana independiente sigue declarada como pendiente;
- README, ROADMAP, STATUS, portal, guías de rol y estándar pedagógico describen el alcance planificado de 540 clases (Partes 40–44, `SE-481`–`SE-540`) sin publicarlo como clases: los conteos generados siguen siendo 480 clases y 40 partes;
- nueva decisión `ADR-004-expand-to-540-class-scope.md`.

## 2026-11-13 — Parte 22 desarrollada y profundizada con simulaciones sintéticas reproducibles

- las clases `SE-265`–`SE-276` pasan de borradores genéricos a clases completas sobre un nodo ambiental de una sala de estudio: hardware, firmware y software embebido,
  microcontroladores, periféricos y buses, restricciones de memoria, energía y cómputo, sistemas de tiempo real, interrupciones y estado compartido, protocolos IoT y conectividad
  intermitente, actualizaciones OTA y recuperación, identidad de dispositivo y gestión de claves, edge y pasarelas, safety, seguridad y vida útil prolongada, un taller de modelado
  de fallos y un dispositivo simulado operable y actualizable; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: latencia de un botón, un acumulador de 16 bits y mutantes de un antirrebote; eficiencia de I²C y SPI, errores no
  detectados por paridad, suma y CRC-8 y sobremuestreo de un convertidor; vida de una pila, desgaste de una flash y zona muerta de un filtro de enteros; planificabilidad rate-monotonic,
  plazos incumplidos e inversión de prioridad; posiciones de una interrupción, lecturas partidas y búfer circular; garantías de entrega, cola de almacenar y reenviar y tormenta de
  reconexión; cortes de energía en una actualización, actualización diferencial y despliegue por etapas; alcance de una clave extraída, ventanas de tiempo y semillas débiles;
  estrategias de reporte, decisión local o en la nube y codificación de la carga; votación con causa común, plazo de vigilancia y vuelta de un contador; inyección de fallos, cortes
  durante una escritura y estabilidad de un AMFE; y un mes de flota simulada, un validador de paquetes y una versión defectuosa en mil dispositivos;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- las doce simulaciones se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con cifras idénticas, sin excepción; los datos son sintéticos, los parámetros son
  supuestos del autor, los dos validadores se afinaron con los mismos casos que los evalúan y no se usó ningún microcontrolador, sistema operativo de tiempo real, agente MQTT,
  cargador de arranque, pasarela ni red real, ni se midió consumo, peor caso de ejecución o ataque alguno; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: sondear un botón en un bucle con radio da una espera máxima de 166 ms frente a 0,03 ms con una interrupción; 32 lecturas de 12 bits desbordan siempre un
  acumulador de 16 bits con señal alta; la paridad no detecta ningún error de dos bits; sobrescribir una imagen deja el dispositivo inservible en 17 de 19 cortes de energía; una
  espera exponencial sin jitter deja 4309 de 5000 dispositivos sin conectar a los 900 s; la comparación directa de tiempos decide mal el 33,35 % de los temporizadores armados antes
  de la vuelta de un contador de 32 bits; una deriva lenta pasa todas las comprobaciones locales y solo una referencia independiente la ve.

## 2026-11-13 — Parte 20 desarrollada y profundizada con experimentos sintéticos y modelos reproducibles de backend, APIs y procesamiento asíncrono

- las clases `SE-241`–`SE-252` pasan de borradores genéricos a clases completas sobre el backend de la plataforma de entregas de tareas: fronteras de confirmación, recursos y semántica de
  métodos, estilos de interfaz, validación y errores, identidad y autorización por objeto, idempotencia y reintentos, trabajo diferido, archivos extensos, caché y limitación de tasa,
  sondeos y apagado ordenado, un taller de reparación de una API defectuosa y un proyecto de servicio contractual; el portal publica ahora el contenido íntegro de las doce clases y el
  índice de la parte;
- 36 figuras con cálculos, simulaciones y mediciones de datos sintéticos y semilla fija: cadena síncrona frente a diferida, 24 escenarios de caída con y sin outbox y tres servidores HTTP
  locales, un GET con efecto frente a un rastreador, actualización perdida e `If-Match` y paginación por desplazamiento frente a clave, bytes por pantalla, consultas N+1 y coste de consultas
  anidadas, 14 cargas JSON contra dos validadores, deriva de un contrato y reintentos por clase de error, ocho ataques a un token, filas ajenas con y sin comprobación de dueño y cobertura de
  una política, duplicados con y sin clave, tormenta de reintentos y ventana de la clave, efectos duplicados en una cola, espera frente a M/M/1 y mensaje venenoso, memoria por trozos,
  subida reanudable, nombres hostiles y bombas de descompresión, aciertos y obsolescencia de una caché, estampida y cuatro limitadores, sondeos de vida, apagado con drenaje y
  calentamiento, tres suites contra una API con diez defectos, inyección SQL y caídas inyectadas, alertas por tasa de consumo y deriva de un contrato;
- cada clase añade tres secciones con experimentos, `Fallo controlado`, `Errores comunes`, `Preguntas frecuentes`, `Puente hacia el trabajo con agentes` y fuentes vinculadas a afirmaciones;
  los experimentos usan CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2 con salidas deterministas idénticas; las diferencias informadas son los tiempos de servidor local, las
  consultas al origen sin protección en una estampida de hilos, los nombres de archivo con barra invertida y los tiempos de comparación de firmas;
- los parámetros (latencias, porcentajes de caída, capacidades, SLO, defectos de la API y mutaciones) son supuestos del autor; no se midió a ninguna persona, producto ni servicio, y las
  fuentes sin enlace verificado en esta ejecución (por falta de acceso de red autorizado) se citan por título y se enumeran en `Evidencia medida y límites`;
- la guía de la parte incorpora una sección «Evidencia medida y límites», el resumen operativo y el proyecto integrador.

## 2026-11-13 — Parte 21 desarrollada y profundizada con experimentos sintéticos y modelos reproducibles de software móvil, escritorio y multiplataforma

- las clases `SE-253`–`SE-264` pasan de borradores genéricos a clases completas sobre el cliente de la plataforma de entregas de tareas: modelos de aplicación, ciclo de vida y restauración
  del estado, decisión de construcción, almacenamiento local y fusión, permisos y capacidades, interacción y accesibilidad, distribución y versiones que conviven, trabajo sin conexión y
  conflictos, presupuesto de recursos, seguridad del cliente, un taller de adaptación a dos plataformas y un proyecto con sincronización; el portal publica ahora el contenido íntegro
  de las doce clases y el índice de la parte;
- 36 figuras con cálculos, simulaciones y mediciones de datos sintéticos y semilla fija: dos copias sobre un archivo compartido, controles alcanzables según el ancho y arranques en frío,
  ediciones perdidas por política de guardado, restauración con tres políticas de lectura y coste de guardar de forma atómica, pesos sorteados de cuatro opciones, coste de una frontera
  entre capas y capacidades comunes, modos de SQLite, terminación a mitad de escritura y fusión por registro o campo, estados de permiso, revocación y unicidad de la ubicación, acierto
  de toques simulados, orden de foco y contraste, adopción por canal, clientes rotos al retirar un campo y descarga por bloques, estructuras replicadas, duplicados y relojes desfasados,
  lista completa o ventana, sondeo, lote y empuje y tamaño de caché, integridad, confinamiento de rutas y secretos, siete diferencias entre Windows y Ubuntu, coste de adaptación con
  intervalo y contrato de adaptadores, sincronización con fallos, un servidor local con clave de idempotencia y 240 mutaciones de un paquete;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas deterministas idénticas salvo los tiempos, la versión de SQLite (3.45.3 y 3.45.1)
  y los siete comportamientos de sistema que `SE-263` mide porque difieren; los datos son sintéticos, los parámetros son supuestos del autor, no se usó ningún teléfono, emulador, SDK,
  tienda ni biblioteca de producción, no se midió la batería ni se cortó la energía y los secretos y rutas son ficticios; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: dos copias de una aplicación sobre un mismo archivo dejan 127,65 de 200 actualizaciones; con una recuperación de memoria agresiva el 66,5 % de los regresos
  parte de cero; guardar solo al cerrar pierde 109 ediciones por sesión y combinar guardado periódico y de segundo plano 1,7; el ganador de una tabla de decisión cambia con una
  unidad en las puntuaciones en el 41 % de los casos; 500 inserciones tardan 2874 ms en transacciones separadas y 8 ms en un lote; un par de lugares a 1 km identifica al 99,1 % de
  2000 personas ficticias; un gris habitual queda a 0,02 del contraste mínimo; retirar un campo a los 30 días rompe al 73,7 % de un canal empresarial lento; reintentar sin identificador
  convierte 30 operaciones en 44; siete de siete comportamientos del sistema de archivos difieren entre Windows y Ubuntu; y un validador de presencia deja pasar 104 de 240 mutaciones.

## 2026-11-13 — Parte 18 desarrollada y profundizada con experimentos sintéticos y procesos locales reproducibles

- las clases `SE-217`–`SE-228` pasan de borradores genéricos a clases completas sobre `notas`, una herramienta de línea de comandos sintética de la plataforma de entregas: diseño de la
  superficie de una CLI, entrada y salida estándar y tuberías, configuración y precedencia, códigos de salida y diagnóstico, presentación en terminales y accesibilidad, servicios y
  ciclo de vida, planificadores, trabajadores y lotes, automatización idempotente y reanudable, distribución y actualización de binarios, telemetría opt-in, un taller de
  endurecimiento y un paquete operable multiplataforma; el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos, simulaciones y mediciones de procesos locales: abreviaturas de flags que dejan de valer, contrato observable de una CLI, búfer y cierre de tuberías,
  seis resolvedores de precedencia frente a 64 combinaciones, códigos de salida por sistema, coste de los reintentos, color y truncado en tuberías, ancho de nombres Unicode,
  terminación y preparación de servicios, políticas de solape y trabajos venenosos, seis estrategias de escritura frente a 40 caídas, integridad y lanzamientos escalonados,
  unicidad de atributos y sesgo del opt-in, diez fallos inyectados, citado de argumentos y trece pruebas de contrato con seis defectos y 102 mutantes de un manifiesto;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo las diferencias que se informan como resultados (el código
  de salida fuera de 0–255, la excepción de una tubería cerrada, `terminate()` frente a `SIGTERM`, el reemplazo de un archivo abierto, el citado con `shell=True`, el salto de línea
  del hash de un archivo y los tiempos); los datos son sintéticos, los parámetros son supuestos del autor, los defectos inyectados son variaciones sobre herramientas de juguete y
  no se usó ningún terminal interactivo, servicio de Windows, systemd, orquestador, cola real ni telemetría de personas; la parte no tiene laboratorio en `labs/`;
- `build_phase3.py` y `build_phase4.py` publican ahora el contenido de `content/part-XX/` también para las clases de la fase 4 que lo tienen (`published_markdown`);
- hallazgos del análisis: un flag nuevo rompió 9 de 14 abreviaturas que funcionaban; `sys.exit(256)` se lee como éxito en Linux y como 256 en Windows; `false | cat` devuelve 0; el
  color partió la búsqueda de una frase en 200 líneas; `terminate()` no ejecuta limpieza en Windows; reintentar todo gastó 24 092 intentos inútiles; la estrategia «anexar y marcar»
  duplicó en 19 de 40 caídas; `os.replace` falla con el destino abierto en Windows; seis de diez atributos hicieron únicas a dos de cada tres instalaciones; la versión frágil de una
  copia de seguridad dañó en silencio 7 de 10 escenarios; y una suite de contrato descubrió que `allow_abbrev` no se hereda en los subcomandos.

## 2026-11-13 — Parte 19 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-229`–`SE-240` pasan de borradores genéricos a clases completas sobre una aplicación web de entregas de tareas con conectividad irregular: HTML semántico, contraste y
  cascada, JavaScript, DOM y eventos, renderizado en cliente, servidor, estático e híbrido, estado y datos remotos, formularios y validación, URLs y enrutado, rendimiento y presupuestos,
  seguridad del navegador, PWA y sincronización, SEO y metadatos, un taller de flujo resiliente y un proyecto de aplicación accesible y offline; el portal publica ahora el contenido
  íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: un linter semántico con 220 mutaciones y la razón de contraste de 5000 pares de colores, una carrera de
  especificidad, un modelo de dos colas del bucle de eventos contrastado con Node y una delegación de eventos en un modelo de DOM, bytes reales y un modelo de tiempo de tres
  estrategias de renderizado, desajustes de hidratación y obsolescencia por caducidad, reconciliación de listas, estado copiado frente a derivado y respuestas fuera de orden,
  seis validadores de correo y normalización Unicode, normalización de URLs, enrutado y estado en la URL, compresión, ruta crítica y percentiles con pocas visitas, codificación por
  contexto, políticas de contenido, SameSite y CORS, estrategias de caché, descargas por versión y duplicados al sincronizar, dos analizadores de `robots.txt`, navegación facetada y
  un auditor de metadatos, una máquina de estados mutada, reintentos con y sin dispersión y defectos de accesibilidad automatizables, y un validador de manifiesto, una auditoría de
  cabeceras de un servidor local y una suite de pares frente a defectos de tres factores;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9, Node 24.11) y en Ubuntu bajo WSL2 (3.12.3, Node 20.20) con salidas idénticas salvo los tiempos de compresión y de render;
  los datos son sintéticos, los parámetros son supuestos del autor, las reglas de los linters se escribieron sabiendo qué mutaciones se aplicarían, y no se usó ningún navegador,
  lector de pantalla, service worker real, buscador ni herramienta de auditoría ni se midió a ninguna persona; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: un linter de ocho reglas detecta 200 de 220 mutaciones y ninguna de las 20 que cambian el significado de un texto alternativo; solo 11 % de los pares de colores
  aleatorios alcanza 4,5:1; un modelo de dos colas acierta el orden de 300 programas y uno de una cola 221; un total copiado diverge en 13,5 % de las secuencias con 1 % de olvidos; la
  última respuesta recibida deja un resultado obsoleto en 34,67 % de las búsquedas; con 30 visitas se declara que se cumple un presupuesto que no se cumple en 22 % de los casos; sin clave
  de idempotencia 2000 envíos producen 476 duplicados; el reintento exponencial sin dispersión tarda 902 s frente a 23 s con dispersión; y una suite de pares halla 32 de 60 defectos de tres
  factores.

## 2026-11-13 — Parte 17 desarrollada y profundizada con experimentos sintéticos y de Git reproducibles

- las clases `SE-205`–`SE-216` pasan de borradores genéricos a clases completas sobre el portal documental de la plataforma de entregas de tareas: audiencias y tareas, los cuatro
  tipos de página, README y primer éxito, registros de decisiones, diagramas generados, documentación de una API con ejemplos ejecutables, runbooks, documentación como código,
  búsqueda y glosarios, documentación para máquinas y agentes, un taller de reconstrucción de conocimiento perdido y un portal versionado con paquete reproducible y auditoría; el
  portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: clics hasta una página y coherencia de un dato repetido, un clasificador de tipos de página y un tutorial
  ejecutable, un embudo de pasos y un detector de deriva del README, un linter de ADR y la caducidad de sus suposiciones, cruces de aristas y un generador de diagramas estable, ejemplos
  de una API y los códigos de un servidor local, idempotencia de los pasos de un runbook, enlaces rotos y huellas de construcción, búsqueda con sinónimos, fragmentación de documentos
  para recuperación, el factor de camión y `git log -S`, versiones etiquetadas y un paquete zip reproducible;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9, Git 2.55) y en Ubuntu bajo WSL2 (3.12.3, Git 2.43) con salidas idénticas; durante el trabajo aparecieron dos
  diferencias entre sistemas que se corrigieron y se documentan: un servidor local que responde 413 sin leer el cuerpo aborta la conexión en Windows y no en Ubuntu, y un zip con
  orden, fecha y permisos fijos tenía huellas distintas en cada sistema hasta fijar también el campo de sistema de origen; los datos son sintéticos, los parámetros son supuestos
  del autor, las reglas léxicas se probaron con casos construidos por el propio autor, no se usó ningún modelo de lenguaje, herramienta de documentación de producción ni portal real,
  y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: con tres cambios al año, un dato repetido en seis páginas solo sigue coherente el 5,3 % de las veces; un linter de ADR que ve la forma no detecta ninguna de
  las alternativas vacías; renombrar 5 archivos y 8 títulos rompe 66 enlaces; el 55 % de las respuestas de un servidor ante peticiones erróneas lleva códigos no documentados; un
  linter que ignora los bloques de código da 102 avisos de los cuales 97 son falsos; fragmentar por 500 caracteres separa la regla de su excepción en dos de cada tres casos; un
  filtro léxico detecta las 6 instrucciones ocultas literales y ninguna de las 8 ofuscadas; cuando se va la persona con más commits queda sin responsable el 45 % de los archivos.


## 2026-11-13 — Parte 16 desarrollada y profundizada con experimentos reproducibles de Git y colaboración

- las clases `SE-193`–`SE-204` pasan de borradores genéricos a clases completas sobre el repositorio de la plataforma de entregas de tareas: modelo de objetos y áreas de Git, commits
  atómicos y recuperación, integración con fusión, rebase y squash, revisión por riesgo, flujos de ramas, trazabilidad de issues, propietarios y convenciones, contribución externa y
  gobernanza, licencias, firmas y protección del repositorio, un taller de rescate de una integración y un proyecto de contribución revisable; el portal publica ahora el contenido
  íntegro de las doce clases y el índice de la parte;
- 36 figuras con experimentos de Git real en repositorios temporales con identidad y fechas fijas o con datos sintéticos y semilla fija: identificadores de blob, árbol y commit
  reconstruidos a mano, estados entre las tres áreas, objetos sueltos frente a empaquetados, bisección sobre cuatro historias, qué sobrevive a seis errores, reiniciar frente a
  revertir, fusión, rebase y squash, probabilidad de conflicto según distancia y ediciones, `rerere`, `range-diff`, triaje por riesgo de 300 pull requests sintéticos, pilas de PR,
  conflictos según la vida de la rama, un conflicto semántico, backports, extracción de cierres con dos reglas, reproducción según el detalle del informe, una matriz de trazabilidad,
  un archivo de propietarios sobre 600 rutas, un validador de mensajes, autoría tras un reformateo, concentración de commits, reglas de decisión, un fork desfasado, un analizador de
  expresiones de licencia, un inventario transitivo, la huella de un texto de licencia, firmas SSH, la reescritura de una cadena de firmados, políticas de protección, seis órdenes de
  fusión de tres ramas, tres rescates, estilos de marcas y un validador de doce comprobaciones sobre catorce contribuciones;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9 y Git 2.55) y en Ubuntu bajo WSL2 (Python 3.12.3 y Git 2.43) con salidas idénticas salvo los tiempos de firma y verificación
  de commits; los datos son sintéticos, los parámetros son supuestos del autor, la clave de firma es desechable, la regla de cierres y el modelo de CODEOWNERS simplifican los de una
  plataforma, y no se usó ningún alojamiento, servicio de firma ni herramienta de inventario de licencias; la parte no tiene laboratorio en `labs/` y no ofrece asesoría legal;
- hallazgos del análisis: agrupar cuatro cambios por commit ahorra dos ejecuciones de bisección y multiplica por 2,5 las líneas que hay que leer; un cambio sin agregar o un archivo sin
  rastrear no se recuperan tras un `reset --hard`; reiniciar y forzar la publicación hace reaparecer los commits «borrados» cuando otro clon publica; las ediciones en líneas contiguas
  entran en conflicto el 100 % de las veces; una fusión sin conflicto de texto dejó un panel imprimiendo 42 en lugar de 60; revertir una fusión mala y volver a fusionar responde
  «Already up to date»; una comparación literal decidió mal 146 de 300 expresiones de licencia y un análisis de dependencias directas no ve el 89 % de los paquetes fuera de política;
  una prueba que afirma `True` pasa las doce comprobaciones de forma.

## 2026-11-13 — Parte 15 desarrollada y profundizada con simulaciones sintéticas reproducibles

- las clases `SE-181`–`SE-192` pasan de borradores genéricos a clases completas sobre el plan de lanzamiento de la plataforma de entregas de tareas: modelos predictivos, iterativos
  e incrementales, principios ágiles frente a ceremonias, Scrum, Kanban, XP y Shape Up leídos por sus políticas, Lean, teoría de colas y límites de trabajo, estimación con rango y
  evidencia histórica, planificación de entregas y dependencias, riesgos, supuestos, issues y decisiones, definiciones de listo, terminado y aceptación, métricas de flujo, calidad
  y resultados, retrospectivas y mejora del sistema de trabajo, un taller de planificación bajo incertidumbre y un plan adaptativo con disparadores y barreras; el portal publica
  ahora el contenido íntegro de las doce clases y el índice de la parte, y `build_phase4.py` usa las fuentes editoriales de `content/part-15/` para esas clases;
- 36 figuras con simulaciones de datos sintéticos y semilla fija: esfuerzo según el intervalo de retroalimentación, valor si el proyecto se corta y cruce según la volatilidad;
  valor perdido por no aprender del uso, sobrecoste de ceremonias y conflictos según la vida de una rama; espera de un urgente, reglas de compromiso y tiempo fijo; espera según la
  utilización, ley de Little con límite de trabajo y variabilidad con lotes; suma de medianas, cobertura de intervalos y solape de tallas; convergencia de caminos, dependencias
  externas y órdenes de entrega; riesgos con causa común, orden de validación de supuestos y un verificador de decisiones; comprobaciones correlacionadas, refinamiento previo y un
  verificador de criterios; resumen de tiempos, velocidad premiada y tamaño de muestra de un percentil; acciones por retrospectiva, detección de una mejora e intervenciones sobre una
  cola; calibración de pronósticos, margen frente a colchón y sensibilidad; disparadores de replanificación, un validador de planes y mil proyectos con tres estrategias;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- las doce simulaciones se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas, sin excepción; los datos son sintéticos, los parámetros son
  supuestos del autor, los tres verificadores se afinaron con pocos ejemplos y se evaluaron con casos propios o nuevos mínimos, y no se observó ningún equipo ni se midió ninguna
  estimación, retrospectiva o métrica real; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: el intervalo de menor esfuerzo está en ciclos de cuatro piezas y no en el más corto; comprometer la media del rendimiento falla en 44 % de los sprints;
  la espera se multiplica por 19 entre 50 % y 95 % de utilización; cumplir la suma de medianas de 30 tareas ocurre en 12,4 % de los casos; un intervalo del 80 % con 3 semanas de
  historia cubre 32,5 %; con una causa común el percentil 85 del retraso de diez riesgos sube de 35 a 66 días; añadir comprobaciones correlacionadas deja los escapes en 4258 de 10 000;
  acordar 8 acciones por retrospectiva termina las mismas 9,4 que acordar 2; un disparador de 4 semanas con un aviso da falsa alarma en 68 % de los proyectos sanos.

## 2026-11-13 — Parte 14 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-169`–`SE-180` pasan de borradores genéricos a clases completas sobre la entrega de una tarea en la plataforma de entregas: diseño centrado en personas y tareas,
  arquitectura de información, interacción y retroalimentación, estados vacíos, de carga y de error, criterios de accesibilidad, semántica, teclado y foco, diseño visual,
  adaptación a anchos y preferencias, internacionalización, medición de usabilidad, un taller de auditoría y reparación y un prototipo evaluado; el portal publica ahora el
  contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: tres diseños cronometrados con operadores, la persona promedio en varias dimensiones y un embudo,
  anchura de menús, ordenamiento de tarjetas y alcance de un grafo, tamaño del objetivo, doble envío y confirmar frente a deshacer, estados imposibles, reintentos y latencias,
  razones de contraste, un auditor de reglas y destinos, orden de foco, nombre accesible y encabezados, daltonismo, reflujo e inversión de colores, anchos de pantalla, matriz
  de preferencias y peso de imágenes, plurales, Unicode y fechas ambiguas, problemas hallados, intervalos y potencia, una auditoría con órdenes de reparación y mutaciones y
  la probabilidad de ver una barrera, la cobertura de modalidades y kappa;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas; los datos son sintéticos, los parámetros son supuestos del autor
  o valores medios de la literatura, las matrices de daltonismo son una aproximación, y no se usó ningún escáner de producción, lector de pantalla, navegador ni biblioteca de
  localización ni se evaluó a ninguna persona; la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: un formulario de nueve campos tarda 50,7 s frente a 18,6 s con tres; con diez dimensiones ninguna de 5 000 personas es promedio en todas; una sola
  etapa de seis pierde 315 de 1 000 personas; un auditor de reglas detecta 7 de 12 defectos y ninguno de los presentes pero incorrectos; el rojo y el verde caen de 119,8 a 7,3 de
  distancia en deuteranopía; invertir colores hace perder el contraste a 956 de 2 441 pares que lo cumplían; la regla de «uno o plural» falla en 120 de 121 números en ruso; cinco
  participantes hallan 62 % de los problemas frente al 76,6 % de la fórmula; y declarar conformidad ignorando lo no probado permite 368 de 1 000 afirmaciones que una política
  estricta no admite.

## 2026-11-13 — Parte 13 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-157`–`SE-168` pasan de borradores genéricos a clases completas sobre la regla de penalización por entrega tardía de una plataforma de entregas: especificación
  informal, semiformal y formal, ejemplos y BDD, contratos e invariantes, modelos, máquinas de estados, esquemas, interfaces y eventos, compatibilidad y versionado, papel de la
  especificación frente al código, pruebas contractuales, un taller y un paquete de especificaciones trazables; el portal publica ahora el contenido íntegro de las doce clases y
  el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: dieciséis lecturas de una frase y huecos de una tabla de decisión, variantes defectuosas frente a suites
  de ejemplos y cobertura de pares, contratos frente a pruebas de ejemplo y subtipado, deriva entre modelo y código y normalización en SQLite, búsqueda en anchura con contraejemplo,
  explosión de estados e intercalados de una carrera, esquemas abiertos y cerrados y una expresión regular con retroceso, un linter OpenAPI, eventos duplicados y reordenados,
  compatibilidad entre lectores y ventanas de deprecación, deriva y regeneración de código, contratos de consumidor frente a un doble, un bucle de contraejemplos y un validador
  de trazabilidad con huellas;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y Crossref y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo los tiempos, la versión de SQLite (3.45.3 y 3.45.1), las
  latencias de un servidor local y la huella de un paquete escrito con el modo de texto por defecto; los datos son sintéticos, los parámetros son supuestos del autor, las reglas
  léxicas se afinaron con pocos ejemplos y se probaron con seis casos nuevos, y no se usó ninguna herramienta de producción ni se auditó una API real; la parte no tiene laboratorio
  en `labs/`;
- hallazgos del análisis: el ejemplo más típico elimina solo la mitad de las dieciséis lecturas de una frase; tres ejemplos elegidos matan los nueve mutantes distinguibles que diez
  al azar no matan; cinco pruebas de ejemplo no detectan ninguno de nueve defectos que los contratos sí detectan; una expresión regular tarda 1,65 s con 25 caracteres; comprobar
  una deriva cada 20 commits la deja 13 commits; el mismo paquete tiene dos huellas distintas en Windows y Ubuntu si no se fija el salto de línea.


## 2026-11-13 — Parte 12 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-145`–`SE-156` pasan de borradores genéricos a clases completas sobre el requisito conductor de la plataforma de entregas de tareas (recuperar el borrador
  cuando la sesión expira): elicitación, análisis, especificación y validación, requisitos funcionales y reglas de negocio, atributos de calidad y restricciones, casos de
  uso, historias y job stories, criterios de aceptación y ejemplos, priorización con dependencias y negociación, trazabilidad, requisitos regulatorios, de datos y
  seguridad, gestión de cambios y líneas base, ambigüedad, contradicción e incompletitud, un taller de reparación y un proyecto de especificación revisable; el portal
  publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: cobertura de elicitación y revisión con defectos desiguales, tabla de decisión con huecos,
  horas locales inexistentes y mutantes frente a suites, media frente a percentil, ventanas de disponibilidad y costo de PBKDF2, caminos de un caso de uso y corte
  vertical, mutantes y pruebas de pares, dependencias, inflación de Must y ciclos de mayoría, densidad de trazabilidad y trazas con `sys.settrace`, variantes de una regla
  de retención, STRIDE por elemento y cadena de hashes, alcance de cambios y hash normalizado, lecturas de frases con conectores y conflictos mínimos, la regla de tres, y
  un validador de especificaciones con 16 mutaciones y captura–recaptura;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y un puente
  hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo los tiempos de PBKDF2 de `SE-147` y las latencias de
  un servidor local de `SE-155`; los datos son sintéticos, los parámetros son supuestos del autor y las reglas léxicas se afinaron con pocos ejemplos: no hubo personas,
  organizaciones ni normas interpretadas, y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: ocho entrevistas cubren 77,2 % de 40 requisitos sintéticos por el conocimiento tácito; cinco reglas razonables dejan 4 de 24 combinaciones con hueco
  o conflicto; la media cumple «menos de 2 s» mientras el percentil 99 no; los ejemplos felices detectan 0 de 10 mutantes y las fronteras los 10; los primeros k por
  valor/costo no son entregables; ningún par de doce requisitos se contradice y el conjunto sí; y un validador con 11 de 16 mutaciones detectadas deja pasar los defectos semánticos.
## 2026-11-13 — Parte 11 desarrollada y profundizada con experimentos de economía, métricas y decisiones

- las clases `SE-133`–`SE-144` pasan de borradores genéricos a clases completas sobre la economía de la plataforma de entregas de tareas: modelos de negocio y sostenibilidad,
  costos de construcción, operación y oportunidad, resultados frente a actividad, adopción y retención, telemetría y consentimiento, experimentos y causalidad, métrica norte
  con guardas, FinOps y costo por resultado, portafolio y opciones, decisiones reversibles, un taller de árbol de métricas y un proyecto de caso de viabilidad; el portal publica
  el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: razón de valor de vida y costo de adquisición como intervalo, tres modelos de precio y concentración
  de ingresos, costo de propiedad y suma de medianas, tasa de descuento que invierte un ranking, meta de cerrados frente a resueltos, registros acumulados frente a activos,
  curva de retención por mezcla y cohortes incompletas, sesgo por consentimiento y unicidad por campos, once mutantes de una puerta de consentimiento, sesgo de selección, control
  de proporciones y regresión a la media, optimización con y sin guarda, alarmas con varias guardas, reparto de costos con tres reglas y compromiso de capacidad, arrepentimiento
  de una cartera, valor de un piloto, secuencias con dependencias, umbral de reversibilidad, seis migraciones en SQLite, despliegue progresivo, dos validadores con dieciséis
  mutaciones cada uno, descomposición exacta, oscilación del valor presente y compuerta de abandono;
- tres secciones nuevas por clase, preguntas frecuentes, tabla de errores, ejercicios y fallo controlado propios de cada una, un puente hacia el trabajo con agentes y fuentes
  primarias verificadas con `curl` (la página del Reglamento (UE) 2016/679 en EUR-Lex no respondió desde el entorno de ejecución y se sustituyó por las directrices del EDPB; dos
  páginas que devolvieron 403 se excluyeron);
- hallazgos del análisis: contar cohortes incompletas como no retenidas baja una retención de 34 % a 27 %; una tasa constante ajustada a cuatro semanas subestima 15 veces la
  retención a 26 semanas; tres pruebas del camino feliz matan 2 de 11 mutantes de una puerta de consentimiento y nueve pruebas dirigidas matan 10; una compuerta de abandono no
  elevó el valor esperado en ningún umbral y solo redujo el riesgo; solo 3 de 6 migraciones vuelven con todos sus datos;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (Python 3.12.3) con salidas idénticas, salvo la versión de SQLite (3.45.3 y 3.45.1); la parte no
  tiene laboratorio en `labs/`; todos los precios, costos, tasas y probabilidades son supuestos del autor en unidades ficticias y no se midió ninguna plataforma, empresa o persona.

## 2026-11-13 — Parte 09 profundizada con experimentos de bibliotecas, paquetes, SDK y automatización

- 36 figuras para `SE-109`–`SE-120` con mediciones reales: pila de llamadas de biblioteca y framework, costo de importar y timeout por defecto, versiones PEP 440
  frente a SemVer, cambios de firma y de contrato, un resolutor con retroceso, `pip` sobre ruedas locales y hashes, ruedas sin y con `package-data`, sombras en `sys.path` y
  etiquetas, códigos de salida, precedencia de configuración y tuberías, idempotencia, escritura atómica y actualización perdida, carga y aislamiento de plugins, generación
  determinista e inyección en plantillas, metadatos y expresiones de licencia y cobertura SPDX de este repositorio, tiempo hasta el primer éxito, errores y obsolescencia,
  siete defectos de empaquetado, doce mutantes de un SDK, archivo de referencia de la CLI y compilaciones reproducibles;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las doce clases, por versiones
  específicas de cada una; fuentes primarias verificadas con `curl` (dos páginas de gnu.org devolvieron 403 y se excluyeron) y un puente hacia el trabajo con agentes;
- hallazgos del análisis: el orden de `entry_points` difiere entre Windows y Linux con el mismo código; un bloqueo `O_EXCL` mató a un proceso en Windows con `PermissionError`;
  setuptools 84.0.0 incluye `py.typed` por sí solo y 68.1.2 no; la rueda sale distinta entre plataformas aun con `SOURCE_DATE_EPOCH`; este repositorio no tiene cabeceras SPDX
  en ninguno de 3 176 archivos revisados;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); la parte no tiene laboratorio en `labs/`; los tiempos son de un equipo y no se midieron
  otros constructores, gestores, intérpretes ni macOS.
## 2026-11-13 — Parte 10 desarrollada y profundizada con experimentos sintéticos reproducibles

- las clases `SE-121`–`SE-132` pasan de borradores genéricos a clases completas sobre una plataforma de entregas de tareas: síntomas frente a causas, actores y contextos,
  entrevistas y evidencia cualitativa, hipótesis, propuesta de valor, segmentos y mercado, experimentos, priorización, ética y protección de participantes, criterios de
  abandono, un taller y un proyecto integrador (brief respaldado por evidencia); el portal publica ahora el contenido íntegro de las doce clases y el índice de la parte;
- 36 figuras con cálculos y simulaciones de datos sintéticos y semilla fija: conteo de frases frente a causas y dimensionamiento con rangos, usuario promedio y paradoja de
  Simpson, saturación de temas y kappa, sensibilidad de supuestos y comparaciones múltiples, estabilidad de rankings y de k-means frente a ruido, tamaño de muestra y
  falsos positivos al mirar varias veces, RICE bajo perturbación y coste del retraso, unicidad por cuasi-identificadores y reversión de un hash, reglas de abandono y zona
  gris, y un validador de briefs con doce mutaciones;
- tres secciones nuevas por clase, preguntas frecuentes, errores, ejercicios y fallos controlados propios de cada una, fuentes primarias verificadas con `curl` y un puente
  hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Ubuntu bajo WSL2 (3.12.3) con salidas idénticas salvo los tiempos de hash de `SE-129`; los datos son
  sintéticos, los parámetros son supuestos del autor y las reglas léxicas se afinaron con pocos ejemplos y se probaron con casos nuevos mínimos: no hubo personas, usuarios
  ni mercados reales, y la parte no tiene laboratorio en `labs/`;
- hallazgos del análisis: la frase más repetida de 600 tickets no coincide con la causa más frecuente; con cinco atributos corrientes el 64,2 % de 500 participantes es único;
  un hash sin clave de siete dígitos se revierte en 16–20 s; mirar 10 veces una prueba A/A produce 21,1 % de falsos positivos; una regla léxica con 100 % de acierto en sus
  ejemplos acierta 50 % con preguntas nuevas.

## 2026-11-13 — Parte 08 profundizada con experimentos de herramientas y entornos

- 36 figuras para `SE-097`–`SE-108` con mediciones reales: un intercambio LSP con `ruff server`, una sesión de `pdb` y el costo de observar la ejecución, perfiladores
  por llamada, de memoria y por muestreo, la matriz de defectos de ruff y mypy, el estado oculto de un cuaderno, el arranque y la resolución de intérpretes,
  entornos virtuales, la instalación de una rueda local, reducción de casos y bisección, contraste WCAG y la reproducibilidad de una rueda;
- tres secciones nuevas por clase y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios por versiones específicas de cada clase; fuentes verificadas y un puente hacia agentes;
- con el motor de Docker en marcha se construyó una imagen mínima desde `scratch` (9 383 bytes, dos construcciones con identificadores distintos) y se creó un contenedor en 314 ms; no se arrancó ningún proceso en un contenedor y se declara como límite; los tiempos son de un equipo y se leen como razones.

## 2026-11-13 — Parte 05 profundizada con mediciones y mutaciones del laboratorio

- 36 figuras para `SE-061`–`SE-072` con datos reales: expresiones y tipos, tabla de verdad, recursión y memoria de iteradores, argumentos por defecto y cierres,
  jerarquía y costo de excepciones, colecciones, codificaciones y plataformas, `json`, grafo de importaciones, diez mutaciones de la suite del laboratorio,
  métricas con `ast`, un refactor protegido, semántica Python/Rust (Rust solo documentada) y catorce invocaciones de la CLI con sus códigos de salida;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, errores, ejercicios y fallos controlados genéricos por versiones propias de cada clase;
  fuentes primarias verificadas y un puente hacia el trabajo con agentes;
- hallazgos del análisis: seis de diez mutaciones sobreviven a la suite original, cinco se cierran con pruebas nuevas (verificadas en una copia) y la sexta es
  equivalente; los mensajes de error de la CLI incluyen la ruta absoluta del archivo;
- las quince pruebas del laboratorio se ejecutaron en Windows (Python 3.12.9) y Linux (3.12.3); `rustc` no estaba disponible y el puerto Rust no se compiló.

## 2026-11-13 — Parte 07 profundizada con experimentos de estructuras y algoritmos

- 36 figuras para `SE-085`–`SE-096` con mediciones y cuentas reales: capacidad de listas y `pop(0)` frente a `deque`, colas de prioridad y empates,
  colisiones de hash y claves mutadas, altura de árboles (BST, AVL, trie y `bisect`), BFS frente a DFS y representaciones de grafos, comparaciones por
  algoritmo de ordenamiento, monedas, intervalos y mochila, n reinas y poda, índices de SQLite, filtros de Bloom y Count-Min, pendientes log-log y
  ruido de medición, matrices de compromisos por carga y mutantes frente a un oráculo diferencial;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las doce clases,
  por versiones específicas de cada una; fuentes primarias verificadas (enlaces con `curl`, DOI con Crossref) y un puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); la parte no tiene laboratorio en `labs/`; los tiempos son de un
  equipo y varían entre pasadas (una pendiente dio 1,21 y luego 1,02), y no se midieron otros intérpretes ni cargas reales.

## 2026-11-13 — Parte 06 profundizada con experimentos de paradigmas ejecutados

- 36 figuras para `SE-073`–`SE-084` con mediciones reales: aliasing y costo de copiar, costo de llamar funciones y límite de
  recursión, memoria con `__slots__`, resolución de herencia, formas de filtrar, planes de consulta de SQLite, conflictos entre reglas,
  costo del orden de las metas y unificación, orden y bloqueo del bucle de `asyncio`, contrapresión, condición de carrera, hilos frente a
  procesos y buzones, y una misma regla en cinco paradigmas con contrato común, superficie de cambio y mutantes;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las
  doce clases, por versiones específicas de cada una; fuentes primarias verificadas (los DOI de ACM bloquean `curl` y se marcan como no verificados) y un
  puente hacia el trabajo con agentes;
- los experimentos se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); la parte no tiene laboratorio en `labs/`; no se ejecutaron Prolog,
  Erlang, Rust ni bibliotecas reactivas, y se declara como límite.

## 2026-11-13 — Parte 04 profundizada con cálculos y mediciones reales

- 36 figuras para `SE-049`–`SE-060`: descomposición del incidente, implicación y modelos, orden topológico y ciclos, aserciones y contratos,
  recursión y memoización, terminación (Euclides y Collatz), crecimiento al duplicar n, heurísticas frente al óptimo, máquina de estados de un pedido,
  bisección y pruebas intermitentes, requisitos contradictorios y las trece pruebas del laboratorio;
- tres secciones nuevas por clase y sustitución de las preguntas frecuentes, errores y ejercicios idénticos por versiones propias de cada clase; fuentes verificadas y puente hacia agentes;
- las trece pruebas del laboratorio pasaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); los tiempos son de un equipo y se declaran como límite.

## 2026-11-13 — Parte 03 profundizada con mediciones de red reales

- 36 figuras para `SE-037`–`SE-048` con mediciones reales: fases de una petición HTTPS, MTU y límite de 1472 bytes,
  aritmética y clasificación de direcciones, estados TCP, rechazo frente a silencio y la espera de Nagle, resolución DNS y TTL,
  cabeceras y estados HTTP, certificado y veredictos TLS con una CA de laboratorio, proxy y balanceo simulados, contrapresión, variación
  por fase, la suite del laboratorio y el reintento con retroceso y jitter;
- tres secciones nuevas por clase, y sustitución de las preguntas frecuentes, la tabla de errores y los ejercicios, que eran idénticos en las doce clases, por
  versiones específicas de cada una; fuentes primarias verificadas y un puente hacia el trabajo con agentes;
- las once pruebas del laboratorio se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3); no se capturaron paquetes ni se midió
  Wi-Fi, QUIC o HTTP/3, y se declara como límite.

## 2026-11-13 — Parte 02 profundizada con evidencia medida en Windows y Linux

- 36 figuras para `SE-025`–`SE-036` con datos reales de Windows 11 y Ubuntu 24.04 bajo WSL2: sistemas de
  archivos (NTFS, ext4 y 9p) y su costo de metadatos, efecto de `chmod`, códigos de salida de procesos, expansión
  de argumentos y pipelines en Bash y PowerShell 5.1, visibilidad de un secreto ficticio, propiedad de archivos en
  `dpkg`, registros, espacios de nombres con `unshare` y la secuencia del laboratorio;
- tres a cuatro secciones nuevas por clase, fallos controlados ampliados, preguntas frecuentes, puentes hacia el
  trabajo con agentes y fuentes verificadas;
- las diez pruebas del laboratorio se ejecutaron en Windows (Python 3.12.9) y en Linux (Python 3.12.3);
  macOS, PowerShell 7 y los contenedores de Docker no se ejecutaron y se declaran como documentados;
- las pruebas de figuras cubren las Partes 00 a 02.

## 2026-11-13 — Parte 01 profundizada en contenido y figuras

- 40 figuras SVG para `SE-013`–`SE-024` (de tres a cuatro por clase), varias con datos medidos
  en CPython 3.12.9 sobre Windows y declarados como tales: tiempo de pared frente a CPU,
  recorrido secuencial frente a barajado, memoria de una lista frente a un `array`, costo de
  `fsync`, hilos frente a procesos, compilar frente a cargar bytecode y retención frente a flujo;
- cada clase añade entre tres y cuatro secciones de contenido nuevo con mecanismo, ejemplos
  ejecutados y límites (complemento a dos, aritmética de números de secuencia, UTF-8 por dentro,
  absorción y cancelación en coma flotante, simulador de ISA con 22 instrucciones dinámicas,
  jerarquía y durabilidad, GIL y carreras de datos, etapas de compilación y `.pyc`, conteo de
  referencias y ciclos, protocolo de benchmark, percentiles, Amdahl, dossier de referencia y
  estudio de ejemplo con regla de decisión previa);
- fallos controlados ampliados, preguntas frecuentes, puentes hacia el trabajo con agentes y
  fuentes primarias verificadas (DOI comprobados con Crossref, enlaces con respuesta 200);
- el generador de figuras pasa a `scripts/build_figures.py`, que descubre los módulos
  `scripts/figures_partXX_*.py`; las pruebas de figuras cubren las Partes 00 y 01.

## 2026-11-13 — Parte 00 profundizada con figuras de apoyo

- 36 figuras SVG estáticas (tres por clase) para `SE-001`–`SE-012`: modelos del
  mecanismo, secuencias de fallo, comparaciones y gráficos con datos sintéticos
  declarados, cada una con título, descripción, texto alternativo y un párrafo que
  explica cómo leerla y dónde deja de valer;
- cada clase añade un fallo controlado con protocolo, preguntas frecuentes sobre
  ambigüedades reales, un puente hacia el trabajo con agentes y fuentes primarias
  nuevas verificadas;
- el portal publica las figuras sin JavaScript externo (`site/assets/figures/`) y el
  README de GitHub las enlaza por ruta relativa; el generador de figuras vive en
  `scripts/build_figures.py` y se comprueba con `--check`;
- nuevo documento `docs/METHODOLOGY-GAP-AUDIT-2026-11-13.md` con la auditoría de
  brechas (metodologías de la era de la IA, patrones y arquitecturas) y el alcance
  decidido de 540 clases; el alcance no se publica en `curriculum.yaml` hasta que cada
  parte tenga contenido desarrollado.

## 2026-10-06 — Parte 05 desarrollada

- revisión clase a clase de `SE-061`–`SE-072`, conservando el hilo desde tipos y
  control hasta módulos, pruebas, mantenimiento y entrega;
- laboratorio empaquetado con quince contratos para parsing estricto, estado
  inmutable, JSONL acotado, errores explícitos, streams y códigos de salida;
- puerto Rust compilado en CI contra fixtures compartidas, con alcance de equivalencia
  deliberadamente limitado y documentado;
- actividades, rúbricas, portal y métricas reconciliados a 72 clases desarrolladas,
  288 borradores y 120 estructuras curriculares.

## 2026-10-06 — Parte 04 desarrollada

- revisión clase a clase de `SE-049`–`SE-060`, preservando la progresión desde
  ambigüedad hasta especificación, algoritmo, oráculo y contraejemplos;
- laboratorio ejecutable con trece pruebas para lógica, grafos, contratos,
  terminación, complejidad, heurísticas, estados y requisitos contradictorios;
- actividades, rúbricas, portal y métricas reconciliados a 60 clases desarrolladas,
  300 borradores y 120 estructuras curriculares.

## 2026-10-06 — Parte 03 desarrollada

- revisión cualitativa clase a clase de `SE-037`–`SE-048`, con DNSSEC, caché
  negativa, confianza de cabeceras y Trace Context vinculados a fuentes primarias;
- laboratorio local de petición observable con siete escenarios, once pruebas,
  resultados tipados, correlación, redacción y limpieza determinista;
- actividades y rúbricas específicas, portal íntegro, índices y estado reconciliados
  a 48 clases desarrolladas, 312 borradores y 120 estructuras curriculares.

## Unreleased — fase 3

### Parte 02 — sistemas operativos, terminal y automatización base

- revisión cualitativa y publicación como desarrolladas de `SE-025`–`SE-036`, con
  actividades, rúbricas, fallos y evidencia específica para cada competencia;
- laboratorio seguro sin dependencias externas para preparar, inspeccionar, reparar
  y limpiar un entorno controlado, con diez pruebas y adaptadores PowerShell/Bash;
- fuentes primarias reconsultadas para POSIX.1-2024, GNU Bash 5.3, PowerShell y WSL,
  sin copiar estándares protegidos ni atribuir capacidades no ejecutadas;
- CI ampliada con pruebas del laboratorio, smoke tests nativos y matriz
  Windows/macOS/Linux; estado reconciliado a 36 clases desarrolladas, 324 borradores
  y 120 estructuras curriculares.

### Parte 01 — computadores y representación de información

- revisión cualitativa y publicación como desarrolladas de `SE-013`–`SE-024`, con
  secuencias, actividades y rúbricas específicas para cada competencia;
- laboratorio reproducible sin dependencias externas para inspección de
  representación, Unicode, números, AST, bytecode, memoria y medición de tiempo;
- actualización no retroactiva de las referencias vigentes a Unicode 18.0 y Java
  Virtual Machine Specification SE 27;
- CI ampliada con las seis pruebas del laboratorio en estructura y portabilidad;
- nueva auditoría de cobertura y backlog trazable: 24 clases desarrolladas, 336
  borradores y 120 estructuras, sin crear IDs nuevos antes de demostrar una brecha
  indivisible.

### Licencias y automatización

- transición no retroactiva desde MIT a una matriz explícita: Apache-2.0 para
  software propio y CC BY-NC-SA 4.0 para contenido educativo, datos y activos
  originales;
- incorporación de `NOTICE`, auditoría, historia verificable, marcas e inventarios
  de terceros, datos y activos, con un validador y pruebas dedicados;
- workflow de seguridad con Gitleaks, Bandit y gobernanza semanal; CI ampliada con
  lint Markdown, resumen de evidencia y contratos de licencia;
- Pages cubre todas sus fuentes de generación y configura el despliegue mediante una
  acción fijada a SHA; la arquitectura y los límites de los tres workflows quedan
  documentados en profundidad;

### README y rutas profesionales

- rediseño integral del README principal siguiendo el ritmo visual y documental del
  programa de ciberseguridad: identidad, fuentes, mapa completo, uso, rutas, calidad,
  límites, licencia y llamada final a apoyar el repositorio;
- cabecera y cierre centrados, badges jerarquizados, accesos visuales, comparación en
  dos columnas y badges sociales reales de stars, forks y seguimiento;
- 40 guías profesionales propias, derivadas de las capacidades reales de las partes,
  con misión, jornada, responsabilidades, límites, conocimientos, recorrido,
  evidencia de portafolio, progresión, mitos y siguientes pasos;
- índice por familias y mapa de transiciones para distinguir especialización técnica,
  producto, calidad, plataforma, gobierno, arquitectura, liderazgo e IA;
- validación automática del inventario, la estructura y la navegación de las rutas.
- profundización de las 40 guías a más de 2.200 palabras cada una, con dos gráficos
  Mermaid, mapas parte → clases asociadas → evidencia, decisiones, escenarios de
  fallo, métricas, proyectos integradores, planes 30/60/90 y fuentes oficiales;
- mapa profesional ampliado en el README principal y en `roles/README.md`, con enlaces
  directos a 480 asociaciones de clase, tarjetas verticales adaptables y generación
  reproducible de los bloques;

### Roadmap curricular y simplificación editorial

- retiro de `PROMPT_MAESTRO.md`: la definición pública del programa vive ahora en un
  roadmap curricular detallado y las reglas de agentes permanecen en `AGENTS.md`;
- eliminación de etiquetas de flujo o madurez por clase en manifiestos, esquemas,
  generadores, portal, actividades, auditorías pedagógicas e índices;
- roadmap de las 40 partes con contenidos, artefactos y comprobaciones concretas,
  además de progresión, ejes transversales, proyectos y fases de implementación;
- auditoría de cobertura fechada con matriz de estado, profundidad, brechas y acción;
- ADR que preserva `SE-001`–`SE-480` y condiciona la aproximación a 500 clases a
  competencias no cubiertas, sin renumeración ni relleno;
- guardrails automáticos para impedir que misión, auditoría y decisión arquitectónica
  desaparezcan o se desincronicen silenciosamente.

### Corrección de integridad pedagógica

- fase 3 reabierta con alcance correcto de 180 clases (`SE-001`–`SE-180`);
- retiro de la afirmación incorrecta de 156 clases desarrolladas;
- incorporación del estándar pedagógico permanente y gate cualitativo;
- publicación del contenido completo de cada borrador en lugar de fichas resumidas;
- descripción factual del contenido disponible, sin asignar estados a cada clase.

### Fase 3 — declaración anterior, sustituida por la corrección

- 156 clases de las etapas A y C declaradas desarrolladas sin evidencia suficiente;
- guías específicas con conceptos, ejemplos, prácticas, ejercicios y fallos controlados;
- 156 contratos de actividad y 156 rúbricas machine-readable;
- catálogo de fuentes primarias u oficiales verificadas para trece partes;
- portal con páginas enlazadas al material completo;
- validador de fase 3 y quince pruebas estructurales.

### Fase 2 — generadores y controles

- scaffolding no destructivo para 480 clases y 40 partes;
- metadatos e índices generados desde `curriculum.yaml`;
- registro bibliográfico inicial para cada clase;
- validadores dedicados de contrato pedagógico y UTF-8;
- sitio estático de 521 páginas con búsqueda y filtros;
- workflow de GitHub Pages con acciones fijadas a SHA;
- diez pruebas estructurales y comprobación multiplataforma.

### Fase 1 — especificación y arquitectura

- arquitectura de ocho etapas, 40 partes y 480 clases planificadas;
- manifiesto y catálogo generados con 2.160 horas estimadas;
- mapa de cobertura, fronteras, ADR y plan de publicación pública;
- línea base de fuentes oficiales y primarias;
- validación estricta, pruebas estructurales y CI multiplataforma fijado por SHA;
- repositorio público con metadatos coherentes y workflow verde.

## 0.1.0 — 2026-08-19

- suite integradora inicial;
- programa profesional de 260 horas;
- documento de instrucciones interno, retirado posteriormente al consolidar el roadmap;
- manifiesto de cuatro repositorios;
- mapa de competencias, proyectos y blueprint;
- portal local y validación automática;
- plantillas de ingeniería y rúbrica final.
