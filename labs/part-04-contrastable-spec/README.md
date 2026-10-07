# Laboratorio de la Parte 04 — especificación y solución contrastable

Este laboratorio transforma el incidente de red de la Parte 03 en un modelo de
decisión pequeño, ejecutable y refutable. La especificación declara hipótesis,
pruebas, resultados esperados, autorización y presupuesto; las observaciones reducen
el conjunto de candidatos sin esconder contradicciones.

## Uso

Requiere Python 3.11 o posterior y solo biblioteca estándar.

```console
python labs/part-04-contrastable-spec/diagnostic_model.py labs/part-04-contrastable-spec/cases/incident-spec.json labs/part-04-contrastable-spec/cases/observations.json
python -m unittest discover -s labs/part-04-contrastable-spec/tests -v
```

El resultado `resolved` solo significa que queda una hipótesis dentro del modelo. No
prueba que el mundo real esté completo ni que las premisas sean verdaderas.

## Recorrido clase a clase

| Clase | Trabajo con el laboratorio | Evidencia |
|---|---|---|
| `SE-049` | separar decisión, hipótesis, pruebas y restricciones | árbol y supuestos |
| `SE-050` | construir la tabla de la implicación y un contraejemplo | `logic-check.md` |
| `SE-051` | representar dependencias como grafo con ciclos | consultas y recorrido |
| `SE-052` | comprobar autorización, presupuesto y subconjunto | contratos e invariantes |
| `SE-053` | explicar caso base, reducción y visitados | argumento estructural |
| `SE-054` | usar candidatos restantes como variante | corrección parcial y terminación |
| `SE-055` | comparar conteos lineales y por pares | teoría separada de benchmark |
| `SE-056` | adversar la selección codiciosa | límite y contraejemplo de heurística |
| `SE-057` | ejecutar transiciones legales e ilegales | máquina de estados |
| `SE-058` | conservar hipótesis, observación y descarte | registro trazable |
| `SE-059` | introducir requisitos contradictorios | preguntas abiertas y negociación |
| `SE-060` | empaquetar especificación, solución, oráculo y casos | suite de trece pruebas |

## Contrato de evaluación

La entrega incluye `problem.md`, la especificación JSON, casos normales, límite,
inválidos y contradictorios, y un argumento que distingue:

- corrección respecto del modelo;
- terminación del procedimiento;
- crecimiento de operaciones;
- calidad no garantizada de la heurística;
- supuestos aún no confirmados del dominio.

Cambiar un resultado esperado para que una implementación pase invalida la evidencia.
Un contraejemplo obliga a revisar la regla, el modelo o el alcance.

## Fuentes

- [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)
- [MIT Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- [MIT Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/)
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering)

Las fuentes sostienen los conceptos; las pruebas sostienen únicamente el contrato
ejecutable y los casos incluidos en este repositorio.
