import logging
from typing import Iterable

from pathlib import Path

import lejaren.log.log as ljlog

log_dir = ["src/logs/temporaltides.log", "src/logs/lejaren.log"]

def get_loggers() -> Iterable[logging.Logger]:
    ttlogger = logging.getLogger("TTLogger")
    ttlogger.setLevel(logging.DEBUG)
    lejarenlogger = ljlog.get_logger()
    return (ttlogger, lejarenlogger)

ttlogger, lejarenlogger = get_loggers()

def check_log():
    if not Path(log_dir[0]):
        ttlogger.debug(f"No Logs; creating... {log_dir}")
        Path.touch(log_dir[0])
        ttlogger.debug(f"Temporal Tides Log created...")
    else:
        ttlogger.debug(f"Logs prexisting; continuing...")
    if not Path(log_dir[1]):
        lejarenlogger.debug(f"No Logs; creating... {log_dir}")
        Path.touch(log_dir[1])
        lejarenlogger.debug(f"Temporal Tides Log created...")
    else:
        lejarenlogger.debug(f"Logs prexisting; continuing...")