import pytest

from pathlib import Path

from logging import Logger

import src.logs.logger as log

@pytest.fixture
def ttlog():
    ttlog, ljlog = log.get_loggers()
    return ttlog

@pytest.fixture
def ljlog():
    ttlog, ljlog = log.get_loggers()
    return ljlog

def test_log_creation(ttlog, ljlog):
    assert isinstance(ttlog, Logger)
    assert isinstance(ljlog, Logger)

def test_log_file_creation(ttlog, ljlog):
    assert Path("src/logs/temporaltides.log")
    assert Path("src/logs/lejaren.log")