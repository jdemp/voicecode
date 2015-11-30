from keywords import Keywords
from math_parser import MathParser
import helper


def format_variable(words):
    formated = ""
    for w in words:
        formated += w + '_'
    return formated[:-1]


def format_class(words):
    formated = ""
    for w in words:
        formated += w.capitalize()
    return formated


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
        snippet = ['class ']
        start_index_v = helper.find_next_index({'base'}, words)
        if start_index_v == -1:
            snippet[0] += format_class(words) + '():'
        else:
            snippet[0] += format_class(words[0:start_index_v]) + '('
            while True:
                next_index_v = helper.find_next_index({'base'}, words, start_index_v)
                if next_index_v == -1:
                    snippet[0] += format_class(words[start_index_v+1:]) + '):'
                    break
                else:
                    snippet[0] += format_class(words[start_index_v+1:next_index_v]) + ', '
                start_index_v = next_index_v
        return snippet

    def create_function(self, words):
        snippets = [""]
        snippets[0] = 'def '
        start_index_v = helper.find_next_index({'variable'}, words)
        if start_index_v == -1:
            for w in words:
                snippets[0] += w.lower() + '_'
            snippets[0] = snippets[0][:-1] + '():'
        else:
            snippets[0] += format_variable(words[0:start_index_v]) + '('
            while True:
                next_index_v = helper.find_next_index({'variable'}, words, start_index_v)
                if next_index_v == -1:
                    snippets[0] += format_variable(words[start_index_v+1:]) + '):'
                    break
                else:
                    snippets[0] += format_variable(words[start_index_v+1:next_index_v]) + ', '
                start_index_v = next_index_v
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
        return snippets

    def create_while(self, words):
        snippets = [""]
        if words[0] == 'call':
            snippets[0] = 'while'+ self.create_call(words[1:])[0] + ':'
        elif words[0] == 'variable':
            snippets[0] = 'while ' + format_variable(words) + ':'
        else:
            # used process later
            snippets[0] = 'while ' + self.process_conditional_math(helper.convert_to_string(words)) + ':'
        return snippets

    def create_if(self, words):
        snippets = ["if "]
        processed = self.process_conditional_math(helper.convert_to_string(words))
        snippets[0] += processed + ':'
        return snippets

    def create_elif(self, words):
        snippets = ["elif "]
        processed = self.process_conditional_math(helper.convert_to_string(words))
        snippets[0] += processed + ':'
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
        return snippets

    def create_print(self, words):
        snippets = [""]
        length = len(words)
        print(str(words))
        if words[0] == 'variable' and length > 1:
            snippets[0] = 'print(str(' + format_variable(words[1:]) + '))'
        else:
            pass
            #  is that right up to the limitationsnippets[0] = 'print(str({0}))'.format(helper.convert_to_string(words))
        return snippets

    def create_variable(self, words):
        snippets = [""]

        index_type = helper.find_next_index({'array', 'dictionary', 'set', 'call', 'integer', 'string', 'equals'}, words)

        if index_type > 0:
            if words[index_type] == 'array':
                snippets[0] = format_variable(words[0:index_type]) + ' = []'
            elif words[index_type] == 'dictionary' or words[index_type] == 'set':
                snippets[0] = format_variable(words[0:index_type]) + ' = {}'
            elif words[index_type] == 'call':
                snippets[0] = format_variable(words[0:index_type]) + ' = ' + self.create_call(words[index_type+1:])[0]
            elif words[index_type] == 'integer':
                snippets[0] = format_variable(words[0:index_type]) + ' = ' + helper.verify_number(words[index_type+1])
            elif words[index_type] == 'string':
                snippets[0] = format_variable(words[0:index_type]) + ' = "' + helper.convert_to_string(words[index_type+1:]) + '"'
            elif words[index_type] == 'equals':
                snippets[0] = format_variable(words[0:index_type]) + ' = ' + self.process_conditional_math(helper.convert_to_string(words[index_type+1:]))
            else:
                snippets[0] = format_variable(words[0:index_type]) + ' = '
        else:
            snippets[0] = format_variable(words) + ' = '
        return snippets

    def create_call(self, words):
        snippets = [""]
        start_index_arg = -1
        start_index_sub = helper.find_next_index({'sub', 'period', 'function', 'class'}, words)
        #print(str(start_index_sub))
        if start_index_sub == -1:
            start_index_arg = helper.find_next_index({'variable', 'arg', 'argument'}, words)
            if start_index_arg == -1:
                snippets[0] += format_variable(words)
            else:
                snippets[0] += format_variable(words[0:start_index_arg])
        elif start_index_sub == 0:
            while True:
                next_index_sub = helper.find_next_index({'sub', 'period', 'class', 'function'}, words, start_index_sub)
                if next_index_sub == -1:
                    start_index_arg = helper.find_next_index({'variable', 'arg', 'argument'}, words)
                    if start_index_arg == -1:
                        if words[start_index_sub] == 'class':
                            snippets[0] += format_class(words[start_index_sub+1:])
                        else:
                            snippets[0] += format_variable(words[start_index_sub+1:])
                    else:
                        if words[start_index_sub] == 'class':
                            snippets[0] += format_class(words[start_index_sub+1:start_index_arg])
                        else:
                            snippets[0] += format_variable(words[start_index_sub+1:start_index_arg])
                    break
                else:
                    if words[start_index_sub] == 'class':
                        snippets[0] += format_class(words[start_index_sub+1:next_index_sub]) + '.'
                    else:
                        snippets[0] += format_variable(words[start_index_sub+1:next_index_sub]) + '.'
                start_index_sub = next_index_sub
        else:
            snippets[0] += format_variable(words[0:start_index_sub]) + '.'
            while True:
                next_index_sub = helper.find_next_index({'sub', 'period', 'class', 'function'}, words, start_index_sub)
                if next_index_sub == -1:
                    start_index_arg = helper.find_next_index({'variable', 'arg', 'argument'}, words)
                    if start_index_arg == -1:
                        if words[start_index_sub] == 'class':
                            snippets[0] += format_class(words[start_index_sub+1:])
                        else:
                            snippets[0] += format_variable(words[start_index_sub+1:])
                    else:
                        if words[start_index_sub] == 'class':
                            snippets[0] += format_class(words[start_index_sub+1:start_index_arg])
                        else:
                            snippets[0] += format_variable(words[start_index_sub+1:start_index_arg])
                    break
                else:
                    snippets[0] += format_class(words[start_index_sub+1:next_index_sub]) + '.'
                start_index_sub = next_index_sub

        # handle any arguments
        if start_index_arg == -1:
            snippets[0] += '()'
        else:
            snippets[0] += '('
            while True:
                next_index_arg = helper.find_next_index({'variable', 'arg', 'argument'}, words, start_index_arg)
                if next_index_arg == -1:
                    snippets[0] += format_variable(words[start_index_arg+1:]) + ')'
                    break
                else:
                    snippets[0] += format_variable(words[start_index_arg+1:next_index_arg]) + ', '
                start_index_arg = next_index_arg
        return snippets

    def process_math(self, words):
        replaced = words
        for i in range(0,len(Keywords.math_keyword_list)):
            if Keywords.math_keyword_list[i] in replaced:
                replaced = replaced.replace(Keywords.math_keyword_list[i], Keywords.math_replacement_list[i])
        return replaced

    def process_conditional_math(self, words):
        replaced = words
        for i in range(0,len(Keywords.conditional_keyword_list)):
            if Keywords.conditional_keyword_list[i] in replaced:
                replaced = replaced.replace(Keywords.conditional_keyword_list[i], Keywords.conditional_replacement_list[i])
        replaced = self.process_math(replaced)
        replaced_array = replaced.split(' ')
        # print(str(replaced_array))
        snippet = ''
        start_index_symbol = helper.find_next_index(Keywords.symbols, replaced_array)
        snippet += format_variable(replaced_array[0:start_index_symbol]) + ' '
        while True:
            next_index_symbol = helper.find_next_index(Keywords.symbols, words, start_index_symbol)
            if next_index_symbol == -1:
                snippet += replaced_array[start_index_symbol] + ' ' + format_variable(replaced_array[start_index_symbol+1:])
                break
            else:
                snippet += replaced_array[start_index_symbol] + ' ' + format_variable(replaced_array[start_index_symbol+1:next_index_symbol])
                start_index_symbol = next_index_symbol

        return snippet

    # built ins




