# Recurso

## Definición

Un **recurso** es, en el diseño de APIs, algo con identidad que el sistema puede nombrar y sobre lo que puede actuar mediante métodos (`SE-242`). `SE-042` lo precisa como el objetivo conceptual identificado por una URI. En el trabajo con agentes (`SE-571`) es un dato que un servidor expone y que la aplicación decide cómo incorporar al contexto. Es sustantivo, no acción.

## Por qué importa

Modelar bien los recursos decide la forma de toda la API: qué URL existen, qué métodos tienen sentido, qué se puede cachear y cómo se evitan conflictos de edición. `SE-242` lo muestra con dos fallos concretos: pérdidas silenciosas de cambios por escrituras ciegas y datos viejos servidos por la caché.

## Cómo funciona

En HTTP, la URL identifica al recurso, no a la acción (`SE-242`). «Entrega» es un recurso; «subirEntrega» es una acción que pertenece al método (`POST` sobre la colección). Modelar acciones como recursos (`/entregas/42/apelaciones`) es legítimo cuando la acción crea algo con identidad propia que luego se consulta; ahí el sustantivo es la apelación.

Un recurso editable por varias personas necesita control de concurrencia: el servidor entrega un validador (`ETag`) con cada representación y el cliente lo devuelve en `If-Match` al modificar; si el recurso cambió, el servidor responde `412` y el cliente relee. La caché también necesita validador e invalidación: sin ellos, sirve datos viejos tras editar. En `SE-571`, un recurso expuesto por un servidor no entra al contexto del modelo automáticamente: la aplicación decide si y cómo.

## Ejemplo

```text
GET  /entregas/42           -> 200, ETag: "v7"
PUT  /entregas/42           If-Match: "v7"   -> 200 ("v8")
PUT  /entregas/42           If-Match: "v7"   -> 412 Precondition Failed (otra persona editó antes)
```

## Errores y confusiones comunes

- **Un docente pierde su cambio sin error.** Causa: `PUT` ciego sobre un recurso editable por varias personas; corrección: `ETag`, `If-Match` y `412` con releer (`SE-242`).
- **La caché sirve datos viejos tras editar.** Causa: respuesta cacheable sin validador ni invalidación; corrección: `ETag` y revalidación, evitando TTL largos en recursos editables (`SE-242`).
- **Verbos en las URL.** `/subirEntrega` mezcla acción y recurso.

## Límites y cuándo no aplica

No todo encaja como recurso: operaciones de procesamiento puro o comandos con muchos pasos a veces se modelan mejor como acciones o como un proceso con estado. En otros contextos, «recurso» designa CPU, memoria o conexiones (recursos de cómputo); esta entrada trata el sentido de identidad nombrada. Y en un taller, `SE-023` usa «recursos» para los archivos que se comparan tras verificar un invariante.
