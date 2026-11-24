# Hallazgo

## Definición

Un **hallazgo** es la observación de un incumplimiento con su criterio, lugar, reproducción, afectados, gravedad y evidencia (`SE-179`). Otros usos en el programa: la coincidencia de una regla del verificador con un patrón de riesgo (`SE-491`) y la relación estructurada entre evidencia, interpretación y siguiente prueba (`SE-036`). Lo común es que un hallazgo es un registro accionable, no una impresión.

## Por qué importa

Una auditoría sin hallazgos bien formados no se puede reparar ni comprobar. `SE-179` lo dice con claridad: «mejorar accesibilidad» es un hallazgo vago. Con campos completos, el equipo puede priorizar, asignar y verificar el cierre. Además, decide la lectura de cero hallazgos: no significa «cumple», significa «las reglas no encontraron nada».

## Cómo funciona

Un hallazgo (`SE-179`) registra:

- el **criterio** incumplido;
- **dónde** ocurre y **cómo se reproduce**;
- **a quién afecta**;
- su **gravedad**, en una escala fija y escrita;
- la **evidencia** (captura, fragmento, descripción).

La gravedad no es solo técnica: un bloqueo total del proceso para quien usa teclado es más grave que un título genérico, aunque ambos sean fallos de criterio. Los hallazgos viven en un registro con criterio, gravedad, afectados estimados y esfuerzo; el orden de reparación se discute con la tabla de valor por hora y la lista de bloqueos totales. Cada reparación incluye la prueba que fallaba antes y pasa después, y una revisión con una persona que use tecnologías de apoyo cierra los hallazgos graves.

## Ejemplo

```text
H-014 | criterio: operable por teclado | lugar: paso 3, enviar entrega
reproducción: Tab no alcanza "Enviar" | afectados: usuarios de teclado
gravedad: bloqueo total | evidencia: captura + secuencia de teclas
```

En `SE-491`, un hallazgo de un verificador de workflows puede ser texto de terceros insertado en un script, o código de terceros descargado y ejecutado.

## Errores y confusiones comunes

- **Declarar accesible un flujo con cero hallazgos.** Causa: se confundió «las reglas no encuentran nada» con accesibilidad; corrección: declarar alcance, revisión humana y lo no comprobado (`SE-179`).
- **Arreglar los baratos y dejar esperar los bloqueos.** Causa: orden por facilidad; corrección: comparar órdenes con personas bloqueadas y esfuerzo (`SE-179`).
- **Verificador en cero y hay un incidente.** Causa: se confió en la ausencia de hallazgos; corrección: lista de lo que no ve y revisión humana (`SE-491`).

## Límites y cuándo no aplica

Un hallazgo es tan bueno como su alcance: lo que la auditoría no cubrió no genera hallazgos. Las escalas de gravedad son convenciones del equipo, no medidas objetivas. Y los hallazgos automáticos pueden ser falsos positivos: requieren comprobación antes de convertirse en trabajo.
