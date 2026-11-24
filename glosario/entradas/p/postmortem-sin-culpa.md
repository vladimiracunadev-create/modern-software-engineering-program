# Postmortem sin culpa

[↑ Glosario](../../README.md) · [← Postmortem](./postmortem.md) · [Postura del dispositivo →](./postura-del-dispositivo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Un **postmortem sin culpa** (*blameless postmortem*) es la revisión posterior a un incidente que parte de que cada persona actuó con la mejor información y las herramientas disponibles, y que busca los factores del sistema que hicieron posible el fallo. Es la definición de [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md); [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) lo resume como el análisis de un incidente centrado en el sistema y no en las personas. El **postmortem** es el documento que reconstruye el incidente para aprender de él; **sin culpa** es el principio con que se hace.

## Por qué importa

Decide si la organización aprende o esconde información. [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) da la razón práctica: si nombrar una acción propia tiene consecuencias personales, la información se esconde, y sin información el análisis es mentira. Cambia además dónde se buscan las correcciones: no en «tener más cuidado», sino en el diseño, las señales y los procesos.

## Cómo funciona

El análisis pregunta *por qué esa acción tenía sentido en ese momento*, *qué señales faltaban* y *qué hacía fácil equivocarse*. No elimina la responsabilidad: la **desplaza del individuo al sistema** que dejó un camino fácil hacia el fallo.

[SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) señala un obstáculo cognitivo, el **sesgo de retrospectiva**: quien conoce el desenlace lo ve como previsible y juzga la decisión con información que entonces no existía. Una forma de contrarrestarlo es reconstruir la línea de tiempo con las señales que la persona realmente veía.

Lo que convierte el documento en mejora son las **acciones verificables**: cada una con propietario, fecha y forma de comprobar que se hizo, con seguimiento semanal. Sin eso, el postmortem es literatura.

## Ejemplo

Una persona ejecutó un comando de limpieza en el entorno equivocado. Un postmortem con culpa concluye «error humano; se le recuerda el procedimiento». Uno sin culpa pregunta: ¿por qué el terminal de producción y el de pruebas se veían iguales?, ¿por qué el comando no pedía confirmación?, ¿por qué la persona tenía permiso de borrado en producción sin segundo aprobador? Las acciones resultantes son cambios del sistema: color y nombre distintos del entorno, confirmación y permisos más estrechos, cada una con propietario y fecha. (Ilustración propia; las clases tratan incidentes sintéticos con tiempo virtual.)

## Errores y confusiones comunes

- **El postmortem culpa a una persona.** Se detuvo en «error humano»; corrección de [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md): preguntar por qué la acción tenía sentido y qué la facilitó.
- **El incidente se repite.** Las acciones carecen de propietario, fecha o verificación; hay que hacerlas verificables y darles seguimiento.
- **Creer que «sin culpa» es «sin responsabilidad».** Se mantiene la responsabilidad, pero del sistema y de quien lo diseña o decide.
- **Escribirlo solo para cumplir.** Si nadie lee ni actúa sobre él, no cumple su función.

## Límites y cuándo no aplica

Las definiciones de [SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) son operativas para la API de entregas y sus experimentos usan tiempo virtual y semillas fijas. El enfoque sin culpa no ampara la negligencia deliberada ni el ocultamiento: si alguien incumple a propósito una regla, es otro asunto, y se trata con otros mecanismos. Funciona solo si hay cultura que lo sostenga: un documento que declara «sin culpa» mientras la gestión penaliza a quien habla destruye la confianza que pretendía crear. En [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) la idea se extiende a incidentes de modelos, donde además hay que reconstruir datos y versiones.

## Relación con otros conceptos

- **Prerrequisito:** [Incidente](../i/incidente.md).
- **Ver también:** [Análisis](../a/analisis.md), [Acción correctiva verificable](../a/accion-correctiva-verificable.md), [Exposición](../e/exposicion.md), [Factor contribuyente](../f/factor-contribuyente.md), [Inyección de fallas](../i/inyeccion-de-fallas.md), [Mitigación](../m/mitigacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-501 — Postmortems sin culpa y aprendizaje](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md), [Cloudflare](../../../casos/exito/cloudflare.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — práctica sin culpa; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: Postmortem Culture](https://sre.google/workbook/postmortem-culture/) — adopción y errores comunes; autoridad: Google, SRE Workbook.
- [Cook, «How Complex Systems Fail»](https://how.complexsystems.fail/) — múltiples causas contribuyentes; autoridad: texto del autor, Richard I. Cook.
- [Fischhoff, «Hindsight ≠ foresight»](https://doi.org/10.1037/0096-1523.1.3.288) — sesgo de retrospectiva; autoridad: Journal of Experimental Psychology, 1975.
- [Dekker, «The Field Guide to Understanding “Human Error”»](https://openlibrary.org/isbn/9781472439055) — ISBN 978-1-4724-3905-5; autoridad: libro, CRC Press, 2014.

---

[↑ Glosario](../../README.md) · [← Postmortem](./postmortem.md) · [Postura del dispositivo →](./postura-del-dispositivo.md)
