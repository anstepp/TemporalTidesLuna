import pytest

from hooks.hooks import Hooks

from lejaren.notation import Note

all_hooks = ["remove_grace_notes", 
             "remove_nested_tuplets", 
             "split_hands", 
             "combine_staves"
             ]

@pytest.fixture
def make_hooks():
    hooks = Hooks()
    return hooks

def test_hooks_exist(make_hooks):
    for method in all_hooks:
        assert hasattr(make_hooks, method)

def test_remove_grace_notes(make_hooks):
    assert isinstance(make_hooks.remove_grace_notes(), Note)

def test_remove_nested_tuplets(make_hooks):
    assert make_hooks.remove_nested_tuplets()

def test_split_hands(make_hooks):
    assert make_hooks.split_hands()

def test_combine_staves(make_hooks):
    assert make_hooks.combine_staves()
