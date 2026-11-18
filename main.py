#!/usr/bin/env python3

import sys
import subprocess
from importlib.metadata import version

from src.logs.logger import logger


def is_venv_active() -> bool:
    return sys.prefix != sys.base_prefix

if is_venv_active():
    logger.debug("Running inside a virtual environment.")
else:
    subprocess.run(["source", ".venv/bin/activate"])
    logger.debug("Activated venv")

subprocess.run(["git", "submodule", "update", "--remote", "--merge"])
logger.debug("Grab latest Lejaren...")
subprocess.run(["pip", "install", "./lejaren"])
logger.debug("Install latest Lejaren...")
logger.debug(f"Lejaren version: {version("lejaren")}")

try:
    from src.gui.gui import TemporalTidesLunaApp
except ImportError as e:
    logger.critical(f"GUI import failed, details: {e}, Quitting...")
    raise SystemExit(1)

app = TemporalTidesLunaApp()
app.mainloop()