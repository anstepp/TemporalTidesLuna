import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent
LOG_FILE = LOG_DIR / "temporaltides.log"


class FlushingFileHandler(logging.FileHandler):
    def emit(self, record: logging.LogRecord) -> None:
        super().emit(record)
        self.flush()


def _attach_file_handler(target_logger: logging.Logger) -> None:
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler = FlushingFileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    target_logger.addHandler(file_handler)


class AlwaysEnabledAdapter(logging.LoggerAdapter):
    def isEnabledFor(self, level: int) -> bool:
        self.logger.manager.disable = logging.NOTSET
        self.logger.disabled = False
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            _attach_file_handler(self.logger)
        return True

    def process(self, msg, kwargs):
        self.logger.disabled = False
        return msg, kwargs


def _build_logger() -> AlwaysEnabledAdapter:
    raw_logger = logging.getLogger("TTLogger")
    raw_logger.setLevel(logging.DEBUG)
    raw_logger.disabled = False
    raw_logger.propagate = False

    if not raw_logger.handlers:
        # Clear the log file only on initial handler creation
        LOG_FILE.write_text("", encoding="utf-8")
        _attach_file_handler(raw_logger)

    adapter = AlwaysEnabledAdapter(raw_logger, {})
    adapter.setLevel(logging.DEBUG)
    return adapter


logger = _build_logger()
