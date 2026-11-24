# Versionado

## Definición

**Versionado** es la práctica de identificar y ordenar las versiones de un artefacto (un contrato, una API, un paquete, una página de documentación) para comunicar el alcance del cambio y gestionar la coexistencia entre versiones. El programa lo enseña en varios contextos: contratos de datos (SE-366), portales de documentación (SE-216) y paquetes con dependencias (SE-225). El hilo común: cada versión debe ser coherente consigo misma y declarar qué pasa con los enlaces y la compatibilidad entre versiones.

## Por qué importa

Comunica el alcance del cambio. Un número o una etiqueta de versión es una promesa para quien consume: si el cambio es compatible, puede actualizar con confianza; si no lo es, debe revisar. Un versionado mal hecho produce roturas inesperadas, y uno que ordena mal las versiones puede instalar una anterior (SE-225).

## Cómo funciona

El mecanismo tiene tres piezas. Primero, la **identidad**: cada versión tiene un identificador estable (una etiqueta, un número). Segundo, el **orden**: las versiones se pueden comparar. Aquí aparece un error típico que SE-225 señala: ordenar versiones como cadenas de texto pone «1.10» antes de «1.9»; hay que compararlas por componentes numéricos. Tercero, la **semántica**: qué comunica el cambio de número. El versionado semántico, por ejemplo, reserva el cambio de la versión mayor para los cambios incompatibles, el de la menor para añadidos compatibles y el del parche para correcciones.

En un contrato de datos (SE-366), la versión acompaña a cinco declaraciones: el esquema, la semántica de cada campo, la calidad ofrecida, el nivel de servicio y la gobernanza (dueño, canal de contacto, política de cambios y retención). El contrato es un archivo versionado junto al código del productor, no una página de una wiki, y su verificación se ejecuta en cada cambio.

En un portal documental (SE-216), el versionado se hace desde etiquetas del repositorio: cada versión de la documentación es coherente consigo misma (sus enlaces internos apuntan a su propia versión) y declara qué pasa con los enlaces entre versiones (redirecciones o avisos de retirada). La clase añade una política de retirada y propone trasladar la estructura a otro dominio para comprobar qué parte depende de la plataforma y qué parte es reutilizable.

## Ejemplo

El contrato de la API de entregas lleva la versión `2.3.0`. Un cambio que añade un campo opcional sube a `2.4.0`; uno que renombra un campo o elimina uno sube a `3.0.0` con aviso de retirada. Para decidir cuál de dos versiones es más reciente, se comparan sus componentes como números: `2.10.0` es posterior a `2.9.0`, aunque como texto sea anterior. (Ilustración de las reglas descritas.)

## Errores y confusiones comunes

- **Ordenar versiones como texto**: instala una anterior (SE-225).
- **Versiones incoherentes**: enlaces internos que apuntan a otra versión.
- **Cambios incompatibles bajo un número menor**: rompen a los consumidores.
- **Contratos en una wiki en vez de en el repositorio**, sin verificación.

## Límites y cuándo no aplica

El versionado comunica intención, no la garantiza: un número no impide que un cambio «compatible» rompa a un cliente estricto. Para artefactos que nadie más consume, un esquema formal es excesivo. Mantener muchas versiones vivas tiene un costo; la política de retirada es parte del versionado, no un añadido.
