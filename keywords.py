__author__ = 'jdemp'


class Keywords():

    def __init__(self, language):
        self.keyword_set = {'class', 'function', 'loop', 'while', 'if', 'elif', 'else', 'receives', 'equals', 'define'}
        self.conditional_keyword_set = {'less than', 'greater than', 'equal to', 'less than or equal to',
                                         'greater than or equal to'}

    def setup_python(self):
        pass

    def setup_matlab(self):
        pass

    def is_keyword(self, word):
        return word in self.keyword_set

    def get_keywords(self, dictation):
        positions = []
        return positions

    def replace_math_keywords(self, dictation):
        replaced_dictation = ""