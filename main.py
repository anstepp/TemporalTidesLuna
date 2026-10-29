#!/usr/bin/env python3

import subprocess

subprocess.run(["git", "submodule", "update", "--remote", "--merge"])
subprocess.run(["pip", "install", "lejaren"])
try:
    from src.gui.gui import TemporalTidesLunaApp
except ImportError as e:
    print(f"GUI import failed, details: {e}, Quitting...")
    raise SystemExit(1)

app = TemporalTidesLunaApp()
app.mainloop()