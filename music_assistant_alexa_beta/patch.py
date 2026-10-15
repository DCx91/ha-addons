import py_compile
import re
import pathlib
from pathlib import Path

APP = Path("app/app.py")
UTIL = Path("app/skill/util.py")

# --- 1. Restrict the login-URL regexes in app.py ---
s = APP.read_text()
old = r'''(https?://[^\s'\"]+)'''
new = r'''(https://www\.amazon\.com/ap/oa[^\s'\"]+)'''
assert s.count(old) == 2, f"app.py: expected 2 matches, found {s.count(old)}"
APP.write_text(s.replace(old, new))

# --- 2. Send AudioItemMetadata for non-APL devices ---
s = UTIL.read_text()

for name in ("AudioItemMetadata", "replace_ip_in_url", "import logging"):
    assert name in s, f"util.py: expected to find {name!r}"

pattern = re.compile(
    r"^(?P<outer>[ \t]*)audio_item=AudioItem\(\n(?P<inner>[ \t]*)stream=Stream\(",
    re.M,
)

head, sep, tail = s.partition("\ndef play_later(")
assert sep, "util.py: def play_later( not found"
assert len(pattern.findall(head)) == 1, (
    f"util.py: expected 1 AudioItem anchor in play(), found {len(pattern.findall(head))}"
)
head = pattern.sub(
    lambda m: (
        f"{m['outer']}audio_item=AudioItem(\n"
        f"{m['inner']}metadata=_build_metadata(hostname),\n"
        f"{m['inner']}stream=Stream("
    ),
    head,
)
s = head + sep + tail

s += '''

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
UTIL.write_text(s)
py_compile.compile(str(UTIL), doraise=True)  # fail the build on a syntax error

# --- 3. Tidy logs ---

s = APP.read_text()

pattern = re.compile(
    r"^([ \t]*)app\.logger\.info\('Functional ASK credentials found; suppressing auth UI'\)[ \t]*$",
    re.M,
)

def repl(m):
    i = m.group(1)
    return (
        f"{i}if not getattr(app, '_ask_creds_logged', False):\n"
        f"{i}    app._ask_creds_logged = True\n"
        f"{i}    app.logger.info('Functional ASK credentials found; suppressing auth UI')"
    )

s, n = pattern.subn(repl, s)
assert n == 1, f"expected 1 match for ASK creds log line, got {n}"
APP.write_text(s)

py_compile.compile(str(APP), doraise=True)

# --- 4. Fix cryptography deprecation warning ---

matches = list(Path("/app").rglob("ask_sdk_webservice_support/verifier.py"))
assert len(matches) == 1, f"Expected 1 verifier.py, found {len(matches)}: {matches}"

VERIFIER = matches[0]
s = VERIFIER.read_text()

s, n = re.subn(r"x509_cert\.not_valid_(before|after)\b", r"x509_cert.not_valid_\1_utc", s)
assert n >= 2, f"Expected at least 2 deprecated references, found {n}"

head, sep, tail = s.partition("def _validate_end_certificate")
assert sep, "_validate_end_certificate not found"
body, sep2, rest = tail.partition("\n    def ")

NOW_OLD = "datetime.utcnow()"
assert body.count(NOW_OLD) == 1, f"Expected 1 utcnow() in that function, found {body.count(NOW_OLD)}"
body = body.replace(NOW_OLD, "datetime.now(__import__('datetime').timezone.utc)")

VERIFIER.write_text(head + sep + body + sep2 + rest)
py_compile.compile(str(VERIFIER), doraise=True)

# --- 5. Persist the skill ID to /data/skill_id ---

matches = list(Path("/app").rglob("ask_create_skill.sh"))
assert len(matches) == 1, (
    f"Expected 1 ask_create_skill.sh, found {len(matches)}: {matches}"
)

ASK_SCRIPT = matches[0]
s = ASK_SCRIPT.read_text()

if "/data/skill_id" not in s:
    SNIPPET = '''
# Persist the skill ID so the add-on can load it on later starts
case "$SKILL_ID" in
  amzn1.ask.skill.*) printf '%s' "$SKILL_ID" > /data/skill_id || echo "WARNING: could not write /data/skill_id" >&2 ;;
esac
'''
    pattern = re.compile(
        r'(echo "Rebuilt existing skill: \$SKILL_ID"[ \t]*\n[ \t]*fi[ \t]*(?:\n|$))'
    )
    assert len(pattern.findall(s)) == 1, (
        f"ask_create_skill.sh: expected 1 anchor, found {len(pattern.findall(s))}"
    )
    s = pattern.sub(lambda m: m.group(1) + SNIPPET, s, count=1)
    ASK_SCRIPT.write_text(s)
