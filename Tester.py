import json
import pickle
from glob import glob

from BookProcessor import BookProcessor
from Chapter import Chapter
from StudyGuideCreator import StudyGuideCreator

"""
Kelly word list
Academic word/vocabulary list
   Dewey, maybe Davies
   
TFIDF
"""


def process_book(directory):
    print("Loading chapters")
    chapters = load_book(f'{directory}/chapters')

    print("Processing book")
    bookProcessor = BookProcessor()
    bookProcessor.load_book(chapters)
    chapters = bookProcessor.process_book(level='C2', words_per_chapter=15)
    return chapters

def pickle_chapters(chapters, directory):
    print("Pickling chapters")
    write_chapter_words(chapters, f'{directory}/chapter_words')

def unpickle_chapters(directory):
    print("Unpickling chapters")
    chapters = load_chapters(f'{directory}/chapter_words')
    return chapters

def create_study_guides(directory, language_code, chapters):
    print("Creating study guides")
    studyGuideCreator = StudyGuideCreator(language_code)
    try:
        studyGuideCreator.create_study_guides(chapters, f'{directory}/{language_code}/study_guides')
    except KeyboardInterrupt:
        studyGuideCreator.close_creator()
        exit()

    studyGuideCreator.close_creator()


def load_book(directory):
    chapter_filenames = glob(f'{directory}/*.txt')
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
    with open(f'{directory}/{str(chapter.number).zfill(2)}_words_only.pkl', 'wb') as f:
        pickle.dump(chapter, f)


def load_chapters(directory):
    filenames = glob(f'{directory}/*.pkl')
    chapters = list()
    for filename in filenames:
        with open(filename, 'rb') as f:
            chapter = pickle.load(f)
            chapters.append(chapter)
    return chapters


def json_to_dict(json_string):
    return json.loads(json_string)


if __name__ == '__main__':
    directory = 'Wizard_Of_Oz'
    language_code = 'es'

    # chapters = process_book(directory)
    # pickle_chapters(chapters, directory)
    chapters = unpickle_chapters(directory)
    create_study_guides(directory, language_code, chapters)
    print("Complete")
