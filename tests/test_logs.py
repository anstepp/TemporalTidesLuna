import pytest

import src.logs.logger as log

def test_log_creation():
    ttlog, ljlog = log.get_loggers()
    assert ttlog
    assert ljlog