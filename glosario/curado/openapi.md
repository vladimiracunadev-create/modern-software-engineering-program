# OpenAPI

## Definición

**OpenAPI** es un formato de descripción de interfaces HTTP: rutas con sus operaciones, parámetros, respuestas por código y esquemas de las cargas (SE-163). Un documento OpenAPI es un contrato legible por personas y por herramientas. Su compañero para interfaces basadas en eventos es AsyncAPI.

## Por qué importa

Convierte la interfaz en un artefacto que se puede versionar, revisar y verificar, en lugar de un acuerdo oral o un texto en un wiki. Habilita documentación generada, clientes generados y pruebas. Cambia una decisión de diseño: la descripción de la API se mantiene junto al código y se comprueba contra él.

## Cómo funciona

El documento enumera cada ruta y operación con sus parámetros (de ruta, consulta, cabecera), cuerpos y respuestas por código de estado, con esquemas para las cargas. Como es estructurado, una herramienta puede validar su forma, generar documentación, producir clientes en distintos lenguajes y derivar pruebas.

SE-163 subraya su **límite central: describe, no obliga**. El servicio puede responder otra cosa y el documento seguirá siendo válido: documento y servicio pueden divergir sin que ninguna herramienta lo advierta. La corrección es la **prueba contractual**: una comprobación en integración continua que verifica que el servicio responde lo que el documento promete (SE-166). La clase añade que un contrato HTTP incluye además la semántica definida en RFC 9110 (métodos, códigos, cabeceras), y es en esos detalles donde aparecen las discrepancias.

En la plataforma de entregas, el documento OpenAPI de la API y el documento AsyncAPI de los eventos viven en el repositorio, versionados con el código. Un linter de integración continua verifica la forma (identificadores únicos, parámetros, respuestas de error); una prueba contractual comprueba que el servicio responda lo prometido, incluida la respuesta 201 de `crearEntrega`. El documento de eventos declara la semántica de entrega («al menos una vez», sin orden global) y exige identificador y versión en cada mensaje; los consumidores son idempotentes por diseño.

## Ejemplo

Fragmento mínimo de una operación (ilustración del formato):

```yaml
paths:
  /entregas:
    post:
      operationId: crearEntrega
      responses:
        "201":
          description: Entrega creada
```

Un cliente generado a partir de este documento llamará a `POST /entregas` y esperará un 201. Si el servicio real devuelve 200, el documento sigue siendo válido pero el cliente falla: justo el síntoma que SE-163 asocia a la divergencia, y que la prueba contractual detecta.

## Errores y confusiones comunes

- **Un cliente generado falla contra el servicio real**: documento y servicio divergieron; corrección: pruebas contractuales en integración continua.
- **Notificaciones duplicadas**: el consumidor no es idempotente y la entrega es «al menos una vez»; corrección: identificador único por evento y descarte de repetidos.
- **Creer que el documento valida el servicio**: lo describe.
- **Confundir OpenAPI con Swagger**: Swagger es el nombre histórico y un conjunto de herramientas; OpenAPI es la especificación.

## Límites y cuándo no aplica

No describe bien APIs que no son HTTP/REST (por ejemplo, GraphQL o gRPC tienen sus propios lenguajes de esquema). No captura reglas de negocio complejas ni orden entre llamadas. Un documento generado automáticamente del código puede heredar sus defectos; uno escrito primero puede divergir. En cualquier caso hace falta la comprobación contractual.
