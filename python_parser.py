__author__ = 'jdemp'
import pickle
from keywords import Keywords
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
        self.keywords = Keywords("python")
        self.math_parser = MathParser

    def parse(self, dictation):
        words = dictation.split()
        # print(str(words))
        if self.keywords.is_keyword(words[0]):
            parser = "create_" + words[0]
            return getattr(self, parser)(words[1:])
        else:
            return [False]

    def create_class(self, words):
        snippets = ["","",""]
        snippets[0] = 'class '
        for w in words:
            snippets[0] += w.capitalize()
        snippets[0] += '():'
        snippets[1] = 'nl'
        return snippets

    def create_function(self, words):
        snippets = ["","",""]
        snippets[0] = 'def '
        for w in words:
            snippets[0] += w.lower() + '_'
        snippets[0] = snippets[0][:-1] + '():'
        snippets[1] = 'nl'
        return snippets


    def create_loop(self, words):
        snippets = ["","",""]
        print(words)
        snippets[0] = 'for ' + words[0] + ' in range( ' + words[2] + ', '
        stop = int(words[4]) + 1
        snippets[0] += str(stop) + '):'
        snippets[1] = 'nl'
        return snippets


