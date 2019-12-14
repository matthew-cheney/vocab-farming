from glob import glob
import json
import os

from PyDictionary import PyDictionary
from google.cloud import translate_v2 as translate

from Utils.JSON_Utils import json_to_dict, dict_to_json


class Translator:

    def __init__(self, language_code='definitions'):
        self.local_dictionary = dict()
        self.language_code = language_code
        self.def_dictionary = PyDictionary()  # Dictionary for definitions
        self.api_dictionary = translate.Client()  # Dictionary for translations

        # To avoid inadvertent api usage in development, uncomment next line
        # self.api_dictionary = PyDictionary()

        # pos codes used by PyDictionary
        self.pydictionary_codes = {
            'n': 'Noun',
            'v': 'Verb',
            'j': 'Adjective',
            'i': 'Adjective',
            'r': 'Adverb'
        }

        if not os.path.exists(f'Local_Dictionaries/{language_code}'):
            # Directory for local dictionary does not exist, create it now
            os.mkdir(f'Local_Dictionaries/{language_code}')
            with open(f'Local_Dictionaries/{language_code}/en_dictionary_01.json', mode='w') as f:
                f.write('{}')

        self._load_local_dictionary()  # Contains previously translated data

    def write_local_dictionary(self):
        """ Write working dictionary to local dictionary for future access """

        json_string = dict_to_json(self.local_dictionary)
        self._write_dict(json_string)

    def _load_local_dictionary(self):
        """ Load local dictionary for quicker and less api-expensive access """

        d_filenames = glob(f"Local_Dictionaries/{self.language_code}/*.json")
        for name in d_filenames:
            with open (name, mode='r') as f:
                raw_text = f.read()
                self.local_dictionary.update(json_to_dict(raw_text))

    def _write_dict(self, json_string):
        """ Write dictionary to file """

        with open(f'Local_Dictionaries/{self.language_code}/en_dictionary_01.json', mode='w') as f:
            f.write(json_string)

    def get_translation(self, tuple_in):
        """ Get translation for word (tuple_in) """

        source_word = tuple_in[0]
        source_pos = tuple_in[1]

        # Check local dictionary for translation
        translation = self._query_local_dictionary(self._tuple_to_string(tuple_in))

        if translation is None:
            # Translation not in local dictionary, go to api
            translation = self._query_api(source_word, source_pos)
            self._add_to_local_dictionary(self._tuple_to_string(tuple_in), translation)

        return translation

    def _tuple_to_string(self, tuple_in):
        """ Convert tuple_in to string """

        return f'{tuple_in[0]} : {tuple_in[1]}'

    def _query_local_dictionary(self, source_string):
        """ Check local dictionary for source_string """

        if source_string in self.local_dictionary:
            return self.local_dictionary[source_string]
        else:
            return None

    def _add_to_local_dictionary(self, tuple_string, translation):
        """ Add tuple_string and its translation to local dictionary """

        if tuple_string in self.local_dictionary:
            # tuple_string already in local dictionary
            return False
        else:
            self.local_dictionary[tuple_string] = translation
            return True

    def _query_api(self, source_string, source_pos):
        """ Query the appropriate api for translation of source_string """

        if self.language_code == 'definitions':
            # Use PyDictionary api (free)
            result = self.def_dictionary.meaning(source_string)
            if isinstance(result, type(None)):
                # No definition found in api
                return 'no translation found'

            # Try to get appropriate pos definition
            if source_pos in self.pydictionary_codes:
                result_pos = self.pydictionary_codes[source_pos]
                if result_pos in result.keys():
                    return result[result_pos]
            return result[list(result.keys())[0]]

        else:
            # Use Google Translate API (free tier)
            search_string = source_string

            # If verb, convert to infinitive form (i.e. prepend 'to')
            if source_pos == 'v':
                search_string = 'to ' + search_string

            result = self.api_dictionary.translate(search_string,
                                                   target_language=
                                                   self.language_code)

            if result is None or 'translatedText' not in result:
                # No translation found
                return 'no translation found'

            return result['translatedText']
