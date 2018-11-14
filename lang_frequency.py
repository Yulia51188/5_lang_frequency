from collections import Counter
import argparse
import string


def get_most_frequent_words(text, output_word_count):
    letter_text = text.lower()
    for symbol in string.punctuation:
        letter_text.replace(symbol, ' ')
    word_list = letter_text.split()
    word_statistic = Counter(word_list).most_common(output_word_count)
    return word_statistic


def parse_arguments():
    parser = argparse.ArgumentParser(description='The word frequency counter.')
    parser.add_argument(
        'text_file', type=argparse.FileType(),
        help='a path to the text file where the script counts word frequency'
    )
    parser.add_argument(
        '-c', '--output_word_count', type=int, default=10,
        help='how many words with statistic print as a result'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    text = args.text_file.read()
    if text is '':
        exit("The file is empty")
    for word, frequency in get_most_frequent_words(text, args.output_word_count):
        print('{word} - {frequency}'.format(word=word, frequency=frequency))
