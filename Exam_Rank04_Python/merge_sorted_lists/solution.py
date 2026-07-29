import heapq


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    result = []
    for lst in lists:
        result.extend(lst)
    return sorted(result)


def merge_sorted_lists2(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    return list(heapq.merge(*lists))
``