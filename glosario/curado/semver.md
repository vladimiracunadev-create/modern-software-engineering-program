# Semver

## Definición

**SemVer** (*Semantic Versioning*, versionado semántico) es una convención de la especificación publicada en semver.org para numerar versiones con tres componentes, `MAYOR.MENOR.PARCHE`, de modo que el número **comunique el tipo de cambio**: se incrementa la **mayor** cuando hay cambios incompatibles de la API pública, la **menor** cuando se añade funcionalidad de forma compatible y el **parche** cuando se corrige un defecto de forma compatible. `SE-110` subraya la condición previa: SemVer **exige declarar la API pública**; sin ella, los números no significan nada. Existen reglas particulares antes de la 1.0.0.

## Por qué importa

Quien depende de una biblioteca necesita decidir si puede actualizar sin romper su código. Con SemVer, esa decisión se apoya en el número: un parche o una versión menor deberían ser seguros; una mayor exige revisar. Pero `SE-110` cuida el alcance: **el número comunica una intención; no verifica que el cambio la cumpla, ni reemplaza una política de soporte**. La decisión que cambia es cuánta confianza se deposita en el número de versión de terceros y cuánta responsabilidad se asume al emitir el propio: el número es una promesa que hay que respaldar con pruebas de compatibilidad.

## Cómo funciona

Las reglas de la especificación que `SE-110` utiliza:

- **MAYOR** (`X.y.z`): cambios incompatibles de la API pública.
- **MENOR** (`x.Y.z`): funcionalidad nueva compatible hacia atrás.
- **PARCHE** (`x.y.Z`): correcciones compatibles.
- Una vez publicada una versión, **su contenido no debe modificarse**; cualquier cambio se publica como versión nueva.
- La versión **0.y.z** es para desarrollo inicial: cualquier cosa puede cambiar en cualquier momento y la API pública no debe considerarse estable.
- Las versiones **preliminares** (*prerelease*) se marcan con un sufijo (`1.0.0-rc.1`).

Un punto crítico es el entorno concreto. Python no usa SemVer como esquema propio sino el de **PEP 440**, que difiere en detalles. `SE-110` documenta dos consecuencias: una versión SemVer con guion (`1.0.0-alpha.beta`) se rechaza al publicar porque **no es una versión PEP 440 válida**, y la corrección es normalizar al esquema de Python o cambiar de esquema y documentarlo; y `1.0.post1 > 1.0.0` es un concepto (la **post-versión**) que SemVer no define. Es decir, SemVer se adapta al ecosistema de empaquetado en que se usa.

## Ejemplo

Un SDK pasa de `1.2.4` a distintas versiones según el cambio:

```text
1.2.4 -> 1.2.5   corrección de un defecto, sin cambiar la API pública
1.2.4 -> 1.3.0   nueva opción con valor por defecto compatible
1.2.4 -> 2.0.0   se elimina una función pública o se cambia una firma
2.0.0rc1         prerelease de la versión siguiente (forma PEP 440)
```

La clasificación se hace comparando la API pública (por ejemplo, con un comparador de firmas) y con la prueba del consumidor anterior contra el *release* nuevo. Si el comparador detecta una firma eliminada y el equipo había planeado un parche, el número propuesto es incorrecto: el número se decide **después** de clasificar el cambio, no antes.

## Errores y confusiones comunes

- **No declarar la API pública.** El número carece de referente.
- **Creer que el número garantiza compatibilidad.** Comunica intención; hay que verificarla.
- **Usar SemVer de semver.org sin adaptarlo al ecosistema.** En Python, la versión debe ser válida según PEP 440.
- **Modificar una versión ya publicada.** Rompe la confianza en la inmutabilidad.

## Límites y cuándo no aplica

Antes de la 1.0.0 las reglas son laxas y la versión no promete compatibilidad. SemVer no cubre cambios que son incompatibles en la práctica pero no en la API (rendimiento, uso de memoria, comportamiento no documentado). Para software que se despliega continuamente sin consumidores externos, o para aplicaciones cuyo versionado responde al calendario (versionado por fecha), puede no ser el esquema adecuado, y lo correcto es elegir uno y documentarlo.
