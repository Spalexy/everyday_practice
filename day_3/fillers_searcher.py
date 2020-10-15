import string
from functools import wraps
from json import dumps
from collections import Counter


def get_string_exclude_punctuation(string_to_exclude_punctuation) -> str:
    exclude = set(string.punctuation)
    return ''.join(char for char in string_to_exclude_punctuation if char not in exclude).lower()


def get_words_counter(string_to_count_words) -> Counter:
    return Counter([''.join(filter(str.isalpha, x))
                    for x in string_to_count_words.split() if ''.join(filter(str.isalpha, x))])


def to_json(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return dumps(func(*args, **kwargs), ensure_ascii=False)
    return wrapped


@to_json
def fillers_searcher(test_to_search_fillers, max_amount) -> dict:
    word_count_dictionary = dict(
        get_words_counter(
            get_string_exclude_punctuation(test_to_search_fillers)))
    keys_to_remove = [key for key, value in word_count_dictionary.items() if int(value) < max_amount]

    for key in keys_to_remove:
        del word_count_dictionary[key]
    return word_count_dictionary


text = "Ну что ж я, я найти решения правильного не смогу ж? Смогу ж конечно, я ж старательный все ж таки."

print(fillers_searcher(text, 3))
