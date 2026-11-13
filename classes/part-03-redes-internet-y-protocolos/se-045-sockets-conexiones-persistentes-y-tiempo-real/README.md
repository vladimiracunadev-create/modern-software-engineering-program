# SE-045 — Sockets, conexiones persistentes y tiempo real

[← SE-044 — Proxies, balanceadores, gateways y CDN](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) · [↑ Parte 03](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-045.html) · [SE-046 — Captura, medición y diagnóstico de tráfico →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para modelar conexiones persistentes y tiempo real por estados, framing, heartbeat y backpressure.

**Por qué aparece aquí.** Se sitúa después de **Proxies, balanceadores, gateways y CDN** y antes de **Captura, medición y diagnóstico de tráfico**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Confundir conexión abierta con entrega garantizada o ignorar consumidores lentos.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Connection-state.md con apertura, mensajes, cierre, timeout y cola acotada. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** WebSocket no define semántica de negocio ni recuperación por sí solo.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) | define la semántica normativa del protocolo nombrado en el título y sus límites interoperables | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [RFC 6455 — The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455) | define la semántica normativa del protocolo nombrado en el título y sus límites interoperables | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) | define la semántica normativa del protocolo nombrado en el título y sus límites interoperables | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa la **petición observable de extremo a extremo de la Parte 3**. No estudia redes como una lista de siglas: añade una decisión concreta al mismo recorrido y obliga a explicar dónde nace cada señal. Conserva una bitácora con cuatro columnas —hecho, interpretación, hipótesis rival y próxima prueba—; si una conclusión no apunta a evidencia, todavía no es diagnóstico.

## Prerrequisitos

- Haber completado `SE-044` o poder explicar su evidencia principal.
- Trabajar solo contra `localhost`, una red propia o un destino con autorización expresa.
- Disponer de navegador, `curl` y herramientas equivalentes del sistema; registra versiones y plataforma.

## Problema auténtico

La petición observable de extremo a extremo necesita mostrar eventos en vivo. Mantener conexiones para siempre agota recursos; reconectar sin cursor pierde o duplica eventos. El equipo debe diseñar socket, framing, heartbeat, backpressure y reanudación.

## Objetivos observables

Al terminar podrás:

1. explicar socket, conexión y framing como conceptos distintos;
2. comparar polling, SSE y WebSocket por dirección y operación;
3. diseñar heartbeat, cierre y reconexión;
4. manejar backpressure y continuidad de eventos;
5. comunicar límites y una siguiente prueba sin presentar inferencias como hechos.

## Mapa conceptual

```mermaid
flowchart LR
    I[Intento de comunicación] --> O[Observación localizada]
    O --> H[Hipótesis y alternativa]
    H --> P[Prueba discriminante]
    P --> D[Decisión reversible]
    D --> E[Evidencia para la siguiente clase]
    P -->|no separa hipótesis| H
```

El ciclo evita el diagnóstico por intuición. La observación se ubica antes de interpretarse; la prueba debe producir resultados diferentes bajo hipótesis rivales; la decisión conserva una salida de recuperación. En esta clase la pregunta rectora es: **¿Cómo se conserva una conversación larga sin perder límites, vida útil ni recuperación?**

## Temas y por qué importan

| Núcleo | Pregunta de trabajo | Evidencia esperada |
|---|---|---|
| alcance | ¿dónde es válido este identificador o estado? | mapa de fronteras |
| mecanismo | ¿qué entrada produce qué transición? | secuencia comentada |
| garantía | ¿qué promete el protocolo y qué no? | ejemplo y contraejemplo |
| diagnóstico | ¿qué prueba separa causas plausibles? | comparación reproducible |
| operación | ¿cómo falla, se limita y se recupera? | caso sano, degradado y restaurado |
## Conceptos y decisiones

### 1. Socket y ciclo de vida

Un socket es una abstracción del sistema operativo asociada a un endpoint. En TCP, escuchar, aceptar, leer, escribir y cerrar cambian estados y consumen descriptores, buffers y memoria. Que el cliente desaparezca no siempre se detecta hasta leer, escribir o vencer un temporizador.

### 2. Framing sobre flujo

TCP no conserva mensajes. Protocolos de longitud prefijada, delimitadores o formatos autocontenidos permiten reconstruirlos. El parser debe limitar tamaño antes de reservar memoria y manejar un mensaje incompleto sin bloquear todos los clientes.

### 3. Polling, SSE y WebSocket

Polling repite HTTP y es simple pero añade demora y carga. SSE mantiene un flujo servidor→cliente con semántica textual y reconexión del navegador. WebSocket realiza un handshake HTTP y luego intercambia frames bidireccionales. La opción correcta depende de dirección, frecuencia, intermediarios y soporte.

### 4. Heartbeat y estado medio abierto

Ping/pong o mensajes de aplicación detectan peers silenciosos, pero demasiado frecuentes consumen batería y ancho de banda. TCP keepalive puede tener intervalos largos y no reemplaza deadlines de negocio. El cierre debe distinguir mantenimiento, error, expiración y decisión del usuario.

### 5. Backpressure y reanudación

Si el productor supera al consumidor, una cola infinita solo aplaza el fallo. Se puede bloquear, muestrear, descartar con política o desconectar con cursor. Un ID monotónico o token de reanudación permite solicitar eventos posteriores, pero necesita retención y semántica de duplicados.

### Reutilizar la conexión: cuánto ahorra y cuándo no

Abrir una conexión por petición paga un handshake TCP cada vez. En una prueba en loopback con un servidor HTTP/1.1 local, en Windows una conexión nueva por petición tardó 1,396 ms y reutilizar la misma 0,366 ms: 3,8 veces menos. En Linux, con el mismo diseño, la conexión reutilizada tardó 44,12 ms por petición cuando el servidor escribía las cabeceras y el cuerpo en *dos* llamadas, frente a 0,31 ms con una sola escritura y 0,34 ms con `TCP_NODELAY`. Es la interacción del algoritmo de Nagle con el ACK retrasado (SE-040): reutilizar es casi siempre una
ventaja, pero un detalle del envío puede anularla.

![Figura 1. Tabla con mediciones en loopback: conexión nueva por petición frente a reutilizada en Windows, y reutilizada con dos escrituras frente a una en Linux](../../../content/part-03/figures/se-045-reutilizar-conexion.svg)

**Cómo leer la figura.** Las dos primeras filas muestran el ahorro del handshake; las dos últimas, la penalización de dos escrituras pequeñas. **Dónde deja de valer:** el loopback no tiene RTT: con una red real el handshake cuesta más y el ahorro es mayor. Y la espera de 40 ms no aparece en Windows en esta prueba, de modo que una conclusión sobre «la reutilización» debe medirse en el sistema donde se ejecutará.

### Contrapresión: cuando el receptor no lee

Un emisor más rápido que su receptor llena los búferes. En una prueba, un emisor envió datos a un receptor que *no leía*: pudo escribir 327 680 bytes (320 KiB) en Windows y 2 621 440 bytes (2,5 MiB) en Linux antes de que el envío se bloqueara (con el socket en modo no bloqueante, `send` lanzó `BlockingIOError`). Esa señal es la *contrapresión*: el sistema le dice al emisor que espere. Si la aplicación la ignora, acumula memoria en su propia cola o
pierde datos. El tamaño de los búferes depende del sistema y de su configuración: no es un contrato. La política (esperar, descartar las muestras antiguas, rechazar al cliente) la define la aplicación.

![Figura 2. Barras con una medición real: 327 680 bytes en Windows y 2 621 440 bytes en Linux antes de que el emisor se bloquee con un receptor que no lee](../../../content/part-03/figures/se-045-contrapresion.svg)

**Cómo leer la figura.** Cada barra es la cantidad de bytes aceptados antes del bloqueo. **Dónde deja de valer:** el valor depende del ajuste de búferes y de la ventana de recepción, y varía entre ejecuciones; no se debe usar como una constante. Lo que se conserva es el diseño: toda cola entre dos componentes necesita un límite y una política cuando se llena.

### Ciclo de vida del socket, plazos y detección de fallos

Un socket pasa por crear, conectar o escuchar, intercambiar con *framing*, esperar y cerrar. Cada fase necesita su plazo: una lectura con timeout de 0,1 s contra un servidor lento lanzó `TimeoutError` a los 0,1 s, de modo que la aplicación recupera el control. Cerrar correctamente importa: si un extremo cierra y el otro no, el segundo queda en `CLOSE-WAIT`. Y una conexión inactiva *no detecta* que el otro extremo desapareció sin enviar FIN ni RST (un corte de energía, un
cable desconectado): hacen falta *heartbeats* a nivel de aplicación o *keepalives* de TCP con un plazo y una política de reconexión. Los canales de larga vida (SSE, WebSocket) añaden además la necesidad de reanudar desde el último evento recibido.

![Figura 3. Cuatro fases de un socket con su límite de tiempo: conexión, intercambio con framing, espera con timeout de lectura y cierre](../../../content/part-03/figures/se-045-ciclo-de-vida-del-socket.svg)

**Cómo leer la figura.** Cada caja es una fase y la inferior recuerda que hay tres tiempos distintos (conexión, lectura y plazo total). **Dónde deja de valer:** los canales sobre HTTP/2 o HTTP/3 comparten una sola conexión entre muchos *streams* y heredan sus problemas de cabeza de línea o de control de flujo; los tiempos se aplican entonces por stream y por conexión.

## Definiciones de trabajo

- **socket:** endpoint de comunicación administrado por el sistema operativo.
- **framing:** regla para delimitar mensajes sobre un transporte.
- **heartbeat:** mensaje periódico para comprobar continuidad.
- **backpressure:** mecanismo que limita al productor cuando el consumidor no alcanza.
- **cursor:** posición reanudable dentro de una secuencia de eventos.

Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal.

## Ejemplo mínimo

Implementa o representa un protocolo local de longitud prefijada. Divide deliberadamente el encabezado entre dos lecturas y demuestra que el parser espera sin confundir datos parciales con EOF.

El ejemplo se acepta cuando incluye predicción previa, salida relevante y explicación de qué hipótesis descarta. Copiar una salida sin interpretación no demuestra comprensión.

## Ejemplo profesional

La petición observable de extremo a extremo usa SSE para estados unidireccionales y entrega `id` por evento. El cliente reanuda con el último ID; el servidor conserva una ventana finita y responde explícitamente cuando el cursor expiró. Métricas separan conexiones abiertas, clientes lentos, bytes pendientes y reconexiones.

La diferencia profesional es la trazabilidad: la decisión conecta requisito, mecanismo, señal, riesgo y recuperación. El equipo puede cambiar de herramienta sin perder el razonamiento.

## Práctica guiada

1. modela estados desde conexión hasta cierre.
2. mide recursos con 1, 10 y 100 conexiones locales.
3. introduce un consumidor lento.
4. define límite de cola y política de descarte.
5. corta la red o proceso y prueba reanudación con eventos duplicados.
6. entrega `trace.md` con comandos redactados, marcas de tiempo y condiciones de repetición.

## Ejercicios

1. **Framing:** escribe un protocolo con prefijo de longitud y un receptor que reconstruya mensajes partidos y pegados.
2. **Medición:** compara una petición por conexión con una conexión reutilizada en tu entorno e informa la razón con el rango.
3. **Contrapresión:** diseña la política de un emisor de telemetría cuando el receptor se atrasa: qué descarta y cuándo avisa.
4. **Detección:** explica por qué un corte de energía en el servidor no se detecta sin datos y cómo un heartbeat lo resuelve.

## Reto verificable

Entrega una traza comentada que permita a otra persona responder: qué se intentó, qué frontera se observó, qué garantía aplicaba, qué falló, qué alternativa fue descartada y cómo se restauró el estado. La persona revisora debe poder repetir al menos una prueba sin instrucciones orales.

## Demostración guiada

1. Predice el primer evento observable y el resultado sano.
2. Ejecuta una sola petición de la petición observable de extremo a extremo y asigna cada marca a una frontera.
3. Introduce el fallo controlado descrito abajo.
4. Compara por **primera divergencia**, no por cantidad de errores posteriores.
5. Restaura, repite y conserva evidencia de recuperación.

Una demostración que no incluye restauración solo prueba cómo romper el laboratorio.

## Preguntas frecuentes

### ¿Cuándo debo abrir una conexión nueva en lugar de reutilizar?

Cuando la conexión se cerró, falló o llegó a su límite de uso, o cuando una política de balanceo exige redistribuir. Un cliente robusto detecta una conexión obsoleta (el servidor la cerró durante la inactividad) y reintenta una vez sobre una conexión nueva si la operación es idempotente.

### ¿WebSocket, SSE o sondeo?

Sondeo es simple y escala mal en latencia y carga; SSE es unidireccional del servidor al cliente, sobre HTTP, con reanudación; WebSocket es bidireccional y exige gestionar su propio ciclo de vida y framing. La elección depende de la dirección del flujo, la frecuencia y los intermediarios (algunos proxies cortan conexiones inactivas).

### ¿Qué es el estado medio abierto?

Una conexión que un extremo considera viva y el otro ya no, porque no hubo FIN ni RST. Se detecta con *heartbeats* y plazos. Sin ellos, la aplicación espera indefinidamente a un interlocutor desaparecido.

### ¿Ajustar el tamaño de los búferes soluciona la contrapresión?

Solo la retrasa. Búferes mayores absorben ráfagas, pero si el receptor es sistemáticamente más lento, se llenan igual y aumentan la latencia. La solución es regular la tasa del emisor o rechazar carga.
## Fallo controlado y diagnóstico

Detén el consumo mientras el productor continúa. Observa crecimiento hasta un límite bajo y seguro; implementa backpressure o desconexión explícita. La corrección no es aumentar memoria sin límite.

Registra estado previo, acción, síntoma, primera divergencia, causa, corrección y estado posterior. Si la acción afecta red compartida, requiere privilegios amplios o no tiene rollback probado, reemplázala por una simulación local.


Una práctica provoca contrapresión de forma segura. Levanta un receptor local que acepte la conexión y *no lea*, y un emisor no bloqueante que envíe bloques de 64 KiB hasta recibir `BlockingIOError`; registra cuántos bytes aceptó el sistema. **Síntoma:** el envío se detiene sin error de red. **Hipótesis:** el receptor es lento o está colgado. **Prueba:** leer del receptor y comprobar que el emisor puede continuar.
**Corrección de diseño:** el emisor define un límite de cola, un plazo y una política (descartar muestras antiguas o rechazar), y el receptor consume con un límite de tiempo. Limita el tamaño total enviado para no presionar el equipo, y cierra todos los sockets al terminar.

## Errores comunes y cómo corregirlos

| Síntoma | Causa | Corrección |
|---|---|---|
| Latencia de ≈40 ms con conexión reutilizada | Dos escrituras pequeñas con Nagle y ACK retrasado | Escribir el mensaje completo o fijar `TCP_NODELAY` |
| Memoria creciente en el emisor | Ignora la contrapresión y acumula una cola sin límite | Limitar la cola y definir política al llenarse |
| Esperas infinitas por un interlocutor caído | No hay heartbeat ni plazo | Añadir heartbeats, keepalives y un timeout por fase |
| Mensajes truncados o pegados | Se asumió que TCP conserva fronteras | Definir framing con longitud o delimitador |
| Sockets en `CLOSE-WAIT` acumulados | La aplicación no cierra su lado tras el FIN | Cerrar en todas las rutas (con administradores de contexto) |

## Entorno y archivos clave

```text
work/SE-045/
├── README.md          # alcance, autorización y reproducción
├── request.txt        # petición sin credenciales
├── trace.md           # línea temporal y evidencias
├── failure-report.md  # hipótesis, prueba y recuperación
└── diagram.mmd        # mapa accesible acompañado de texto
```

Los archivos son contenedores, no evidencia automática. `README.md` declara sistema operativo, versiones, red utilizada y limpieza. Nunca confirmes cambios de red destructivos sin una ruta de recuperación.

### Laboratorio integrado de la Parte 03

Verifica con las pruebas de la [petición observable](https://github.com/vladimiracunadev-create/modern-software-engineering-program/tree/main/labs/part-03-observable-request) que el servidor termina y el hilo se une incluso después de un timeout. Luego diseña en `connection-state.md` la transición equivalente para polling, SSE y WebSocket: apertura, heartbeat, consumidor lento, cursor, cierre y reconexión. La ejecución HTTP local no demuestra framing ni backpressure de WebSocket.

## Seguridad, ética y accesibilidad

- captura únicamente tráfico propio o autorizado y durante la ventana mínima;
- redacta cookies, tokens, query strings, IP privadas y nombres de personas;
- no desactives TLS, firewall o aislamiento como solución permanente;
- acompaña color y diagramas con orden, etiquetas y una explicación textual;
- ofrece comandos equivalentes o resultados esperados para quien no pueda modificar una red;
- considera que telemetría e IP pueden identificar o perfilar personas.

## Puente hacia el trabajo con agentes

Los agentes mantienen canales de larga vida (transmisión de respuestas del modelo, flujos de eventos de herramientas, conexiones a servidores MCP) y heredan todos los problemas de esta clase: un canal inactivo que nadie detecta caído, un consumidor lento que provoca acumulación de tokens, mensajes partidos y reanudación tras un corte. El harness debe fijar plazos por fase, heartbeats, límites de cola y reintento con reanudación desde el último identificador recibido. Además, la contrapresión protege el costo: un agente
que genera más rápido de lo que el sistema consume debe frenarse, no acumular. Las partes de herramientas, MCP y operación de agentes desarrollan estos contratos.

## Transferencia

Traslada el mecanismo a una segunda red o protocolo sin repetir comandos mecánicamente. Conserva la pregunta y el criterio de evidencia; cambia los supuestos de dirección, intermediación y política. Escribe qué observación seguiría siendo válida y cuál depende de la topología original.

## Evaluación y evidencia

| Criterio | Evidencia mínima | Señal de dominio |
|---|---|---|
| modelo causal | mapa con fronteras y unidades correctas | explica interacción y fugas del modelo |
| protocolo | garantía y límite apoyados en fuente | distingue semántica de implementación |
| diagnóstico | hipótesis rival y prueba discriminante | encuentra primera divergencia |
| reproducibilidad | contexto, comandos y salida redactada | otra persona repite el resultado |
| responsabilidad | autorización, minimización y rollback | reduce riesgo sin borrar evidencia |

La clase no se aprueba por ejecutar comandos. Se aprueba cuando la evidencia sostiene las conclusiones y declara lo que todavía no puede saberse.

## Fuentes



- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 6455 — The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

Las RFC describen contratos de protocolo, no certifican una red, proveedor o herramienta. Cada afirmación de comportamiento local debe contrastarse con evidencia de ese entorno.

- [RFC 6455, The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455) y [especificación de Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html): canales de larga vida y su ciclo de vida; respaldan la figura 3.
- [RFC 1122 §4.2.3.6, keepalives de TCP](https://www.rfc-editor.org/rfc/rfc1122) y [socket(7)](https://man7.org/linux/man-pages/man7/socket.7.html): detección de interlocutores caídos y tamaño de búferes de envío y recepción.
- [Python `socket`](https://docs.python.org/3/library/socket.html): opciones `TCP_NODELAY`, modo no bloqueante y timeouts usados en las pruebas.

## Límites y siguiente paso

Tiempo real aquí significa baja latencia percibida, no garantía hard real-time. Proxies pueden imponer timeouts. La siguiente clase enseña a capturar y medir sin violar privacidad.

## Glosario

- **socket:** endpoint de comunicación administrado por el sistema operativo.
- **framing:** regla para delimitar mensajes sobre un transporte.
- **heartbeat:** mensaje periódico para comprobar continuidad.
- **backpressure:** mecanismo que limita al productor cuando el consumidor no alcanza.
- **cursor:** posición reanudable dentro de una secuencia de eventos.

---

[← SE-044 — Proxies, balanceadores, gateways y CDN](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) · [↑ Parte 03](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-045.html) · [SE-046 — Captura, medición y diagnóstico de tráfico →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)
