from glob import glob
import json

"""
This converter file can be copied and tailored to each project specifically.
"""

def main():
    """ Convert raw chapter text to JSON formatted for processing """

    # Load raw chapter files
    chapter_filenames = glob("raw_chapters/*.txt")
    chapter_counter = 0

    # Sort chapters by filename
    sorted_chapter_names = sorted(chapter_filenames)

    # Format each chapter for processing
    for filename in sorted_chapter_names:
        with open(filename) as f:
            raw_text = f.read()

        by_lines = raw_text.split('\n')
        title = by_lines[0]
        body = '\n'.join(by_lines[1:])

        json_dict = dict()
        json_dict['chapter_number'] = chapter_counter
        json_dict['chapter_title'] = title
        json_dict['body'] = body

        # Convert chapter dictionary to json string
        out_text = dict_to_json(json_dict)

        # Write formatted chapter to file
        with open(f'chapters/{str(chapter_counter).zfill(2)}_formatted.txt',
                  'w') as f:
            f.write(out_text)
        chapter_counter += 1


def dict_to_json(json_dict):
    """ Convert python dict to JSON string """

    return json.dumps(json_dict, indent=4)


if __name__ == '__main__':
    main()
