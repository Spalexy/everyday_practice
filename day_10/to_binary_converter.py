
def convert_to_binary(number):
    binary = ''
    while number > 0:
        binary = '{0}{1}'.format(str(number % 2), binary)
        number = number // 2
    return '{0}{1}'.format('0b', binary)
