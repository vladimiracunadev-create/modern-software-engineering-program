# Entorno de vista previa

## Definición

Un **entorno de vista previa** (*preview environment*) es una instancia completa y temporal de la aplicación creada para un cambio propuesto, con una dirección propia donde revisar el resultado antes de integrarlo. Es la definición de `SE-488`.

## Por qué importa

Convierte la revisión de algo que se *lee* en algo que se *prueba*. En lugar de imaginar el efecto de un diff, quien revisa abre la aplicación con ese cambio, la usa y comparte el enlace con producto o diseño. Cambia la decisión de cuándo se descubre un problema de integración: antes de fusionar, no después.

## Cómo funciona

`SE-488` le atribuye un requisito y un ciclo de vida.

**Requisito:** que el sistema se pueda levantar desde código. Eso significa infraestructura declarada, configuración por entorno y datos iniciales. Si levantar la aplicación exige pasos manuales, no hay vista previa automática posible.

**Ciclo de vida**, en cuatro momentos:

1. Se **crea** al abrir o actualizar la solicitud de integración.
2. Se **usa** durante la revisión.
3. Se **renueva** cuando hay actividad.
4. Se **destruye** al cerrarse la solicitud o al vencer su vida.

Un generador de aplicaciones a partir de las solicitudes abiertas (la clase menciona el generador por solicitud de integración de algunas herramientas de GitOps) automatiza la creación y la destrucción. La destrucción importa tanto como la creación: sin ella, cada solicitud deja infraestructura huérfana y costo.

La causa de su utilidad es que cada cambio recibe un aislamiento propio, de modo que dos solicitudes no se pisan una a otra como lo harían en un único entorno compartido de pruebas.

## Ejemplo

Se abre una solicitud que cambia la pantalla de entregas. La automatización levanta una instancia con su dirección propia, carga datos iniciales y publica el enlace en la solicitud. Quien revisa prueba el flujo; se actualiza la rama y la instancia se renueva; al fusionar o cerrar la solicitud, la instancia se destruye. Los datos iniciales son un asunto aparte: `SE-488` advierte que un entorno de pruebas con datos que identifican a personas por vinculación es un riesgo, y por eso los datos se enmascaran.

## Errores y confusiones comunes

- **Una persona es identificable en un entorno de pruebas.** Cuasi-identificadores sin generalizar; corrección: medir la unicidad, generalizar y suprimir grupos pequeños.
- **Las pruebas de integridad fallan con datos enmascarados.** Sustitución aleatoria por tabla; corrección: sustitución determinista con clave protegida.
- **Confundirlo con el entorno de staging.** Staging es uno y compartido; la vista previa es uno por cambio y efímero.
- **Olvidar el apagado.** Sin destrucción automática, los entornos se acumulan.

## Límites y cuándo no aplica

Exige que el sistema sea reproducible desde código; en sistemas con dependencias que no se pueden replicar (un sistema externo único, hardware, grandes volúmenes de datos) la vista previa será parcial y conviene declarar qué simula. No prueba el rendimiento ni el comportamiento con carga real de producción. Y su costo debe acotarse con vida máxima y límite de instancias simultáneas.
