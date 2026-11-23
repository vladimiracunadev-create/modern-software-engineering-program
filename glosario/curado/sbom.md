# SBOM

## Definición

Un **SBOM** (*software bill of materials*, lista de materiales de software) es una lista estructurada de los componentes de un artefacto, con identificador, versión y huella. Es la definición de `SE-472`, que trabaja con un esquema simplificado inspirado en CycloneDX.

## Por qué importa

Responde «¿qué hay dentro de este artefacto?» sin abrirlo y permite saber si una vulnerabilidad en un componente afecta a un artefacto publicado. Es una pieza de la cadena de suministro: junto con la procedencia, dice qué se entregó y cómo se construyó.

## Cómo funciona

Cada componente se identifica con un identificador y una versión (`SE-472` recomienda usar *purl*) y con una huella. El SBOM debe cumplir los elementos mínimos (autor, fecha, identificadores) para ser utilizable. Lo que lo hace confiable es su vínculo con el artefacto real: se identifica el sujeto por la huella del artefacto, y se genera desde el bloqueo de dependencias y se contrasta escaneando el artefacto final, no desde el manifiesto.

## Ejemplo

`SE-472` trabaja con 100 proyectos sintéticos cuyos componentes se reparten, por supuesto del autor, en 62 % declarados, 24 % transitivos, 7 % copiados, 4 % enlazados y 3 % descargados en ejecución. Las categorías copiada, enlazada y descargada no aparecen en un manifiesto, por lo que un SBOM generado solo desde el manifiesto queda incompleto.

## Errores y confusiones comunes

- **El SBOM no contiene una pieza que está en el artefacto.** Se generó desde el manifiesto; hay que generarlo desde el bloqueo y escanear el artefacto final.
- **Un SBOM válido describe otro artefacto.** Falta el vínculo por huella.
- **Un SBOM bien formado con un componente falso.** Solo se validó la forma; hay que comparar con el contenido real.
- **Nadie puede usarlo.** Faltan autor, fecha o identificadores; cumplir los elementos mínimos y usar purl.

## Límites y cuándo no aplica

`SE-472` declara que su SBOM sigue un esquema simplificado inspirado en CycloneDX y que las procedencias son documentos propios con campos cercanos a SLSA e in-toto, no los formatos completos; los 100 proyectos y su composición son supuestos del autor, y no se usó ninguna herramienta generadora de SBOM ni base de vulnerabilidades. Un SBOM describe composición, no seguridad: no dice si un componente es vulnerable ni si fue construido con garantías.
