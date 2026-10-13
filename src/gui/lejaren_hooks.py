from re import search
from lxml import etree

from lejaren.notation import score as ljns

class LejarenHooks:

    def __init__(self):
        pass

    # TODO: Add features here
    def create_output(self, input_dir, fname_list): # -> None or Bool on Success

        for fname in fname_list:
            if not isinstance(fname, str):
                raise TypeError(f"Not a filename, file is: {fname} instead")
            elif search(r'[a-zA-Z0-9]*\.musicxml', fname) == None:
                raise ValueError(f"Not a musicxml file: {fname}")
            else:
                temp_tree = etree.parse(input_dir+"/"+fname)
                temp_root = etree.getroot()
                ljns.Score(temp_tree)
                print("Yay")

        