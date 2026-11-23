# Modelo de amenazas

[↑ Glosario](../../README.md) · [← Modelo conductual](./modelo-conductual.md) · [Modelo de aplicación →](./modelo-de-aplicacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Un **modelo de amenazas** es la representación mantenida de qué activos hay, quién puede atacarlos y con qué capacidades, qué amenazas se identificaron, qué decisiones de defensa se tomaron y qué validación se hizo. [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) lo define como la descripción de qué activos hay, quién puede atacarlos, con qué capacidades y qué defensas se derivan; [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) añade que se mantiene mientras el sistema cambia; [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) lo reduce a tres preguntas: qué activo se protege, quién es el adversario y qué capacidad tiene. El sentido del programa es el de un artefacto vivo, no el de un informe que se entrega una vez.

## Por qué importa

Sin modelo, la seguridad se decide por susto: se arregla lo que alguien cita más. El modelo ordena las decisiones: de las tres preguntas de [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) sale la **frontera adecuada** (entre dos servicios del mismo equipo, un contenedor con límites suele bastar; entre una plataforma y código enviado por terceros se acude a una máquina virtual o a una microVM). Y [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) muestra una consecuencia concreta: un cliente corre en un entorno que otra persona controla, por lo que se deriva validar todo en el servidor, no confiar en comprobaciones del cliente y no guardar secretos de servicio en él.

## Cómo funciona

[SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) lo construye en pasos, cada uno con su razón:

1. **Activos, atacantes y supuestos.** Se empieza por lo que se quiere conservar, no por lo que se teme: calificaciones (integridad), entregas de cada estudiante (confidencialidad), disponibilidad el día del cierre. A cada activo corresponde un atacante con otra motivación, capacidad y paciencia.
2. **Diagrama de flujo de datos y fronteras de confianza.** Actores, procesos, almacenes y flujos, con líneas donde cambia quién controla qué. La frontera entre el navegador y la API es la más importante: todo lo que cruza, incluso un campo oculto o una cabecera, lo decide quien está del lado del cliente.
3. **Enumerar amenazas con STRIDE.** Seis categorías (suplantación, manipulación, repudio, divulgación de información, denegación de servicio y elevación de privilegios) usadas como lista de preguntas por elemento del diagrama, no como clasificación definitiva.
4. **Priorizar con un grafo de ataque.** Una lista no dice cuáles importan: el camino de menor costo desde el atacante hasta el objetivo es la estimación de riesgo más relevante, porque un atacante racional lo elige.
5. **Mantenerlo.** Un disparador por cambio (una regla que señala cuándo un cambio añade una frontera, un almacén o un flujo hacia un tercero) más una revisión periódica que busca lo que la regla no ve.

## Ejemplo

En [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), un grafo de doce aristas desde `internet` hasta `alterar nota` (robo de credenciales de un estudiante con costo 4, phishing a un docente con 6, token de servicio filtrado con 7, inyección SQL con 5, un campo de rol aceptado en el registro con 3, un identificador de nota adivinable con 2, y las aristas que llevan al objetivo) se evalúa con Dijkstra. La inyección SQL, que es la vulnerabilidad más citada, no estaba en el camino más barato: corregirla dejó el costo mínimo en 7. Hicieron falta cuatro bloqueos, uno por camino, para llegar a 27. Es un grafo sintético con costos asignados por la clase.

## Errores y confusiones comunes

- **Se arregla lo grave y nada mejora.** Se prioriza por gravedad y no por camino; corrección ([SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md)): calcular el camino más barato y recalcularlo tras cada decisión.
- **Una lista de 80 amenazas sin dueño.** Se enumera sin descartar ni decidir; corrección: una fila por amenaza con elemento, respuesta y supuesto.
- **Un diagrama sin fronteras.** Se dibujó la arquitectura, no la confianza; hay que marcar dónde cambia quién controla el dato.
- **Dos revisores puntúan distinto.** Una escala numérica sin criterio verificable da poca concordancia: en la simulación de la clase, dos personas razonables comparten menos de la mitad de sus cinco amenazas más graves. Se sustituye el puntaje por preguntas que se puedan comprobar.

## Límites y cuándo no aplica

Ninguna frontera es absoluta: se elige la que hace el ataque más costoso que el beneficio y se complementa con permisos mínimos, red cerrada y límites de recursos ([SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md)). Los resultados cuantitativos de [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) salen de grafos y simulaciones sintéticos; por ejemplo, el disparador por cambio acierta donde la regla ve la frontera y falla en silencio donde no (12 de 24 en esa simulación). La combinación de disparador y revisión periódica es la única que reduce la media por debajo de 30 días y el máximo por debajo de 90. El modelo pierde validez cuando cambia el sistema y el modelo no se entera.

## Relación con otros conceptos

- **Prerrequisito:** [Capacidad](../c/capacidad.md).
- **Ver también:** [Activo](../a/activo.md), [Representación](../r/representacion.md), [Validación](../v/validacion.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Contenedor](../c/contenedor.md), [Espacio de nombres](../e/espacio-de-nombres.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-262 — Firma, sandbox y seguridad del cliente](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-398 — Máquinas virtuales, contenedores y aislamiento](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-457 — Principios de seguridad y modelos de amenaza](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Modelo de amenaza».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [namespaces(7)](https://man7.org/linux/man-pages/man7/namespaces.7.html) — espacios de nombres como vista propia de recursos globales; autoridad: manual de Linux (proyecto man-pages).
- [Control Group v2](https://docs.kernel.org/admin-guide/cgroup-v2.html) — grupos de control y distribución de recursos; autoridad: documentación del núcleo Linux.
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec) — configuración y ciclo de vida de un contenedor; autoridad: Open Container Initiative.
- [Firecracker: Lightweight Virtualization for Serverless Applications](https://www.usenix.org/conference/nsdi20/presentation/agache) — microVMs como compromiso entre aislamiento y arranque; autoridad: artículo de USENIX NSDI 2020.
- [Python: subprocess](https://docs.python.org/3/library/subprocess.html) — API usada para medir procesos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Modelo conductual](./modelo-conductual.md) · [Modelo de aplicación →](./modelo-de-aplicacion.md)
