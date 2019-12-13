import json
import pickle
from glob import glob
import sys
import os

from BookProcessor import BookProcessor
from Models.Chapter import Chapter
from PDFGenerator import PDFGenerator
from StudyGuideCreator import StudyGuideCreator
from DictionaryCreator import DictionaryCreator


def process_book(directory):
    print("Loading chapters")
    chapters = load_book(f'{directory}/chapters')

    print("Processing book")
    print(f'{len(chapters)} chapters')
    bookProcessor = BookProcessor()
    bookProcessor.load_book(chapters)
    chapters, all_words = bookProcessor.process_book(level='C2',
                                                     words_per_chapter=20)
    return chapters, all_words


def pickle_chapters(chapters, directory):
    print("Pickling chapters")
    write_chapter_words(chapters, f'{directory}/chapter_words')


def unpickle_chapters(directory):
    print("Unpickling chapters")
    chapters = load_chapters(f'{directory}/chapter_words')
    return chapters


def unpickle_dictionary(directory):
    print("Unpickling dictionary")
    with open(f'Projects/{directory}/dictionary_words_only.pkl', 'rb') as f:
        all_words = pickle.load(f)
    return all_words


def create_study_guides(directory, language_code, chapters):
    print("Creating study guides")
    studyGuideCreator = StudyGuideCreator(language_code)
    try:
        if not os.path.exists(
                f'Projects/{directory}/{language_code}/study_guides'):
            os.mkdir(f'Projects/{directory}/{language_code}/study_guides')
        studyGuideCreator.create_study_guides(chapters,
                                              f'Projects/{directory}/{language_code}/study_guides')
    except KeyboardInterrupt:
        studyGuideCreator.close_creator()
        exit()

    studyGuideCreator.close_creator()


def load_book(directory):
    chapter_filenames = glob(f'Projects/{directory}/*.txt')
    chapters = []
    for filename in chapter_filenames:
        with open(filename, 'r') as f:
            json_dict = json_to_dict(f.read())
        chapter_number = json_dict['chapter_number']
        chapter_number = int(chapter_number)
        chapter_title = json_dict['chapter_title']
        chapter_body = json_dict['body']
        chapters.append(Chapter(chapter_number, chapter_title,
                                chapter_body))
    return chapters


def write_chapter_words(chapters, directory):
    for chapter in chapters:
        store_chapter(chapter, directory)


def store_chapter(chapter, directory):
    with open(
            f'Projects/{directory}/{str(chapter.number).zfill(2)}_words_only.pkl',
            'wb') as f:
        pickle.dump(chapter, f)


def load_chapters(directory):
    filenames = glob(f'Projects/{directory}/*.pkl')
    chapters = list()
    for filename in filenames:
        with open(filename, 'rb') as f:
            chapter = pickle.load(f)
            chapters.append(chapter)
    return chapters


def json_to_dict(json_string):
    return json.loads(json_string)


def create_master_dictionary(all_words, language_code):
    print('Creating master dictionary')
    dictionaryCreator = DictionaryCreator()
    all_words_dictionary = dictionaryCreator.create_dictionary(all_words,
                                                               language_code)
    return all_words_dictionary


def write_master_dictionary(all_words_dictionary, directory, language_code):
    json_string = dict_to_json(all_words_dictionary)
    with open(f'Projects/{directory}/{language_code}/master_dictionary.txt',
              'w') as f:
        f.write(json_string)


def dict_to_json(json_dict):
    return json.dumps(json_dict, sort_keys=True, indent=4)


def check_file_structure(directory, language_code):
    if not os.path.exists(f'Projects/{directory}'):
        return f'directory \'Projects/{directory}\' does not exist'
    if not os.path.exists(f'Projects/{directory}/chapters'):
        return f'directory \'Projects/{directory}/chapters\' does not exist'
    return 'success'


def create_file_structure(directory, language_code):
    if not os.path.exists(f'Projects/{directory}/chapter_words'):
        os.mkdir(f'Projects/{directory}/chapter_words')
    if not os.path.exists(f'Projects/{directory}/{language_code}'):
        os.mkdir(f'Projects/{directory}/{language_code}')


def generate_pdf(directory, language_code):
    pdf_generator = PDFGenerator()
    pdf_generator.generate_pdf(directory.replace("_", " "), directory,
                               language_code)


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print(f'USAGE: {sys.argv[0]} <directory> <language_code>')
        exit(1)

    directory = sys.argv[1]
    language_code = sys.argv[2]

    available_language_codes = ['definitions', 'ru', 'es']

    if not language_code in available_language_codes:
        print(f'{language_code} is not yet supported')
        exit()

    message = check_file_structure(directory, language_code)
    if not message == 'success':
        print(message)
        exit(2)

    print("Creating file structure")
    create_file_structure(directory, language_code)

    print("Processing book")
    chapters, all_words = process_book(directory)
    pickle_chapters(chapters, directory)
    print("Pickling dictionary")
    with open(f'Projects/{directory}/dictionary_words_only.pkl', 'wb') as f:
        pickle.dump(all_words, f)
    chapters = unpickle_chapters(directory)
    all_words = unpickle_dictionary(directory)
    create_study_guides(directory, language_code, chapters)
    all_words_dictionary = create_master_dictionary(all_words, language_code)
    write_master_dictionary(all_words_dictionary, directory, language_code)
    print(f'{len(all_words_dictionary.keys())} items in dictionary')
    print("Generating PDF study guide")
    generate_pdf(directory, language_code)
    print("Complete")
