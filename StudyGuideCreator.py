import json

class StudyGuideCreator:

    def __init__(self):
        pass

    def create_study_guides(self, chapters):
        for chapter in chapters:
            json_dict = self._chapter_to_json_dict(chapter)
            json_string = self._dict_to_json(json_dict)
            self._write_to_file(json_string, f'Tom_Sawyer/study_guides/chapter_{chapter.number}_{chapter.title}.txt')

    def _chapter_to_json_dict(self, chapter):
        json_dict = dict()
        words_with_definitions = {x[0]: 'a definition!' for x in chapter.featured_words}
        dict_with_definitions = {x[0]: 'another definition!' for x in chapter.dictionary_words}
        json_dict['chapter_number'] = chapter.number
        json_dict['chapter_title'] = chapter.title
        json_dict['featured_words'] = words_with_definitions
        json_dict['dictionary_words'] = dict_with_definitions
        return json_dict

    def _dict_to_json(self, json_dict):
        return json.dumps(json_dict, indent=4)

    def _write_to_file(self, out_string, filename):
        with open(filename, mode='w') as f:
            f.write(out_string)
