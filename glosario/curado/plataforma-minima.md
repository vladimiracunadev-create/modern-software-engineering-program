# Plataforma mínima

## Definición

Una **plataforma mínima** es el conjunto acotado de capacidades que una plataforma ofrece y puede sostener con evidencia comprobable (`SE-408`). No es una plataforma pequeña: es la que ofrece solo lo que puede respaldar.

## Por qué importa

Una plataforma interna se mide por lo que los equipos pueden usar con confianza, no por lo que anuncia. Un catálogo largo y declarativo, con capacidades que nadie ha verificado, genera confianza falsa y deuda. La decisión que cambia es el criterio de ampliación: una capacidad solo se añade cuando existe el artefacto que la demuestra y alguien que lo revisó.

## Cómo funciona

`SE-408` ilustra con la plataforma de entregas, que ofrece cuatro capacidades, cada una atada a las clases que la construyen:

1. Un **entorno aislado y con identidad mínima**.
2. Su **descripción declarativa**, con estado y política de cambios.
3. Un **camino de creación con verificador**.
4. Un **ciclo de vida** con presupuesto, caducidad y prueba de destrucción.

Cada capacidad nombra el artefacto que la respalda y quién lo revisó. La regla es lo que no está respaldado no se ofrece: es mejor un catálogo corto y comprobable que uno largo y declarativo.

La causa de la regla es la confianza. Quien consume la plataforma toma decisiones basándose en lo que esta dice ofrecer; cada capacidad sin evidencia es una promesa que puede incumplirse en el peor momento. La evidencia tiene fecha: la clase advierte que un validador que solo comprueba la forma puede aprobar un paquete con evidencia vieja, por lo que añade revisión por otra persona y una fecha máxima de antigüedad. Y la evidencia debe ser reproducible: si la suma de verificación de un artefacto cambia entre máquinas, hay marcas de tiempo, orden o campos del sistema en el archivo; se normalizan y se compara en dos sistemas.

## Ejemplo

El equipo quiere anunciar «backups automáticos» como capacidad. No hay prueba de restauración reciente. Según el criterio de la clase, la capacidad no se ofrece hasta tener el artefacto (una restauración probada, con fecha y revisor). Mientras tanto el catálogo muestra cuatro capacidades respaldadas, no cinco con una sin respaldo. Aplicación del criterio de `SE-408`.

## Errores y confusiones comunes

- **La suma cambia entre máquinas**: marcas de tiempo, orden o campos del sistema en el archivo; se normaliza y se compara en dos sistemas.
- **El validador aprueba un paquete con evidencia vieja**: solo comprueba la forma; se corrige con revisión por otra persona y fecha máxima de antigüedad.
- **Confundir mínima con pobre**: mínima es lo sostenible, no lo escaso.
- **Declarar capacidades sin artefacto**.

## Límites y cuándo no aplica

El criterio no dice cuántas capacidades debe tener una plataforma: eso depende de la organización. Una plataforma mínima puede no cubrir necesidades legítimas, que los equipos resolverán por su cuenta con el costo que eso implica; la clase prefiere eso a prometer lo que no puede sostenerse. Y la evidencia es de un momento: requiere renovarse, o la capacidad vuelve a quedar sin respaldo.
