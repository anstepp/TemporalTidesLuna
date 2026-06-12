import pytest

from src.gui import TemporalTidesLunaApp

function_list = ["check_result", "on_submit"]

class TestTemporalTidesLunaApp:

	def test_app_instantiated(self, temporal_tides_app):
		"""Fixture provides a hidden app instance."""
		assert isinstance(temporal_tides_app, TemporalTidesLunaApp)

	def test_methods_present(self, temporal_tides_app):
		# Ensure common member methods exist so grouped tests can call them
		for function_to_check in function_list:
			assert hasattr(temporal_tides_app, function_to_check)

