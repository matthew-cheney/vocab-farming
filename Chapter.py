from nltk import FreqDist


class Chapter:

    def __init__(self, number, title, body):
        self.number = number
        self.title = title
        self.body = body
        self.featured_words = set()
        self.dictionary_words = set()
        self.word_frequency_list = FreqDist()
        self.featured_in_previous_chapters = dict()

    def __lt__(self, other):
        return self.number < other.number

    def __repr__(self):
        return f'number={self.number}; title={self.title}'

    def to_dict(self):
        to_dict = dict()
        to_dict['chapter_number'] = self.number
        to_dict['chapter_title'] = self.title
        to_dict['featured_words'] = list(self.featured_words)
        to_dict['dictionary_words'] = list(self.dictionary_words)
        to_dict['featured_in_previous_chapters'] = self.featured_in_previous_chapters
        return to_dict