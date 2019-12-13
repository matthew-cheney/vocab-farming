import copy
from nltk.stem import WordNetLemmatizer
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from Models.Word import Word


class BookProcessor:

    def __init__(self):
        self.chapters = list()
        self.STOPS = STOP_WORDS
        self.level_dictionary = {
            'A1': 1,
            'A2': 2,
            'B1': 3,
            'B2': 4,
            'C1': 5,
            'C2': 6
        }
        # self.STOPS = stopwords.words('english')
        self.frequency_list, self.frequency_list_no_pos = self._load_freq_list()
        self.nlp = spacy.load('en')
        self.all_dictionary_words = set()

    def _load_freq_list(self):
        frequency_list = dict()
        frequency_list_no_tags = dict()
        with open("Kelly_English.csv", 'r') as f:
            for line in f:
                line_split = line.split(',')
                rank = int(line_split[0])
                word = line_split[1].lower()
                pos = line_split[2]
                level = self.level_dictionary[line_split[3][:-1]]
                frequency_list[(word, pos)] = Word(rank, word, pos, level)
                if not word in frequency_list_no_tags:
                    frequency_list_no_tags[word] = Word(rank, word, pos, level)
        return frequency_list, frequency_list_no_tags

    def load_book(self, chapters):
        self.chapters = chapters
        self.chapters.sort()

    def process_book(self, difficulty=0, level='A1', words_per_chapter=15,
                     dictionary_words_per_chapter=15):
        already_featured = dict()
        level = self.level_dictionary[level]
        for chapter in self.chapters:
            self._process_chapter(chapter)
            self._set_featured_words(chapter, difficulty, level,
                                     words_per_chapter,
                                     dictionary_words_per_chapter,
                                     already_featured)
            self._add_to_already_featured(chapter, already_featured)
        return self.chapters, self.all_dictionary_words

    def _add_to_already_featured(self, chapter, already_featured):
        for each in chapter.featured_words:
            if not each in already_featured:
                already_featured[each] = list()
            already_featured[each].append(chapter.number)

    def _process_chapter(self, chapter):
        doc = self.nlp(chapter.body)
        tagged_list = list()
        for token in doc:
            tagged_list.append((token.lemma_, token.tag_))
        simplified_tags = self._filter_word_list(tagged_list)
        chapter.word_frequency_list.update(simplified_tags)

    def _filter_word_list(self, tagged_list):
        tagged_list = self._to_lower_case(tagged_list)
        tagged_list = self._filter_by_alpha(tagged_list)
        tagged_list = self._remove_stopwords(tagged_list)
        tagged_list = self._remove_numbers(tagged_list)
        tagged_list = self._remove_proper_nouns(tagged_list)
        tagged_list = self._remove_two_letter_words(tagged_list)
        simplified_tags = self._get_simplified_tags(tagged_list)
        return simplified_tags

    def _to_lower_case(self, tokens):
        return [(word[0].lower(), word[1]) for word in tokens]

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

    def _set_featured_words(self, chapter, difficulty, level,
                            words_per_chapter, dictionary_words_per_chapter,
                            used_words):
        sorted_by_frequency = chapter.word_frequency_list.most_common()
        words_chosen = 0
        target_index = 0  # Can probably remove this variable
        for target_word_tuple, freq in sorted_by_frequency:

            # Reached end of sorted_by_frequency
            if target_index == len(sorted_by_frequency):
                break
            # target_word_tuple = sorted_by_frequency[target_index][0]

            if target_word_tuple in used_words:
                # Word already featured in previous chapter
                if not target_word_tuple in chapter.featured_in_previous_chapters:
                    # Word not already in previous word list for this chapter
                    chapter.featured_in_previous_chapters[
                        target_word_tuple] = list()
                chapter.featured_in_previous_chapters[
                    target_word_tuple].extend(
                    copy.copy(used_words[target_word_tuple]))
                target_index += 1
                continue

            if (target_word_tuple in self.frequency_list and \
                    (self.frequency_list[
                         target_word_tuple].rank < difficulty or \
                     self.frequency_list[target_word_tuple].level < level)):
                # Word is below specified level
                target_index += 1
                continue
            elif (target_word_tuple[0] in self.frequency_list_no_pos and \
                  (self.frequency_list_no_pos[
                       target_word_tuple[0]].rank < difficulty or \
                   self.frequency_list_no_pos[
                       target_word_tuple[0]].level < level)):
                # Word is below specified level
                target_index += 1
                continue

            if words_chosen < words_per_chapter:
                chapter.featured_words.add(target_word_tuple)
            elif len(chapter.dictionary_words) < dictionary_words_per_chapter:
                chapter.dictionary_words.add(target_word_tuple)
            self.all_dictionary_words.add(target_word_tuple)
            words_chosen += 1
            target_index += 1
