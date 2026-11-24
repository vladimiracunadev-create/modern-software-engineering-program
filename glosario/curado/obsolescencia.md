# Obsolescencia

## Definición

La **obsolescencia** se usa en el programa con dos significados relacionados:

- **Deprecación** (`SE-474`, *deprecation*): el aviso de que una funcionalidad se retirará, con alternativa y plazo.
- **Obsolescencia general** (`SE-009`): pérdida de utilidad de un software por cambios técnicos u organizativos.

El primero es una acción deliberada del mantenedor; el segundo es un estado que se acumula si nadie decide.

## Por qué importa

Una ruptura anunciada es una transición; una ruptura sorpresa es un incidente (`SE-474`). Planificar la obsolescencia evita acumular legado que nadie arregla y, a la vez, evita romper a quienes dependen del producto. `SE-009` observa que mantener todo indefinidamente tampoco es sostenible: aumenta costo, exposición y carga cognitiva.

## Cómo funciona

**Como política** (`SE-474`): una funcionalidad se marca como pendiente de retiro con:

- un **aviso visible en tiempo de ejecución**;
- una **versión en la que se avisa** y otra **en la que se retira**;
- la **alternativa recomendada**;
- una **ventana mínima** publicada (por ejemplo, al menos dos versiones menores o seis meses antes de retirar).

Además hay que decidir cuánto tiempo se mantienen las versiones antiguas con correcciones de seguridad: sin fecha de fin de soporte, el ecosistema acumula versiones que nadie arregla.

**Como proceso** (`SE-009`): la sostenibilidad técnica considera que el software pueda entenderse, adaptarse y retirarse. Dependencias sin mantenimiento, formatos cerrados y conocimiento concentrado crean obsolescencia. Las políticas de versión, migración y retiro equilibran continuidad con reducción de legado.

## Ejemplo

Ilustración en Python de un aviso de deprecación visible:

```python
import warnings
def f_vieja():
    warnings.warn("f_vieja se retira en 3.0; use f_nueva", DeprecationWarning, stacklevel=2)
```

Acompañada de una guía de migración y una entrada en el registro de cambios con formato fijo.

## Errores y confusiones comunes

- **Los clientes no se enteran de una ruptura.** Causa: registro de cambios genérico o sin aviso previo; corrección: formato fijo, guía de migración y obsolescencia anunciada (`SE-474`).
- **Retirar sin alternativa.** El aviso sin camino de migración transfiere el problema.
- **Confundir obsolescencia con edad.** Un componente antiguo y estable no es obsoleto; uno sin mantenimiento sí puede serlo.

## Límites y cuándo no aplica

Una ventana de «dos versiones o seis meses» es un ejemplo de política razonable, no una norma universal. En software interno con pocos consumidores, un aviso corto y una conversación bastan. Y la deprecación no sustituye al versionado semántico: cuando se retira, el cambio incompatible sigue requiriendo señalarse en la versión.
