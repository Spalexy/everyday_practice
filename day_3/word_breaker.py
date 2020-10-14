
def word_breaker(sticky_list) -> list:
    separated_list = []
    for element in sticky_list:
        separated_item = element.split(' ')
        separated_list.extend(separated_item)
    return separated_list


data_array = ["apple banana", "orange", "banana", "kiwi strawberry blueberry"]

print(word_breaker(data_array))
