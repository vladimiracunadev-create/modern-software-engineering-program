# Aplicaciones para Windows y Android

El portal del programa (612 clases, 32 casos de estudio, glosario de 2.743 conceptos, guías
de rol y figuras) se empaqueta también como aplicaciones que **funcionan sin conexión**. Son
una **vista empaquetada** del portal: el repositorio y GitHub Pages siguen siendo la fuente
viva, y ninguna app se edita a mano. Los binarios no entran en git; se publican como activos
de un GitHub Release (versión `v0.1.0` y siguientes, independientes del release de PDF
descrito en [`PDF.md`](PDF.md)).

## Qué se publica

| Plataforma | Activo | Para qué sirve |
| --- | --- | --- |
| Windows | `Ingenieria-Software-Moderna-<v>-setup-windows-x64.exe` | Instalador (Inno Setup): menú de inicio y desinstalador |
| Windows | `Ingenieria-Software-Moderna-<v>-windows-x64.msi` | MSI para implantación gestionada (`msiexec /qn`, directivas de grupo) |
| Windows | `Ingenieria-Software-Moderna-<v>-portable-windows-x64.zip` | Carpeta portable: descomprimir y ejecutar |
| Windows | `Ingenieria-Software-Moderna-<v>-windows-x64.exe` | Ejecutable único: un solo fichero, arranque más lento |
| Android | `Ingenieria-Software-Moderna-<v>-android.apk` | Aplicación con el portal embebido |
| ambas | `SHA256SUMS-windows.txt` y `SHA256SUMS-android.txt` | Sumas SHA-256 por plataforma |

Los nombres y tamaños exactos de cada edición están en la página de su release.

## Cómo funcionan

- **Windows** (`apps/desktop/main.py`, Tkinter y PyInstaller). La app sirve la carpeta `site/`
  empaquetada desde `127.0.0.1` (solo loopback, sin salir a la red) y abre el navegador
  predeterminado. Hace falta HTTP porque el índice del portal carga `assets/catalog.json` con
  `fetch`, algo que `file://` no permite. Cerrar la ventana detiene el servidor.
- **Android** (`apps/android`, Capacitor 8). El APK lleva `site/` en `assets/public/` y lo
  muestra una WebView con el esquema interno `https://localhost`. No hay servidor remoto.
- **Sin servicios externos.** Los diagramas Mermaid ya están prerenderizados como SVG dentro
  del portal; los enlaces a fuentes externas (normas, artículos) sí necesitan conexión, como
  en cualquier lectura sin red.

## Instalación

```powershell
# Instalador: doble clic, o en silencio
.\Ingenieria-Software-Moderna-0.1.0-setup-windows-x64.exe /VERYSILENT
# MSI
msiexec /i .\Ingenieria-Software-Moderna-0.1.0-windows-x64.msi /qn
```

En Android, copia el APK al dispositivo y permite la instalación de orígenes desconocidos
para la aplicación con la que lo abras.

## Comprobar una descarga

```powershell
Get-FileHash .\Ingenieria-Software-Moderna-0.1.0-windows-x64.exe -Algorithm SHA256
```

```bash
sha256sum -c SHA256SUMS-windows.txt --ignore-missing
sha256sum -c SHA256SUMS-android.txt --ignore-missing
```

## Cómo se verifica un artefacto

Que el build termine, el APK se firme y la suma cuadre **no prueba que lleve el programa**: el
fallo clásico es un artefacto que compila y se instala vacío. Por eso
[`scripts/verify_apps.py`](../scripts/verify_apps.py) abre cada artefacto y lo compara con el
`site/` del repositorio:

- todos los ficheros de `site/` están dentro con el mismo SHA-256 (nada falta ni cambió; en el
  APK se excluye `.nojekyll`, que Android no empaqueta);
- las 612 clases `SE-001`–`SE-612` (derivadas de `content/part-NN/SE-NNN.md`), cada una con
  contenido real, los 32 casos y los 2.743 conceptos del glosario;
- los `.exe`, abiertos con `--self-check`, cuentan lo mismo y devuelven la misma huella;
- el instalador se instala en silencio y se desinstala; el MSI se extrae con `msiexec /a`;
- el APK trae `AndroidManifest.xml`, `classes.dex` y el portal en `assets/public/`;
- cada `SHA256SUMS-*.txt` coincide con los ficheros y no deja ninguno fuera.

Un paso que no puede ejecutarse (por ejemplo, el MSI fuera de Windows) sale **OMITIDO**, nunca
aprobado. `tests/test_apps_tooling.py` comprueba que el verificador detecta portales vacíos,
clases huecas, ficheros cambiados y APK vacíos.

## Construir

El workflow [`apps.yml`](../.github/workflows/apps.yml) construye y verifica ambas
plataformas; la versión canónica es [`apps/VERSION`](../apps/VERSION). En local:

```powershell
python -m pip install pyinstaller==6.19.0 pillow==12.2.0
python scripts/build_apps.py windows              # ejecutable único y portable
python scripts/build_apps.py windows --installers # además setup.exe (Inno Setup 6) y .msi (WiX 5)
python scripts/build_apps.py sums windows
python scripts/verify_apps.py --dir dist --require windows
```

El APK exige Node 22+, JDK 21 y el SDK de Android 36; los pasos están en `apps.yml`
(`android-prepare`, `npx cap add android`, `gradlew assembleDebug`, `android-collect`).
`apps/android/package-lock.json` es la única excepción a la política de no versionar
lockfiles: fija el árbol npm para que `npm ci` sea reproducible.

## Límites honestos

- **Sin firma de código en Windows.** SmartScreen avisará la primera vez; verifica la suma
  SHA-256 antes de ejecutar.
- **El APK está firmado con la clave de depuración**, no con una de publicación: no procede de
  Google Play, no se actualiza solo y exige permitir orígenes desconocidos.
- **Reproducible no es idéntico bit a bit.** Mismo código, mismas versiones fijadas y mismos
  comandos, pero PyInstaller, Inno Setup, WiX y Gradle no garantizan binarios idénticos.
- **Solo x64 en Windows** y solo probadas las versiones de Windows y Android de los runners de CI.
- **No se ha probado a mano en dispositivos físicos.** La verificación es automática: abre y
  cuenta el contenido; no certifica la experiencia de uso, la accesibilidad ni el rendimiento
  del WebView en cada dispositivo.
- **Pesan decenas de MB** porque llevan todo el portal; no hay actualización automática: se
  instala la edición nueva encima.
- **El contenido sigue pendiente de revisión editorial humana independiente**, igual que el
  portal y los PDF; las apps no cambian esa condición.
