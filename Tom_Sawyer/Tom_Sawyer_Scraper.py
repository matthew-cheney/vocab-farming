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
    chapter_re = r'\n\n\n\n(CHAPTER [XVI].*?)'
    chapters = re.findall(chapter_re, text, flags=re.S)
    chapters = text.split('\n\n\n\n\n')
    return chapters[3:]


def chapter_to_file(chapter, number):
    # end = chapter.find('\n')
    # filename = chapter[:end]
    with open(f'chapters/{number}_full_text.txt', mode='w') as f:
        f.write(chapter)


if __name__ == '__main__':
    main()