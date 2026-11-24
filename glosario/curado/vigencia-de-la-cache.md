# Vigencia de la caché

## Definición

La **vigencia de la caché** (TTL, *time to live*) es el tiempo máximo durante el cual un dato guardado puede reutilizarse sin comprobarse de nuevo. El programa la aplica en contextos distintos:

- **Registros DNS** (`SE-041`): tiempo máximo indicado para reutilizar un dato en caché.
- **Respuestas HTTP** (`SE-249`): tiempo durante el cual una respuesta guardada se considera fresca.
- **Valores de aplicación** (`SE-356`): tiempo máximo que un valor puede servirse desde la caché sin comprobarse.
- **Decisiones de autorización** (`SE-514`): tiempo durante el cual un cliente reutiliza una decisión sin consultarla.
- **Recursos temporales** (`SE-488`): tiempo máximo de vida de un recurso tras el cual se destruye salvo que se renueve.

## Por qué importa

La vigencia es la cuantificación de «cuánto aceptamos estar desactualizados» a cambio de velocidad y menor carga. Es una decisión de producto además de técnica: determina cuánto tarda en notarse un cambio y, en seguridad, cuánto tiempo sigue siendo válida una decisión revocada.

## Cómo funciona

Durante la vigencia, quien tiene la copia no pregunta al origen; al expirar, vuelve a consultar. De ahí se derivan consecuencias medibles:

- **Exposición tras revocación** (`SE-514`): si la revocación ocurre en un instante cualquiera, cada cliente conserva el acceso hasta que expire su entrada, a una distancia uniforme entre 0 y TTL; la exposición media es TTL/2 y la máxima, TTL. El experimento de la clase calcula, con 2 000 clientes que hacen 0,5 peticiones por segundo, las exposiciones y las peticiones autorizadas para cinco vigencias.
- **Propagación** (`SE-041`): TTL limita cuánto tiempo puede reutilizarse un registro; no fija una hora universal de propagación. Las respuestas negativas también pueden almacenarse.
- **Expiraciones simultáneas** (`SE-356`): tras un despliegue con caché fría, todas las entradas expiran a la vez y la base se satura.

## Ejemplo

Antes de migrar un servicio, bajar el TTL del registro DNS de 3600 s a 60 s con anticipación. Así, cuando se cambia el destino, las cachés de resolvedores que respetan la política expiran pronto. Ilustración de cálculo de `SE-514`:

```python
ttl = 300
exposicion_media = ttl / 2    # 150 s
exposicion_maxima = ttl       # 300 s
```

## Errores y confusiones comunes

- **Cambiar un registro y esperar efecto inmediato.** Causa: el TTL anterior y las cachés demoran la propagación; corrección: bajar el TTL antes del cambio y esperar su expiración (`SE-041`).
- **Los docentes ven notas viejas.** Causa: TTL largo en datos que cambian; corrección: TTL corto o invalidación al cambiar, y revalidación condicional (`SE-249`).
- **La base se satura tras un despliegue.** Causa: caché fría y expiraciones simultáneas; corrección: variar el TTL, precalentar escalonadamente y recarga única (`SE-356`).

## Límites y cuándo no aplica

Reducir el TTL antes de una migración reduce la persistencia futura, pero no invalida copias ya almacenadas ni clientes que incumplen la política (`SE-041`). En autorización, un TTL corto no equivale a revocación inmediata. Y la vigencia aplica a copias; si el dato debe ser siempre el más reciente, no corresponde una caché sin validación.
