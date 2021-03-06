from collections import Counter
import argparse
import string
import os


def load_data_from_file(filepath):
    with open(filepath, 'r') as file_object:
        str_data = file_object.read()
    return str_data


def get_most_frequent_words(text, output_word_count):
    letter_text = text.lower()
    for symbol in string.punctuation:
        letter_text.replace(symbol, ' ')
    word_list = letter_text.split()
    word_statistic = Counter(word_list).most_common(output_word_count)
    return word_statistic


def check_is_natural(input_string, default_value=10):
    if not input_string.isdigit():
        return default_value
    if int(input_string) > 0:
        return int(input_string)
    else:
        return default_value


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='The word frequency counter.'
    )
    parser.add_argument(
        'filepath',
        type=str,
        help='a path to the text file where the script counts word frequency'
    )
    parser.add_argument(
        '-c',
        '--output_word_count',
        type=check_is_natural,
        default=10,
        help='how many words with statistic print as a result'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if not os.path.exists(args.filepath):
        exit("File doesn't exist")
    text = load_data_from_file(args.filepath)
    if text is '':
        exit("The file is empty")
    for word, frequency in get_most_frequent_words(text, args.output_word_count):
        print('{word} - {frequency}'.format(word=word, frequency=frequency))
