__author__ = 'jdemp'

class PythonParser():
    translations = {}

    def __init__(self):
        self.keywords = {'class': self.create_class, 'define': self.create_method()}

    def parse(self, cmd):
        words = cmd.split(maxsplit=1)
        print(str(words))
        snippet = self.keywords[words[0].lower()](words[1])
        return snippet

    def create_class(self, cmd):
        snippet = 'class '
        words = cmd.split()
        for w in words:
            snippet += w.capitalize()
        snippet += '():'
        print(snippet)
        return snippet

    def create_method(self):
        pass
