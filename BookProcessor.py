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
import copy
from glob import glob
from bs4 import BeautifulSoup
from Chapter import Chapter
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
from spacy.lang.en.stop_words import STOP_WORDS


class BookProcessor:

    def __init__(self):
        self.chapters = list()
        self.STOPS = STOP_WORDS
        # self.STOPS = stopwords.words('english')
        self.frequency_list = self._load_freq_list()
        self.nlp = spacy.load('en')

    def _load_freq_list(self):
        frequency_list = dict()
        with open("5000_english_words.csv", 'r') as f:
            for line in f:
                line_split = line.split(',')
                pos = line_split[2]
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
            chapter_body = str(soup.find('body').contents[0])
            self.chapters.append(Chapter(chapter_number, chapter_title,
                                         chapter_body))
        self.chapters.sort()

    def process_book(self, difficulty=1000, words_per_chapter=15):
        already_featured = dict()
        for chapter in self.chapters:
            self._process_chapter(chapter)
            self._set_featured_words(chapter, difficulty, words_per_chapter, already_featured)
            for each in chapter.featured_words:
                if not each in already_featured:
                    already_featured[each] = list()
                already_featured[each].append(chapter.number)
            # Generate this chapter's featured words
            # Include any previous featured words
            # Generate other hard reference words

    def _process_chapter(self, chapter):
        doc = self.nlp(chapter.body)
        tagged_list = list()
        for token in doc:
            tagged_list.append((token.lemma_, token.tag_))
        tagged_list = self._filter_by_alpha(tagged_list)
        tagged_list = self._remove_stopwords(tagged_list)
        tagged_list = self._remove_numbers(tagged_list)
        tagged_list = self._remove_proper_nouns(tagged_list)
        tagged_list = self._remove_two_letter_words(tagged_list)
        simplified_tags = self._get_simplified_tags(tagged_list)
        chapter.word_frequency_list.update(simplified_tags)

    def _filter_by_alpha(self, tokens):
        return [word for word in tokens if word[0].isalpha()]

    def _remove_stopwords(self, tagged_tokens):
        return [x for x in tagged_tokens if x[0].lower() not in self.STOPS]

    def _remove_numbers(self, tagged_tokens):
        return [x for x in tagged_tokens if x[1] != "CD"]

    def _remove_proper_nouns(self, tagged_tokens):
        return [x for x in tagged_tokens if x[1] != 'NNP']

    def _remove_two_letter_words(self, tagged_tokens):
        return [x for x in tagged_tokens if len(x[0]) > 2]

    def _get_simplified_tags(self, tagged_tokens):
        simplified_tags = list()
        for tok, tag in tagged_tokens:
            new_tag = tag[0].lower()
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

            if target_word_tuple in used_words:
                if not target_word_tuple in chapter.featured_in_previous_chapters:
                    chapter.featured_in_previous_chapters[target_word_tuple] = list()
                chapter.featured_in_previous_chapters[target_word_tuple].extend(copy.copy(used_words[target_word_tuple]))

            if (target_word_tuple in self.frequency_list and \
                    self.frequency_list[target_word_tuple] < difficulty):
                target_index += 1
                continue
            chapter.featured_words.add(target_word_tuple)
            words_chosen += 1
            target_index += 1
        x = 0
