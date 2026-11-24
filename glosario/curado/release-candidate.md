# Release candidate

## Definición

Un **release candidate** (RC, candidato a versión) es, en el proyecto de `SE-120`, una versión **candidata a publicarse tal cual**: se construye con **artefactos inmutables**, con *changelog*, **hashes** y **guía de migración**, y se somete a verificación completa. Si no aparecen problemas, ese mismo artefacto es el que se publica como versión final. En versionado semántico, un RC se publica como *prerelease* (por ejemplo `1.3.0rc1`). Es un uso estándar del término en distribución de software; el programa añade el rigor de verificar exactamente lo que se entrega.

## Por qué importa

El fallo clásico de un lanzamiento es probar una cosa y publicar otra: la suite pasó sobre un árbol de trabajo, pero el artefacto que se sube se construyó después, con otro entorno, y difiere. La decisión que cambia es qué se prueba: **se instala exactamente el artefacto que se pretende publicar**. Y qué ocurre si algo cambia: según `SE-120`, **si cambia un byte tras la prueba, se genera otro *prerelease***, no se «arregla» silenciosamente el anterior.

## Cómo funciona

El proceso de un RC tiene un orden:

1. **Congelar** el contenido: etiqueta de versión y artefactos construidos una vez (rueda y fuente), que no se reconstruyen.
2. **Calcular y publicar hashes** de cada artefacto, para poder demostrar después que lo probado es lo entregado.
3. **Verificar el artefacto**, no el árbol: instalarlo en un entorno limpio, ejecutar la matriz de compatibilidad, la prueba de consumidor y la aceptación.
4. **Documentar:** *changelog* con cambios y clasificación de compatibilidad, y guía de migración si hay cambios incompatibles.
5. **Decidir:** si todo pasa, promover ese artefacto; si algo cambia, otro RC y se repite.

La inmutabilidad es lo que da sentido a todo: un artefacto que puede cambiar tras la verificación hace que el resultado de la prueba no se aplique a lo publicado. Los hashes permiten comprobarlo mecánicamente.

## Ejemplo

El SDK del programa prepara la versión 1.3.0:

```bash
python -m build                                   # una sola construcción
sha256sum dist/* > dist/SHA256SUMS                # hashes de los artefactos
python -m venv .venv-rc && . .venv-rc/bin/activate  # entorno limpio
pip install dist/engineering_sdk-1.3.0rc1-py3-none-any.whl
python -m pytest tests_consumidor/                # prueba desde el consumidor
```

Si una corrección de última hora cambia un archivo, el artefacto cambia, los hashes cambian y se publica `1.3.0rc2`; los resultados de `rc1` ya no se aplican. Si `rc2` pasa todas las verificaciones, se promueve exactamente `rc2` (con el mismo hash) a `1.3.0`. Dos fallos documentados que este procedimiento busca evitar: un cambio «interno» que rompe a un consumidor sin que ninguna prueba falle (la promesa no estaba escrita como prueba de contrato) y la comparación de API que marca un cambio que no importa (se compara solo la lista pública).

## Errores y confusiones comunes

- **Reconstruir tras probar.** El artefacto publicado no es el verificado.
- **«Corregir» un RC sin cambiar su identificador.** Nadie sabe qué RC se probó.
- **Omitir la guía de migración.** Los consumidores descubren la ruptura al actualizar.
- **Tratar el RC como etiqueta.** Es el artefacto lo que se verifica, no el nombre.

## Límites y cuándo no aplica

El proyecto acredita un RC dentro de su matriz, no disponibilidad, seguridad ni soporte productivo (`SE-120`). Un RC no sustituye la observación posterior a la publicación (monitoreo, reversión). Para bibliotecas de uso interno con un solo consumidor que se actualiza a la vez, el ritual completo puede ser excesivo; se justifica cuando hay consumidores externos que no controlas.
