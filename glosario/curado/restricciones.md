# Restricciones

## Definición

Una **restricción** es una decisión ya tomada o una condición externa que descarta alternativas sin discutirlas, con una fuente y un coste de levantarla (`SE-325`). `SE-147` la precisa: una condición impuesta fuera del equipo que limita el diseño y no se negocia como requisito. `SE-008` la sitúa dentro del alcance: una obligación legal, un límite físico, una fecha externa o una compatibilidad contractual.

## Por qué importa

Es lo primero que se aplica al decidir: reduce el espacio de alternativas antes de ponderar. Mal identificada, produce los dos errores opuestos: tratar una preferencia como restricción («tiene que ser serverless») o una restricción real como preferencia («ya veremos lo de los datos»). El resultado es arquitectura rehecha a mitad de proyecto o incumplimientos tardíos.

## Cómo funciona

`SE-325` da ejemplos: «se despliega en la infraestructura de la universidad», «los datos de estudiantes no salen del país», «el equipo domina Python». Se distinguen de los requisitos porque su tratamiento es distinto (`SE-147`): un requisito se prioriza y se negocia; una restricción se cumple, y su origen es una decisión externa que hay que registrar. La regla práctica de `SE-325`: anotar **quién** impuso la restricción, **desde cuándo** y **qué costaría levantarla**. Sin esa información es una opinión.

En el proceso de decisión, se aplican primero las restricciones y la dominancia (una alternativa peor en todo que otra), y se pondera solo lo que queda; ponderar sin descartar compara alternativas que una restricción ya excluía.

## Ejemplo

```text
R-03  Los datos de estudiantes no salen del país.
fuente: política de la universidad | desde: 2024-03 | costo de levantarla: aprobación del comité jurídico
efecto: descarta el proveedor X (única región fuera del país)
```

## Errores y confusiones comunes

- **Una restricción desaparece a mitad del proyecto.** Causa: era una preferencia sin dueño; corrección: registrar fuente, fecha y coste de levantarla (`SE-325`).
- **Se pondera sin descartar.** Causa: se comparan alternativas que una restricción ya excluía; corrección: aplicar primero restricciones y dominancia (`SE-325`).
- **Se discute como un requisito más.** Causa: no se identificó su origen externo; corrección: registrar origen, fecha y quién puede cambiarla (`SE-147`).

## Límites y cuándo no aplica

Una restricción no es eterna: su coste de levantarla puede ser aceptable si el beneficio es grande, y por eso hay que registrarlo. No toda limitación técnica es una restricción: la que se puede resolver con trabajo del equipo es un requisito de diseño. Y demasiadas restricciones sin revisar pueden dejar espacio de diseño vacío: entonces hay que renegociar alguna con su dueño.
