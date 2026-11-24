# Aceptación desde el consumidor

## Definición

La **aceptación desde el consumidor** es el criterio de cierre de un producto reutilizable que `SE-120` plantea así: una persona nueva, que no conoce el código, sigue el quickstart, ejecuta un caso, interpreta un error, instala un plugin y migra de una versión a otra. El producto se acepta cuando esa persona lo consigue con la documentación y los artefactos publicados, no cuando quien lo construyó puede demostrarlo en su máquina. En el programa el término aparece en el proyecto SDK y CLI; no es una certificación formal, es un procedimiento de aceptación propio del proyecto.

## Por qué importa

Quien construye una biblioteca arrastra conocimiento que el consumidor no tiene: qué variable de entorno hay que fijar, qué orden de instalación funciona, qué mensaje de error significa qué. Una demostración hecha por el autor oculta justo esas brechas. Aceptar desde el consumidor cambia una decisión concreta: la fecha de «terminado» deja de depender de que las pruebas internas pasen y depende de que un tercero llegue a un resultado correcto con lo que se entrega. También obliga a registrar tiempo y bloqueos, de modo que la facilidad de adopción deja de ser una impresión y pasa a ser un dato.

## Cómo funciona

El procedimiento tiene cinco recorridos, cada uno con una salida observable:

1. **Quickstart:** instalar en un entorno limpio y obtener un primer resultado correcto.
2. **Ejecutar un caso:** usar la interfaz pública con una entrada propia, no la del ejemplo.
3. **Interpretar un error:** provocar una entrada inválida y comprobar que el mensaje permite actuar.
4. **Instalar un plugin:** usar el punto de extensión con un complemento compatible y con uno incompatible.
5. **Migrar:** pasar de la versión anterior a la nueva siguiendo la guía de migración.

Se anotan el tiempo hasta el primer éxito y cada punto donde la persona se detuvo. La causa de que el método funcione es la separación de roles: quien acepta no es quien implementó, así que cada supuesto implícito se vuelve un bloqueo visible. El cierre incluye además los **problemas conocidos** y la **ruta de rollback**; una demostración solo del camino feliz no los contiene.

## Ejemplo

En el producto reutilizable de `SE-120`, un release agrupa contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La aceptación consiste en que alguien ajeno parta del paquete instalado (no del repositorio clonado) y recorra los cinco pasos. Si en el paso 3 el mensaje dice solo «error de configuración», el bloqueo se registra y la corrección es mejorar el mensaje, no explicarlo en voz alta. Una forma mínima de dejarlo escrito (ilustración, no un formato del programa):

```text
paso: instalar plugin incompatible
esperado: rechazo con versión requerida y versión encontrada
observado: traza interna sin mencionar versiones
bloqueo: sí (12 min)  -> corregir mensaje antes de aceptar
```

## Errores y confusiones comunes

- **Aceptar con la demo del autor.** El autor conoce los atajos; la prueba pierde su valor. Debe ejecutarla alguien que no escribió el producto.
- **Confundirla con una prueba de contrato.** La prueba de contrato (`SE-120` la pide desde el consumidor) verifica promesas automáticamente; la aceptación verifica además documentación, mensajes y migración con una persona.
- **Medir solo el éxito.** Sin tiempo ni bloqueos registrados no hay dato para mejorar.
- **Omitir problemas conocidos y rollback.** Un cierre sin ellos oculta el riesgo de adoptar la versión.

## Límites y cuándo no aplica

Una persona es una muestra pequeña: encuentra bloqueos, pero no estima cuántos usuarios fallarían. El procedimiento acredita un release candidato dentro de su matriz de versiones y entornos, no disponibilidad, seguridad ni soporte en producción (`SE-120` lo declara). No aplica a código interno de un solo uso, donde el costo de reclutar a alguien supera lo que se aprende, y no sustituye una prueba de usabilidad con varios perfiles cuando el producto tiene muchos consumidores.
