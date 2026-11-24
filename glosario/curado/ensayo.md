# Ensayo

## Definición

Un **ensayo** es una repetición del evento con el que se comprueba un control, por ejemplo revocar una credencial y verificar que deja de funcionar (`SE-514`).

## Por qué importa

Un control que pasa una prueba puede ser débil. Cuántos ensayos hacen falta depende de la cota que se quiere afirmar sobre la tasa de fallas.

## Cómo funciona

Si el control tiene eficacia real *p*, la probabilidad de que *n* ensayos independientes salgan todos bien es `p^n`. Un control con eficacia de 95 % (falla una vez de cada veinte) pasa 5 ensayos con probabilidad 77 %, 20 ensayos con 36 % y 59 ensayos con solo 4,8 %. De ahí sale la **regla de tres**: si *n* ensayos salen bien, con 95 % de confianza la tasa de fallas es menor que 3/*n*; con 59 ensayos, menor que 5 %.

## Ejemplo

`SE-514` (caso hipotético): para la revocación, el criterio de aceptación es «con 59 ensayos con cuentas de prueba, el acceso termina en menos de 30 s en todos».

## Errores y confusiones comunes

- **Un control débil aprueba la auditoría.** Pocos ensayos; fijar ensayos acordes a la cota que se afirma.
- **Un control bueno falla alguna vez.** Criterio «cero fallas» con muchos ensayos; declarar tolerancia y repetición antes del experimento.

## Límites y cuándo no aplica

Supone ensayos independientes; la regla de tres da una cota, no la tasa real.
