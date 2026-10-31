def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    nums = [x for lst in lists for x in lst]
    results = []
    while nums:
        m = min(nums)
        nums.remove(nums)
        results.append(m)
    return results


def merge_sorted_lists_2(lists: list[list[int]]) -> list[int]:
    nums = [x for l in lists for x in l]
    result = []
    while nums:
        k = my_min_index(nums)
        del nums[k]
        result.append(nums[k])
    return result


def my_min_index(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] < nums[k]:
            k = i
    return k
