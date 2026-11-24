# Capacidad

## Definición

**Capacidad** es una palabra con varios sentidos que el programa usa en clases distintas; ninguno es «cantidad máxima»:

- **Función del dispositivo protegida por el sistema** (`SE-257`): ubicación, cámara, notificaciones o archivos, que exigen una autorización. Es el sentido principal.
- **Resultado que un sistema produce bajo condiciones declaradas** (`SE-001`): lo que el producto permite hacer, no la solución que lo implementa.
- **Operación comprobable** (`SE-025`, `SE-036`): algo cuya disponibilidad se verifica en vez de suponerla por el nombre de la plataforma.
- **Referencia no falsificable a un recurso** (`SE-277`): por ejemplo un descriptor de directorio que permite operar solo sobre ese recurso.

## Por qué importa

Cada capacidad que una aplicación pide es una superficie de ataque y una carga de confianza (`SE-257`). Pedir menos reduce lo que puede filtrarse, abusarse o exigirse en una revisión de tienda. En portabilidad (`SE-025`), comprobar capacidades en lugar de deducirlas por el nombre del sistema evita decisiones falsas; y en la definición de objetivos (`SE-001`), hablar de capacidades evita formular soluciones como necesidades.

## Cómo funciona

El criterio de `SE-257` es preguntar qué función falla sin la capacidad, no qué dato podría ser útil. Si solo hace falta saber que se entregó en una ciudad, la ubicación aproximada basta; si solo se adjunta una imagen, el selector del sistema evita pedir acceso a toda la galería. El equipo escribe una tabla con una fila por función: capacidad necesaria, precisión, cuándo se pide, qué hace si se deniega o revoca y cuánto tiempo guarda el dato; cada fila tiene una prueba por estado del permiso. En `SE-277`, el modelo por capacidades (WASI) da a un módulo solo los descriptores que se le entregan: no hay autoridad ambiente. En `SE-036`, el adaptador declara qué operaciones ofrece la plataforma y la herramienta las comprueba.

## Ejemplo

`SE-257`: «Adjuntar foto» usa el selector del sistema o la cámara y, si se deniega, ofrece la galería; «Notificar vencimiento» usa notificaciones y, si se deniega, muestra un aviso en la aplicación; «Registrar lugar de entrega» no existe, porque el equipo decidió no pedir ubicación.

## Errores y confusiones comunes

- **La tienda rechaza el permiso solicitado.** Causa: se pidió una capacidad que ninguna función usa; corrección: eliminarla (`SE-257`).
- **El objetivo dice «construir el portal».** Causa: una solución formulada como necesidad; corrección: reescribir capacidad, persona, condición de éxito y de fracaso (`SE-001`).
- **El primer intento exige administrador.** Causa: se trató el privilegio como comodidad; corrección: observar sin elevación y justificar cada capacidad adicional (`SE-025`).
- **Confundir detección con autorización.** Una capacidad presente puede estar bloqueada por permisos o políticas.

## Límites y cuándo no aplica

Como la persona decide sin contexto, se conceden capacidades que quizá nunca se usen, y cada una añade superficie (`SE-257`). Una tabla de capacidades solo vale si se mantiene al añadir funciones. El sentido de `SE-277` no equivale al de permisos móviles: allí es una referencia que se pasa, aquí un permiso que se concede.
