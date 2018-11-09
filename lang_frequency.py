import sys
import os
from collections import Counter

WORD_COUNT = 10
PUNCTUATION_SET = ('.', ',', ':', '(', ')', '#', ' - ', '[',']', '"', '@', '—', ';')


def load_data_from_file(filepath):
    with open(filepath, 'r') as file_object:
        str_data = file_object.read()
    if str_data == '':
        return None
    return str_data


def get_most_frequent_words(text):
    letter_text = text.lower()
    for symbol in PUNCTUATION_SET:
        letter_text.replace(symbol, ' ')
    word_list = letter_text.split()
    word_statistic = Counter(word_list).most_common(WORD_COUNT)
    return word_statistic


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        exit('No filepath received as argument')
    if not os.path.exists(sys.argv[1]):
        exit("File doesn't exist")
    text = load_data_from_file(sys.argv[1])
    if text is None:
        exit("Can't read text from file")
    for word_stat in get_most_frequent_words(text):
        print('{word} - {count}'.format(word=word_stat[0],
                                        count=word_stat[1]))
