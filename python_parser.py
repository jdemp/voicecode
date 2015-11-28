from keywords import Keywords
from math_parser import MathParser
import helper


def format_variable(words):
    formated = ""
    for w in words:
        formated += w + '_'
    return formated[:-1]


class PythonParser():

    def __init__(self):
        self.keywords = Keywords("python")
        self.math_parser = MathParser()

    def parse(self, dictation):
        words = dictation.split()
        # print(str(words))
        if self.keywords.is_keyword(words[0]):
            parser = "create_" + words[0]
            return getattr(self, parser)(words[1:])
        else:
            return ["Bad command"]

    def create_class(self, words):
        snippets = [""]
        snippets[0] = 'class '
        for w in words:
            snippets[0] += w.capitalize()
        snippets[0] += '():'
        snippets.append("nl")
        return snippets

    def create_function(self, words):
        snippets = [""]
        snippets[0] = 'def '
        for w in words:
            snippets[0] += w.lower() + '_'
        snippets[0] = snippets[0][:-1] + '():'
        snippets.append("nl")
        return snippets

    def create_define(self, words):
        return self.create_function(words)

    def create_for(self, words):
        snippets = [""]
        # X from start to end
        if words[1] == 'from':
            snippets[0] = 'for ' + words[0] + ' in range( ' + words[2] + ', '
            stop = int(words[4]) + 1
            snippets[0] += str(stop) + '):'
        # X in List
        elif words[1] == 'in':
            snippets[0] = 'for ' + words[0] + ' in ' + format_variable(words[2:]) + ':'
        else:
            snippets[0] = 'for '
        snippets.append("nl")
        return snippets

    def create_while(self, words):
        snippets = [""]
        if words[0] == 'call':
            pass
        else:
            # used process later
            snippets[0] = 'while ' + format_variable(words) + ':'
        snippets.append('nl')
        return snippets

    def create_if(self, words):
        snippets = ["if "]
        processed = self.process_conditional(helper.convert_to_string(words))
        snippets[0] += processed + ':'
        snippets.append('nl')
        return snippets

    def create_elif(self, words):
        snippets = ["elif "]
        processed = self.process_conditional(helper.convert_to_string(words))
        snippets[0] += processed + ':'
        snippets.append('nl')
        return snippets

    def create_else(self, words):
        snippets = ["else:", "nl"]
        return snippets

    def create_return(self, words):
        snippets = [""]
        if words[0] == 'variable':
            snippets[0] = format_variable(words[1:])
        else:
            snippets[0] = helper.convert_to_string(words)
        snippets.append('nl')
        return snippets

    def create_print(self, words):
        snippets = [""]
        length = len(words)
        print(str(words))
        if words[0] == 'variable' and length > 1:
            snippets[0] = 'print(str(' + format_variable(words[1:]) + '))'
            snippets.append('nl')
        else:
            pass
            # snippets[0] = "print('" + convert_to_string(words) + "')"
        return snippets

    def create_variable(self, words):
        snippets = [""]
        if len(words) < 2:
            snippets[0] = words[0] + ' = '
        elif words[1] == 'array':
            snippets[0] = words[0] + ' = []'
        elif words[1] == 'dictionary':
            snippets[0] = words[0] + ' = {}'
        elif words[1] == 'call':
            snippets[0] = words[0] + ' = ' + self.create_call(words[2:])[0]
        elif words[1] == 'integer':
            snippets[0] = words[0] + ' = ' + words[2]
        else:
            snippets[0] = words[0] + ' = ' + helper.convert_to_string(words[1:])
        return snippets

    def create_math(self, words):
        replaced = self.math_parser.parser(words)
        snippet = [helper.convert_to_string(replaced), 'nl']
        return snippet

    def create_call(self, words):
        snippet = [""]

        return snippet

    def process_conditional(self, words):
        replaced = words
        for i in range(0,len(Keywords.conditional_keyword_list)):
            if Keywords.conditional_keyword_list[i] in replaced:
                replaced = replaced.replace(Keywords.conditional_keyword_list[i], Keywords.conditional_replacement_list[i])
        return replaced




