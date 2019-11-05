from BookProcessor import BookProcessor
from StudyGuideCreator import StudyGuideCreator

"""
Kelly word list
Academic word/vocabulary list
   Dewey, maybe Davies
   
TFIDF
"""

def main():
    bookProcessor = BookProcessor()
    bookProcessor.load_book("Tom_Sawyer/chapters")
    chapters = bookProcessor.process_book(level='C1', words_per_chapter=5)

    studyGuideCreator = StudyGuideCreator()
    studyGuideCreator.create_study_guides(chapters)

if __name__ == '__main__':
    main()