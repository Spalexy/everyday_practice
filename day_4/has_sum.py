
def has_sum(nums, target):
    lookup = []
    for i, num in enumerate(nums):
        if target - num in lookup:
            return True
        lookup.append(num)


list_of_numbers = [1, 2, 4, 7, 2, 5, 25, 64, 4, 5, 6, 1, 1, 1, 1, 1]
target_sum = 5

has_sum(list_of_numbers, target_sum)
