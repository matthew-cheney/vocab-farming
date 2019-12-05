from glob import glob
import json
import os

from PyDictionary import PyDictionary
from google.cloud import translate_v2 as translate


class Translator:

    def __init__(self, language_code='definitions'):
        self.local_dictionary = dict()
        self.language_code = language_code
        self.dictionary_holder = PyDictionary()
        self.api_dictionary = translate.Client()
        # self.api_dictionary = PyDictionary()
        self.pydictionary_codes = {
            'n': 'Noun',
            'v': 'Verb',
            'j': 'Adjective',
            'i': 'Adjective',
            'r': 'Adverb'
        }

        if not os.path.exists(f'Local_Dictionaries/{language_code}'):
            os.mkdir(f'Local_Dictionaries/{language_code}')
            with open(f'Local_Dictionaries/{language_code}/en_dictionary_01.json', mode='w') as f:
                f.write('{}')

        self._load_local_dictionary()

    def _write_local_dictionary(self):
        json_string = self._json_dict_to_string(self.local_dictionary)
        self._write_dict(json_string)

    def _load_local_dictionary(self):
        d_filenames = glob(f"Local_Dictionaries/{self.language_code}/*.json")
        for name in d_filenames:
            with open (name, mode='r') as f:
                raw_text = f.read()
                self.local_dictionary.update(self._json_string_to_dict(raw_text))

    def _json_string_to_dict(self, json_string):
        return json.loads(json_string)

    def _json_dict_to_string(self, json_dict):
        """
        Converts json_dict to a json string
        :param json_dict: must be of form: ('',''): ''
        :return: the json string
        """
        # new_dict = {f'{x[0]} : {x[1]}': json_dict[x] for x in json_dict}
        return json.dumps(json_dict, indent=4)

    def _write_dict(self, json_string):
        with open(f'Local_Dictionaries/{self.language_code}/en_dictionary_01.json', mode='w') as f:
            f.write(json_string)

    def get_translation(self, tuple_in):
        source_word = tuple_in[0]
        source_pos = tuple_in[1]
        # if source_pos == 'v':
        #     source_word = 'to ' + source_word

        translation = self._query_local_dictionary(self._tuple_to_string(tuple_in))
        if translation is None:
            translation = self._query_api(source_word, source_pos)
            self._add_to_local_dictionary(self._tuple_to_string(tuple_in), translation)
        return translation

    def _tuple_to_string(self, tuple_in):
        return f'{tuple_in[0]} : {tuple_in[1]}'

    def _query_local_dictionary(self, source_string):
        if source_string in self.local_dictionary:
            return self.local_dictionary[source_string]
        else:
            return None

    def _add_to_local_dictionary(self, tuple_string, translation):
        if tuple_string in self.local_dictionary:
            return False
        else:
            self.local_dictionary[tuple_string] = translation
            return True

    def _query_api(self, source_string, source_pos):
        # do the query here
        # PyDictionary is placeholder for Google Translation API
        if self.language_code == 'definitions':
            # print(f'getting definition for {source_string}')
            result = self.dictionary_holder.meaning(source_string)
            if isinstance(result, type(None)):
                # print(f'no translation for {source_string}\n\n')
                return 'no translation found'
            # print('found')
            if source_pos in self.pydictionary_codes:
                result_pos = self.pydictionary_codes[source_pos]
                if result_pos in result.keys():
                    return result[result_pos]
            return result[list(result.keys())[0]]
        else:
            search_string = source_string
            if source_pos == 'v':
                search_string = 'to ' + search_string
            # print(f'searching for {source_string} : {source_pos}')
            result = self.api_dictionary.translate(search_string, target_language=self.language_code)
            # result = self.dictionary_holder.meaning(source_string)
            # print('found')
            if result is None:
                return 'no translation found'
            if 'translatedText' not in result:
                # print('investigate this...')
                return 'no translation found'
            return result['translatedText']

