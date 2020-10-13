import json
import functools


def get_pure_text(text_to_purifying: str, black_list_words: list) -> str:
    pure_text = text_to_purifying
    for word in black_list_words:
        pure_text = pure_text.replace(word, '***')
    return pure_text


def get_short_text(text_to_cropping: str, max_length: int) -> str:
    continuation = ''
    if len(text_to_cropping) > max_length:
        continuation = '...'
    short_text = '{0}{1}'.format(text_to_cropping[0:(max_length + 1)], continuation)
    return short_text


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs), ensure_ascii=False)
    return wrapped


@to_json
def text_analyzer_improved(text_to_analyze: str, max_length: int, black_list_words: list) -> dict:
    return {
        'length': len(text_to_analyze),
        'pure_length': len(text_to_analyze.replace(' ', '')),
        'origin_text': text_to_analyze,
        'pure_text': get_pure_text(text_to_analyze, black_list_words),
        'pure_short_text': get_short_text(text_to_analyze, max_length),
    }


text = '"Не забывайте о том, что все великие волшебники в истории в свое время были такими же, ' \
       'как мы, – школьниками. Если у них получилось, то получится и у нас", – Гарри Поттер.'
maxlen = 35
forbidden_words = ["волшебники", "Гарри Поттер"]

print(text_analyzer_improved(text, maxlen, forbidden_words))
