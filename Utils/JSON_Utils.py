import json


def json_to_dict(json_string):
    """ Convert json string into python dictionary """
    return json.loads(json_string)


def dict_to_json(json_dict):
    """ Convert python dictionary to json string """
    return json.dumps(json_dict, sort_keys=True, indent=4)
