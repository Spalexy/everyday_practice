import string


def get_shift(char_index, operation_type):
    if operation_type == 'encoding':
        shift = char_index + 1
    elif operation_type == 'decoding':
        shift = char_index - 1
    else:
        raise ValueError
    return shift


def get_modified_string(str_to_operation, string_template, operation_type):
    new_str = []
    letters = string_template.format(string.ascii_lowercase)
    for char in str_to_operation:
        is_upper = char.isupper()
        if char.isalpha() and not is_upper:
            char_index = letters.index(char)
            new_str.append((letters[get_shift(char_index, operation_type)]).capitalize())
        elif char.isalpha():
            char_index = letters.index(char.lower())
            new_str.append((letters[get_shift(char_index, operation_type)]))
        else:
            new_str.append(char)
    return ''.join(new_str)


def get_encoded_text(str_to_encode):
    return get_modified_string(str_to_encode, '{}a', 'encoding')


def get_decoded_text(str_to_decode):
    return get_modified_string(str_to_decode, 'a{}', 'decoding')


coded_text = get_encoded_text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
decoded_text = get_decoded_text(coded_text)
print(coded_text, decoded_text)
