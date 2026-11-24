# Minimización

## Definición

La **minimización** (de datos) es el principio de recoger y conservar solo los datos necesarios para una finalidad declarada (`SE-358`). `SE-137` lo aplica a la analítica de producto: recoger solo los datos, el tiempo y la granularidad que una decisión necesita. Depende de una **finalidad** escrita: sin ella no se puede decir qué es «necesario».

## Por qué importa

El dato que no se recoge no se puede filtrar, no hay que protegerlo, borrarlo ni responder por él (`SE-358`). Reduce superficie de ataque, costo de cumplimiento y riesgo de uso indebido. Cambia una decisión de diseño de esquema: cada campo nuevo debe llegar con su razón.

## Cómo funciona

`SE-358` parte de un **inventario** de datos personales: qué datos hay, para qué se recogen (finalidad), quién accede, cuánto tiempo se conservan y dónde viven: base, índices, cachés, respaldos, registros, exportaciones. Sobre ese inventario se pregunta si hace falta cada dato. La minimización opera en varias dimensiones:

- **qué** se recoge (¿fecha de nacimiento completa o un rango de edad?);
- **cuánto tiempo** se conserva (retención);
- **con qué granularidad** (agregado en lugar de evento individual, `SE-137`);
- **dónde** se copia (cada copia es otro lugar que proteger).

El inventario es un artefacto vivo: se actualiza cada vez que cambia el esquema. En la plataforma de entregas, el correo es necesario para el acceso; la fecha de nacimiento completa quizá no, y un rango de edad podría bastar.

## Ejemplo

Antes: `usuarios(id, correo, fecha_nacimiento, direccion, telefono)`. Tras preguntar por la finalidad de cada campo, queda `usuarios(id, correo, rango_edad)` porque dirección y teléfono no tienen finalidad. Ilustración de un registro de finalidad:

```yaml
correo: { finalidad: acceso, retencion_dias: 365, acceso: [auth] }
rango_edad: { finalidad: segmentar avisos, retencion_dias: 180, acceso: [producto] }
```

## Errores y confusiones comunes

- **Recoger «por si acaso».** Sin finalidad no hay forma de justificar el dato; el costo de guardarlo existe aunque no se use.
- **Minimizar la tabla y olvidar las copias.** Cachés, respaldos, registros y exportaciones conservan el dato (`SE-358`).
- **Confundir minimización con anonimización.** Minimizar es recoger menos; anonimizar es transformar lo recogido.

## Límites y cuándo no aplica

La minimización exige una finalidad concreta, y algunas obligaciones legales exigen conservar más de lo que el producto necesita; esas decisiones requieren asesoría. No es una regla «menos es siempre mejor»: recoger lo necesario para detectar abuso o auditar puede ser una finalidad legítima. Y reducir la granularidad puede impedir análisis posteriores: hay que decidirlo conscientemente.
