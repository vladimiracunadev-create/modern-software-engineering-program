# Metadata de proyecto

## Definición

La **metadata de proyecto** es el conjunto de datos declarativos que describen un paquete y permiten construirlo e instalarlo: **nombre, versión, versión mínima del *runtime*, dependencias, licencia, autores y *entry points*** (puntos de entrada que el paquete declara, como comandos o plugins). En Python, esta metadata se declara en la tabla `[project]` de `pyproject.toml` y se publica con el paquete; las especificaciones de la Python Packaging Authority definen sus campos. `SE-112` la presenta como la parte del paquete que no es código pero que decide cómo se comporta al distribuirse.

## Por qué importa

La metadata es lo primero que el instalador lee. Si es incorrecta o está desactualizada, el paquete se instala con dependencias equivocadas, se publica con una versión ambigua o declara una licencia que no corresponde. La decisión que cambia es dónde vive cada dato: **la versión tiene una fuente canónica y las demás superficies se derivan de ella**. Con varias copias editadas a mano (en `pyproject.toml`, en el código y en la etiqueta de Git) tarde o temprano discrepan.

## Cómo funciona

El constructor lee la metadata y genera los archivos de distribución con ella. Esa metadata se consulta de dos formas: el instalador resuelve las dependencias y la versión mínima del *runtime* antes de instalar, y el paquete instalado la expone (por ejemplo, con `importlib.metadata`) para que otros programas la consulten. Por esa razón:

- **Nombre y versión** identifican de forma única el artefacto.
- **Dependencias y versión de *runtime*** determinan dónde puede instalarse; declararlas mal produce `ModuleNotFoundError` en entornos limpios.
- ***Entry points*:** declaran qué comandos o extensiones expone el paquete, y son la base del descubrimiento de plugins.
- **Licencia y autores:** metadatos legales y de procedencia.

`SE-112` advierte que **la metadata incoherente con el código o con la etiqueta produce releases ambiguos**: nadie sabe qué versión es realmente la publicada. Por eso se fija una sola fuente (por ejemplo, la etiqueta de Git, de la que el constructor deriva la versión) y se verifica que las demás coincidan.

## Ejemplo

Un `pyproject.toml` mínimo (ilustración):

```toml
[project]
name = "engineering-sdk"
version = "1.3.0"
requires-python = ">=3.9"
dependencies = ["tomli>=2; python_version < '3.11'"]
license = {text = "MIT"}

[project.scripts]
engineering = "engineering_sdk.cli:main"
```

Si una prueba compara la versión del paquete instalado con la de la etiqueta publicada y falla cuando difieren, se evita publicar una versión ambigua. `SE-112` documenta dos fallos del empaquetado: `FileNotFoundError` solo tras instalar porque el archivo de datos no está declarado en `package-data` (se declara y se compara el contenido de la rueda con una lista esperada), e `import json` que devuelve un objeto raro porque un `json.py` local tapa la biblioteca estándar (se renombra y se verifica con `-I` o `-P`).

## Errores y confusiones comunes

- **Varias fuentes de versión.** Discrepan y generan releases ambiguos.
- **Dependencias no declaradas.** Funcionan en la máquina del autor y fallan en un entorno limpio.
- **Copiar metadata de otro proyecto.** Licencia o autores incorrectos.
- **Olvidar los archivos de datos.** El paquete instalado no los encuentra.

## Límites y cuándo no aplica

Un paquete instalado todavía necesita una interfaz operable y estable (`SE-112`): la metadata describe, no garantiza comportamiento. No sustituye una política de versionado ni la verificación de procedencia. Y para un script de un solo archivo que no se distribuye como paquete, declarar metadata completa no aporta.
