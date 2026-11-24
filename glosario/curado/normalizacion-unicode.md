# Normalización Unicode

## Definición

La **normalización Unicode** transforma una cadena a una forma canónica para que secuencias equivalentes se comparen como iguales (SE-233, SE-177, SE-221, SE-441). Unicode permite representar un mismo carácter visible de más de una manera: «é» puede ser un único carácter precompuesto o una «e» seguida de un acento combinante. Las dos se ven igual y no son iguales byte a byte.

## Por qué importa

Sin normalizar, la misma palabra escrita por dos teclados o sistemas distintos es dos cadenas diferentes: la misma persona aparece duplicada, una búsqueda no encuentra lo que existe, una comparación de contraseñas o de identificadores falla de modo inconsistente. SE-233 lo cita como causa de que «la misma persona aparezca dos veces en el sistema»: nombres con acentos en formas Unicode distintas.

## Cómo funciona

Las formas canónicas más usadas, nombradas en SE-221 y SE-441, son **NFC** (compone: prefiere el carácter precompuesto) y **NFD** (descompone: carácter base más marcas combinantes). Existen además las formas de compatibilidad (NFKC y NFKD), que también unifican variantes como ligaduras o anchuras. Se normaliza ambos lados antes de comparar: dos cadenas equivalentes dan los mismos bytes tras normalizarse a la misma forma.

SE-233 aplica la idea a un formulario de entrega: los nombres se guardan **tal como se escriben** (lo que la persona escribió se respeta) y se comparan **normalizados y plegados** (normalización más plegado de mayúsculas). Y la longitud máxima se define en **grafemas** (lo que la persona percibe como un carácter) y se comprueba en bytes en el servidor, porque un grafema puede ocupar varios puntos de código y varios bytes. Separar lo que se guarda de lo que se compara evita perder información y a la vez evita duplicados.

## Ejemplo

El nombre «José» escrito desde un teclado que genera «é» precompuesto (U+00E9) y desde otro que genera «e» + U+0301 son visualmente idénticos. Comparados byte a byte, difieren; el sistema crea dos personas. Tras normalizar ambos a NFC, coinciden. En Python, `unicodedata.normalize("NFC", s)` hace esa conversión. (Ilustración con la biblioteca estándar; SE-233 describe el mismo principio.)

## Errores y confusiones comunes

- **La misma persona aparece dos veces**: nombres con acentos en formas distintas; corrección: normalizar y plegar para comparar, y guardar el nombre tal como se escribió.
- **Normalizar antes de guardar y perder lo escrito**: algunas formas de compatibilidad alteran el texto.
- **Medir la longitud en caracteres o bytes sin considerar grafemas.**
- **Confundir normalización con plegado de mayúsculas o con eliminación de acentos**: son operaciones distintas.

## Límites y cuándo no aplica

La normalización no resuelve la confusión visual entre caracteres distintos de aspecto parecido (una «a» latina y una «а» cirílica son caracteres diferentes y seguirán diferenciándose), lo que importa en seguridad. No es apropiada para datos binarios ni para identificadores que deben compararse byte a byte. La forma elegida debe ser la misma en todo el sistema, o la comparación sigue siendo inconsistente.
