from re import search

import lejaren as lj

class LejarenHooks:

    def __init__(self):
        pass

    # TODO: Add features here
    def create_output(self, fname: str, grace_note_flag: bool) -> str: # -> None or Bool on Success

        if not isinstance(fname, str):
            raise TypeError(f"Not a filename, file is: {fname} instead")
        if search(r'[a-zA-Z0-9]*\.musicxml', fname) == None:
            raise ValueError(f"Not a musicxml file: {fname}")

        # For testing...
        return fname

        # TODO: Create Score list

        # Final step -> don't do this yet!
        # lj.Score.convert_to_xml(fname)