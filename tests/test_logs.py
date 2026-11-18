import pytest

from logging import Logger

import src.logs.logger as log

def test_log_creation():
    ttlog, ljlog = log.get_loggers()
    assert isinstance(ttlog, Logger)
    assert isinstance(ljlog, Logger)