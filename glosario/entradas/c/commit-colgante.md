# Commit colgante

[↑ Glosario](../../README.md) · [← Commit atómico](./commit-atomico.md) · [Compactación →](./compactacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Objeto que ninguna referencia alcanza y que sigue en la base hasta la poda.

Definición de trabajo de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), existe con este propósito: la clase existe para que cada commit sea una unidad que se pueda revisar, localizar y deshacer, y para que, cuando alguien se equivoca, la respuesta sea una recuperación planificada y no una búsqueda a ciegas.

## Cómo funciona

Según [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

En un repositorio con un archivo confirmado se simularon seis situaciones y se buscó el texto perdido en toda la base de objetos. Un commit seguido de `reset --hard HEAD~1`: **sigue** (y el reflog apunta a él). Un cambio agregado al índice y luego `reset --hard`: **sigue** como blob suelto. Un cambio editado sin agregar y luego `reset --hard`: **no sigue**. Un archivo no rastreado y luego `clean -fd`: **no sigue**. Un `stash` seguido de `stash drop`: **sigue** como commit colgante. Un commit, un `reset`, la expiración del reflog y `gc --prune=now`: **no sigue**. El resultado fue idéntico con Git 2.55 en Windows y 2.43 en Ubuntu.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

En la plataforma, cada cambio a `penal.py` va en un commit con una frase de resumen, un cuerpo que explica la regla de negocio afectada y un pie con el issue. Una prueba corta (`pytest -q tests/test_penal.py`) se ejecuta con `git bisect run` cuando una nota sale mal. El equipo exige que cada commit de una rama compile, de modo que la bisección no deba omitir puntos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son:

- **La bisección no señala un solo commit** — causa: hay un commit que no compila junto al defecto. Corrección: reordenar la rama para que cada paso compile y repetir.
- **Hay que leer cientos de líneas tras la bisección** — causa: el commit culpable mezcla varias intenciones. Corrección: dividir los commits con `git add -p` antes de publicarlos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales en Windows y Ubuntu (WSL2) con resultados idénticos. La prueba de bisección fue determinista, el remoto no tenía protección, las historias son de 64 cambios de dos líneas y no se midió a ninguna persona leyendo ni un repositorio real. La siguiente clase pregunta qué pasa cuando varias personas hacen commits a la vez en ramas distintas y cómo se integran.

## Relación con otros conceptos

- **Prerrequisito:** [Objeto](../o/objeto.md), [Referencia](../r/referencia.md).
- **Ver también:** [Base](../b/base.md), [Poda](../p/poda.md), [Bisección](../b/biseccion.md), [Commit atómico](./commit-atomico.md), [Recuperación](../r/recuperacion.md), [Reescribir historia](../r/reescribir-historia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria y `bisect run`; autoridad: documentación de Git.
- [git-reflog](https://git-scm.com/docs/git-reflog) — registro de movimientos de referencias; autoridad: documentación de Git.
- [git-revert](https://git-scm.com/docs/git-revert) — deshacer con un commit nuevo; autoridad: documentación de Git.
- [git-reset](https://git-scm.com/docs/git-reset) — mover una rama y sus efectos en el índice y el árbol de trabajo; autoridad: documentación de Git.
- [git-fsck](https://git-scm.com/docs/git-fsck) — objetos colgantes y `--lost-found`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Commit atómico](./commit-atomico.md) · [Compactación →](./compactacion.md)
