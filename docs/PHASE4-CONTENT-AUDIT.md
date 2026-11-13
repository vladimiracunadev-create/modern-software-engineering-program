# Auditoría de contenido de fase 4

## Alcance

La fase 4 comprende 180 clases consecutivas, `SE-181`–`SE-360`, distribuidas en
las partes 15–29. Cubre proceso y colaboración, documentación, interfaces de
software, web, backend, cliente, embedded, dominios especializados, diseño,
arquitectura, persistencia, integración, sistemas distribuidos y cloud.

## Estado verificable

| Comprobación | Resultado |
| --- | ---: |
| clases dentro del alcance | 180 |
| partes cubiertas | 15 |
| actividades estructuradas | 180 |
| rúbricas estructuradas | 180 |
| páginas con navegación bidireccional | 180 |
| fuentes primarias u oficiales registradas | 34 |
| clases aprobadas | 0 |

Los documentos son **borradores estructurales ampliados**. Incorporan problema,
objetivos, temas, conceptos, ejemplos, práctica, reto, fallo controlado, entorno,
evaluación, FAQ y fuentes. Esa cobertura estructural no equivale a una revisión
técnica y pedagógica clase por clase.

## Deuda cualitativa conocida

- los desarrollos conceptuales parten de perfiles por parte y aún pueden resultar
  intercambiables entre clases próximas;
- las definiciones son operativas y deben contrastarse con terminología normativa;
- los ejemplos y prácticas requieren ejecución o revisión humana por tecnología;
- las fuentes están asignadas por parte, pero todavía no respaldan cada afirmación
  mediante citas de proximidad;
- no existe evidencia de laboratorio suficiente para afirmar que las prácticas se
  ejecutaron de forma reproducible.

## Avance editorial de la Parte 15

Las clases `SE-181`–`SE-192` se reconstruyeron en `content/part-15/` alrededor del plan
de lanzamiento de la plataforma de entregas de tareas, que recorre la parte: modelos
de proceso y su cruce según la volatilidad, principios frente a ceremonias, cuatro
marcos leídos por sus políticas, teoría de colas y ley de Little, estimaciones con
rango y cobertura, redes con dependencias, registros de riesgos y decisiones, puertas
de listo y terminado, métricas con contrapesos, retrospectivas con capacidad limitada,
un taller de calibración y un plan adaptativo con disparadores y barreras. Cada clase
incluye tres simulaciones con datos sintéticos y semilla fija, ejecutadas en Windows y
Ubuntu (WSL2) con salidas idénticas, y declara que no se observó ningún equipo, no se
usó ninguna herramienta de gestión de proyectos y no se midió ninguna retrospectiva,
estimación ni métrica real. Las doce clases todavía requieren revisión por personas con
experiencia en gestión de proyectos y no presentan un verificador, una regla de
replanificación ni un pronóstico como sustitutos del juicio ni de la responsabilidad del
equipo que planifica.

## Avance editorial de la Parte 19

Las clases `SE-229`–`SE-240` se reconstruyeron en `content/part-19/` alrededor de una
aplicación web de entregas de tareas con conectividad irregular, que recorre la parte:
estructura semántica, contraste y cascada, modelo de ejecución y de eventos del
navegador, dónde se construye el HTML, estado con identidad y datos remotos,
formularios y Unicode, URLs y enrutado, rendimiento y presupuestos con percentiles,
codificación por contexto, política de contenido y cookies, service worker, versionado
y sincronización idempotente, rastreo y metadatos, un taller de flujo con fallos como
máquina de estados y un proyecto con manifiesto, cabeceras y matriz de pruebas. Cada
clase incluye tres experimentos con datos sintéticos y semilla fija, ejecutados en
Windows (CPython 3.12.9, Node 24) y Ubuntu (WSL2, 3.12.3, Node 20) con salidas idénticas
salvo los tiempos, y declara que no se usó ningún navegador, lector de pantalla, marco
de interfaz, service worker real, buscador ni herramienta de auditoría y que no se midió
a ninguna persona. Las doce clases todavía requieren revisión por personas con
experiencia en desarrollo web y accesibilidad y no presentan un linter, un auditor de
metadatos ni una política de contenido como sustitutos de una auditoría, de una revisión
con tecnologías de apoyo ni de una prueba en navegadores reales.

## Avance editorial de la Parte 22

Las clases `SE-265`–`SE-276` se reconstruyeron en `content/part-22/` alrededor de un nodo
ambiental de una sala de estudio, un caso sintético que recorre la parte: firmware y su
separación del hardware, buses y convertidores, presupuesto de energía, memoria y precisión,
plazos de tiempo real, datos compartidos con las interrupciones, conectividad intermitente,
actualización con recuperación, identidad y claves, procesamiento en el borde, safety,
seguridad y vida útil, un taller de modelado de fallos y un dispositivo simulado operable.
Cada clase incluye tres simulaciones con datos sintéticos y semilla fija, ejecutadas en
Windows y Ubuntu (WSL2) con cifras idénticas, y declara que no se usó ningún
microcontrolador, sistema operativo de tiempo real, agente MQTT, cargador de arranque ni red
real, que no se midió consumo ni peor caso de ejecución y que no se atacó ningún chip. Las doce
clases todavía requieren revisión por personas con experiencia en sistemas embebidos y de
seguridad funcional, y no presentan una simulación, un validador de paquetes ni un análisis
de fallos como sustitutos de las normas, de las pruebas con hardware ni de la responsabilidad
de quien diseña un dispositivo.

## Avance editorial de la Parte 23

Las clases `SE-277`–`SE-288` se reconstruyeron en `content/part-23/` alrededor de una plataforma
educativa ficticia que incorpora, una por clase, una pieza de un dominio especializado: la
reproducibilidad de un cálculo, una cadena de datos, un componente de aprendizaje automático, un
laboratorio de física con bucle de juego, una sala virtual con audio y realidad extendida, el cobro
de matrículas, un módulo de enfermería escolar, certificados verificables, un mapa con calendario,
una automatización visual, un taller de comparación de riesgos y un proyecto de diseño de un
dominio. Cada clase incluye tres simulaciones con datos sintéticos y semilla fija, ejecutadas en
Windows y Ubuntu (WSL2) con cifras idénticas, y declara que no se usó ningún código científico real,
motor de procesamiento, biblioteca de aprendizaje automático, motor de juego, tarjeta gráfica, casco,
procesador de pagos, dato clínico, red de cadena de bloques ni base de datos de zonas horarias o
espacial, que no se midió confort ni percepción y que no se evaluó ninguna norma. Las puntuaciones de
riesgo de `SE-287` son un juicio ilustrativo del autor. Las doce clases todavía requieren revisión por
personas con experiencia en cada dominio, y no presentan una simulación, un oráculo ni un validador
como sustitutos de la validación de dominio, de las pruebas con sistemas reales ni de la normativa
aplicable.

## Gate pendiente

Cada clase continúa como borrador hasta demostrar cobertura específica de todos sus
temas, ejemplos no intercambiables, práctica reproducible, fuentes ligadas a
afirmaciones y revisión cualitativa contra
[`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md). La fase no se contabiliza
por archivos creados, sino por clases que superan ese gate.
