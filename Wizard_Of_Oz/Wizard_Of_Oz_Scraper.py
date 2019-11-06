import re


def main():
    with open('full_book.txt', mode='r') as f:
        full_text = f.read()
    chapters = parse_text_to_chapters(full_text)
    counter = 0
    for chapter in chapters:
        chapter_to_file(chapter, counter)
        counter += 1


def parse_text_to_chapters(text):
    chapter_re = r'([0-9]*\.[^0123456789]*)'
    chapters = re.findall(chapter_re, text, flags=re.S)
    # chapters = text.split('\n\n\n\n\n')
    return chapters


def chapter_to_file(chapter, number):
    # end = chapter.find('\n')
    # filename = chapter[:end]
    with open(f'raw_chapters/{str(number).zfill(2)}_full_text.txt', mode='w') as f:
        f.write(chapter)


if __name__ == '__main__':
    main()