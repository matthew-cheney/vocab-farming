import re

"""
This converter file can be copied and tailored to each project specifically.
"""

def main():
    """ Split full <book title> text to chapters """

    # Load full book text
    with open('full_book.txt', mode='r') as f:
        full_text = f.read()

    # Parse out each chapter
    chapters = parse_text_to_chapters(full_text)

    # Save chapters to files
    counter = 0
    for chapter in chapters:
        chapter_to_file(chapter, counter)
        counter += 1


def parse_text_to_chapters(text):
    """ Separate chapters by regex: <regex below> """

    chapter_re = r'INSERT REGEX HERE'
    chapters = re.findall(chapter_re, text, flags=re.S)
    return chapters


def chapter_to_file(chapter, number):
    """ Write chapter to file, including number in title """

    with open(f'raw_chapters/{str(number).zfill(2)}_full_text.txt',
              mode='w') as f:
        f.write(chapter)


if __name__ == '__main__':
    main()
