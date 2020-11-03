def check_if_numbers_in_list(list_to_checking: list) -> bool:
    numbers = {13, 41}
    return set(list_to_checking).issuperset(numbers)


print(check_if_numbers_in_list((13, 4, 41)))
