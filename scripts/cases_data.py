"""Fixed list of the case studies ("Casos de estudio") and the shared contract of the surface.

The cases are not classes, roles or parts: they never change the 588 / 49 counters. The list below is
the single source for the index pages, the README section, the portal pages and the validators.
Each case lives in ``casos/<kind>/<slug>.md`` and may ship ``scripts/figures_case_<slug>.py`` (a
``FIGURES`` mapping like ``scripts/figures_part*_a.py``) whose SVG files go to ``casos/figures/`` and
whose file names start with ``<slug>-``.
"""
from __future__ import annotations

GITHUB_BLOB = "https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/"

# Marker kept by every skeleton; the session that writes a case removes it by replacing the file.
SKELETON_MARKER = "<!-- case:status=skeleton -->"

KINDS = {
    "exito": {
        "title": "Plataformas exitosas",
        "label": "éxito",
        "emoji": "🚀",
    },
    "fallo": {
        "title": "Plataformas y sistemas que fallaron",
        "label": "fallo",
        "emoji": "🧯",
    },
}

# slug, kind, name, year (founding / launch for success, event for failure), who, place, hook
CASES: list[dict[str, str]] = [
    {"slug": "netflix", "kind": "exito", "name": "Netflix", "year": "1997",
     "who": "Reed Hastings y Marc Randolph", "place": "Los Gatos, California (EE. UU.)",
     "hook": "Del alquiler de DVD por correo a una plataforma de streaming que diseña su infraestructura para que cualquier pieza pueda fallar sin que el espectador lo note."},
    {"slug": "whatsapp", "kind": "exito", "name": "WhatsApp", "year": "2009",
     "who": "Jan Koum y Brian Acton", "place": "Mountain View, California (EE. UU.)",
     "hook": "Un servicio de mensajería que llegó a cientos de millones de usuarios con un equipo de ingeniería diminuto, apostando por la simplicidad y la concurrencia."},
    {"slug": "uber", "kind": "exito", "name": "Uber", "year": "2009",
     "who": "Travis Kalanick y Garrett Camp", "place": "San Francisco, California (EE. UU.)",
     "hook": "Un mercado de dos lados en tiempo real donde emparejar conductor y pasajero es un problema de ubicación, precio y confianza a la vez."},
    {"slug": "mercado-libre", "kind": "exito", "name": "Mercado Libre", "year": "1999",
     "who": "Marcos Galperin", "place": "Buenos Aires (Argentina)",
     "hook": "Un marketplace construido en América Latina que tuvo que resolver pagos, logística y confianza donde la infraestructura asumida en otros mercados no existía."},
    {"slug": "amazon", "kind": "exito", "name": "Amazon", "year": "1994",
     "who": "Jeff Bezos", "place": "Seattle, Washington (EE. UU.)",
     "hook": "Una librería en línea cuyas capacidades internas, expuestas como servicios con contrato, acabaron convirtiéndose en el negocio de nube más grande del mundo."},
    {"slug": "spotify", "kind": "exito", "name": "Spotify", "year": "2006",
     "who": "Daniel Ek y Martin Lorentzon", "place": "Estocolmo (Suecia)",
     "hook": "Un servicio de música por streaming cuya organización en equipos autónomos es tan conocida como su arquitectura, y no siempre se entiende bien."},
    {"slug": "airbnb", "kind": "exito", "name": "Airbnb", "year": "2008",
     "who": "Brian Chesky, Joe Gebbia y Nathan Blecharczyk", "place": "San Francisco, California (EE. UU.)",
     "hook": "Un mercado de alojamiento entre desconocidos donde la confianza, la búsqueda y la disponibilidad son tan técnicas como comerciales."},
    {"slug": "stripe", "kind": "exito", "name": "Stripe", "year": "2010",
     "who": "Patrick y John Collison", "place": "San Francisco, California (EE. UU.)",
     "hook": "Una empresa de pagos que convirtió una integración dolorosa en una API que se aprende en una tarde, con idempotencia y versionado como producto."},
    {"slug": "slack", "kind": "exito", "name": "Slack", "year": "2014",
     "who": "Stewart Butterfield y otros tres cofundadores", "place": "San Francisco, California (EE. UU.)",
     "hook": "Una mensajería de equipos que creció de cientos a decenas de miles de personas por organización y cuyos incidentes publicados enseñan cómo se rompe y se repara una plataforma de tiempo real."},
    {"slug": "shopify", "kind": "exito", "name": "Shopify", "year": "2004",
     "who": "Tobias Lütke", "place": "Ottawa (Canadá)",
     "hook": "Una plataforma de comercio multi-inquilino que sigue siendo un monolito de Rails y que aisló a sus comerciantes en pods para que la venta de uno no tumbe a los demás."},
    {"slug": "instagram", "kind": "exito", "name": "Instagram", "year": "2010",
     "who": "Kevin Systrom y Mike Krieger", "place": "San Francisco, California (EE. UU.)",
     "hook": "Una aplicación de fotos que llegó a más de cien millones de usuarios registrados con muy pocos ingenieros y que Facebook compró en 2012 cuando aún no tenía ingresos."},
    {"slug": "discord", "kind": "exito", "name": "Discord", "year": "2015",
     "who": "Jason Citron y Stanislav Vishnevskiy", "place": "San Francisco, California (EE. UU.)",
     "hook": "Un chat para jugadores que escaló a más de 90 millones de usuarios diarios con Elixir, Rust y bases de datos que su equipo cambió tres veces por la forma real de sus datos."},
    {"slug": "cloudflare", "kind": "exito", "name": "Cloudflare", "year": "2009",
     "who": "Matthew Prince, Michelle Zatlyn y Lee Holloway", "place": "San Francisco, California (EE. UU.)",
     "hook": "Una red global que se puso entre los sitios y sus visitantes, publica con detalle sus propias caídas y reescribió su proxy, su configuración y su cómputo cuando NGINX y los contenedores dejaron de bastar."},
    {"slug": "dropbox", "kind": "exito", "name": "Dropbox", "year": "2007",
     "who": "Drew Houston y Arash Ferdowsi", "place": "San Francisco, California (EE. UU.)",
     "hook": "Una carpeta que se sincroniza entre dispositivos y que, al llegar a miles de millones de archivos, migró entre 2015 y 2016 la mayor parte de su almacenamiento a infraestructura propia, y su margen bruto pasó de 54 % a 76 % entre 2015 y 2017."},
    {"slug": "youtube", "kind": "exito", "name": "YouTube", "year": "2005",
     "who": "Chad Hurley y Steve Chen", "place": "San Bruno, California (EE. UU.)",
     "hook": "Una plataforma de vídeo comprada por Google en 2006 por 1 650 millones de dólares en acciones, cuya base de datos dio origen a Vitess y cuyo procesamiento de vídeo acabó en hardware propio."},
    {"slug": "pix", "kind": "exito", "name": "Pix", "year": "2020",
     "who": "Banco Central do Brasil (organización)", "place": "Brasil",
     "hook": "El sistema de pagos instantáneos que un banco central diseñó, reguló y opera, y que en cinco años pasó de cero a casi 80 000 millones de transacciones al año con liquidación continua las 24 horas."},
    {"slug": "knight-capital", "kind": "fallo", "name": "Knight Capital", "year": "2012",
     "who": "Knight Capital Group (organización)", "place": "Jersey City, Nueva Jersey (EE. UU.)",
     "hook": "Un despliegue incompleto reactivó código antiguo en producción y una firma de trading perdió cientos de millones de dólares en menos de una hora."},
    {"slug": "healthcare-gov", "kind": "fallo", "name": "HealthCare.gov", "year": "2013",
     "who": "CMS y contratistas federales (organización)", "place": "Estados Unidos",
     "hook": "Un sitio público de inscripción que se lanzó sin haber sido probado de extremo a extremo con la carga real y dejó a muchos usuarios sin poder inscribirse en las primeras semanas."},
    {"slug": "tsb", "kind": "fallo", "name": "TSB Bank", "year": "2018",
     "who": "TSB Bank (organización)", "place": "Reino Unido",
     "hook": "Una migración de plataforma bancaria hecha de una sola vez dejó a clientes sin acceso y con datos de otras personas durante semanas."},
    {"slug": "meta-2021", "kind": "fallo", "name": "Caída global de Meta", "year": "2021",
     "who": "Meta, entonces Facebook, Inc. (organización)", "place": "Menlo Park, California (EE. UU.)",
     "hook": "Un cambio de configuración de red desconectó los servicios de la empresa de Internet y, además, dejó sin herramientas a quienes debían repararlos."},
    {"slug": "crowdstrike", "kind": "fallo", "name": "CrowdStrike", "year": "2024",
     "who": "CrowdStrike (organización)", "place": "Austin, Texas (EE. UU.)",
     "hook": "Una actualización de contenido de un agente de seguridad dejó inservibles millones de equipos Windows a la vez, en aeropuertos, hospitales y bancos."},
    {"slug": "therac-25", "kind": "fallo", "name": "Therac-25", "year": "1985",
     "who": "Atomic Energy of Canada Limited (organización)", "place": "Canadá y Estados Unidos",
     "hook": "Una máquina de radioterapia cuyo software sustituyó a los enclavamientos de hardware causó sobredosis de radiación mortales entre 1985 y 1987."},
    {"slug": "gitlab-2017", "kind": "fallo", "name": "Incidente de base de datos de GitLab", "year": "2017",
     "who": "GitLab Inc. (organización)", "place": "San Francisco, California (EE. UU.)",
     "hook": "Un comando ejecutado en el servidor equivocado borró datos de producción y los respaldos que debían salvarlos resultaron no servir."},
    {"slug": "quibi", "kind": "fallo", "name": "Quibi", "year": "2018",
     "who": "Jeffrey Katzenberg y Meg Whitman", "place": "Los Ángeles, California (EE. UU.)",
     "hook": "Una plataforma de vídeo corto para móvil que recaudó más de mil millones de dólares y cerró en 2020, meses después de lanzarse, porque resolvía un problema que casi nadie tenía."},
    {"slug": "ariane-5-vuelo-501", "kind": "fallo", "name": "Ariane 5, vuelo 501", "year": "1996",
     "who": "ESA y CNES (organizaciones)", "place": "Kourou, Guayana Francesa",
     "hook": "En el primer vuelo del cohete europeo, software de Ariane 4 reutilizado sin revisar sus supuestos detuvo las dos unidades de guiado idénticas y el lanzador se destruyó a los 39 segundos."},
    {"slug": "boeing-737-max-mcas", "kind": "fallo", "name": "Boeing 737 MAX y MCAS", "year": "2018",
     "who": "Boeing y la FAA (organizaciones)", "place": "Estados Unidos, Indonesia y Etiopía",
     "hook": "Una función nueva del control de vuelo que dependía de un solo sensor empujó el morro de dos aviones hacia abajo, y los análisis de seguridad suponían que los pilotos la reconocerían y la cortarían."},
    {"slug": "post-office-horizon", "kind": "fallo", "name": "Post Office Horizon", "year": "2000",
     "who": "Post Office Ltd y Fujitsu (organizaciones)", "place": "Reino Unido",
     "hook": "Un sistema contable con errores conocidos, sin función de disputa y usado como prueba contra los gestores de sucursales llevó a cientos de acusaciones injustas que los tribunales acabaron anulando."},
    {"slug": "equifax-2017", "kind": "fallo", "name": "Equifax 2017", "year": "2017",
     "who": "Equifax (organización)", "place": "Atlanta, Georgia (EE. UU.)",
     "hook": "Una vulnerabilidad conocida con parche disponible se quedó sin aplicar en un portal de disputas y expuso los datos personales de unos 148 millones de personas."},
    {"slug": "solarwinds-2020", "kind": "fallo", "name": "SolarWinds 2020", "year": "2020",
     "who": "SolarWinds (organización)", "place": "Estados Unidos",
     "hook": "Un atacante insertó código en las compilaciones de una herramienta de monitoreo y las actualizaciones firmadas llegaron a agencias federales y empresas."},
    {"slug": "cloudflare-2019", "kind": "fallo", "name": "Cloudflare 2019", "year": "2019",
     "who": "Cloudflare (organización)", "place": "San Francisco, California (EE. UU.)",
     "hook": "Una expresión regular de una regla del cortafuegos, desplegada a todo el mundo en segundos, agotó la CPU de la red y dejó sin servicio los dominios de Cloudflare durante 27 minutos."},
    {"slug": "aws-s3-2017", "kind": "fallo", "name": "Interrupción de Amazon S3 en 2017", "year": "2017",
     "who": "Amazon Web Services (organización)", "place": "Norte de Virginia (EE. UU.)",
     "hook": "Un comando con una entrada mal escrita retiró demasiada capacidad de los subsistemas de índice y ubicación de S3 y la región US-EAST-1 dejó de servir peticiones durante unas cuatro horas."},
]

GROUP_FILES = {"exito": "casos/exito/README.md", "fallo": "casos/fallo/README.md"}


NUMBER_WORDS = {8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce",
                15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte",
                21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro", 25: "veinticinco",
                26: "veintiséis", 27: "veintisiete", 28: "veintiocho", 29: "veintinueve", 30: "treinta",
                31: "treinta y uno", 32: "treinta y dos"}


def number_word(count: int) -> str:
    """Spanish word for a case count (digits above the table), so prose never hard-codes a count."""
    return NUMBER_WORDS.get(count, str(count))


def count_of(kind: str | None = None) -> int:
    return len([c for c in CASES if kind is None or c["kind"] == kind])


def names_phrase(kind: str) -> str:
    """'A, B y C' with the names of the cases of a kind, in registry order."""
    names = [c["name"] for c in cases_of(kind)]
    return ", ".join(names[:-1]) + " y " + names[-1]


def cases_of(kind: str) -> list[dict[str, str]]:
    return [case for case in CASES if case["kind"] == kind]


def case_path(case: dict[str, str]) -> str:
    return f"casos/{case['kind']}/{case['slug']}.md"
