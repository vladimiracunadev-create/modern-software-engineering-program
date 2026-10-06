# Laboratorio de la Parte 03 — petición observable y fallos por fase

Este laboratorio convierte `SE-037`–`SE-048` en una práctica reproducible. Ejecuta
un servicio HTTP efímero en `127.0.0.1`, propaga un identificador de correlación y
produce una línea temporal estructurada. Los fallos de DNS, conexión, confianza TLS,
latencia, pérdida y HTTP 503 tienen una primera divergencia comprobable.

## Contrato de seguridad

- el programa no acepta hosts ni URL aportados por el usuario;
- el único socket servidor se enlaza a `127.0.0.1` y usa un puerto efímero;
- no modifica DNS, rutas, certificados, proxies ni firewall del sistema;
- DNS, validación de nombre TLS y pérdida son modelos explícitos y deterministas;
- el tráfico HTTP es real, local y se cierra al terminar cada escenario;
- cabeceras sensibles se redactan y el resultado no contiene cuerpos personales.

Por diseño, la simulación TLS no demuestra un handshake criptográfico. `SE-043`
mantiene separada la práctica real con un certificado de laboratorio autorizado. La
simulación permite evaluar orden de fases y política de rechazo sin guardar claves.

## Uso

Requiere Python 3.11 o posterior y solo biblioteca estándar.

```console
python labs/part-03-observable-request/observable_request.py healthy
python labs/part-03-observable-request/observable_request.py suite
python -m unittest discover -s labs/part-03-observable-request/tests -v
```

Cada resultado declara `scenario`, `outcome`, `attempts`, `request_id`, `failure`,
`events` y `limits`. La evidencia se interpreta por la primera fase que difiere del
caso sano; una lista de errores posteriores no sustituye esa comparación.

## Recorrido clase a clase

| Clase | Uso del laboratorio | Evidencia que se conserva |
|---|---|---|
| `SE-037` | asignar cada evento a un modelo y declarar fugas | mapa capa → observación |
| `SE-038` | delimitar qué ocurre realmente en loopback | frontera local y lo no observado |
| `SE-039` | razonar sobre dirección, ruta y puerto sin cambiar el host | decisión de entrega |
| `SE-040` | distinguir conexión, timeout y reintento | matriz por fase e idempotencia |
| `SE-041` | contrastar resolución sana y negativa | primera divergencia DNS |
| `SE-042` | interpretar 200 y 503 por semántica | intercambio y política de reintento |
| `SE-043` | validar el nombre antes de HTTP | rechazo tipado y límite del modelo |
| `SE-044` | definir la frontera que acepta IDs entrantes | política de cabeceras confiables |
| `SE-045` | observar ciclo de vida y deadline | cierre del servidor y consumidor lento |
| `SE-046` | medir tiempos mínimos sin capturar payload | línea temporal estructurada |
| `SE-047` | correlacionar todos los eventos | request ID y primera divergencia |
| `SE-048` | ejecutar la matriz sana/degradada/recuperada | suite, pruebas y runbook |

## Entrega evaluable

La persona estudiante entrega `request-timeline.md`, el JSON de la suite y una
matriz con predicción, observación, hipótesis rival, prueba, recuperación y límite.
Debe explicar por qué `transient_loss` y `http_503` admiten un reintento acotado del
GET, y por qué el mismo automatismo no se transfiere sin más a una escritura.

## Fuentes

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446)
- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [Python `http.server`](https://docs.python.org/3/library/http.server.html)
- [Python `urllib.request`](https://docs.python.org/3/library/urllib.request.html)

Estas fuentes definen protocolos o APIs; no certifican que el laboratorio represente
toda red real. Las pruebas automatizadas respaldan únicamente los escenarios locales
declarados.
