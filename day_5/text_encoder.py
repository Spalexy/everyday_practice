import string


def get_encoded_text(some_str):
    coded_str = []
    letters = '{}a'.format(string.ascii_lowercase)
    for char in some_str:
        is_upper = char.isupper()
        if char.isalpha() and not is_upper:
            char_index = letters.index(char)
            coded_str.append((letters[char_index + 1]).capitalize())
        elif char.isalpha():
            char_index = letters.index(char.lower())
            coded_str.append((letters[char_index + 1]))
        else:
            coded_str.append(char)
    return ''.join(coded_str)


def get_decoded_text(some_str):
    coded_str = []
    letters = 'a{}'.format(string.ascii_lowercase)
    for char in some_str:
        is_upper = char.isupper()
        if char.isalpha() and not is_upper:
            char_index = letters.index(char)
            coded_str.append((letters[char_index - 1]).capitalize())
        elif char.isalpha():
            char_index = letters.index(char.lower())
            coded_str.append((letters[char_index - 1]))
        else:
            coded_str.append(char)
    return ''.join(coded_str)


coded_text = get_encoded_text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
decoded_text = get_decoded_text(coded_text)
print(coded_text, decoded_text)
