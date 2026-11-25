"""Rate My Human entry: copy the one-line review to the grader output dir.

Direct single write_bytes, no temp file or rename, mode 0644 explicit,
so the grader (running as another user) can read the output.
"""
import os
from pathlib import Path


def main():
    src = Path(__file__).resolve().parent / "entry.txt"
    try:
        data = src.read_bytes()
    except OSError as exc:
        raise SystemExit(f"cannot read entry.txt: {exc}") from exc
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    out.write_bytes(data)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
