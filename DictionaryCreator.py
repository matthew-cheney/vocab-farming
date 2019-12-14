from Translator import Translator
from tqdm import tqdm


class DictionaryCreator:

    def create_dictionary(self, all_words, language_code):
        """ Generate dictionary with translations for all_words
        in language_code """

        all_words_dictionary = dict()
        translator = Translator(language_code=language_code)

        for word in tqdm(all_words):
            all_words_dictionary[f'{word[0]} : {word[1]}'] \
                = translator.get_translation(word)

        # Update local dictionary with new translations for future access
        translator.write_local_dictionary()

        return all_words_dictionary
