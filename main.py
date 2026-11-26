import os
from pathlib import Path

src = Path(__file__).parent / "entry.txt"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
data = src.read_bytes().rstrip(b"\r\n")
if not data:
    raise SystemExit("entry.txt is empty")
(out_dir / "entry.txt").write_bytes(data)
