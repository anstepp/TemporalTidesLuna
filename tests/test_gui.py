import pytest

from src.gui import TemporalTidesLunaApp


class TestTemporalTidesLunaApp:

	def test_app_instantiated(self, temporal_tides_app):
		"""Fixture provides a hidden app instance."""
		assert isinstance(temporal_tides_app, TemporalTidesLunaApp)

	def test_methods_present(self, temporal_tides_app):
		# Ensure common member methods exist so grouped tests can call them
		assert hasattr(temporal_tides_app, "check_result") or hasattr(temporal_tides_app, "on_submit")


