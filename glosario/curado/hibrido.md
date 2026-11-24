# Híbrido

## Definición

«Híbrido» tiene en el programa dos sentidos que conviene no mezclar. El principal, de `SE-285` (criptografía poscuántica y migración), es la **combinación de un algoritmo clásico y uno poscuántico en una misma clave de sesión**. El segundo, de `SE-589` (workflows frente a agentes), es una **arquitectura donde un enrutador manda cada solicitud al workflow o al agente que le corresponde**. (En `SE-255` aparece además «híbrido en contenedor», una web dentro de una aplicación; ese es otro asunto, tratado en el enfoque de construcción.)

## Por qué importa

En criptografía, el híbrido protege si cualquiera de los dos resiste: si el algoritmo poscuántico resulta tener un defecto, el clásico sigue protegiendo, y si un computador cuántico rompe el clásico, el poscuántico sigue protegiendo. En agentes, permite pagar el agente solo donde aporta, y usar un workflow determinista para el resto.

## Cómo funciona

**Criptográfico (`SE-285`).** El saludo de TLS intercambia, entre otras cosas, una clave pública del cliente y un texto cifrado o clave pública del servidor. El tamaño importa:

- X25519: unos 64 bytes; cabe en un segmento de red.
- ML-KEM-768 solo: 1 184 + 1 088 = 2 272 bytes; dos segmentos de 1 460 bytes.
- Híbrido (X25519 más ML-KEM-768): 2 336 bytes; también dos.

Dos segmentos en lugar de uno aumentan la probabilidad de fragmentación y de pérdida y, en redes con dispositivos intermedios que esperan el primer mensaje en un paquete, causan errores reales de conexión. El RFC 10024 define tres mecanismos híbridos para TLS 1.3 (X25519MLKEM768, SecP256r1MLKEM768 y SecP384r1MLKEM1024).

**De arquitectura (`SE-589`).** Un enrutador clasifica cada solicitud y la manda al flujo fijo (workflow) cuando el camino es conocido, o al agente cuando exige decidir.

## Ejemplo

El equipo de *Avisos* en `SE-285` hace un inventario y encuentra 31 usos de criptografía de clave pública (TLS entre cliente y servicio y entre servicios, firmas de artefactos, tokens de sesión, certificados de dispositivos, cifrado de copias con clave pública…), y los prioriza para migrar. Ilustración de `SE-589`: solicitudes frecuentes y predecibles van al workflow; las raras y abiertas, al agente.

## Errores y confusiones comunes

- **Pasar a poscuántico solo y perder la protección clásica,** sin necesidad.
- **Ignorar el tamaño del saludo:** la fragmentación puede romper conexiones por dispositivos intermedios.
- **Confundir «híbrido» cripto con «híbrido» de aplicación o de nube,** que no tienen relación.
- **Usar un agente para todo** en lugar de enrutar (`SE-589`).

## Límites y cuándo no aplica

El híbrido criptográfico no resuelve el inventario ni la migración de los demás usos (firmas, certificados). Los tamaños son los de `SE-285` para esos algoritmos; otros parámetros difieren. El enrutador de agentes añade su propio punto de fallo: clasificar mal una solicitud.
