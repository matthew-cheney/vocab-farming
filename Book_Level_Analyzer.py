import json
from glob import glob
import sys
import spacy
from tqdm import tqdm

from Models.Word import Word

"""
This script analyses the rough difficulty of a book.
It calculates how many words it contains at each reading level, both
including and excluding duplicates.
"""


def main(project_name):
    nlp = spacy.load('en')

    print('Loading chapters')
    filenames = glob(f"Projects/{project_name}/chapters/*.txt")

    # Check for files to process
    if len(filenames) == 0:
        print('No files found')
        return

    # Collect list of all words with pos
    print('Gathering unique words in each chapter')
    all_words = list()
    for file in tqdm(filenames):
        with open(file, 'r') as f:
            raw_text = f.read()
            json_dict = json_to_dict(raw_text)
            chapter_body = json_dict['body']
            doc = nlp(chapter_body)
            for token in doc:
                if not token.is_punct:
                    all_words.append(token.lemma_.lower())
    freq_list = load_freq_list()

    # Lists to hold words by difficulty
    ones = list()
    twos = list()
    threes = list()
    fours = list()
    fives = list()
    sixes = list()
    others = list()

    # Sort words by difficulty
    print('Sorting words by difficulty')
    for word in tqdm(all_words):
        if word in freq_list:
            word_level = freq_list[word].level
            if word_level == 1:
                ones.append(word)
            elif word_level == 2:
                twos.append(word)
            elif word_level == 3:
                threes.append(word)
            elif word_level == 4:
                fours.append(word)
            elif word_level == 5:
                fives.append(word)
            elif word_level == 6:
                sixes.append(word)
            else:
                others.append(word)
        else:
            others.append(word)

    # Print results
    print("\nIncluding duplicates:")
    print(f'ones: {len(ones)}\n'
          f'twos: {len(twos)}\n'
          f'threes: {len(threes)}\n'
          f'fours: {len(fours)}\n'
          f'fives: {len(fives)}\n'
          f'sixes: {len(sixes)}\n'
          f'others: {len(others)}\n')

    print("Uniques:")
    print(f'ones: {len(set(ones))}\n'
          f'twos: {len(set(twos))}\n'
          f'threes: {len(set(threes))}\n'
          f'fours: {len(set(fours))}\n'
          f'fives: {len(set(fives))}\n'
          f'sixes: {len(set(sixes))}\n'
          f'others: {len(set(others))}\n')


def json_to_dict(json_string):
    return json.loads(json_string)


def load_freq_list():
    """ Load English word frequency list """

    # Map difficulty levels to integers
    level_dictionary = {
        'A1': 1,
        'A2': 2,
        'B1': 3,
        'B2': 4,
        'C1': 5,
        'C2': 6
    }

    frequency_list = dict()
    with open("Resources/Kelly_English.csv", 'r') as f:
        for line in f:
            # Each line in f is formatted: <rank>,<word>,<pos>,<level>
            line_split = line.split(',')
            rank = int(line_split[0])
            word = line_split[1].lower()
            pos = line_split[2]
            level = level_dictionary[line_split[3][:-1]]
            frequency_list[word.lower()] = Word(rank, word, pos, level)
    return frequency_list


if __name__ == '__main__':
    # Check for correct argument(s)
    if len(sys.argv) < 2:
        print(f'USAGE: {sys.argv[0]} <project_name>')
        exit(0)
    project_name = sys.argv[1]

    main(project_name)
