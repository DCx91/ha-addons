import py_compile
import re
import pathlib
from pathlib import Path

# Adjust these after checking the real layout (see the find command below).
APP = Path("app/app.py")
UTIL = Path("app/skill/util.py")

# --- 1. Restrict the login-URL regexes in app.py ---------------------------
s = APP.read_text()
old = r'''(https?://[^\s'\"]+)'''
new = r'''(https://www\.amazon\.com/ap/oa[^\s'\"]+)'''
assert s.count(old) == 2, f"app.py: expected 2 matches, found {s.count(old)}"
APP.write_text(s.replace(old, new))

# --- 2. Send AudioItemMetadata for non-APL devices -------------
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
