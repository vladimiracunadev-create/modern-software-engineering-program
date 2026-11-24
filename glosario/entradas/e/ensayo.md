# Ensayo

[↑ Glosario](../../README.md) · [← Enrutador de celdas](./enrutador-de-celdas.md) · [Ensayo de vuelta atrás →](./ensayo-de-vuelta-atras.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Un **ensayo** es una repetición del evento con el que se comprueba un control, por ejemplo revocar una credencial y verificar que deja de funcionar ([SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md)).

## Por qué importa

Un control que pasa una prueba puede ser débil. Cuántos ensayos hacen falta depende de la cota que se quiere afirmar sobre la tasa de fallas.

## Cómo funciona

Si el control tiene eficacia real *p*, la probabilidad de que *n* ensayos independientes salgan todos bien es `p^n`. Un control con eficacia de 95 % (falla una vez de cada veinte) pasa 5 ensayos con probabilidad 77 %, 20 ensayos con 36 % y 59 ensayos con solo 4,8 %. De ahí sale la **regla de tres**: si *n* ensayos salen bien, con 95 % de confianza la tasa de fallas es menor que 3/*n*; con 59 ensayos, menor que 5 %.

## Ejemplo

[SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md) (caso hipotético): para la revocación, el criterio de aceptación es «con 59 ensayos con cuentas de prueba, el acceso termina en menos de 30 s en todos».

## Errores y confusiones comunes

- **Un control débil aprueba la auditoría.** Pocos ensayos; fijar ensayos acordes a la cota que se afirma.
- **Un control bueno falla alguna vez.** Criterio «cero fallas» con muchos ensayos; declarar tolerancia y repetición antes del experimento.

## Límites y cuándo no aplica

Supone ensayos independientes; la regla de tres da una cota, no la tasa real.

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
