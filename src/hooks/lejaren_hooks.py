from re import search
from lxml import etree

from src.logs.logger import logger

try:
    from lejaren.notation import score as ljns
except ImportError as e:
    logger.critical(f"Hooks failed import, details: {e}, quitting...")
    raise SystemExit(1)
else:
    logger.debug("Hooks import success...")

class LejarenHooks:

    def __init__(self):
        logger.debug("Hooks init...")
        self.score_list = []

    # TODO: Add features here
    def create_output(self, input_dir, fname_list): # -> None or Bool on Success
        logger.debug(f"Hooks, Create Output, reading: {input_dir}, files: {fname_list}")
        for fname in fname_list:
            logger.debug(f"Hooks, Create Output, processing: {fname}")
            if not isinstance(fname, str):
                logger.warning(f"Hooks, Create Output, {fname} bad type, {type(fname)}")
                raise TypeError(f"Not a filename, file is: {fname} instead")
            elif search(r'[a-zA-Z0-9]*\.(musicxml|mxml|xml)', fname) == None:
                logger.warning(f"Hooks, Create Output, {fname} bad suffix, {fname[:-4]}")
                raise ValueError(f"Not a musicxml file: {fname}")
            else:
                logger.debug(f"Parsing {fname}...")
                temp_tree = etree.parse(input_dir+"/"+fname)
                temp_root = temp_tree.getroot()
                temp_score = ljns.Score(temp_tree)
                self.score_list.append([temp_score, fname])

    def write_output(self, output_dir): # -> None or Bool on Success

        logger.debug(f"Hooks, Write Output... {output_dir}")

        for score in self.score_list:
            logger.debug(f"Writing, score being processed: {score}")
            if not isinstance(score[0], ljns.Score):
                logger.warning(f"Score file non-existent in hooks, {score}, {type(score)}, failure likely...")
                raise TypeError(f"Not a Score, file is: {type(score)} instead")
            else:
                logger.debug(f"Success on score, {score} likely writing to file...")
                score[0].convert_to_xml(output_dir+"/"+score[1])
        