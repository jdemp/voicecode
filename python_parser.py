__author__ = 'jdemp'
import pickle
import translations
from math_parser import MathParser


def create_class(command):
    snippet = []
    snippet [0] = 'class '
    words = command.split()
    for w in words:
        snippet[0] += w.capitalize()
    snippet[0] += '():'
    snippet[1] = 'return'
    return snippet


def create_method(command):
    snippet = []
    snippet[0] = 'def '
    words = command.split
    for w in words:
        snippet[0] += w.lower() + '_'
    snippet[0] = snippet[0][:-1] + '():'
    snippet[1] = 'return'
    return snippet


def create_for(command):
    snippet = []
    snippet[0] = 'for '
    words = command.split()
    # create for loop


class PythonParser():

    def __init__(self):
        self.keywords = {'class': create_class,
                         'define': create_method,
                         'for': create_for,
                         'call': self.parse_call}
        self.math_parser = MathParser
        # make an sqlite db

    def parse(self, dictation):
        words = dictation.split(maxsplit=1)
        print(str(words))
        snippet = self.keywords[words[0].lower()](words[1])
        return snippet

    def find_keywords(self, command):
        pass

    def translate(self, command):
        pass

    def add_keyword(self, key, value):
        self.keywords[key] = value

    def edit_keywords(self):
        pass

    def save_keywords(self):
        file = 'python_keywords.p'
        pickle.dump(self.keywords,open(file, "wb"))

    def edit_translations(self):
        pass

    def save_translations(self):
        file = 'python_translations.p'
        pickle.dump(self.keywords,open(file, "wb"))