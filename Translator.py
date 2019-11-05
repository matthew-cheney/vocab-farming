from glob import glob
import json


class Translator:

    def __init__(self):
        self.local_dictionary = dict()
        pass

    def _load_local_dictionary(self, language_code='en'):
        d_filenames = glob(f"Local_Dictionaries/{language_code}/*.json")
        for name in d_filenames:
            with open (name, mode='r') as f:
                raw_text = f.read()
                self.local_dictionary.update(self._read_json_in(raw_text))

    def _read_json_in(self, json_string):
        return json.loads(json_string)

    def _write_json_to_file(self, json_dict):
        json.dumps(json_dict, indent=4)