# Adopción

## Definición

La **adopción** es la parte de una población objetivo declarada que comienza a usar el servicio en una ventana de tiempo (SE-136). Es una fracción: un numerador (quienes empezaron a usarlo) sobre un denominador (la población que podía hacerlo). SE-259 usa el término en otro sentido cercano, de despliegue: la fracción de la base instalada que ya tiene una versión determinada en un momento dado.

## Por qué importa

Una cifra de adopción sin población objetivo es un porcentaje sin referente: «60 %» puede significar casi cualquier cosa. Cambia la decisión de qué se informa y cómo se compara: dos paneles pueden dar cifras distintas para el mismo producto simplemente porque eligieron denominadores distintos. En el sentido de despliegue, cambia la planificación: cuánto tardará una corrección urgente en llegar a la mayoría depende de cómo se adopta cada versión.

## Cómo funciona

Su punto delicado es el denominador. SE-136 plantea la pregunta: ¿todos los centros con cuenta, los que activaron, los que firmaron? Cada elección cambia el valor, y por eso la guía del Gobierno británico sobre adopción digital exige declarar la población para que la cifra tenga referente. También hay que fijar el **evento** que cuenta como «empezar a usar» (crear la cuenta no es lo mismo que lograr una entrega aceptada) y la **ventana** (los primeros 14 días, por ejemplo).

El contrato de la plataforma de entregas lo materializa en un archivo de métricas que define cada una con población, evento, ventana y filtros: adopción es «centros con al menos una entrega aceptada en los primeros 14 días, sobre centros con cuenta activada». Y ninguna cifra se publica sin su n, sin la edad mínima de la cohorte y sin su intervalo.

En el sentido de despliegue (SE-259), la adopción de una versión sigue una curva que depende del **canal**: una actualización automática llega a casi todos en días; una que exige acción de la persona, en semanas o nunca. Medirla por canal es lo que permite saber cuánto tarda una corrección urgente en cubrir a la mayoría.

## Ejemplo

La plataforma tiene 100 centros con cuenta, de los cuales 40 activaron la cuenta y 18 lograron una entrega aceptada en 14 días. Con denominador «cuentas» la adopción es 18 %; con «activaron» es 45 %. Ambas son legítimas, pero no comparables. Si la base crece a 200 centros por una campaña y los nuevos aún no activan, la adopción «baja» sin que nadie haya dejado de usar el producto: cambió el denominador. (Cifras ilustrativas del mecanismo de SE-136.)

## Errores y confusiones comunes

- **La adopción baja al crecer la base**: el denominador cambió; corrección: fijar y declarar la población objetivo.
- **Corrección urgente que tarda semanas en llegar a la mayoría**: se supuso un canal rápido; corrección: medir la adopción por canal y planear en consecuencia (SE-259).
- **Confundir adopción con retención**: la primera mide quién empieza; la segunda, quién sigue.
- **Informar sin n ni intervalo.**

## Límites y cuándo no aplica

Con poblaciones muy pequeñas la fracción tiene mucha incertidumbre y el intervalo importa más que el porcentaje. La adopción mide inicio, no valor: un producto muy adoptado puede no servir. Y en productos obligatorios (de uso impuesto por la organización) la adopción es poco informativa; interesa más la tarea útil.
