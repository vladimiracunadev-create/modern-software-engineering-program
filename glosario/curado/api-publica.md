# API pública

## Definición

La **API pública** es, según `SE-110`, el conjunto de nombres, tipos, errores, efectos, orden, formato y comportamiento documentado de los que los consumidores pueden depender. `SE-474` la formula como el conjunto de interfaces y comportamientos que un proyecto promete mantener. Lo decisivo es la palabra *promete*: la API pública no es todo lo que es visible, sino lo que el proyecto declara estable. No se limita a funciones exportadas: una CLI, un formato de archivo, una variable de entorno o un mensaje que otros programas analizan también son contrato si se presentan como estables.

## Por qué importa

Todo el versionado y la compatibilidad se apoyan en esta frontera. Sin ella, el número de versión no comunica nada: `SE-110` señala que una versión puede ser válida y aun así inútil si el autor no define qué es su API pública. La decisión profesional que cambia es qué se puede modificar sin avisar. Lo privado se refactoriza libremente; lo público exige deprecación, migración y un cambio de versión mayor si se rompe. Declarar el límite protege a ambas partes: el autor conserva libertad interna y el consumidor sabe dónde puede apoyarse.

## Cómo funciona

La API pública se construye de tres piezas:

- **Declaración explícita.** Una lista de lo exportado (por ejemplo `__all__` en Python), una convención de nombres (prefijo `_` para lo interno) y documentación que diga qué se promete. `SE-120` recomienda comparar solo esa lista, para que el comparador de API no marque cambios en lo que nadie prometió.
- **Superficie amplia.** Además de firmas, entran errores (qué excepción y cuándo), efectos (qué escribe o envía), orden (si un listado viene ordenado solo si está especificado) y formatos de salida.
- **Verificación.** Un comparador de firmas entre versiones y pruebas de contrato escritas desde el consumidor detectan cambios incompatibles antes de publicar.

La causa de que el límite funcione es la ley de Hyrum, enunciada ampliamente en la práctica: con suficientes usuarios, alguien depende de cualquier comportamiento observable. Por eso lo que no se declara debe, además, no prometerse por escrito: «el comportamiento no documentado no se promete» (`SE-474`).

## Ejemplo

En `SE-474`, el equipo define la API pública de la API de entregas: los puntos finales documentados, sus parámetros, los campos de respuesta, los códigos de error y el orden de los listados cuando está especificado. Cada solicitud de integración corre el comparador de firmas y las pruebas de contrato, y quien revisa elige el nivel de versión; si hay discrepancia, gana el mayor. Una funcionalidad deprecada emite un aviso en ejecución desde que se marca hasta que se retira, con un mínimo de dos versiones menores y seis meses. Si un cliente dependía del orden de un listado que nunca se especificó, el cambio de orden no es un cambio de API pública; el programa lo trata como riesgo comunicado, no como ruptura.

## Errores y confusiones comunes

- **Creer que público es lo no privado en el lenguaje.** Que un símbolo sea importable no lo vuelve promesa.
- **Reducirla a firmas de funciones.** Errores, efectos, formato de salida y CLI también cuentan (`SE-110`).
- **No definirla y versionar igual.** El número de versión queda sin significado y los consumidores no saben qué esperar.
- **Prometer sin querer.** Un ejemplo de documentación que muestra un detalle interno lo convierte en dependencia de hecho.

## Límites y cuándo no aplica

Declarar la API no impide que alguien dependa de lo no declarado; solo traslada la responsabilidad. En código de un solo equipo con un único consumidor, formalizarla puede costar más que coordinar el cambio. Y para sistemas con vigencia de pocas semanas, la disciplina de versionado semántico puede no compensar. La API pública se mide contra consumidores reales: sin una prueba desde el consumidor, la lista declarada es una intención.
