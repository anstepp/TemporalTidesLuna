import pytest

from src.gui import TemporalTidesLunaApp

function_list = {
	"controller": ["check_result", "on_submit", "button_check", "get_short_rest_bool", "get_replace_rests_bool", "get_simplify_tuplets_bool"],
	"model": ["on_start"],
	"view": ["_show_display"],
	}

class TestTemporalTidesLunaApp:

	def test_app_instantiated(self, temporal_tides_app):
		"""Fixture provides a hidden app instance."""
		assert isinstance(temporal_tides_app, TemporalTidesLunaApp)

	def test_methods_present(self, temporal_tides_app):
		# Ensure common member methods exist so grouped tests can call them
		for part, functions in function_list.items():
			assert hasattr(temporal_tides_app, part)
			sub_class = getattr(temporal_tides_app, part)
			for function in functions:			
				assert hasattr(sub_class, function)

	def test_on_start(self, temporal_tides_app):
		temporal_tides_app.model.replace_rests.set(True)
		temporal_tides_app.model.remove_short_rests.set(True)
		temporal_tides_app.model.simplify_tuplets.set(True)
		assert temporal_tides_app.model.on_start(temporal_tides_app.controller)

	def test_get_short_rest_bool(self, temporal_tides_app):
		temporal_tides_app.model.remove_short_rests.set(True)
		assert temporal_tides_app.controller.get_short_rest_bool(temporal_tides_app.model)
		temporal_tides_app.model.remove_short_rests.set(False)
		assert False == temporal_tides_app.controller.get_short_rest_bool(temporal_tides_app.model)

	def test_get_replace_rests_bool(self, temporal_tides_app):
		temporal_tides_app.model.replace_rests.set(True)
		assert temporal_tides_app.controller.get_replace_rests_bool(temporal_tides_app.model)

	def test_get_simplify_tuplets_bool(self, temporal_tides_app):
		temporal_tides_app.model.simplify_tuplets.set(True)
		assert temporal_tides_app.controller.get_simplify_tuplets_bool(temporal_tides_app.model)
		

