import py_compile
import re
from pathlib import Path

APP = Path("app/app.py")
UTIL = Path("app/skill/util.py")

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def write(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")

def replace_exact(s, old, new, expected, label):
    n = s.count(old)
    assert n == expected, f"{label}: expected {expected} match(es), found {n}"
    return s.replace(old, new)

def sub_exact(s, pattern, repl, label, expected=1, flags=0):
    s, n = re.subn(pattern, repl, s, flags=flags)
    assert n == expected, f"{label}: expected {expected} match(es), found {n}"
    return s

def find_one(root, name):
    matches = list(Path(root).rglob(name))
    assert len(matches) == 1, f"Expected 1 {name}, found {len(matches)}: {matches}"
    return matches[0]

METADATA_HELPER = '''

def _build_metadata(hostname):
    info = data.info
    art = None
    image_url = info.get("coverImageSource") or ""
    if image_url:
        image_url = replace_ip_in_url(image_url, hostname)
        if image_url.startswith("https://"):
            from ask_sdk_model.interfaces.display import Image as DisplayImage, ImageInstance
            art = DisplayImage(sources=[ImageInstance(url=image_url)])
    try:
        return AudioItemMetadata(
            title=info.get("primaryText") or None,
            subtitle=info.get("secondaryText") or None,
            art=art,
            background_image=art,
        )
    except Exception:
        logging.exception("Failed to build audio metadata")
        return None
'''

ASK_CREDS_LOG = re.compile(
    r"^([ \t]*)app\.logger\.info\('Functional ASK credentials found; suppressing auth UI'\)[ \t]*$",
    re.M,
)

SKILL_ID_SNIPPET = '''
case "$SKILL_ID" in
  amzn1.ask.skill.*) printf '%s' "$SKILL_ID" > /data/skill_id || echo "WARNING: could not write /data/skill_id" >&2 ;;
esac
'''

# --- app.py: Restrict login-URL regexes, only log the ASK-creds line once ---
app = read(APP)
app = replace_exact(
    app,
    r'''(https?://[^\s'\"]+)''',
    r'''(https://www\.amazon\.com/ap/oa[^\s'\"]+)''',
    expected=2, label="app.py login-URL regex",
)
app = sub_exact(
    app, ASK_CREDS_LOG,
    lambda m: (
        f"{m[1]}if not getattr(app, '_ask_creds_logged', False):\n"
        f"{m[1]}    app._ask_creds_logged = True\n"
        f"{m[1]}    app.logger.info('Functional ASK credentials found; suppressing auth UI')"
    ),
    label="ASK creds log line",
)
write(APP, app)
py_compile.compile(str(APP), doraise=True)

# --- util.py: Send AudioItemMetadata ---
util = read(UTIL)
for name in ("AudioItemMetadata", "replace_ip_in_url", "import logging", "data", "hostname"):
    assert name in util, f"util.py: expected to find {name!r}"

head, sep, tail = util.partition("\ndef play_later(")
assert sep, "util.py: def play_later( not found"
head = sub_exact(
    head,
    r"^(?P<outer>[ \t]*)audio_item=AudioItem\(\n(?P<inner>[ \t]*)stream=Stream\(",
    lambda m: (
        f"{m['outer']}audio_item=AudioItem(\n"
        f"{m['inner']}metadata=_build_metadata(hostname),\n"
        f"{m['inner']}stream=Stream("
    ),
    label="AudioItem anchor in play()", flags=re.M,
)
write(UTIL, head + sep + tail + METADATA_HELPER)
py_compile.compile(str(UTIL), doraise=True)

# --- Cryptography deprecation fixes in the ASK SDK verifier ---
VERIFIER = find_one("/app", "ask_sdk_webservice_support/verifier.py")
v = read(VERIFIER)
v = sub_exact(
    v, r"x509_cert\.not_valid_(before|after)\b", r"x509_cert.not_valid_\1_utc",
    label="deprecated not_valid_*", expected=2,
) if len(re.findall(r"x509_cert\.not_valid_(?:before|after)\b", v)) == 2 else \
    sub_exact(v, r"x509_cert\.not_valid_(before|after)\b",
              r"x509_cert.not_valid_\1_utc", label="deprecated not_valid_*",
              expected=len(re.findall(r"x509_cert\.not_valid_(?:before|after)\b", v)))

head, sep, tail = v.partition("def _validate_end_certificate")
assert sep, "_validate_end_certificate not found"
body, sep2, rest = tail.partition("\n    def ")
body = replace_exact(
    body, "datetime.utcnow()",
    "datetime.now(__import__('datetime').timezone.utc)",
    expected=1, label="utcnow() in _validate_end_certificate",
)
write(VERIFIER, head + sep + body + sep2 + rest)
py_compile.compile(str(VERIFIER), doraise=True)

# --- Persist skill ID to /data/skill_id ---
ASK_SCRIPT = find_one("/app", "ask_create_skill.sh")
sh = read(ASK_SCRIPT)
if "/data/skill_id" not in sh:
    sh = sub_exact(
        sh,
        r'(echo "Rebuilt existing skill: \$SKILL_ID"[ \t]*\n[ \t]*fi[ \t]*(?:\n|$))',
        lambda m: m.group(1) + SKILL_ID_SNIPPET,
        label="ask_create_skill.sh anchor",
    )
    write(ASK_SCRIPT, sh)
