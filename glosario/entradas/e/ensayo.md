# Ensayo

[↑ Glosario](../../README.md) · [← Enrutador de celdas](./enrutador-de-celdas.md) · [Ensayo de vuelta atrás →](./ensayo-de-vuelta-atras.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Una repetición del evento con el que se comprueba un control.

Definición de trabajo de [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md).

## Por qué importa

En [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), el tema «Número de ensayos» importa porque pocos ensayos aprueban controles débiles; muchos fallan a los buenos.

## Cómo funciona

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

Un ensayo es una repetición del evento (revocar una credencial y comprobar que deja de funcionar). Si el control tiene eficacia real p, la probabilidad de que n ensayos independientes salgan todos bien es `p^n`. Un control con eficacia de 95 % (falla una vez de cada veinte) pasa 5 ensayos con probabilidad 77 %, 20 ensayos con 36 % y 59 ensayos con solo 4,8 %. Eso fija la **regla de tres**: si n ensayos salen bien, con 95 % de confianza la tasa de fallas es menor que 3/n; con 59 ensayos, menor que 5 %. No es una peculiaridad: es la forma de pasar de «no vimos fallas» a «la tasa de fallas es menor que el límite con tal confianza».

Según [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md):

Supón, como caso hipotético y no como medición, que el equipo de la API de entregas escribe para cada control un criterio de aceptación. Para la revocación: «con 59 ensayos con cuentas de prueba, el acceso termina en menos de 30 s en todos»; para los certificados internos: «una prueba mensual con un certificado de prueba vencido comprueba que salta la alerta con 30 días de antelación»; para el registro de auditoría: «con el almacén lleno, la API deja de aceptar escrituras sensibles (falla cerrada) y emite una alerta en menos de 60 s». Cada experimento tiene radio de una cuenta de prueba, aborto, reversión y un responsable, y conserva su evidencia con huella.

## Ejemplo

Ejemplo de [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la probabilidad de que un control de eficacia p pase n ensayos y el número de ensayos que sostienen una cota. Antes de ejecutarlo, predice cuántos ensayos hacen falta para sostener una tasa de fallas menor que 1 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un control débil aprueba la auditoría** — causa: pocos ensayos. Corrección: fijar ensayos acordes a la cota que se afirma. ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md))
- **Un control bueno falla alguna vez** — causa: criterio «cero fallas» con muchos ensayos. Corrección: declarar tolerancia y repetición antes del experimento. ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un ensayo es una repetición del evento (revocar una credencial y comprobar que deja de funcionar). ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md))
- La transferencia está lograda cuando puedes decir qué cota sostiene la evidencia y qué no, no cuando el control tiene un ensayo. ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Control](../c/control.md), [Evento](./evento.md), [Repetición](../r/repeticion.md), [Caos de seguridad](../c/caos-de-seguridad.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Evidencia de cumplimiento](./evidencia-de-cumplimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-514 — Aprender de los experimentos: hallazgos, métricas y mejora](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (58 clases más lo mencionan; las que más):

[SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — Security Monkey y verificación de certificados; autoridad: blog de ingeniería de Netflix.
- [Reglamento (UE) 2022/2554 sobre resiliencia operativa digital del sector financiero](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — pruebas de resiliencia como requisito regulatorio; autoridad: Diario Oficial de la Unión Europea.
- [NIST SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planificación, prueba y mantenimiento de contingencias; autoridad: National Institute of Standards and Technology.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — variar eventos reales y medir la salida; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [IETF RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) — validez temporal de los certificados X.509; autoridad: Internet Engineering Task Force.

---

[↑ Glosario](../../README.md) · [← Enrutador de celdas](./enrutador-de-celdas.md) · [Ensayo de vuelta atrás →](./ensayo-de-vuelta-atras.md)
