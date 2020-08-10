# -*- coding: utf-8 -*-

import glob
import os
from orbis_eval.core import app
from pathlib import Path

import logging
logger = logging.getLogger(__name__)


class Main(object):

    def __init__(self, rucksack, path=None):
        super(Main, self).__init__()
        self.rucksack = rucksack
        if not path:
            self.corpus_path = Path(self.rucksack.open['config']['corpus_path'])
        else:
            self.corpus_path = path

    def run(self):
        corpus = {}
        for file in self.corpus_path.glob('*.txt'):
            try:
                file_number = file.stem
                with open(file, encoding="utf-8") as open_file:
                    corpus[file_number] = open_file.read()
            except Exception as exception:
                logger.error(f"Corpus file empty: {file} ({exception})")
        return corpus
