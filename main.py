#!/usr/bin/env python3

try:
    from src.gui.gui import TemporalTidesLunaApp
except ImportError as e:
    print(f"GUI import failed, details: {e}, Quitting...")
    raise SystemExit(1)

app = TemporalTidesLunaApp()
app.mainloop()