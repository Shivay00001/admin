# Admin — ERP Key Generator

Built by [VisionQuantech](https://visionquantech.com) — AI agents, apps & tools for small businesses.

Desktop GUI app (tkinter). Generates license keys for the Indian SMB ERP product (admin tool — not for end users).

## Run

```bash
python key_gen_ui.py
```

Requires Python 3.10+ with tkinter (standard on Windows; on Linux install `python3-tk`). Verified boot on Python 3.12 (Linux, xvfb, 2026-09-24) — window initializes with no errors.

Not a web/cloud app: it is a desktop tool. Package with PyInstaller for distribution.