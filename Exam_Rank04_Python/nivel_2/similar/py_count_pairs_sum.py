def count_pairs_sum(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    count = 0

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            count += 1
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return count