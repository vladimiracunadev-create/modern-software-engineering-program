# Contrato entre equipos

## Definición

Un **contrato entre equipos** es una interfaz documentada con propietario, versiones y una vía de solicitud de cambios. Es la definición de trabajo de `SE-530`. No es un contrato legal: es el acuerdo explícito que describe qué ofrece un equipo a otro a través de una frontera, quién responde por ello y cómo se cambia.

## Por qué importa

Hay fronteras inevitables: en el ejemplo de `SE-530`, la exportación al ministerio la necesitan varios equipos. Lo que decide el costo de cruzarlas es si existe contrato. Sin él, cada cambio se negocia de nuevo, depende de quién esté disponible y se pierde en reuniones. Con un contrato, la dependencia se vuelve predecible: se sabe a quién pedir, con qué información, por qué canal y en qué plazo.

## Cómo funciona

`SE-530` enumera sus partes: una **interfaz documentada**, **versiones**, un **propietario** claro y un acuerdo sobre cómo se **solicitan cambios** (canal, plazo, información requerida). La causa de su utilidad es que sustituye la coordinación en tiempo real por un acuerdo escrito: el equipo consumidor puede planificar sin esperar a una persona.

La clase añade el contrapeso: con un contrato demasiado rígido, quien usa la interfaz espera semanas por una modificación trivial. Por eso el contrato incluye una **vía de autoservicio**: qué puede cambiar una persona de otro equipo en este módulo, con revisión de las dueñas, sin esperar su iteración. Así el contrato fija la responsabilidad sin convertirla en cuello de botella.

El contrato se apoya en lo ya visto sobre interfaces y compatibilidad: versionar permite que ambos lados cambien a ritmos distintos sin romperse.

## Ejemplo

En `SE-530` (plataforma educativa, datos sintéticos), varios equipos necesitan la exportación al ministerio. El módulo tiene un propietario, una especificación del formato versionada y un procedimiento: las solicitudes de cambio entran por un canal con plazo y plantilla. Para cambios menores (añadir una columna opcional) hay autoservicio: otra persona prepara el cambio, las dueñas lo revisan y se integra sin esperar a la siguiente iteración. Un cambio que rompe el formato exige versión nueva y aviso.

## Errores y confusiones comunes

- **Un archivo espera semanas por una persona.** Causa señalada en `SE-530`: propiedad fuerte sin segundo conocedor. Corrección: revisión obligatoria por una segunda persona y rotación.
- **Todo cambio requiere tres equipos.** Fronteras por capa, no por dominio. Corrección: reorganizar por dominio o abrir vía de autoservicio.
- **Contrato sin propietario.** Una interfaz «de todos» no tiene a quién pedirle cambios.
- **Confundir el contrato con la documentación.** Documentar la interfaz es una parte; falta propiedad, versiones y proceso de cambio.

## Límites y cuándo no aplica

Las definiciones de `SE-530` son operativas para el equipo de plataforma educativa y sus experimentos usan datos sintéticos: no se analizó ningún repositorio, equipo ni guardia reales, y el reparto del conocimiento, las capas tocadas y el costo por relevo son construcciones del autor. Un contrato no sustituye al diseño de las fronteras: si cada cambio cruza varios equipos, el problema está en dónde se trazaron. En equipos pequeños con una frontera trivial, un contrato formal puede costar más de lo que ahorra.
