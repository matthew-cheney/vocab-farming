from glob import glob
import sys
import os

from Core_Scripts.BookProcessor import BookProcessor
from Models.Chapter import Chapter
from Core_Scripts.PDFGenerator import PDFGenerator
from Core_Scripts.StudyGuideCreator import StudyGuideCreator
from Core_Scripts.DictionaryCreator import DictionaryCreator
from Utils.JSON_Utils import *

""" Main function located at bottom of script """


def process_book(directory):
    """ Process each chapter in directory, identify featured words,
    dictionary words, etc. """

    print("Loading chapters")
    chapters = load_book(f'{directory}/chapters')

    print("Processing book")
    print(f'{len(chapters)} chapters')
    bookProcessor = BookProcessor()

    # Load chapters into book processor
    bookProcessor.load_book(chapters)

    # Process chapters, get chapters and all unique words in book
    chapters, all_words = bookProcessor.process_book(level='C2',
                                                     words_per_chapter=20)
    return chapters, all_words


def create_study_guides(directory, language_code, chapters):
    """ Create JSON study guides for each chapter """

    studyGuideCreator = StudyGuideCreator(language_code)

    try:
        if not os.path.exists(
                f'Projects/{directory}/{language_code}/study_guides'):
            # Create directory to hold study guides
            os.mkdir(f'Projects/{directory}/{language_code}/study_guides')
        # Create all JSON study guides
        studyGuideCreator.create_study_guides(chapters,
                                              f'Projects/{directory}/{language_code}/study_guides')  # noqa: E501
    except KeyboardInterrupt:
        # If stopped early, do close methods (i.e. saving local dictionary)
        studyGuideCreator.close_creator()
        exit()

    studyGuideCreator.close_creator()


def load_book(directory):
    """ Open JSON chapter files, convert to python objects """

    # Note - 'directory' contains path to chapters folder
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


def create_master_dictionary(all_words, language_code):
    """ Create dictionary for end of study guide """

    dictionaryCreator = DictionaryCreator()
    all_words_dictionary = dictionaryCreator.create_dictionary(all_words,
                                                               language_code)
    return all_words_dictionary


def write_master_dictionary(all_words_dictionary, directory, language_code):
    """ Write dictionary to JSON file, sorted alphabetically by term """

    json_string = dict_to_json(all_words_dictionary)

    with open(f'Projects/{directory}/{language_code}/master_dictionary.txt',
              'w') as f:
        f.write(json_string)


def check_file_structure(directory):
    """ Ensure necessary file structure is in place """

    if not os.path.exists(f'Projects/{directory}'):
        return f'directory \'Projects/{directory}\' does not exist'
    if not os.path.exists(f'Projects/{directory}/chapters'):
        return f'directory \'Projects/{directory}/chapters\' does not exist'
    return 'success'


def create_file_structure(directory, language_code):
    """ Create necessary file structure """

    if not os.path.exists(f'Projects/{directory}/{language_code}'):
        os.mkdir(f'Projects/{directory}/{language_code}')


def generate_pdf(directory, language_code):
    """ Generate PDF of book study guide with dictionary """

    pdf_generator = PDFGenerator()
    pdf_generator.generate_pdf(directory.replace("_", " "), directory,
                               language_code)


if __name__ == '__main__':

    # Check for correct command line args
    if len(sys.argv) < 3:
        print(f'USAGE: {sys.argv[0]} <directory> <language_code>')
        exit(0)

    directory_main = sys.argv[1]
    language_code_main = sys.argv[2]

    available_language_codes = ['definitions', 'ru', 'es']

    # Check if language code is supported
    if language_code_main not in available_language_codes:
        print(f'{language_code_main} is not yet supported')
        exit(0)

    message = check_file_structure(directory_main)
    if not message == 'success':
        print(message)
        exit(0)

    print("Creating file structure")
    create_file_structure(directory_main, language_code_main)

    print("Processing book")
    chapters_main, all_words_main = process_book(directory_main)

    print("Creating study guides")
    create_study_guides(directory_main, language_code_main, chapters_main)

    print("Creating dictionary")
    all_words_dictionary_main = create_master_dictionary(all_words_main,
                                                         language_code_main)

    print("Writing dictionary to file")
    write_master_dictionary(all_words_dictionary_main, directory_main,
                            language_code_main)

    print(f'{len(all_words_dictionary_main.keys())} items in dictionary')

    # Skip creating pdf if language code is definitions (not supported yet)
    if not language_code_main == 'definitions':
        print("Generating PDF study guide")
        generate_pdf(directory_main, language_code_main)

    print("Complete")
