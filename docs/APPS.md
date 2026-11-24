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
| Linux | `Ingenieria-Software-Moderna-<v>-linux-x86_64.tar.gz` y `-linux-aarch64.tar.gz` | Carpeta autocontenida: descomprimir y ejecutar `Ingenieria-Software-Moderna` |
| Linux | `Ingenieria-Software-Moderna-<v>-linux-amd64.deb` y `-linux-arm64.deb` | Paquete Debian/Ubuntu: `/opt`, lanzador en el menú y `ingenieria-software-moderna` en el PATH |
| macOS | `Ingenieria-Software-Moderna-<v>-macos-arm64.dmg` / `.zip` (Apple Silicon) y `-macos-x86_64.dmg` / `.zip` (Intel) | `.app` sin firmar dentro de un `.dmg` (arrastrar a Aplicaciones) o de un `.zip` |
| todas | `SHA256SUMS-windows.txt`, `SHA256SUMS-android.txt`, `SHA256SUMS-linux.txt` y `SHA256SUMS-macos.txt` | Sumas SHA-256 por plataforma |

> [!NOTE]
> Los activos de Linux y macOS y los APK por ABI se añaden a `v0.1.0` después de su
> publicación inicial del 2026-11-24 (que traía los cuatro activos de Windows, el APK
> universal y sus sumas). Android: `scripts/build_apps.py android-configure` activa los ABI
> splits de Gradle (`arm64-v8a`, `armeabi-v7a`, `x86_64`), pero la app es una WebView sin
> código nativo, así que los APK por ABI salen **byte a byte idénticos** al universal y no
> se publican duplicados: el APK universal sirve en todos los móviles y emuladores.

## Requisitos mínimos

| Sistema | Requisito |
| --- | --- |
| Windows | Windows 10 u 11 de 64 bits (x64) |
| Android | El mínimo que fija la plantilla de Capacitor 8 (API 24 según su documentación, sin comprobar en dispositivos); cualquier ABI; WebView actualizado |
| Linux | glibc de Ubuntu 24.04 o posterior (x86_64 o aarch64) y un navegador; `python3-tk` solo si se quiere la ventana |
| macOS | Construido en macOS 14 (arm64) y 15 (Intel); no se ha comprobado en versiones anteriores |

Los mínimos de Linux y macOS son los de los equipos de construcción, no un compromiso de
compatibilidad más amplia.

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

## Gatekeeper y SmartScreen

Ningún binario está firmado ni notarizado (no hay certificado de Windows ni cuenta de Apple).
En macOS, al abrir la app descargada Gatekeeper la bloqueará; tras copiarla a Aplicaciones:

```bash
xattr -dr com.apple.quarantine "/Applications/Ingenieria-Software-Moderna.app"
```

o abre con clic derecho › Abrir. En Windows, SmartScreen pide «Más información › Ejecutar de
todas formas». En ambos casos verifica antes la suma SHA-256.

## Límites honestos

- **Sin firma de código en Windows.** SmartScreen avisará la primera vez; verifica la suma
  SHA-256 antes de ejecutar.
- **El APK está firmado con la clave de depuración**, no con una de publicación: no procede de
  Google Play, no se actualiza solo y exige permitir orígenes desconocidos.
- **Reproducible no es idéntico bit a bit.** Mismo código, mismas versiones fijadas y mismos
  comandos, pero PyInstaller, Inno Setup, WiX y Gradle no garantizan binarios idénticos.
- **Linux y macOS solo se han verificado en los runners de CI** (ubuntu-24.04 y ubuntu-24.04-arm; macOS arm64 e Intel), sin pruebas en equipos físicos; el `.deb` de arm64 y los `.zip` de macOS se abren y cuentan, pero su ejecutable no se arranca con `--self-check`.
- **Solo x64 en Windows** y solo probadas las versiones de Windows y Android de los runners de CI.
- **No se ha probado a mano en dispositivos físicos.** La verificación es automática: abre y
  cuenta el contenido; no certifica la experiencia de uso, la accesibilidad ni el rendimiento
  del WebView en cada dispositivo.
- **Pesan decenas de MB** porque llevan todo el portal; no hay actualización automática: se
  instala la edición nueva encima.
- **El contenido sigue pendiente de revisión editorial humana independiente**, igual que el
  portal y los PDF; las apps no cambian esa condición.
