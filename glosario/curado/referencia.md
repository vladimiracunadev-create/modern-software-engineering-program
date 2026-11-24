# Referencia

## Definición

**Referencia** tiene tres sentidos en el programa. El principal (SE-206, documentación) es una descripción completa y neutral de los elementos de un producto, estructurada como el producto. SE-193 (Git) la usa para un nombre (rama, etiqueta, HEAD) que apunta a un commit o a otra referencia. SE-608 (monitoreo de modelos) la usa para la distribución con la que se compara, normalmente la de entrenamiento o la de un periodo sano. Esta entrada desarrolla los dos primeros, que son los más usados, y señala el tercero.

## Por qué importa

En documentación, distingue lo que se **consulta** de lo que se lee: la referencia describe la máquina con completitud y sin opinión. En Git, la distinción entre «existe» y «es alcanzable» es la base de toda la recuperación (SE-194): un objeto está a salvo mientras alguna referencia lo alcance.

## Cómo funciona

**Referencia documental (SE-206).** Describe la máquina: los parámetros, sus tipos, sus valores por defecto, los errores que puede devolver. Se consulta de forma puntual y por eso importa más que sea completa, uniforme y exacta que agradable. Su estructura imita la del producto, no la de las tareas. Es el único tipo de documentación cuya exactitud puede comprobarse casi por completo con herramientas, porque sus afirmaciones tienen una contraparte en el código: nombres, firmas, límites; por eso se genera de la configuración o del código. Una referencia con opiniones («recomendamos un tope del 50 %») mezcla tipos: la opinión va a una guía o a una explicación.

**Referencia de Git (SE-193).** Una rama, una etiqueta y HEAD son archivos pequeños con un identificador (o con el nombre de otra referencia). Mover una rama no borra objetos: solo cambia a qué commit se llega desde ese nombre. Un objeto queda a salvo mientras sea alcanzable desde alguna referencia o desde el registro de movimientos (reflog); si deja de serlo, es candidato a la poda.

**Referencia de comparación (SE-608).** En monitoreo, la distribución de referencia (entrenamiento o un periodo sano) es contra la que se mide la deriva de los datos actuales.

## Ejemplo

La plataforma de entregas separa la penalización en cuatro páginas (SE-206): tutorial, guía, explicación y una referencia, «Parámetros de penalización», que se genera de la configuración y lista cada parámetro con su tipo, valor por defecto y límites. En Git (SE-193), tras `git reset --hard HEAD~1`, el commit descartado deja de ser alcanzable desde la rama, pero sigue existiendo en el reflog durante un tiempo, y con `git reflog` se localiza y se recupera con una nueva rama. (El segundo caso es un ejemplo estándar de Git.)

## Errores y confusiones comunes

- **Opinión en la referencia**: se mezcla descripción con recomendación.
- **Referencia escrita a mano que diverge del código.**
- **Creer que mover una rama borra commits**: solo cambia el puntero.
- **Confundir los tres sentidos**: la referencia documental, la de Git y la de comparación no tienen relación técnica.

## Límites y cuándo no aplica

La referencia documental no sirve para aprender (necesita tutorial) ni para decidir (necesita explicación). Las referencias de Git no impiden la pérdida: un objeto no alcanzable se poda con el tiempo, y el reflog es local, de modo que no protege a otras personas ni a clones. Y una distribución de referencia de ML se vuelve obsoleta si el mundo cambia.
