# This script assumes chapters are located in directory:
# DIRECTORY/*.txt
# Each file must start with prologue. Pre-first chapter: chapter0.txt

# Word list: https://www.wordfrequency.info/top5000.asp

"""
For each chapter:
    ~15 new words
    Any featured words from previous chapters
    Any words above certain difficulty level? (like in Russ 441)

"""

from glob import glob
from bs4 import BeautifulSoup
from Chapter import Chapter
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class BookProcessor:

    def __init__(self):
        self.chapters = list()
        self.STOPS = stopwords.words('english')
        self.frequency_list = self._load_freq_list()

    def _load_freq_list(self):
        frequency_list = dict()
        with open("5000_english_words.csv", 'r') as f:
            for line in f:
                line_split = line.split(',')
                pos = 'n'
                if line_split[2] == 'v':
                    pos = 'v'
                elif line_split[2] == 'j':
                    pos = 'a'
                frequency_list[(line_split[1], pos)] = int(line_split[0])
        return frequency_list


    def load_book(self, directory):
        chapter_filenames = glob(f'{directory}/*.txt')
        for filename in chapter_filenames:
            with open(filename, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')
            chapter_number = soup.find('chapter_number').contents[0]
            chapter_number = int(chapter_number)
            chapter_title = soup.find('title').contents[0]
            chapter_body = soup.find('body').contents[0]
            self.chapters.append(Chapter(chapter_number, chapter_title,
                                         chapter_body))
        self.chapters.sort()

    def process_book(self, difficulty=1000, words_per_chapter=15):
        already_featured = set()
        for chapter in self.chapters:
            self._process_chapter(chapter)
            self._set_featured_words(chapter, difficulty, words_per_chapter, already_featured)
            # Generate this chapter's featured words
            # Include any previous featured words
            # Generate other hard reference words

    def _process_chapter(self, chapter):
        tokens = nltk.word_tokenize(chapter.body)
        tokens = self._filter_by_alpha(tokens)
        tagged_tokens = nltk.pos_tag(tokens)
        tagged_tokens = self._remove_stopwords(tagged_tokens)
        tagged_tokens = self._remove_proper_nouns(tagged_tokens)
        simplified_tags = self._get_simplified_tags(tagged_tokens)
        lemmas_list = self._toks_to_lemmas(simplified_tags)
        chapter.word_frequency_list.update(lemmas_list)

    def _filter_by_alpha(self, tokens):
        return [word for word in tokens if word.isalpha()]

    def _remove_stopwords(self, tagged_tokens):
        return [x for x in tagged_tokens if x[0].lower() not in self.STOPS]

    def _remove_proper_nouns(self, tagged_tokens):
        return [x for x in tagged_tokens if x[1] != 'NNP']

    def _get_simplified_tags(self, tagged_tokens):
        simplified_tags = list()
        for tok, tag in tagged_tokens:
            new_tag = 'n'
            if tag.startswith('J'):
                new_tag = 'a'
            elif tag.startswith('V'):
                new_tag = 'v'
            simplified_tags.append((tok, new_tag))
        return simplified_tags

    def _toks_to_lemmas(self, simplified_tags):
        lemmas_list = list()
        lemmatizer = WordNetLemmatizer()
        for tok, tag in simplified_tags:
            lemma = lemmatizer.lemmatize(tok, pos=tag)
            lemmas_list.append((lemma, tag))
        return lemmas_list

    def _set_featured_words(self, chapter, difficulty, words_per_chapter, used_words):
        sorted_by_frequency = chapter.word_frequency_list.most_common()
        words_chosen = 0
        target_index = 0
        while words_chosen < words_per_chapter:
            if target_index == len(sorted_by_frequency):
                break
            target_word_tuple = sorted_by_frequency[target_index][0]
            if target_word_tuple in self.frequency_list and\
                    self.frequency_list[target_word_tuple] < difficulty:
                target_index += 1
                continue
            chapter.featured_words.add(target_word_tuple)
            words_chosen += 1
            target_index += 1
        x = 0
