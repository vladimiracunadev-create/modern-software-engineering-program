# Parte 26 — Datos, persistencia y recuperación

La Parte 25 dejó fronteras, agregados y decisiones registradas. La pregunta cambia de «cómo se divide el sistema» a «qué pasa con los datos cuando varias personas escriben a la vez, un cliente se equivoca, un despliegue cambia el esquema o una copia es lo único que queda». Esta parte trabaja sobre **la capa de datos de la plataforma de entregas de tareas**, un caso sintético: estudiantes, cursos, entregas y calificaciones guardados en una base que debe seguir siendo correcta, rápida, evolucionable y recuperable. Recorre el modelo conceptual, lógico y físico, la elección entre filas, documentos, claves y grafos, las transacciones y el aislamiento, las restricciones, los índices, las migraciones compatibles, la replicación y la partición, las cachés, los respaldos con su restauración, el ciclo de vida de los datos personales, un taller de migración peligrosa y un paquete de capa de datos recuperable.

## Pregunta rectora

> ¿Qué invariantes deben sobrevivir a la concurrencia, al fallo y a la restauración, y cómo lo sabría quien opera esta base?

## Antes del recorrido clase por clase

Esta parte no enseña un motor de bases de datos ni un producto. Enseña a distinguir lo que el negocio afirma de lo que el motor guarda, a medir qué cuesta cada elección de modelo, a enumerar las intercalaciones que rompen una invariante, a decidir qué regla impone el motor y cuál queda a un cliente, a leer un plan de ejecución y contar lo que cada índice cobra, a dividir un cambio incompatible en fases, a elegir una garantía de lectura y una clave de reparto, a dar a una caché su política, a medir qué ve una verificación de respaldo y qué deja pasar, a comprobar dónde queda un dato borrado, a ensayar una migración con instrumentos de distinta potencia y a entregar un paquete cuyos límites conoces. Cada clase ejecuta experimentos con datos sintéticos que muestran un mecanismo (un contador que acierta en 6 de 90 intercalaciones, una copia del archivo que da «ok» y una suma 197 unidades menor, un hash de correo que un diccionario invierte por completo) y declara lo que esa medida no demuestra.

```mermaid
flowchart LR
    A[Modelo conceptual, lógico y físico] --> B[Modelos de almacenamiento]
    B --> C[Transacciones y aislamiento]
    C --> D[Restricciones e invariantes]
    D --> E[Consultas e índices]
    E --> F[Migraciones compatibles]
    F --> G[Replicación y partición]
    G --> H[Cachés entre capas]
    H --> I[Respaldos y restauración]
    I --> J[Privacidad y ciclo de vida]
    J --> K[Taller de migración peligrosa]
    K --> L[Paquete de capa de datos]
    L -->|incidente o hallazgo| A
```

El diagrama se lee de izquierda a derecha y no es un proceso obligatorio. El retorno indica que un incidente, un hallazgo del ensayo de restauración o un cambio de requisito reabre el modelo; un paquete aprobado no cierra el diseño, lo fecha.

## Resultados acumulativos

Podrás separar las decisiones de negocio, lógicas y físicas de un esquema y medir las anomalías de una tabla plana, el costo de una clave y los falsos positivos de una lista en una columna; comparar los costos de lectura, de reescritura y de búsqueda de filas, documentos y claves y recorrer un grafo con una consulta recursiva que no se desboca ante un ciclo; enumerar las intercalaciones de varios clientes, comparar leer-sumar-escribir, comprobación de versión y actualización atómica y reproducir un sesgo de escritura; medir qué filas inválidas deja pasar cada capa de restricciones y cuántas inserciones duplicadas evita una restricción de unicidad; leer un plan de ejecución, medir el trabajo con y sin índice, elegir el orden de un índice compuesto y contar el costo de escritura de cada índice; construir la matriz de compatibilidad entre versiones de una migración en fases, medir el efecto del tamaño de un lote y comprobar qué migraciones son reversibles de verdad; cuantificar las lecturas obsoletas de una réplica, un cuórum y los movimientos de claves de dos funciones de reparto, y detectar una clave caliente; comparar políticas de caché, el pico de una estampida y una carrera de relleno; calcular la pérdida por intervalo de copia, distinguir una copia consistente de una ingenua y medir qué detecta cada nivel de verificación; contar los restos de un dato tras borrarlo, la unicidad de atributos combinados y la recuperación de un hash por diccionario; ensayar una migración en tres entornos y cortarla en cada paso; y entregar un paquete con un validador cuyos límites conoces.

Al finalizar podrás defender una capa de datos con sus invariantes, su plan de migraciones, sus objetivos de recuperación medidos, su política de caché y de distribución, su ciclo de vida de los datos personales y una lista de lo que ninguna prueba ni validador ve, y podrás indicar qué parte de tu conclusión es observación, cuál es inferencia y cuál es suposición.

## Prerrequisitos enlazados

- [Parte 4 — Pensamiento computacional](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/): modelado, enumeración de casos y razonamiento sobre evidencia.
- [Parte 7 — Estructuras de datos y algoritmos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/): costo de las operaciones, tablas hash e índices como estructuras de búsqueda.
- [Parte 13 — Especificaciones, contratos y modelos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-13-especificaciones-contratos-y-modelos/): invariantes, compatibilidad entre versiones y contratos comprobables.
- [Parte 20 — Backend, APIs y procesamiento asíncrono](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-20-backend-apis-y-procesamiento-asincrono/): idempotencia, reintentos y consistencia en el servidor.
- [Parte 25 — Arquitectura de software y dominio](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-25-arquitectura-de-software-y-dominio/): fronteras, agregados y decisiones registradas.
- Python 3.11+ y terminal; los experimentos usan solo la biblioteca estándar (incluido `sqlite3`) y datos sintéticos.

## Bloques y progresión

1. **Modelar los datos:** las clases 313 y 314 separan los niveles de modelo y comparan filas, documentos, claves y grafos por las preguntas que abaratan.
2. **Corrección bajo concurrencia:** las clases 315 y 316 enumeran las intercalaciones que rompen una invariante y miden qué capa de restricciones la protege.
3. **Rendimiento y cambio:** las clases 317 y 318 miden qué ayuda y qué cuesta un índice y dividen un cambio de esquema en fases compatibles.
4. **Distribución y capas:** las clases 319 y 320 miden lecturas obsoletas, movimiento de claves, estampidas y carreras de relleno.
5. **Recuperación y ciclo de vida:** las clases 321 y 322 miden qué verifica una restauración y dónde queda un dato borrado o supuestamente anónimo.
6. **Aplicar e integrar:** las clases 323 y 324 ensayan una migración peligrosa y entregan un paquete de capa de datos recuperable.

## Evidencia medida y límites

Las figuras y los ejemplos de esta parte usan experimentos ejecutados con CPython 3.12.9 en Windows 11 (SQLite 3.45.3) y repetidos con CPython 3.12.3 en Ubuntu bajo WSL2 (SQLite 3.45.1). Los datos son **sintéticos** y las semillas están fijadas: las salidas de los doce experimentos fueron idénticas en ambos sistemas en todas las cifras salvo dos excepciones, ambas del entorno y no del método: los pasos de la máquina virtual de SQLite del relleno por lotes de `SE-318` difirieron un 7 % entre las dos versiones del motor con la misma proporción entre tamaños de lote (por ejemplo, 1 400 021 y 1 500 021 pasos en la transacción única), y los bytes comprimidos con zlib de `SE-324` difirieron menos de un 1 %. Ninguno mide tiempo de reloj. Todo el código usa solo la biblioteca estándar.

Los experimentos son: una tabla plana frente a un modelo normalizado, el tamaño del archivo con tres claves primarias y los falsos positivos de una lista separada por comas (`SE-313`); las lecturas y reescrituras de filas frente a documentos embebidos, la búsqueda por clave, por posición y por atributo con un índice secundario manual, y una consulta recursiva de prerrequisitos con y sin ciclo (`SE-314`); tres clientes que suben un contador en las 90 intercalaciones, una transferencia cortada en cada paso y dos retiradas de guardia en las 70 intercalaciones bajo tres niveles de aislamiento, con una ejecución real en SQLite (`SE-315`); ocho familias de filas inválidas frente a cuatro capas de restricciones, tres clientes que comprueban y luego insertan en las 90 intercalaciones, y el borrado de un curso con cuatro acciones de clave foránea encendida y apagada (`SE-316`); los pasos de ejecución con y sin índice con 50 000 filas, cinco consultas frente a tres índices compuestos, el costo de escritura de cero a cuatro índices y el patrón de una consulta por elemento (`SE-317`); la matriz de compatibilidad entre dos versiones de la aplicación y cuatro estados del esquema, el relleno de 100 000 filas con cinco tamaños de lote y seis migraciones aplicadas y revertidas (`SE-318`); las lecturas obsoletas de réplicas asíncronas y de un cuórum, las claves movidas por el reparto con módulo y con un anillo de hash y el desequilibrio de carga con popularidad Zipf (`SE-319`); seis políticas de caché sobre 200 000 operaciones, la estampida de mil claves que expiran a la vez y una carrera de lectura y escritura en seis órdenes (`SE-320`); la pérdida por intervalo de copia, una copia del archivo de una base en uso frente a la copia en línea y 200 copias alteradas frente a seis niveles de verificación (`SE-321`); los restos de un valor tras `DELETE`, `secure_delete` y `VACUUM`, las filas vencidas con cuatro políticas de retención, la unicidad de 5 000 personas sintéticas según los atributos combinados y un hash de correo contra un diccionario (`SE-322`); un analizador de texto sobre 200 mutaciones de una migración, seis migraciones defectuosas en tres entornos de ensayo y una migración de cinco pasos cortada en cada punto (`SE-323`); y un validador de paquetes sobre 200 mutaciones, un mes simulado con un borrado y una corrupción silenciosa bajo tres estrategias de respaldo y el costo comprimido de retener copias (`SE-324`).

Los parámetros (los 5 000 y 50 000 registros, el corte del lote tras 100 filas, el fallo del 1 % entre dos escrituras, el retardo exponencial de 50 ms y la lectura entre 0 y 200 ms, la popularidad Zipf con exponentes 1,0 y 1,1, el 5 % de escrituras, el 90 % de entregas «enviadas», el plazo de retención de 12 meses, la tasa de 20 000 eventos al mes, los atributos uniformes e independientes de las 5 000 personas, los siete correos duplicados y las treinta notas en cero, los 200 registros por día y los dos incidentes del mes simulado) son supuestos del autor, no datos de una plataforma, una institución ni de personas reales. Las reglas léxicas de los dos validadores se ajustaron con los mismos casos que los evalúan: su exactitud real es desconocida. El modelo de niveles de aislamiento, el cuórum, las cachés y la bitácora del mes simulado son modelos del autor y no reproducen un motor concreto. Los generadores de números pseudoaleatorios de Python se usaron solo para simular; no son criptográficos. Los plazos de retención no son una interpretación de una ley ni de una norma institucional y esta parte no evalúa el cumplimiento de ninguna. No se usó ningún servidor de bases de datos (solo SQLite), motor documental, de clave-valor o de grafos, base distribuida, caché, red, nube ni proveedor; no se midió latencia, tiempo de restauración, rendimiento ni carga; y no se probó cifrado, discos de estado sólido ni sistemas de archivos con instantáneas. Esta parte no tiene laboratorio propio en `labs/`; el proyecto integrador `SE-324` define el paquete y la evidencia. Cada clase termina con un puente hacia el trabajo con agentes.

## Guía razonada clase por clase

La capa de datos de la plataforma mantiene un modelo, un esquema y un paquete estables mientras cambian las decisiones. Cada clase explica qué incertidumbre reduce, qué experimento la muestra, qué no demuestra y qué evidencia permite abandonar la conclusión.

### Bloque 1 — Modelar los datos

#### SE-313 — Modelado conceptual, lógico y físico

Mezclar los tres niveles hace que un detalle del motor se convierta en una propiedad del negocio que nadie decidió. La clase mide las tres anomalías de una tabla plana, cuánto cuesta una clave de texto frente a una entera y cuántos resultados falsos devuelve buscar identificadores en una lista dentro de una columna.

El estudiante entrega un modelo conceptual y un `schema.sql` con cada decisión clasificada. `SE-314` compara qué cambia cuando los datos se guardan de otras formas.

#### SE-314 — Relacional, documental, clave-valor, grafos y series

Cada modelo abarata una pregunta y encarece un cambio. La clase cuenta lo que toca cada operación con filas y con documentos embebidos, mide la búsqueda por clave y por atributo con un índice manual desincronizable y recorre un grafo de prerrequisitos con una consulta recursiva, con y sin ciclo.

El estudiante entrega una matriz de preguntas frecuentes contra modelos con lo medido. `SE-315` pregunta qué ocurre cuando varias personas cambian los datos a la vez.

### Bloque 2 — Corrección bajo concurrencia

#### SE-315 — Transacciones, aislamiento y concurrencia

La atomicidad evita el corte a mitad y no que otra operación lea un valor viejo. La clase enumera 90 intercalaciones de tres clientes que suben un contador, corta una transferencia antes de cada paso y enumera las 70 intercalaciones que dejan sin docentes de guardia a la plataforma según el nivel de aislamiento.

El estudiante entrega las operaciones concurrentes con su invariante, su mecanismo y su prueba de intercalaciones. `SE-316` pregunta qué invariantes puede imponer el propio motor.

#### SE-316 — Restricciones, invariantes y consistencia

La última defensa contra un dato inválido es la que no depende de cada cliente. La clase mide cuántas de 1 600 filas inválidas deja pasar cada capa de restricciones, enumera los órdenes de tres clientes que comprueban y luego insertan y muestra qué hace borrar un curso con la clave foránea apagada.

El estudiante entrega un catálogo de invariantes con mecanismo y prueba de humo. `SE-317` mide cómo se consultan eficientemente.

### Bloque 3 — Rendimiento y cambio

#### SE-317 — Consultas, índices y patrones de acceso

Un índice ayuda a las consultas que coinciden con su forma y cobra en cada escritura. La clase mide el trabajo de ejecución con y sin índice según la selectividad, el efecto del orden de las columnas de un índice compuesto frente a cinco consultas y el costo de insertar con cero a cuatro índices.

El estudiante entrega un catálogo de patrones de acceso con índices justificados. `SE-318` cambia el esquema sin detener a nadie.

#### SE-318 — Migraciones compatibles y evolución de esquema

Durante un despliegue conviven dos versiones del código con el mismo esquema. La clase construye la matriz de compatibilidad de un renombrado directo y de una migración en fases, mide el tamaño de la transacción más larga con cinco tamaños de lote y cuenta qué datos pierde aplicar y revertir seis migraciones.

El estudiante entrega un plan expandir-migrar-contraer con su punto de no retorno. `SE-319` pregunta qué ocurre cuando los datos viven en más de una máquina.

### Bloque 4 — Distribución y capas

#### SE-319 — Replicación, partición y distribución

Replicar copia el mismo dato y particionar reparte datos distintos, y cada uno introduce su propio riesgo. La clase simula lecturas obsoletas de réplicas y de un cuórum, mide las claves que se mueven con un módulo y con un anillo de hash y calcula el desequilibrio por una clave caliente.

El estudiante entrega la decisión de replicar o particionar con su garantía de lectura propia. `SE-320` mira las copias que se guardan entre capas.

#### SE-320 — Cachés y consistencia entre capas

Una caché es una segunda fuente de verdad con garantías más débiles que una réplica. La clase compara seis políticas por aciertos y lecturas obsoletas, calcula el pico de una estampida con y sin variación del TTL y enumera el orden de un lector y un escritor que deja la caché vieja.

El estudiante entrega la política de caché por dato con su frescura máxima. `SE-321` pregunta qué pasa cuando todo falla.

### Bloque 5 — Recuperación y ciclo de vida

#### SE-321 — Backups, restauración y pruebas de recuperación

Una copia que no se ha restaurado es una hipótesis. La clase calcula la pérdida según el intervalo, compara copiar el archivo de una base en uso con la copia en línea y mide qué detecta cada uno de seis niveles de verificación sobre 200 copias alteradas.

El estudiante entrega los objetivos de recuperación, el procedimiento y la verificación con su manifiesto de negocio. `SE-322` pregunta qué datos no deberían conservarse.

#### SE-322 — Privacidad, retención y ciclo de vida del dato

Borrar una fila no borra el dato. La clase cuenta lo que queda de un valor tras `DELETE`, `secure_delete` y `VACUUM`, calcula las filas vencidas con cuatro políticas de retención y mide cuántas personas son únicas según los atributos combinados y cuántos correos recupera un diccionario de un hash sin clave.

El estudiante entrega un inventario de datos personales con retención, borrado y política de anonimización. `SE-323` pone a prueba las migraciones con un taller.

### Bloque 6 — Aplicar e integrar

#### SE-323 — Taller: corregir una migración peligrosa

Los defectos más caros de una migración tienen la forma correcta y el contenido equivocado. El taller mide qué detecta un analizador de texto sobre 200 mutaciones, qué ve cada uno de tres entornos de ensayo y cuántos cortes de una migración de cinco pasos dejan un estado intermedio.

El estudiante entrega una migración corregida en fases con invariantes y punto de no retorno. `SE-324` la integra en un paquete.

#### SE-324 — Proyecto: capa de datos recuperable

Un paquete completo no es un paquete correcto. El proyecto mide qué detecta un validador sobre 200 mutaciones de un paquete, simula un mes con un borrado y una corrupción silenciosa bajo tres estrategias de respaldo y calcula el costo comprimido de retener copias.

El estudiante entrega un paquete de capa de datos con su restauración ensayada y `LIMITES.md`. La Parte 27 lleva esos datos a la integración entre servicios por mensajes y eventos.

## Fuentes

- [Codd, «A relational model of data for large shared data banks» (1970)](https://dl.acm.org/doi/10.1145/362384.362685) — modelo relacional e independencia de la representación; autoridad: artículo original.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de datos, transacciones, replicación y recuperación como compromisos de diseño; autoridad: autor del libro.
- [PostgreSQL: aislamiento de transacciones](https://www.postgresql.org/docs/current/transaction-iso.html) — niveles y anomalías; autoridad: documentación oficial de PostgreSQL.
- [Berenson et al., «A Critique of ANSI SQL Isolation Levels»](https://arxiv.org/abs/cs/0701157) — anomalías no cubiertas por el estándar; autoridad: artículo de los autores.
- [SQLite: aislamiento](https://www.sqlite.org/isolation.html), [claves foráneas](https://www.sqlite.org/foreignkeys.html) y [planificador de consultas](https://www.sqlite.org/queryplanner.html) — comportamiento del motor usado en los experimentos; autoridad: documentación oficial de SQLite.
- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original.
- [AWS Builders' Library: caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) — consistencia y estampida de una caché; autoridad: Amazon Web Services.
- [SQLite: API de copia en línea](https://www.sqlite.org/backup.html) y [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — copia consistente y planes de contingencia; autoridad: SQLite y NIST.
- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) y [NIST SP 800-88 Rev. 1](https://csrc.nist.gov/pubs/sp/800/88/r1/final) — minimización, retención y saneamiento de medios; autoridad: Unión Europea y NIST.
- [Sweeney, «k-anonymity»](https://doi.org/10.1142/S0218488502001648) — k-anonimato; autoridad: artículo original.

Las fuentes se vinculan también dentro de cada clase. Definen vocabulario y mecanismos; la adecuación de las decisiones de la capa de datos se demuestra con el caso, la evidencia trazable y la revisión de otra persona, no con la autoridad de la fuente.

## Criterios de aceptación de la parte

- cada clase conecta mecanismo, medida y límite en una conclusión revisable;
- cada medida puede reproducirse desde un checkout limpio con las mismas semillas;
- ninguna afirmación sobre un motor, una carga o personas reales se apoya en una simulación;
- los límites declarados permiten a otra persona decidir qué comprobar antes de confiar.

[Volver al índice de clases](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md)
