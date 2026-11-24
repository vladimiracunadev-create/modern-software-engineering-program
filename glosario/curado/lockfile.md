# Lockfile

## Definición

Un **lockfile** (archivo de bloqueo) es un registro de las resoluciones concretas de dependencias para poder repetir una instalación (`SE-032`). `SE-111` precisa su contenido: registra la selección concreta y, según el formato, hashes, fuente, marcadores y grupos. Distingue el manifiesto, que declara rangos aceptables, del lock, que dice qué versiones exactas se eligieron.

## Por qué importa

Sin lock, la misma lista de dependencias puede resolver a versiones distintas mañana y producir un fallo que no estaba en tu código. Con lock, el equipo y la integración continua instalan lo mismo. Pero `SE-111` y `SE-032` advierten un matiz: mejora la repetibilidad dentro de su alcance; no congela runtime, sistema operativo ni disponibilidad del índice. Cambia qué se versiona y qué se revisa.

## Cómo funciona

El resolvedor lee el manifiesto (rangos), calcula un conjunto compatible, incluye las dependencias transitivas y escribe el resultado: nombre, versión, hashes del artefacto, fuente y, según el formato, marcadores de plataforma y grupos (principal, desarrollo). Al instalar desde el lock, el gestor no vuelve a resolver: usa lo registrado y puede verificar los hashes. Se actualiza **deliberadamente** (un comando explícito) y se revisa como cambio de código, porque un cambio en el lock es un cambio de lo que corre.

La causa de sus límites es que el lock describe artefactos, no entornos: se generó en una plataforma y un intérprete concretos. `SE-111` muestra el caso «CI pasa y producción rompe con la misma lista».

## Ejemplo

Ilustración con pip-tools y con npm:

```bash
pip-compile --generate-hashes requirements.in      # genera requirements.txt con versiones y hashes
npm ci                                              # instala exactamente lo que dice package-lock.json
```

Para una biblioteca que se publica, el lock del repositorio sirve para sus pruebas, pero no se transmite a quien la instale (`SE-111`).

## Errores y confusiones comunes

- **CI pasa y producción rompe con la misma lista.** Causa: el lock se generó en otra plataforma o versión de Python; corrección: registrar plataforma e intérprete y probar en cada plataforma soportada (`SE-111`).
- **Presentarlo como garantía total.** Causa: se ignoraron origen, runtime y plataforma; corrección: documentar qué fija y qué queda variable (`SE-032`).
- **Editarlo a mano o regenerarlo sin revisión.** El cambio de versiones queda sin examinar.

## Límites y cuándo no aplica

Para el consumidor de una biblioteca, el lockfile no se hereda: lo decide la aplicación (`SE-111`). No protege si el índice retira un paquete, ni cubre el sistema operativo. Y fijar versiones no es actualizarlas: un lock viejo congela también las vulnerabilidades conocidas, por lo que requiere revisión periódica.
