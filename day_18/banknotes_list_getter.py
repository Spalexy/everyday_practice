
def get_banknotes_list(requested_amount: int, need_exchange: bool) -> dict:
    available_banknotes = [100, 200, 500, 1000, 2000, 5000]
    banknotes_list = dict()

    if not need_exchange:
        get_list_with_minimum_banknotes(available_banknotes, banknotes_list, requested_amount)
    else:
        banknotes_list = dict({requested_amount // available_banknotes[0]: available_banknotes[0]})
    return banknotes_list


def get_list_with_minimum_banknotes(available_banknotes: list, banknotes_list: dict, requested_amount: int) -> dict:
    for banknote in available_banknotes[::-1]:
        banknotes_quantity = requested_amount // banknote
        if banknotes_quantity > 0:
            banknotes_list.update({banknote: banknotes_quantity})
        requested_amount -= banknote * banknotes_quantity
    return banknotes_list


print(get_banknotes_list(3400, True))
print(get_banknotes_list(3400, False))
print(get_banknotes_list(200, True))
print(get_banknotes_list(200, True))
print(get_banknotes_list(12400, False))
