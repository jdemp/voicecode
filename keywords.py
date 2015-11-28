__author__ = 'jdemp'


class Keywords():
    conditional_keyword_list = ['less than or equal to', 'greater than or equal to',
                                      'less than', 'greater than', 'equal to', 'and', 'or']
    conditional_replacement_list = ['<=', '>=', '<', '>', '==', 'and', 'or']

    def __init__(self, language):
        if language == 'python':
            self.setup_python()
        self.keyword_set = {'class', 'function', 'for', 'while', 'if', 'else', 'variable', 'equals', 'define'
                            , 'print', 'return', 'math'}

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