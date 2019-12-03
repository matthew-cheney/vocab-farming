import json
import os

from Translator import Translator

class StudyGuideCreator:

    def __init__(self, language_code='definitions'):
        self.translator = Translator(language_code=language_code)

    def close_creator(self):
        self.translator._write_local_dictionary()

    def create_study_guides(self, chapters, directory):
        study_guides = list()
        for chapter in chapters:
            json_dict = self._chapter_to_json_dict(chapter)
            json_string = self._dict_to_json(json_dict)
            self._write_to_file(json_string, f'{directory}/chapter_{chapter.number}_{chapter.title}.txt')

    def _chapter_to_json_dict(self, chapter):
        json_dict = dict()
        words_with_definitions = {f'{x[0]} ({x[1]})': self._get_translation(x) for x in chapter.featured_words}
        dict_with_definitions = {f'{x[0]} ({x[1]})': self._get_translation(x) for x in chapter.dictionary_words}
        previous_chapter_words = {f'{x[0]} ({x[1]})': self._get_translation(x) for x in list(chapter.featured_in_previous_chapters.keys())}
        json_dict['chapter_number'] = chapter.number
        json_dict['chapter_title'] = chapter.title
        json_dict['featured_words'] = words_with_definitions
        json_dict['dictionary_words'] = dict_with_definitions
        json_dict['previously_featured'] = previous_chapter_words
        return json_dict

    def _dict_to_json(self, json_dict):
        return json.dumps(json_dict, indent=4)

    def _write_to_file(self, out_string, filename):
        with open(filename, mode='w') as f:
            f.write(out_string)

    def _get_translation(self, word_tuple):
        return self.translator.get_translation(word_tuple)