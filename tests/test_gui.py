import pytest

from gui.gui import TemporalTidesLunaApp

function_list = {
	"controller": ["check_result", "on_submit", "_get_grace_note_flag"],
	"model": [],
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

    def test_grace_notes(self, temporal_tides_app):
        assert temporal_tides_app.model._grace_note_flag == False
        assert temporal_tides_app.model._grace_note_gui_bool.get() == False
        temporal_tides_app.model._grace_note_gui_bool.set(True)
        assert temporal_tides_app.model._grace_note_gui_bool.get() == True
        temporal_tides_app.controller._get_grace_note_flag()
        assert temporal_tides_app.model._grace_note_flag == True