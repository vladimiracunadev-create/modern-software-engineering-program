# Registro de decisiones

## Definición

Un **registro de decisiones** es un documento breve con contexto, opciones, decisión, responsable, fecha y condición de revisión (SE-187). En arquitectura se llama ADR (registro de decisión de arquitectura) (SE-333). SE-586 y SE-610 lo usan como historial de quién aprobó qué, con qué evidencia, y SE-557 como la conservación de por qué se eligió una opción y qué se descartó.

## Por qué importa

Conserva el porqué cuando las personas cambian. Sin registro, nadie recuerda por qué se decidió algo y se reinventan o se deshacen decisiones sin conocer las razones. Cambia la gestión del conocimiento: la decisión y su contexto viven junto al código, no en la memoria de quien participó.

## Cómo funciona

SE-333 describe el ADR: un documento corto sobre una **decisión significativa**, con **título, estado** (propuesta, aceptada, reemplazada), **fecha, contexto, decisión, alternativas consideradas y consecuencias**. Se guarda **junto al código**, se numera y **no se edita para borrar el pasado**: si la decisión cambia, un ADR nuevo reemplaza al anterior y este queda con el estado «reemplazada». Así la historia de las decisiones es consultable.

SE-187 sitúa el registro de decisiones junto a otros tres registros de gestión: riesgos, supuestos e issues. En el ejemplo, una hoja de 23 filas se reorganiza en cuatro registros, con siete decisiones tomadas en el trimestre registradas con contexto y disparador de revisión. La **condición de revisión** es parte de la decisión: qué cambio de circunstancias la reabriría.

SE-610 añade un requisito de integridad: el registro debe poder demostrar que **no se alteró**, por ejemplo con firmas o huellas encadenadas, lo que conecta con los registros de auditoría. SE-557 lo usa para exploraciones con asistentes de IA: el registro conserva qué opciones se evaluaron, con qué datos y por qué se eligió una. Y un fallo con corrección conocida: el ganador de una matriz de decisión cambia al mover un peso porque la matriz no discrimina; se calcula la sensibilidad y se sostiene la decisión con un escenario, registrando ambos.

## Ejemplo

ADR-007. Título: «Penalización diaria con tope». Estado: aceptada. Fecha: 2026-03-04. Contexto: reclamos por descuentos arbitrarios. Opciones: penalización fija, diaria con tope, sin penalización. Decisión: diaria con tope del 50 %. Responsable: coordinación académica. Consecuencias: reglas más complejas de explicar. Revisar si: los reclamos no bajan en dos periodos. (Registro ilustrativo en el formato de SE-333.)

## Errores y confusiones comunes

- **Nadie recuerda por qué se decidió algo**: no hay registro; corrección: escribir un ADR con contexto, alternativas y consecuencias.
- **Editar el ADR para «corregir» el pasado.**
- **Registrar la decisión sin las alternativas descartadas.**
- **Decisiones sin responsable ni condición de revisión.**

## Límites y cuándo no aplica

No toda decisión merece registro: solo las significativas o de difícil reversión. Un registro sin lectores se pudre; se enlaza desde el código afectado. Las decisiones triviales y reversibles no justifican el costo de documentarlas.
