# Reflog

[↑ Glosario](../../README.md) · [← Reflexión](./reflexion.md) · [Reflujo →](./reflujo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Registro local de los movimientos de las referencias, que permite volver a commits ya no alcanzables.

Definición de trabajo de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), existe con este propósito: la clase existe para que cada commit sea una unidad que se pueda revisar, localizar y deshacer, y para que, cuando alguien se equivoca, la respuesta sea una recuperación planificada y no una búsqueda a ciegas.

## Cómo funciona

Según [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

Git solo puede recuperar lo que entró en su base de objetos. Un commit que dejó de ser alcanzable sigue ahí hasta que el reflog expira y se poda, y se encuentra con `git reflog`. Un archivo agregado al índice crea un blob que `git fsck --lost-found` puede hallar. Un cambio que nunca se agregó y un archivo sin rastrear no tienen copia. La política de recuperación empieza por esa frontera: lo confirmado se recupera, lo agregado a veces, lo demás no.

Según [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** tras «limpiar» con `reset --hard`, una edición de la regla ha desaparecido y `git reflog` no la muestra. **Hipótesis rivales:** (a) el reflog expiró; (b) la edición nunca llegó a la base de objetos. **Prueba:** busca el texto de la edición en todos los blobs con `git cat-file --batch-all-objects`: no está. **Conclusión:** la causa es (b): el cambio no se agregó ni se confirmó y por tanto no hay copia. **Regresión:** añade al flujo la regla «antes de un comando que sobrescribe, `git stash` o una rama temporal» y una prueba que cree una edición sin agregar, ejecute el comando y verifique que el flujo lo impide.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

En la plataforma, cada cambio a `penal.py` va en un commit con una frase de resumen, un cuerpo que explica la regla de negocio afectada y un pie con el issue. Una prueba corta (`pytest -q tests/test_penal.py`) se ejecuta con `git bisect run` cuando una nota sale mal. El equipo exige que cada commit de una rama compile, de modo que la bisección no deba omitir puntos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son:

- **La bisección no señala un solo commit** — causa: hay un commit que no compila junto al defecto. Corrección: reordenar la rama para que cada paso compile y repetir.
- **Hay que leer cientos de líneas tras la bisección** — causa: el commit culpable mezcla varias intenciones. Corrección: dividir los commits con `git add -p` antes de publicarlos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** se buscó el texto en objetos locales; no se midió cuánto tarda en expirar un reflog real (que depende de la configuración) ni se cubrió un editor que guarde copias propias. ([SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Referencia](./referencia.md).
- **Ver también:** [Registro](./registro.md), [Bisección](../b/biseccion.md), [Commit atómico](../c/commit-atomico.md), [Commit colgante](../c/commit-colgante.md), [Recuperación](./recuperacion.md), [Reescribir historia](./reescribir-historia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-reflog](https://git-scm.com/docs/git-reflog) — registro de movimientos de referencias; autoridad: documentación de Git.
- [git-bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria y `bisect run`; autoridad: documentación de Git.
- [git-revert](https://git-scm.com/docs/git-revert) — deshacer con un commit nuevo; autoridad: documentación de Git.
- [git-reset](https://git-scm.com/docs/git-reset) — mover una rama y sus efectos en el índice y el árbol de trabajo; autoridad: documentación de Git.
- [git-fsck](https://git-scm.com/docs/git-fsck) — objetos colgantes y `--lost-found`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Reflexión](./reflexion.md) · [Reflujo →](./reflujo.md)
