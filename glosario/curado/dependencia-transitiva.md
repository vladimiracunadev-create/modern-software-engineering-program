# Dependencia transitiva

## Definición

Una **dependencia transitiva** es un paquete o componente que un proyecto usa indirectamente, a través de otra dependencia (`SE-201`, `SE-032`). `SE-471` la formula como la pieza que otra dependencia necesita, directa o indirectamente. Si el proyecto declara `A` y `A` necesita `B`, entonces `B` es transitiva respecto del proyecto, aunque nadie la haya elegido.

## Por qué importa

Un proyecto usa unas decenas de paquetes directos que arrastran cientos (`SE-201`). Lo que no se declara también se ejecuta, se licencia y se ataca. Por eso las decisiones de licencias, vulnerabilidades y reproducibilidad no pueden basarse solo en lo que el equipo escribió en su manifiesto: mirar solo las directas deja fuera casi todo.

## Cómo funciona

El gestor de paquetes resuelve el **grafo completo**: cada paquete declara rangos de versiones de sus dependencias y el resolvedor elige un conjunto compatible. Consecuencias que enseña el programa:

- **Licencias** (`SE-201`): las obligaciones se acumulan. El inventario debe recorrer el grafo entero y registrar tres estados distintos: licencia reconocida y permitida, reconocida y no permitida, y no declarada o ilegible. Este último exige revisión; no es una aprobación.
- **Cadena de suministro** (`SE-471`): una pieza comprometida o abandonada a cuatro niveles afecta igual que una directa, y el inventario de componentes (SBOM) existe para verlas.
- **Reproducibilidad** (`SE-032`): sin un archivo de bloqueo (`lockfile`), la resolución puede elegir otras versiones transitivas mañana.

## Ejemplo

`SE-201` analiza expresiones de licencia con sus operadores. Ilustración con npm:

```bash
npm ls --all        # muestra el árbol completo, directas y transitivas
npm ls left-pad     # ¿quién arrastra este paquete?
```

El equipo descubre que `left-pad` entra por un paquete de formato que usa una dependencia de segundo nivel.

## Errores y confusiones comunes

- **Rechazar dependencias válidas.** Causa: comparación literal de texto de la licencia; corrección: analizar la expresión con sus operadores (`SE-201`).
- **Aprobar lo que no se entendió.** Causa: los avisos no se tratan como pendientes; corrección: que lo no reconocido exija revisión (`SE-201`).
- **Fijar solo las directas.** Las versiones transitivas siguen moviéndose sin lockfile.

## Límites y cuándo no aplica

Las definiciones de `SE-201` son operativas para la plataforma de entregas: no se interpretó ninguna licencia ni se auditó ningún proyecto, y las decisiones con consecuencia jurídica requieren asesoría. Un grafo completo muestra qué está, no si es seguro. Y en proyectos con dependencias copiadas al repositorio (vendoring) la distinción directa/transitiva se difumina.
