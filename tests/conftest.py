import pytest
import tkinter as tk

from src.gui import TemporalTidesLunaApp

@pytest.fixture(scope="class")
def temporal_tides_app(request):
    """Create a hidden TK app instance for tests and ensure cleanup.

    The fixture withdraws the root window so no GUI appears, then
    instantiates the application class and yields it for tests. The
    root is destroyed at teardown.
    """
    # Prefer not to pass an existing Tk instance as parent because
    # TemporalTidesLunaApp calls `super().__init__(parent)` which expects
    # a screenName or None, not a Tk instance. Construct with `None` and
    # withdraw the resulting window so tests run headless.
    app = TemporalTidesLunaApp(None)
    try:
        app.withdraw()
    except Exception:
        pass

    def _teardown():
        try:
            app.destroy()
        except Exception:
            pass

    request.addfinalizer(_teardown)
    return app
