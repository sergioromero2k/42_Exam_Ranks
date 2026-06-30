def find_common_elements(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return list(common)