# GitFlow

## Definición

**GitFlow** es un modelo de ramas con una rama de desarrollo y ramas de versión y de corrección, pensado para software con versiones que conviven (SE-197). Se opone a flujos más simples con una rama principal y ramas cortas, como el desarrollo basado en el tronco.

## Por qué importa

Cambia el costo de integrar y de publicar. Elegirlo cuando no corresponde añade ramas, distancia entre ellas y trabajo de sincronización sin dar protección. SE-197 lo plantea como decisión de contexto: sirve a software distribuido que mantiene varias versiones vivas; para un servicio que se despliega continuamente, la rama de versión añade trabajo sin proteger nada.

## Cómo funciona

El modelo mantiene líneas con papeles distintos: una rama de desarrollo donde se integra el trabajo; ramas de versión donde se estabiliza lo que va a publicarse; y ramas de corrección para arreglar versiones ya publicadas. Surgió para software con versiones distribuidas que conviven, donde publicar es costoso y se mantienen varias versiones a la vez.

Su **beneficio** es separar lo que se estabiliza de lo que se desarrolla: la rama de versión recibe solo correcciones mientras la de desarrollo sigue avanzando. Su **costo** es la distancia entre ramas y los *backports* (llevar una corrección de una rama a otras), que son una fuente constante de conflictos y de olvidos. El mecanismo de fondo es el mismo que SE-195 trata en fusiones: cuanto más viven las ramas, más divergen y más caro es reunirlas; SE-197 señala el síntoma de cada integración que exige un día de resolver conflictos, con causa en ramas que viven semanas y corrección en acortarlas e integrar a diario.

## Ejemplo

SE-197 compara dos casos. Un componente distribuido como biblioteca con tres versiones vivas: una rama de versión por línea soportada, con vida acotada, es apropiada. Un servicio que se despliega a diario con GitFlow completo: es peligroso, porque la rama de desarrollo añade distancia sin protección; ahí basta con una rama principal y ramas cortas, y las banderas de funcionalidad separan despliegue de activación.

## Errores y confusiones comunes

- **Aplicar GitFlow completo por moda** a un servicio de despliegue continuo.
- **Ramas de larga vida** que acumulan conflictos.
- **Main roto tras dos PR verdes**: no se probó la combinación; corrección: probar el resultado de la fusión o usar una cola de fusión.
- **Olvidar los backports**: la corrección llega a una versión y no a otra.
- **Confundir GitFlow con Git**: es una convención de uso, no una función de la herramienta.

## Límites y cuándo no aplica

No aplica bien a servicios con una sola versión en producción ni a equipos que integran a diario con pruebas automáticas fuertes. Es razonable cuando hay varias versiones soportadas a la vez (bibliotecas, software instalado, productos con contratos de soporte por versión). Incluso entonces se acota: ramas de versión por línea soportada y con vida limitada, no ramas permanentes por costumbre.
