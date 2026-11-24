# Plataforma

## Definición

Una **plataforma** combina capacidades, políticas, interfaces y operación para que otros construyan (`SE-109`). No es solo un conjunto de librerías ni una marca. En el contexto de ejecución, `SE-025` la define como la combinación relevante de hardware, sistema, versión, políticas y capacidades, no solo un nombre comercial. Son dos sentidos: plataforma como **producto interno o externo** para construir encima, y plataforma como **entorno de ejecución**.

## Por qué importa

Llamar «plataforma» a un conjunto de librerías sin responsables crea una expectativa que nadie cumple. Y tratar «Linux» como una plataforma uniforme esconde diferencias de kernel, distribución y espacio de usuario que cambian el comportamiento. Cambia qué se promete a quien construye encima y qué se prueba en cada entorno.

## Cómo funciona

**Como producto** (`SE-109`): propiedad (*ownership*), SLO, autenticación, cuotas y soporte forman parte de su producto, junto con las capacidades. Una plataforma tiene una política de cambios y un responsable de operarla. Si no ofrece eso, es una biblioteca.

**Como entorno** (`SE-025`): se registran kernel, distribución, versión y herramientas relevantes por separado. `SE-109` mide que las diferencias entre plataformas importan: un intérprete limpio parte con 25 módulos en Windows y 23 en Linux, y el costo de importar `asyncio` es 9,0 veces el de `json` en Windows y 4,9 en Linux; por eso se comparan razones y no milisegundos.

## Ejemplo

Una «plataforma interna de datos» que ofrece pipelines, un catálogo, cuotas por equipo y un canal de soporte con SLO. Si en cambio publica solo un paquete de utilidades sin responsable ni SLO, es una biblioteca, y llamarla plataforma lleva a equipos a depender de algo sin garantías. Ilustración de ficha mínima:

```yaml
plataforma: datos
responsable: equipo-datos
slo: { disponibilidad: 99.5%, soporte: laborable }
cuotas: { consultas_por_equipo: 10000/día }
cambios: aviso de 2 versiones menores
```

## Errores y confusiones comunes

- **Se anuncia «plataforma» sin responsable ni SLO.** Causa: se confundió conjunto de librerías con plataforma; corrección: escribir propiedad, soporte, cuotas y política de cambios, o llamarlo biblioteca (`SE-109`).
- **«Linux» como plataforma uniforme.** Causa: se confundió kernel con distribución y espacio de usuario; corrección: registrar cada capa por separado (`SE-025`).
- **Comparar milisegundos entre plataformas.** Los tiempos absolutos varían; las razones son más estables (`SE-109`).

## Límites y cuándo no aplica

Las cifras de `SE-109` son de un intérprete concreto en dos sistemas y no se trasladan a otros sin medir. No toda organización necesita una plataforma interna: el costo de mantenerla (soporte, SLO) solo se justifica si hay varios equipos consumidores. Y el sentido de entorno no equivale al de producto: una plataforma de ejecución no promete soporte a nadie.
