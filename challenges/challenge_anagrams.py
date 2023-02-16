def merge_sort(input_string: str):
    if len(input_string) <= 1:
        return input_string

    mid = len(input_string) // 2

    left = merge_sort(input_string[:mid])
    right = merge_sort(input_string[mid:])

    return merge(left, right)


def merge(left: str, right: str):
    result_list = []
    char_left_list = list(left)
    char_right_list = list(right)

    while len(char_left_list) > 0 and len(char_right_list) > 0:
        if char_left_list[0] < char_right_list[0]:
            result_list.append(char_left_list.pop(0))
        else:
            result_list.append(char_right_list.pop(0))

    if char_left_list == []:
        result_list += char_right_list
    else:
        result_list += char_left_list

    result_string = "".join(result_list)

    return result_string


def is_anagram(first_string, second_string):
    first_string_ordered = merge_sort(first_string.lower())
    second_string_ordered = merge_sort(second_string.lower())

    if not first_string or not second_string:
        return (first_string_ordered, second_string_ordered, False)

    return (
        first_string_ordered,
        second_string_ordered,
        first_string_ordered == second_string_ordered,
    )
