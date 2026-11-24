# Inventario de conceptos del glosario

[↑ Glosario](README.md)

> Este archivo lo genera `scripts/build_glossary.py` a partir de las clases publicadas; no se edita a mano.

## Resultado

El inventario contiene **2743 conceptos**, cada uno con su entrada: 625 troncales y 2118 de apoyo. Salen de 612 clases y 47 guías de rol.

## Cómo se extrajo

1. **Definiciones de trabajo.** Cada viñeta `- **término:** definición` del apartado «Definiciones de trabajo» (y del «Glosario» cuando es una lista) de las clases es una aparición de un término.
2. **Glosarios en prosa.** Los términos en negrita del apartado «Glosario» de las clases que lo redactan como párrafo.
3. **Temas.** Las filas de la tabla «Temas y por qué importan» que son términos: una a cuatro palabras, sin preguntas ni frases con coma, ni «y»/«o». Solo cuentan si el término ya está definido o el tema se repite en otra clase.
4. **Guías de rol.** Una entrada por guía de `roles/`.

Los términos en negrita sueltos de la prosa, los títulos de clase y los conceptos de los casos de estudio no crean entradas por sí solos: los títulos de clase son listas de temas (ya cubiertas por el apartado de temas) y la negrita de la prosa marca énfasis, no definición. Los casos se enlazan desde las entradas cuando mencionan el concepto (`glosario/casos.json`).

## Normalización

Dos redacciones son el mismo concepto si comparten alguna clave: minúsculas, sin tildes ni puntuación, palabras en singular, con el paréntesis separado como alias (`reversión (rollback)` aporta `reversión` y `rollback`) y con las siglas unidas a su expansión.

| Medida | Valor |
| --- | --- |
| Definiciones de trabajo leídas | 3384 |
| Términos en glosarios en prosa | 78 |
| Filas de temas leídas | 3254 |
| Filas de temas con forma de término | 2056 |
| Redacciones distintas tras separar paréntesis | 3509 |
| Conceptos tras normalizar y deduplicar (sin roles) | 2696 |
| Conceptos con más de una redacción unificada | 743 |

Conceptos que más variantes unificaron:

- Variante defectuosa: Mutante, Mutantes, Variante defectuosa, Variantes defectuosas
- Retroceso: Reversión, Rollback, retroceso, reversión
- Supuestos: Supuesto, Supuestos, supuesto, supuestos
- Restricciones: Restricciones, Restricción, restricciones, restricción
- Huella: Huella, hash, huella, resumen criptográfico
- Escenario de calidad: Escenario de calidad, Escenarios de calidad, escenario de calidad, escenarios de calidad
- Dispersión: Dispersión, Jitter, dispersión, jitter
- Dependencia: Dependencia, Dependencias, dependencia, dependencias
- Código de salida: Código de salida, Códigos de salida, código de salida, códigos de salida
- Bulkhead: Bulkhead, Mamparos, bulkhead, mamparo
- Webhook: Webhook, Webhooks, webhook
- Tubería: Tubería, pipe, tubería

## Criterio de tipificación

La tipificación es léxica y determinista: no es un juicio editorial.

- **Nivel troncal:** el concepto estructura una parte: lo definen o lo titulan tres o más clases, o es a la vez tema, sección y definición de una misma clase, o lo definen dos clases y además es tema o sección. También son troncales las guías de rol. El resto es **de apoyo**.
- **Profundidad:** *desarrollada* si todas las secciones principales de la entrada están escritas a mano en `glosario/curado/`; *compuesta desde las clases* si la entrada reúne, con atribución, lo que las clases ya enseñan sobre el término.
- **Tipo:** sigla (nombre en mayúsculas), norma o marco (nombra un estándar), métrica (tasa, latencia, cobertura…), práctica o técnica (empieza por prueba, revisión, despliegue…), rol profesional y concepto (el resto).

## Conteos

Por nivel:

| Nivel | Entradas |
| --- | --- |
| apoyo | 2118 |
| troncal | 625 |

Por profundidad:

| Profundidad | Entradas |
| --- | --- |
| compuesta desde las clases | 2138 |
| desarrollada | 605 |

Por tipo:

| Tipo | Entradas |
| --- | --- |
| concepto | 2449 |
| práctica o técnica | 101 |
| sigla | 93 |
| métrica | 50 |
| rol profesional | 47 |
| norma o marco | 3 |

Por origen del concepto:

| Origen | Entradas |
| --- | --- |
| definición de trabajo | 2591 |
| glosario de la clase | 65 |
| guía de rol | 47 |
| tema de la clase (en dos o más clases) | 40 |

Por familia (etapa de la primera clase donde aparece):

| Familia | Entradas |
| --- | --- |
| A — Fundamentos de la profesión | 404 |
| B — Programación y construcción | 272 |
| C — Producto, requisitos y especificación | 432 |
| D — Superficies y formas de software | 413 |
| E — Diseño, arquitectura, datos e integración | 493 |
| F — Calidad, seguridad y entrega | 231 |
| G — Operación, evolución y liderazgo | 169 |
| H — Ingeniería de software nativa con IA | 282 |
| Rutas por rol | 47 |

Por parte de primera aparición:

| Parte | Entradas | Troncales | De apoyo |
| --- | --- | --- | --- |
| [Parte 00 — Ingeniería de software como profesión](../classes/part-00-ingenieria-de-software-como-profesion/README.md) | 110 | 28 | 82 |
| [Parte 01 — Computadores y representación de información](../classes/part-01-computadores-y-representacion-de-informacion/README.md) | 107 | 25 | 82 |
| [Parte 02 — Sistemas operativos, terminal y automatización base](../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) | 95 | 37 | 58 |
| [Parte 03 — Redes, Internet y protocolos](../classes/part-03-redes-internet-y-protocolos/README.md) | 55 | 12 | 43 |
| [Parte 04 — Pensamiento computacional y resolución de problemas](../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) | 51 | 14 | 37 |
| [Parte 05 — Fundamentos de programación](../classes/part-05-fundamentos-de-programacion/README.md) | 41 | 7 | 34 |
| [Parte 06 — Paradigmas de programación](../classes/part-06-paradigmas-de-programacion/README.md) | 62 | 20 | 42 |
| [Parte 07 — Estructuras de datos y algoritmos](../classes/part-07-estructuras-de-datos-y-algoritmos/README.md) | 60 | 25 | 35 |
| [Parte 08 — Entornos, herramientas y depuración](../classes/part-08-entornos-herramientas-y-depuracion/README.md) | 62 | 23 | 39 |
| [Parte 09 — Bibliotecas, paquetes, SDK y automatización](../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) | 56 | 27 | 29 |
| [Parte 10 — Descubrimiento y estrategia de producto](../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) | 64 | 38 | 26 |
| [Parte 11 — Economía, métricas y decisiones de producto](../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) | 57 | 26 | 31 |
| [Parte 12 — Ingeniería de requisitos](../classes/part-12-ingenieria-de-requisitos/README.md) | 55 | 40 | 15 |
| [Parte 13 — Especificaciones, contratos y modelos](../classes/part-13-especificaciones-contratos-y-modelos/README.md) | 56 | 31 | 25 |
| [Parte 14 — Experiencia, accesibilidad e internacionalización](../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md) | 55 | 7 | 48 |
| [Parte 15 — Procesos, planificación y estimación](../classes/part-15-procesos-planificacion-y-estimacion/README.md) | 49 | 23 | 26 |
| [Parte 16 — Git, colaboración y código abierto](../classes/part-16-git-colaboracion-y-codigo-abierto/README.md) | 56 | 17 | 39 |
| [Parte 17 — Documentación y conocimiento técnico](../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) | 55 | 14 | 41 |
| [Parte 18 — CLI, TUI, servicios y automatización](../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) | 48 | 9 | 39 |
| [Parte 19 — Web, frontend y aplicaciones progresivas](../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md) | 49 | 6 | 43 |
| [Parte 20 — Backend, APIs y procesamiento asíncrono](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) | 97 | 16 | 81 |
| [Parte 21 — Software móvil, escritorio y multiplataforma](../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) | 45 | 16 | 29 |
| [Parte 22 — Embedded, IoT y tiempo real](../classes/part-22-embedded-iot-y-tiempo-real/README.md) | 49 | 17 | 32 |
| [Parte 23 — Runtimes y plataformas modernas](../classes/part-23-runtimes-y-plataformas-modernas/README.md) | 80 | 9 | 71 |
| [Parte 24 — Software especializado y dominios](../classes/part-24-software-especializado-y-dominios/README.md) | 49 | 8 | 41 |
| [Parte 25 — Diseño, patrones y refactorización](../classes/part-25-diseno-patrones-y-refactorizacion/README.md) | 41 | 11 | 30 |
| [Parte 26 — Patrones de diseño, empresariales y de resiliencia](../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md) | 50 | 6 | 44 |
| [Parte 27 — Arquitectura de software y dominio](../classes/part-27-arquitectura-de-software-y-dominio/README.md) | 41 | 12 | 29 |
| [Parte 28 — Estilos arquitectónicos](../classes/part-28-estilos-arquitectonicos/README.md) | 69 | 7 | 62 |
| [Parte 29 — Datos, persistencia y recuperación](../classes/part-29-datos-persistencia-y-recuperacion/README.md) | 48 | 17 | 31 |
| [Parte 30 — Ingeniería de datos y plataformas de datos](../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md) | 59 | 7 | 52 |
| [Parte 31 — Integración, eventos y mensajería](../classes/part-31-integracion-eventos-y-mensajeria/README.md) | 44 | 11 | 33 |
| [Parte 32 — Concurrencia y sistemas distribuidos](../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md) | 36 | 6 | 30 |
| [Parte 33 — Cloud, plataforma e infraestructura](../classes/part-33-cloud-plataforma-e-infraestructura/README.md) | 42 | 18 | 24 |
| [Parte 34 — SaaS y plataformas de producto](../classes/part-34-saas-y-plataformas-de-producto/README.md) | 68 | 3 | 65 |
| [Parte 35 — Estrategia y técnicas de prueba](../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md) | 32 | 2 | 30 |
| [Parte 36 — Calidad, rendimiento y resiliencia](../classes/part-36-calidad-rendimiento-y-resiliencia/README.md) | 29 | 5 | 24 |
| [Parte 37 — Sistemas críticos, tiempo real y normas de seguridad](../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md) | 63 | 1 | 62 |
| [Parte 38 — Seguridad, privacidad y cumplimiento](../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md) | 39 | 0 | 39 |
| [Parte 39 — Build, release y cadena de suministro](../classes/part-39-build-release-y-cadena-de-suministro/README.md) | 36 | 3 | 33 |
| [Parte 40 — CI/CD, IaC y platform engineering](../classes/part-40-ci-cd-iac-y-platform-engineering/README.md) | 32 | 3 | 29 |
| [Parte 41 — Observabilidad, SRE e incidentes](../classes/part-41-observabilidad-sre-e-incidentes/README.md) | 39 | 1 | 38 |
| [Parte 42 — Ingeniería del caos](../classes/part-42-ingenieria-del-caos/README.md) | 48 | 4 | 44 |
| [Parte 43 — Mantenimiento y modernización legacy](../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md) | 36 | 2 | 34 |
| [Parte 44 — Gestión, liderazgo y práctica profesional](../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) | 46 | 3 | 43 |
| [Parte 45 — Metodologías de desarrollo: de TDD a ODD](../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md) | 51 | 2 | 49 |
| [Parte 46 — Desarrollo de software asistido por IA](../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md) | 46 | 1 | 45 |
| [Parte 47 — SPEC, agentes y ciclo de vida agentic](../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md) | 43 | 0 | 43 |
| [Parte 48 — Harness y agentic engineering](../classes/part-48-harness-y-agentic-engineering/README.md) | 39 | 2 | 37 |
| [Parte 49 — Patrones agénticos y sistemas con LLM](../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md) | 51 | 1 | 50 |
| [Parte 50 — Machine learning en producción y MLOps](../classes/part-50-machine-learning-en-produccion-y-mlops/README.md) | 52 | 2 | 50 |

---

[↑ Glosario](README.md)
