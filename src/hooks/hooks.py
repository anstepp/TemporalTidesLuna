from lejaren.notation import Note

class Hooks:

    def __init__(self):
        pass

    def remove_grace_notes(self):
        return Note(4,4,0)

    def remove_nested_tuplets(self):
        return True

    def split_hands(self):
        return True

    def combine_staves(self):
        return True

