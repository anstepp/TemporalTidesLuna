from re import search
from lxml import etree

from lejaren.notation import score as ljns

class LejarenHooks:

    def __init__(self):
        self.score_list = []

    # TODO: Add features here
    def create_output(self, input_dir, fname_list): # -> None or Bool on Success

        for fname in fname_list:
            if not isinstance(fname, str):
                raise TypeError(f"Not a filename, file is: {fname} instead")
            elif search(r'[a-zA-Z0-9]*\.musicxml', fname) == None:
                raise ValueError(f"Not a musicxml file: {fname}")
            else:
                temp_tree = etree.parse(input_dir+"/"+fname)
                temp_root = temp_tree.getroot()
                temp_score = ljns.Score(temp_tree)
                self.score_list.append([temp_score, fname])

    def write_output(self, output_dir): # -> None or Bool on Success

        for score in self.score_list:
            if not isinstance(score[0], ljns.Score):
                raise TypeError(f"Not a Score, file is: {type(score)} instead")
            else:
                score[0].convert_to_xml(output_dir+"/"+score[1])
        