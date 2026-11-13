# SE-042 — HTTP, semántica, caché y negociación

[← SE-041 — DNS, nombres, resolución y fallos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) · [↑ Parte 03](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-042.html) · [SE-043 — TLS, certificados y confianza en tránsito →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para razonar sobre HTTP por semántica de método, representación, validación, caché y negociación.

**Por qué aparece aquí.** Se sitúa después de **DNS, nombres, resolución y fallos** y antes de **TLS, certificados y confianza en tránsito**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Equiparar GET con ausencia de efectos o 200 con respuesta no cacheada.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Http-exchange.md con mensajes crudos, validators y decisión de caché. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** HTTP define semántica; no garantiza conducta correcta de la aplicación.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) | define la semántica normativa del protocolo nombrado en el título y sus límites interoperables | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) | define la semántica normativa del protocolo nombrado en el título y sus límites interoperables | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa la **petición observable de extremo a extremo de la Parte 3**. No estudia redes como una lista de siglas: añade una decisión concreta al mismo recorrido y obliga a explicar dónde nace cada señal. Conserva una bitácora con cuatro columnas —hecho, interpretación, hipótesis rival y próxima prueba—; si una conclusión no apunta a evidencia, todavía no es diagnóstico.

## Prerrequisitos

- Haber completado `SE-041` o poder explicar su evidencia principal.
- Trabajar solo contra `localhost`, una red propia o un destino con autorización expresa.
- Disponer de navegador, `curl` y herramientas equivalentes del sistema; registra versiones y plataforma.

## Problema auténtico

La petición observable de extremo a extremo actualiza una configuración, pero un reintento duplica el cambio y otra persona sigue viendo una representación antigua. El equipo debe separar método, recurso, representación, estado de respuesta, validación y caché.

## Objetivos observables

Al terminar podrás:

1. interpretar métodos por semántica, seguridad e idempotencia;
2. distinguir recurso de representación;
3. usar estados y cabeceras como contrato observable;
4. diseñar revalidación y variación de caché;
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

El ciclo evita el diagnóstico por intuición. La observación se ubica antes de interpretarse; la prueba debe producir resultados diferentes bajo hipótesis rivales; la decisión conserva una salida de recuperación. En esta clase la pregunta rectora es: **¿Qué intención expresa el mensaje HTTP y qué puede reutilizar un intermediario?**

## Temas y por qué importan

| Núcleo | Pregunta de trabajo | Evidencia esperada |
|---|---|---|
| alcance | ¿dónde es válido este identificador o estado? | mapa de fronteras |
| mecanismo | ¿qué entrada produce qué transición? | secuencia comentada |
| garantía | ¿qué promete el protocolo y qué no? | ejemplo y contraejemplo |
| diagnóstico | ¿qué prueba separa causas plausibles? | comparación reproducible |
| operación | ¿cómo falla, se limita y se recupera? | caso sano, degradado y restaurado |
## Conceptos y decisiones

### 1. Recurso, URI y representación

La URI identifica el objetivo; la respuesta lleva una representación de su estado, no el recurso mismo. Dos formatos pueden representar el mismo recurso. Cambiar de JSON a HTML no debería cambiar la identidad, pero sí metadatos y negociación.

### 2. Métodos y propiedades

GET solicita transferencia de una representación y se define como seguro; PUT y DELETE son idempotentes en su efecto previsto; POST no lo es por defecto. Seguro no significa libre de logs o costo. La semántica permite a clientes e intermediarios decidir reintentos y caché.

### 3. Estados como resultado, no decoración

2xx comunica éxito bajo condiciones específicas; 3xx redirige; 4xx señala que la petición no puede satisfacerse tal como está; 5xx indica incapacidad del servidor. Devolver 200 con un error opaco impide automatizar recuperación y falsea observabilidad.

### 4. Caché, frescura y validación

Una caché reutiliza respuestas si las reglas lo permiten. `Cache-Control` gobierna frescura; ETag y `If-None-Match` permiten validar sin transferir todo. `no-cache` exige revalidación; no equivale a prohibir almacenamiento. Datos personalizados requieren especial cuidado en cachés compartidas.

### 5. Negociación y Vary

Cabeceras como `Accept` describen formatos aceptables. Si la respuesta cambia por una cabecera, `Vary` incorpora esa dimensión a la clave de caché. Variar por demasiados campos destruye reutilización; omitir uno puede entregar idioma o codificación incorrectos.

### Las cabeceras como conversación entre capas

Una respuesta HTTP es un mensaje con cabeceras que informan a cada participante. Pidiendo `https://example.com` con `curl -sI` se observó `HTTP/1.1 200 OK`, `Content-Type: text/html; charset=utf-8`, `Server: cloudflare`, `Last-Modified: Fri, 13 Nov 2026 08:41:42 GMT`, `Age: 3521` y `alt-svc: h3=":443"; ma=86400`, y ninguna cabecera `ETag`. Cada una se lee con su semántica: `Content-Type` define el tipo de medio; `Server` identifica quién responde (aquí un intermediario);
`Last-Modified` es un validador débil basado en el tiempo; `Age` indica que la copia llevaba 3521 segundos en la caché del intermediario; y `alt-svc` anuncia que HTTP/3 está disponible. La ausencia de `ETag` significa que no hay validador fuerte y la revalidación usará la fecha.

![Figura 1. Tabla con las cabeceras reales de example.com: Content-Type, Server, Last-Modified, Age, alt-svc y la ausencia de ETag, con lo que comunica cada una](../../../content/part-03/figures/se-042-cabeceras-reales.svg)

**Cómo leer la figura.** Cada fila es una cabecera, su valor y su significado. **Dónde deja de valer:** son las cabeceras que un sitio concreto devolvió en un momento dado; otro sitio o la misma URL más tarde variarían. Las cabeceras son una conversación con intermediarios: algunas las añaden o eliminan proxies y CDN (SE-044), de modo que no se consideran una descripción fiel del origen.

### Métodos y estados: lo que el servidor decide

El método expresa la intención y el estado, la decisión del servidor sobre el recurso. En pruebas sobre `example.com`: `GET /` devolvió `200` con 577 bytes; `HEAD /` devolvió `200` sin cuerpo (útil para comprobar existencia y tamaño sin transferir); `POST /` y `OPTIONS /` devolvieron `405` (el método no está permitido para ese recurso); `GET /no-existe` devolvió `404`; y una petición condicional
`GET /` con `If-Modified-Since: <Last-Modified>` devolvió `304` *sin cuerpo*, ahorrando 577 bytes. En un servidor local de laboratorio, `GET /503` devolvió `503` con `Retry-After: 1`, una pista sobre cuándo reintentar. Que el estado sea 200 no demuestra que el negocio haya funcionado: es una afirmación del servidor sobre la *representación*.

![Figura 2. Tabla con siete peticiones y su estado real: GET 200, HEAD 200 sin cuerpo, POST 405, OPTIONS 405, 404, 304 condicional y 503 con Retry-After](../../../content/part-03/figures/se-042-metodos-y-estados.svg)

**Cómo leer la figura.** Cada fila es una petición, el estado observado y su lectura. La del `304` es la clave para el rendimiento: el cliente ya tiene la representación y el servidor lo confirma sin repetirla. **Dónde deja de valer:** la política de métodos y estados es del servidor, y se debe leer la documentación o el contrato (OpenAPI); un `405` en OPTIONS, por ejemplo, no es universal. Y un sistema mal diseñado puede responder `200` con un cuerpo de error: el cliente no puede fiarse solo del número.

### Compresión, validación y frescura

La negociación de contenido permite que cliente y servidor acuerden la representación. Enviando `Accept-Encoding: gzip`, el cuerpo de `example.com` viajó en 400 bytes con `Content-Encoding: gzip`, frente a 577 sin compresión (cifras de esta página concreta). La validación condicional (`If-Modified-Since` o `If-None-Match` con un `ETag`) permite al servidor responder `304` y no retransmitir. Y la *frescura* decide si el cliente puede usar la copia sin preguntar: la fija `Cache-Control` (por ejemplo,
`max-age`), y la cabecera `Age` informa cuánto lleva la copia en la caché de un intermediario. Cuando la respuesta *varía* según una cabecera de la petición (como `Accept-Encoding`), el servidor debe declararlo con `Vary` para que los intermediarios no mezclen representaciones.

![Figura 3. Barras con bytes transferidos por el cuerpo: 577 sin compresión, 400 con gzip y 0 con un 304 condicional, y la antigüedad de 3521 s en la caché](../../../content/part-03/figures/se-042-compresion-y-validacion.svg)

**Cómo leer la figura.** Las barras comparan tres maneras de obtener el mismo recurso. **Dónde deja de valer:** el cuerpo de example.com es pequeño y la compresión de un documento tan corto aporta poco; en recursos grandes y compresibles el ahorro es mayor, y en recursos ya comprimidos (imágenes, vídeo) es nulo. Reutilizar una copia con una frescura mal definida puede servir datos obsoletos: la política de caché es una decisión de negocio, no solo de rendimiento.

## Definiciones de trabajo

- **recurso:** objetivo conceptual identificado por una URI.
- **representación:** estado transferible de un recurso en un formato.
- **método seguro:** método cuya semántica solicitada es de solo lectura.
- **ETag:** validador opaco de una representación.
- **Vary:** cabecera que declara dimensiones adicionales de selección de respuesta.

Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal.

## Ejemplo mínimo

Compara `GET /reports/7`, `PUT /reports/7` y `POST /reports`. Para cada uno define intención, respuesta exitosa, repetición tras timeout y si requiere clave idempotente.

El ejemplo se acepta cuando incluye predicción previa, salida relevante y explicación de qué hipótesis descarta. Copiar una salida sin interpretación no demuestra comprensión.

## Ejemplo profesional

La petición observable de extremo a extremo expone `GET /health` sin datos sensibles y `POST /diagnoses` con una clave idempotente. Las respuestas de catálogo usan ETag; las del usuario son privadas. Una traza registra método, target, estado, `Age`, `Cache-Control`, `Vary` y tiempo, evitando cuerpos con secretos.

La diferencia profesional es la trazabilidad: la decisión conecta requisito, mecanismo, señal, riesgo y recuperación. El equipo puede cambiar de herramienta sin perder el razonamiento.

## Práctica guiada

1. envía HEAD y GET al mismo recurso autorizado.
2. observa redirecciones sin seguirlas y luego con seguimiento.
3. prueba una revalidación condicional.
4. cambia `Accept` y comprueba `Content-Type` y `Vary`.
5. diseña una tabla de estados para éxito, entrada inválida, conflicto y fallo temporal.
6. entrega `trace.md` con comandos redactados, marcas de tiempo y condiciones de repetición.

## Ejercicios

1. **Lectura:** interpreta cada cabecera de una respuesta real (`Cache-Control`, `ETag`, `Vary`, `Age`) y di qué decide cada una.
2. **Condicional:** diseña la secuencia de peticiones que descarga un recurso una vez y luego lo valida, y cuántos bytes ahorra.
3. **Estados:** para una API de pedidos, elige el estado adecuado para crear, duplicar, no encontrar, sin permiso y servicio no disponible.
4. **Caché:** define `Cache-Control` para una página pública de baja frecuencia de cambio y para una respuesta personalizada.

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

### ¿Qué diferencia hay entre `404` y `405`?

`404` indica que no hay recurso en esa ruta; `405` indica que el recurso existe pero no admite ese método (y el servidor debería listar los permitidos en `Allow`). Confundirlos oculta si un error es de ruta o de método.

### ¿Un `200` significa que la operación se hizo?

Significa que el servidor procesó la petición y devolvió una representación con éxito. Si el cuerpo contiene un error de negocio, o si la operación se encola, la semántica real está en el contrato de la API. Un buen diseño usa el estado para el resultado del protocolo y el cuerpo para el detalle.

### ¿`ETag` y `Last-Modified` hacen lo mismo?

Ambos permiten validar. `Last-Modified` es un tiempo con resolución de segundos; `ETag` es un identificador de la representación y distingue cambios que ocurren dentro del mismo segundo. Cuando hay ambos, se prefiere `ETag`.

### ¿Cuándo debe un cliente reintentar una petición HTTP?

Cuando el método es idempotente (GET, HEAD, PUT, DELETE por especificación) y el error es transitorio (503, timeout), respetando `Retry-After`. Reintentar un POST sin clave de idempotencia puede duplicar el efecto.
## Fallo controlado y diagnóstico

Sirve una respuesta local con `max-age` y cambia el origen antes de que expire. Observa reutilización legítima; después usa validación condicional. No corrijas agregando parámetros aleatorios: explica la política y su costo.

Registra estado previo, acción, síntoma, primera divergencia, causa, corrección y estado posterior. Si la acción afecta red compartida, requiere privilegios amplios o no tiene rollback probado, reemplázala por una simulación local.


Una práctica compara una petición completa con una condicional. Obtén con `curl -sI` las cabeceras de un recurso propio o de `example.com`, y repite la petición con `If-Modified-Since` (con el valor de `Last-Modified`) y, si existe, con `If-None-Match` (con el `ETag`). **Síntoma esperado:** `304` sin cuerpo en la segunda. **Si responde 200:** el servidor no soporta validación o la copia cambió; compara. Añade `Accept-Encoding: gzip` y compara tamaños y la cabecera `Content-Encoding`.
**Corrección de diseño:** el cliente guarda el validador y lo envía, y el servidor responde con `ETag` y `Cache-Control` coherentes. Registra las cabeceras *tal cual* (sin cookies ni tokens) y la hora.

## Errores comunes y cómo corregirlos

| Síntoma | Causa | Corrección |
|---|---|---|
| Descargar completo un recurso que no cambió | No se usa validación condicional | Enviar `If-None-Match` o `If-Modified-Since` y manejar `304` |
| Mezclar respuestas comprimidas y no comprimidas en una caché | Falta `Vary: Accept-Encoding` | Declarar `Vary` en las respuestas que varían |
| Tratar todo `200` como éxito de negocio | El estado es del protocolo, no del dominio | Usar un contrato y verificar el contenido |
| Reintentar un `POST` tras un timeout | El método no es idempotente | Exigir una clave de idempotencia o consultar el estado |
| Confiar en `Server` o `Via` como identidad | Los intermediarios pueden modificar las cabeceras | Autenticar con TLS y credenciales, no con cabeceras informativas |

## Entorno y archivos clave

```text
work/SE-042/
├── README.md          # alcance, autorización y reproducción
├── request.txt        # petición sin credenciales
├── trace.md           # línea temporal y evidencias
├── failure-report.md  # hipótesis, prueba y recuperación
└── diagram.mmd        # mapa accesible acompañado de texto
```

Los archivos son contenedores, no evidencia automática. `README.md` declara sistema operativo, versiones, red utilizada y limpieza. Nunca confirmes cambios de red destructivos sin una ruta de recuperación.

### Laboratorio integrado de la Parte 03

Ejecuta `healthy` y `http_503` en la [petición observable](https://github.com/vladimiracunadev-create/modern-software-engineering-program/tree/main/labs/part-03-observable-request). Conserva cada respuesta 503 antes de la recuperación y explica por qué el estado, el método y el presupuesto forman juntos la política de reintento. Extiende `http-exchange.md` con un caso de ETag/304 diseñado y declara que el servidor del laboratorio no implementa caché HTTP.

## Seguridad, ética y accesibilidad

- captura únicamente tráfico propio o autorizado y durante la ventana mínima;
- redacta cookies, tokens, query strings, IP privadas y nombres de personas;
- no desactives TLS, firewall o aislamiento como solución permanente;
- acompaña color y diagramas con orden, etiquetas y una explicación textual;
- ofrece comandos equivalentes o resultados esperados para quien no pueda modificar una red;
- considera que telemetría e IP pueden identificar o perfilar personas.

## Puente hacia el trabajo con agentes

HTTP es el protocolo de casi todas las herramientas de un agente, y su semántica decide qué es seguro hacer. Un agente debe distinguir métodos seguros (GET) de los que producen efecto (POST, DELETE), respetar `Retry-After` y `Cache-Control`, y usar la validación condicional para no descargar de nuevo contenido grande. Del lado de la seguridad, el contenido de una respuesta HTTP es *dato no confiable*: puede contener instrucciones dirigidas al modelo (inyección indirecta de instrucciones), de modo que el harness debe tratarlo como texto, sin ejecutarlo, y
limitar los métodos y destinos permitidos por tarea. Las partes de herramientas, MCP y seguridad agentic desarrollan esos contratos y sus pruebas.

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



- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

Las RFC describen contratos de protocolo, no certifican una red, proveedor o herramienta. Cada afirmación de comportamiento local debe contrastarse con evidencia de ese entorno.

- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) y [RFC 9111, HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111): métodos, estados, validación y frescura; respaldan las figuras 1 a 3.
- [RFC 7838, HTTP Alternative Services](https://www.rfc-editor.org/rfc/rfc7838): la cabecera `alt-svc` observada.
- [curl: opciones `-I`, `-H` y `-w`](https://curl.se/docs/manpage.html): herramienta usada para obtener las cabeceras y los tiempos.

## Límites y siguiente paso

HTTP define semántica común, no la lógica de autorización de la petición observable de extremo a extremo. HTTP/1.1, HTTP/2 y HTTP/3 pueden transportar la misma intención de forma distinta. La siguiente clase protege autenticidad, integridad y confidencialidad en tránsito.

## Glosario

- **recurso:** objetivo conceptual identificado por una URI.
- **representación:** estado transferible de un recurso en un formato.
- **método seguro:** método cuya semántica solicitada es de solo lectura.
- **ETag:** validador opaco de una representación.
- **Vary:** cabecera que declara dimensiones adicionales de selección de respuesta.

---

[← SE-041 — DNS, nombres, resolución y fallos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) · [↑ Parte 03](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-042.html) · [SE-043 — TLS, certificados y confianza en tránsito →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)
