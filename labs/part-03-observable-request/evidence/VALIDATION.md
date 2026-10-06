# Evidencia de validación — Parte 03

## Alcance

La validación cubre Python 3.11 o posterior, loopback IPv4 y siete escenarios
deterministas. No acredita DNS público, PKI real, proxies de terceros ni tolerancia
regional.

## Comprobaciones automatizadas

1. petición sana con correlación;
2. fallo DNS antes de conexión;
3. puerto cerrado antes de HTTP;
4. rechazo de nombre TLS antes de HTTP;
5. deadline durante espera del primer byte;
6. pérdida sintética y recuperación en dos intentos;
7. 503 transitorio y recuperación;
8. redacción de cabeceras sensibles;
9. cierre y unión del hilo servidor;
10. límites declarados en todos los resultados;
11. suite CLI con JSON válido.

La evidencia ejecutada y las plataformas de CI se registran en el commit que publica
la parte. Este archivo enumera el contrato de comprobación; no inventa resultados de
una ejecución futura.
