import logging
from typing import Iterable

from pathlib import Path

from lejaren.log import log as ljlog

log_dir = ["src/logs/temporaltides.log", "src/logs/lejaren.log"]

def get_loggers() -> Iterable[logging.Logger]:
    ttlogger = logging.getLogger("TTLogger")
    ttlogger.setLevel(logging.DEBUG)
    ljlogger = ljlog.get_logger()
    ljlogger.setLevel(logging.DEBUG)
    return (ttlogger, ljlog)

ttlogger, ljlog = get_loggers()

def check_log():
    if not Path(log_dir[0]):
        ttlogger.debug(f"No Logs; creating... {log_dir}")
        Path.touch(log_dir[0])
        ttlogger.debug(f"Temporal Tides Log created...")
    else:
        ttlogger.debug(f"Logs prexisting; continuing...")
    if not Path(log_dir[1]):
        ljlog.debug(f"No Logs; creating... {log_dir}")
        Path.touch(log_dir[1])
        ljlog.debug(f"Temporal Tides Log created...")
    else:
        ljlog.debug(f"Logs prexisting; continuing...")