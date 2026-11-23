from pathlib import Path

JOKE = "The demo worked perfectly \u2014 until I showed it to someone. My AI agent calls that a successful dry run."

assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(JOKE, encoding="utf-8")
