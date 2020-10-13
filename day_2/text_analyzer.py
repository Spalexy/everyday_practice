

def text_analyzer(text_to_analize: str, max_length: int) -> str:
    symbols_quantity_space_included = len(text_to_analize)
    symbols_quantity_space_excluded = len(text_to_analize.replace(' ', ''))
    if len(text_to_analize) % 2 == 0:
        is_even = 'четное'
    else:
        is_even = 'нечентное'
    if len(text_to_analize) > max_length:
        to_long = '\nДлина текста превышает длину {} символов'.format(max_length)
    else:
        to_long = ''

    analysis_msg = 'Количество символов в тексте: {0}\n'\
                   'Количество символов без учета пробелов: {1}\n'\
                   'Количество символов в тексте {2}{3}'\
        .format(symbols_quantity_space_included, symbols_quantity_space_excluded, is_even, to_long)

    return analysis_msg


print(text_analyzer('Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 5))
