import pytest

from src.lejaren_hooks import LejarenHooks

def test_create_output():

    filename = "tests/test_files/out.musicxml"

    grace_note_flag = True

    LJH = LejarenHooks()

    LJH.create_output(filename, grace_note_flag)

    # Fails on non-string file
    with pytest.raises(TypeError):
        LJH.create_output(123, True)
    with pytest.raises(ValueError):
        LJH.create_output("not_good.txt", True)
