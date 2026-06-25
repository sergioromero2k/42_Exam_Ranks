# topKFrequent
---

Write a function
```
topKFrequent(nums: list[int], k: int) -> list[int] 
```
that returns the k most frequent elements in the input list nums. The elements should be sorted by frequency in descending order. If multiple elements have the same frequency, their relative order does not matter.

The function should:

* Count how many times each number appears in the list
* Sort the elements by frequency (highest to lowest)
* Return the top k most frequent elements as a list

Example:
```
topKFrequent([1, 2, 2, 3, 3, 3], 2) → [3, 2]
```