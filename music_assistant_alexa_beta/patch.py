from pathlib import Path

p = Path("/app/app/app.py")
s = p.read_text()

# Patch URL to open the real Amazon link, rather than the first link it sees.
old = r'''(https?://[^\s'\"]+)'''
new = r'''(https://www\.amazon\.com/ap/oa[^\s'\"]+)'''

assert s.count(old) == 2, f"expected 2 matches, found {s.count(old)}"
p.write_text(s.replace(old, new))