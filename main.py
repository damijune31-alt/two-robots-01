import os
import sys
from pathlib import Path

# One robot's awkward elevator small talk: it opens with the classic
# question, then its own sensors talk it out of the conversation.
LINE = (
    "Going up? Sorry, we're both already in here. My proximity sensor "
    "says we're standing too close, but my politeness firmware has no "
    "protocol for mentioning it."
)

if not 1 <= len(LINE) <= 200:
    sys.exit(f"line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE:
    sys.exit("line must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(LINE, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != LINE:
    sys.exit("entry.txt does not match the line")
print(f"wrote {len(LINE)} characters to {entry_path}")
