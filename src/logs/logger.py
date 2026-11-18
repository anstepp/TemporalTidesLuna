import logging
from typing import Iterable

from pathlib import Path

import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent
LOG_FILE = LOG_DIR / "temporaltides.log"

class AlwaysEnabledAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        self.logger.disabled = False
        return msg, kwargs

def _build_logger() -> AlwaysEnabledAdapter:
    raw_logger = logging.getLogger("TTLogger")
    raw_logger.setLevel(logging.DEBUG)
    raw_logger.disabled = False
    raw_logger.propagate = False

    if not raw_logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        raw_logger.addHandler(file_handler)

    return AlwaysEnabledAdapter(raw_logger, {})

logger = _build_logger()

