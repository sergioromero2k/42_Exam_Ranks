"""Te dan varias listas que ya vienen ordenadas, y tienes que juntarlas en una sola lista que también esté ordenada de menor a mayor."""


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    nums = [x for lst in lists for x in lst]
    results = []
    while nums:
        m = min(nums)
        nums.remove(m)
        results.append(m)
    return results
