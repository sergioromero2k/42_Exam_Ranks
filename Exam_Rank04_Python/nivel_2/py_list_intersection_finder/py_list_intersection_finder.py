def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    """"""
    result = []
    if not lists:
        return []
    for i in lists[0]:
        if i not in result and all(i in lst for lst in lists[1:]):
            result.append(i)
    return result
