# Throughput

## Definición

El **throughput** (rendimiento, caudal) es la cantidad de trabajo completado por unidad de tiempo: peticiones atendidas por segundo (`SE-281`), unidades completadas por tiempo (`SE-022`) o, en redes, la cantidad *útil* transferida por unidad de tiempo (`SE-046`). Es distinto de la **latencia** (cuánto tarda una unidad) y de la **utilización** (cuánto ocupa un recurso).

## Por qué importa

Es la medida de cuánta carga soporta un sistema, pero se optimiza a costa de otras: `SE-022` advierte que mejorar una de las tres medidas puede empeorar otra. Quien solo persigue throughput puede degradar la latencia que sienten las personas. Cambia lo que se declara como objetivo: una capacidad y una latencia máxima, no un número aislado.

## Cómo funciona

`SE-022` fija el vocabulario: latencia mide cuánto tarda una unidad; throughput, cuántas se completan por tiempo; utilización, cuánto ocupa un recurso. La carga incluye tamaño, distribución, concurrencia, estado y criterio de corrección.

`SE-281` muestra la causa de un compromiso clásico: una llamada a un cálculo tiene un costo fijo (lanzar, sincronizar, mover datos) y otro variable por elemento. Agrupar peticiones en un lote reparte el costo fijo y sube el throughput, pero cada petición espera a que el lote se llene y termine. En la CPU del laboratorio, una capa densa de 1024×1024 en 32 bits dio, por lote: lote 1, 0,27 ms y unas 3 700 peticiones por segundo; lote 16, 4,8 ms y 3 300; lote 64, 7,9 ms y 8 100; lote 256, 14,3 ms y 17 900. El throughput sube casi cinco veces mientras la latencia por lote se multiplica por más de cincuenta.

En redes (`SE-046`), el throughput es lo que realmente llega útil al destino, no el ancho de banda teórico del enlace.

## Ejemplo

```text
demanda: 200 peticiones/s ; lote 256 -> llenar el lote tarda > 1 s
=> el throughput del lote grande no se materializa y la latencia crece
```

Ilustración de cálculo: throughput = n / tiempo = 256 / 0,0143 s ≈ 17 900 peticiones/s en el experimento de lote 256.

## Errores y confusiones comunes

- **Confundirlo con ancho de banda teórico.** El throughput es lo útil y efectivamente transferido (`SE-046`).
- **Maximizar throughput sin mirar latencia.** El lote óptimo es el que cabe en el tiempo de espera que el objetivo de latencia permite (`SE-281`).
- **Comparar throughput de versiones que dan resultados distintos.** No es un benchmark válido (`SE-022`).

## Límites y cuándo no aplica

Con baja demanda el throughput alcanzable es irrelevante: manda la latencia. Las cifras de `SE-281` son de una CPU y una capa concretas. Y el throughput máximo medido en un banco no se sostiene en producción si hay contención, colas o dependencias (véase *utilización* y *ley de Little*).
