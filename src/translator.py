from deep_translator import GoogleTranslator
from src.settings import LANGUAGE

class VocabularyTranslator:
    def __init__(self):
        self.translator = GoogleTranslator(source='fr', target=LANGUAGE)

    def translate(self, word):
        translation = self.translator.translate(word)
        print(translation)
        return translation