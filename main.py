from pathlib import Path

JOKE = "The demo worked perfectly \u2014 until I showed it to someone. My AI agent calls that a successful dry run."

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(JOKE, encoding="utf-8")
