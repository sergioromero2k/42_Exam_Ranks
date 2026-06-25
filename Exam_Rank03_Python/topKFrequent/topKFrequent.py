def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = {}

    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [num for num, _ in sorted_items[:k]]
