from tqdm import tqdm

from Core_Scripts.Translator import Translator
from Utils.JSON_Utils import dict_to_json


class StudyGuideCreator:

    def __init__(self, language_code='definitions'):
        self.translator = Translator(language_code=language_code)

    def close_creator(self):
        """ Write to local dictionary to save api usage """

        self.translator.write_local_dictionary()

    def create_study_guides(self, chapters, directory):
        """ Create study guide for each chapter, write JSON to file """

        study_guides = list()
        for chapter in tqdm(chapters):
            json_dict = self._chapter_to_json_dict(chapter)
            json_string = dict_to_json(json_dict)
            self._write_to_file(json_string, f'{directory}/chapter_{str(chapter.number).zfill(2)}_{chapter.title}.txt')  # noqa: E501

    def _chapter_to_json_dict(self, chapter):
        """ Convert chapter to python dict, ready to make into JSON """
        json_dict = dict()

        # Get each word list
        words_with_definitions = {f'{x[0]} ({x[1]})': self._get_translation(x) for x in chapter.featured_words}  # noqa: E501
        dict_with_definitions = {f'{x[0]} ({x[1]})': self._get_translation(x) for x in chapter.dictionary_words}  # noqa: E501
        previous_chapter_words = {f'{x[0]} ({x[1]})': self._get_translation(x) for x in list(chapter.featured_in_previous_chapters.keys())}  # noqa: E501

        # Add data to dictionary
        json_dict['chapter_number'] = chapter.number
        json_dict['chapter_title'] = chapter.title
        json_dict['featured_words'] = words_with_definitions
        json_dict['dictionary_words'] = dict_with_definitions
        json_dict['previously_featured'] = previous_chapter_words

        return json_dict

    def _write_to_file(self, out_string, filename):
        """ Write out_string to filename """

        with open(filename, mode='w') as f:
            f.write(out_string)

    def _get_translation(self, word_tuple):
        """ Query self.translator for translation of word_tuple """

        return self.translator.get_translation(word_tuple)
