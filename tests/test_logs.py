import pytest

from pathlib import Path

from logging import Logger, LoggerAdapter

from src.logs.logger import logger

def test_log_creation():
    assert isinstance(logger, LoggerAdapter)


def test_log_file_creation():
    assert Path("src/logs/temporaltides.log")
