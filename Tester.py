from BookProcessor import BookProcessor


def main():
    bookProcessor = BookProcessor()
    bookProcessor.load_book("Tom_Sawyer/chapters")
    bookProcessor.process_book(difficulty=5000, words_per_chapter=15)
    x = 0

if __name__ == '__main__':
    main()