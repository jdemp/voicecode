__author__ = 'jdemp'
import pickle


class VoiceParser():

    def __init__(self):
        self.keywords = {}
        self.translations = {}
        self.lang = ''

    def parse(self, cmd):
        words = cmd.split(maxsplit=1)
        print(str(words))
        snippet = self.keywords[words[0].lower()](words[1])
        return snippet

    def edit_keywords(self):
        pass

    def save_keywords(self):
        file = self.lang + '_keywords.p'
        pickle.dump(self.keywords,open(file, "wb"))

    def edit_translations(self):
        pass

    def save_translations(self):
        file = self.lang + '_translations.p'
        pickle.dump(self.keywords,open(file, "wb"))