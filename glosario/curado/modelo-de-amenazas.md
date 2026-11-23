# Modelo de amenazas

## Definición

Un **modelo de amenazas** es la representación mantenida de qué activos hay, quién puede atacarlos y con qué capacidades, qué amenazas se identificaron, qué decisiones de defensa se tomaron y qué validación se hizo. `SE-262` lo define como la descripción de qué activos hay, quién puede atacarlos, con qué capacidades y qué defensas se derivan; `SE-457` añade que se mantiene mientras el sistema cambia; `SE-398` lo reduce a tres preguntas: qué activo se protege, quién es el adversario y qué capacidad tiene. El sentido del programa es el de un artefacto vivo, no el de un informe que se entrega una vez.

## Por qué importa

Sin modelo, la seguridad se decide por susto: se arregla lo que alguien cita más. El modelo ordena las decisiones: de las tres preguntas de `SE-398` sale la **frontera adecuada** (entre dos servicios del mismo equipo, un contenedor con límites suele bastar; entre una plataforma y código enviado por terceros se acude a una máquina virtual o a una microVM). Y `SE-262` muestra una consecuencia concreta: un cliente corre en un entorno que otra persona controla, por lo que se deriva validar todo en el servidor, no confiar en comprobaciones del cliente y no guardar secretos de servicio en él.

## Cómo funciona

`SE-457` lo construye en pasos, cada uno con su razón:

1. **Activos, atacantes y supuestos.** Se empieza por lo que se quiere conservar, no por lo que se teme: calificaciones (integridad), entregas de cada estudiante (confidencialidad), disponibilidad el día del cierre. A cada activo corresponde un atacante con otra motivación, capacidad y paciencia.
2. **Diagrama de flujo de datos y fronteras de confianza.** Actores, procesos, almacenes y flujos, con líneas donde cambia quién controla qué. La frontera entre el navegador y la API es la más importante: todo lo que cruza, incluso un campo oculto o una cabecera, lo decide quien está del lado del cliente.
3. **Enumerar amenazas con STRIDE.** Seis categorías (suplantación, manipulación, repudio, divulgación de información, denegación de servicio y elevación de privilegios) usadas como lista de preguntas por elemento del diagrama, no como clasificación definitiva.
4. **Priorizar con un grafo de ataque.** Una lista no dice cuáles importan: el camino de menor costo desde el atacante hasta el objetivo es la estimación de riesgo más relevante, porque un atacante racional lo elige.
5. **Mantenerlo.** Un disparador por cambio (una regla que señala cuándo un cambio añade una frontera, un almacén o un flujo hacia un tercero) más una revisión periódica que busca lo que la regla no ve.

## Ejemplo

En `SE-457`, un grafo de doce aristas desde `internet` hasta `alterar nota` (robo de credenciales de un estudiante con costo 4, phishing a un docente con 6, token de servicio filtrado con 7, inyección SQL con 5, un campo de rol aceptado en el registro con 3, un identificador de nota adivinable con 2, y las aristas que llevan al objetivo) se evalúa con Dijkstra. La inyección SQL, que es la vulnerabilidad más citada, no estaba en el camino más barato: corregirla dejó el costo mínimo en 7. Hicieron falta cuatro bloqueos, uno por camino, para llegar a 27. Es un grafo sintético con costos asignados por la clase.

## Errores y confusiones comunes

- **Se arregla lo grave y nada mejora.** Se prioriza por gravedad y no por camino; corrección (`SE-457`): calcular el camino más barato y recalcularlo tras cada decisión.
- **Una lista de 80 amenazas sin dueño.** Se enumera sin descartar ni decidir; corrección: una fila por amenaza con elemento, respuesta y supuesto.
- **Un diagrama sin fronteras.** Se dibujó la arquitectura, no la confianza; hay que marcar dónde cambia quién controla el dato.
- **Dos revisores puntúan distinto.** Una escala numérica sin criterio verificable da poca concordancia: en la simulación de la clase, dos personas razonables comparten menos de la mitad de sus cinco amenazas más graves. Se sustituye el puntaje por preguntas que se puedan comprobar.

## Límites y cuándo no aplica

Ninguna frontera es absoluta: se elige la que hace el ataque más costoso que el beneficio y se complementa con permisos mínimos, red cerrada y límites de recursos (`SE-398`). Los resultados cuantitativos de `SE-457` salen de grafos y simulaciones sintéticos; por ejemplo, el disparador por cambio acierta donde la regla ve la frontera y falla en silencio donde no (12 de 24 en esa simulación). La combinación de disparador y revisión periódica es la única que reduce la media por debajo de 30 días y el máximo por debajo de 90. El modelo pierde validez cuando cambia el sistema y el modelo no se entera.
