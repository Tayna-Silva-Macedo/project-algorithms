from collections import Counter


def is_valid_list(array):
    return array and isinstance(array, list)


def is_all_numbers(array):
    return all((isinstance(number, int)) for number in array)


def is_all_positive(array):
    return all((number > 0) for number in array)


def find_duplicate(nums):
    if (
        not is_valid_list(nums)
        or not is_all_numbers(nums)
        or not is_all_positive(nums)
    ):
        return False

    number, quantity = Counter(nums).most_common()[0]

    if quantity == 1:
        return False

    return number
