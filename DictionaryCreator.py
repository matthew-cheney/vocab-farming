from Translator import Translator
from tqdm import tqdm

class DictionaryCreator:

    def __init__(self):
        pass

    def create_dictionary(self, all_words, language_code):
        all_words_dictionary = dict()
        translator = Translator(language_code=language_code)
        # all_words_dictionary = {x[0]: translator.get_translation(x) for x in all_words}

        for word in tqdm(all_words):
            all_words_dictionary[word[0]] = translator.get_translation(word)

        translator._write_local_dictionary()

        return all_words_dictionary