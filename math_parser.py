__author__ = 'jdemp'


class MathParser():

    def __init__(self):
        self.symbols = {'add': '+', 'plus': '+', 'minus':'-', 'subtract': '-', 'times': '*', 'divided': '/',
                        'mod':'%', 'equals': '='}

    def parser(self, equation):
        replaced = equation
        for i in range(0,len(replaced)):
            if replaced[i] in self.symbols:
                replaced[i] = self.symbols[replaced[i]]
        return replaced
