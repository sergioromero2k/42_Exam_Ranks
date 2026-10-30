"""Intercalar los elementos de varias listas, respetando su orden."""


def interleave_lists(lists: list[list]) -> list:
    result = []
    max_len = 0

    for lst in lists:
        if len(lst) > max_len:
            max_len = len(lst)

    for i in range(max_len):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])
    return result
