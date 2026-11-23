# ADR

## Definición

Un **ADR** (*Architecture Decision Record*, registro de decisión arquitectónica) es un documento breve que registra una decisión con su contexto, sus alternativas, la decisión tomada, sus consecuencias y su estado. Es la definición que comparten `SE-208`, `SE-324`, `SE-333` y `SE-348`; `SE-208` añade el **estado** (vigente, sustituida) como parte del registro.

## Por qué importa

Una decisión de arquitectura se toma una vez y se sufre durante años; si no se registra, quien llega después ve el efecto sin la razón y la discute o la deshace sin saber qué se descartó. El ADR conserva el *porqué*: el contexto que había y las alternativas que se descartaron. Convierte «así se hizo» en una decisión que se puede revisar cuando cambian las suposiciones.

## Cómo funciona

Un ADR útil tiene los componentes de la definición, y su valor depende de que cada uno sea real (`SE-208`):

1. **Contexto:** qué fuerzas empujaban.
2. **Alternativas:** al menos dos, cada una con una razón de descarte.
3. **Decisión:** lo que se eligió.
4. **Consecuencias:** lo que se gana y lo que se paga.
5. **Estado y suposiciones:** si está vigente o fue sustituida, qué suposiciones sostiene y cuándo se revisa.

El registro se trata como un conjunto: los ADR forman un grafo en que una decisión sustituye a otra. `SE-208` pide comprobar ese grafo y exigir que el ADR sustituido cambie su estado a «sustituida»; cuando las suposiciones dejan de cumplirse, se abre un RFC de sustitución en vez de editar el original, de modo que la historia se conserva.

## Ejemplo

`SE-208` plantea tres casos límite para decidir cuándo basta un ADR: la decisión pequeña y reversible que solo tiene ADR, la decisión que afecta a otros equipos y exige además un RFC, y el ADR cuyas suposiciones ya no se cumplen, que da lugar a un RFC de sustitución. El criterio práctico que propone para no saturar el registro es limitar los ADR a decisiones difíciles de revertir o con impacto externo.

## Errores y confusiones comunes

- **Plantilla completa y sin alternativas reales.** Se llenaron las secciones sin considerar opciones; corrección: exigir al menos dos alternativas con una razón de descarte cada una (`SE-208`).
- **Decisión que parece vigente con suposiciones vencidas.** No se enumeraron suposiciones ni se fijó revisión; corrección: añadir suposiciones y fecha de revisión, y listar los ADR vencidos.
- **Dos ADR contradictorios vigentes.** El estado no se actualizó al sustituir; corrección: comprobar el grafo.
- **Nadie lee el registro.** Tiene demasiadas entradas triviales; corrección: limitarlo a decisiones difíciles de revertir o con impacto externo.

## Límites y cuándo no aplica

Un ADR registra una decisión; no la justifica por sí solo ni garantiza que fuera acertada. No sustituye a un RFC cuando la decisión afecta a otros equipos y necesita discusión previa (`SE-208`), y su valor se pierde si no se mantiene como un conjunto con estado y revisión. Y es una práctica de documentación, no una herramienta concreta: el formato exacto lo decide el equipo.
