
def get_list_from_int(integer: int) -> list:
    list_to_return = []
    while integer > 0:
        list_to_return.append(integer % 10)
        integer = integer // 10
        list_to_return = list_to_return[::-1]
    return list_to_return


def verify_list_of_lists(verification_mask: int, list_to_verifying) -> bool:
    verification_mask = get_list_from_int(verification_mask)
    if len(verification_mask) == len(list_to_verifying):
        result = True
        for i in range(len(list_to_verifying)):
            if len(list_to_verifying[i]) != verification_mask[i]:
                result = False
                break
    else:
        result = False
    return result


print(verify_list_of_lists(122, [[1], ['apple', 4], [5, 6.4]]))
