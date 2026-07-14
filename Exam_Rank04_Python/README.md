# Exam RANK04- Python Common Core

> LeetCode-style Python exam. 4 questions, medium difficulty.
> Order matters, alphabetical tie-breaking, edge cases are key.

---

## Exercise 1 — `constellation_mapper`

**Subject:** Given a list of `(row, col)` coordinates and a `size`, build a `size x size` grid of `"."` and mark valid coordinates with `"*"`. Return each row as a string inside a list.

```python
def constellation_mapper(coordinates: list[tuple[int, int]], size: int) -> list[list[str]]:
    grid = [["." for _ in range(size)] for _ in range(size)]
    for r, c in coordinates:
        if 0 <= r < size and 0 <= c < size:
            grid[r][c] = "*"
    return [["".join(row)] for row in grid]
```

**Examples:**
```python
constellation_mapper([(0, 0)], 3)              # → [["*.."], ["..."], ["..."]]
constellation_mapper([(0, 0), (1, 2), (2, 1)], 3) # → [["*.."], ["..*"], [".*."]]
constellation_mapper([(-1, 0), (0, 0), (3, 3)], 3) # → [["*.."], ["..."], ["..."]]
constellation_mapper([], 2)                    # → [[".."], [".."]]
constellation_mapper([(0, 0)], 1)              # → [["*"]]
```

**Key points:**
- Out-of-bounds coordinates are silently ignored
- Return format is `[["row_string"], ...]` — each row wrapped in its own list

---

## Exercise 2 — `resolve_dependencies`

**Subject:** Given a dictionary of packages and their dependencies, return the valid installation order (dependencies first). Skip packages with missing deps. Return `[]` if there are cycles. Alphabetical order for tie-breaking.

**Algorithm: Kahn's Algorithm (Topological Sort with BFS)**
1. Calculate `in_degree` (how many dependencies each node has)
2. Start with nodes that have `in_degree = 0` (no dependencies)
3. Install them and reduce `in_degree` of their dependents
4. Use a heap to maintain alphabetical order on ties
5. If not all nodes are installed at the end → cycle detected → return `[]`

```python
import heapq

def resolve_dependencies(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    valid = set(packages)
    skip = {p for p, d in packages.items() if any(x not in valid for x in d)}
    prev = None
    while prev != skip:
        prev = skip.copy()
        skip |= {p for p, d in packages.items() if p not in skip and any(x in skip for x in d)}

    nodes = valid - skip
    in_degree = {n: 0 for n in nodes}
    adj = {n: [] for n in nodes}
    for p in nodes:
        for dep in packages[p]:
            adj[dep].append(p)
            in_degree[p] += 1

    heap = [n for n in nodes if in_degree[n] == 0]
    heapq.heapify(heap)
    result = []
    while heap:
        curr = heapq.heappop(heap)
        result.append(curr)
        for dep in adj[curr]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                heapq.heappush(heap, dep)

    return result if len(result) == len(nodes) else []
```

**Examples:**
```python
{"A": ["B"], "B": ["C"], "C": []}                          # → ["C", "B", "A"]
{"Z": [], "M": [], "A": []}                                 # → ["A", "M", "Z"]
{"App": ["LibraryX", "LibraryY"], "LibraryX": ["Core"],
 "LibraryY": ["Core"], "Core": []}                         # → ["Core", "LibraryX", "LibraryY", "App"]
{"ValidPackage": [], "BrokenPackage": ["GhostDep"]}        # → ["ValidPackage"]
{"chicken": ["egg"], "egg": ["chicken"]}                   # → []
{"X": ["A", "Y"], "Y": ["X"], "A": []}                    # → [] (cycle, even though A is valid)
{}                                                          # → []
```

**Key points:**
- Packages depending on invalid/missing packages are also skipped (propagation)
- If ANY cycle exists in the graph → return `[]`
- Alphabetical tie-breaking via `heapq`

---

## Exercise 3 — `find_common_elements`

**Subject:** Given a list of lists of integers, return the elements that appear in ALL lists. Return `[]` if input is empty or there are no common elements.

```python
def find_common_elements(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    return list(common)
```

**Examples:**
```python
[[1, 2, 3], [2, 4, 5], [6, 2, 7]]   # → [2]
[[1, 2], [3, 4], [5, 6]]             # → []
[[1, 2, 3], [3, 2, 1], [2, 1, 3]]   # → [1, 2, 3] (any order)
[]                                    # → []
[[1, 2], [], [1, 2, 3]]             # → []
[[1, 2, 2, 3]]                       # → [1, 2, 3] (duplicates removed)
```

**Key points:**
- `set` automatically removes duplicates
- One empty sublist makes the intersection empty
- Order doesn't matter in the output (`assertCountEqual`)

---

## Exercise 4 — `min_cuts_no_modules`

**Subject:** Given a string, return the minimum number of cuts so that every part is a palindrome. No external modules allowed.

**Algorithm: Top-down DP with memoization**
- Try every prefix that is a palindrome
- Recursively solve the remaining suffix
- Cache results to avoid recomputation

```python
def min_cuts_no_modules(s: str) -> int:
    if not s or s == s[::-1]:
        return 0

    memo = {}

    def dp(sub: str) -> int:
        if sub in memo:
            return memo[sub]
        if sub == sub[::-1]:
            return 0
        result = min(
            1 + dp(sub[i:])
            for i in range(1, len(sub))
            if sub[:i] == sub[:i][::-1]
        )
        memo[sub] = result
        return result

    return dp(s)
```

**Examples:**
```python
""          # → 0
"a"         # → 0
"racecar"   # → 0
"ab"        # → 1   ("a" | "b")
"abc"       # → 2   ("a" | "b" | "c")
"aab"       # → 1   ("aa" | "b")
"aabcb"     # → 1   ("aa" | "bcb")
"abacd"     # → 2   ("aba" | "c" | "d")
"ababbbabbababa" # → 3
```

**Key points:**
- Check palindrome with `s == s[::-1]`
- Memoization is essential for long strings (otherwise timeout)
- No imports needed

---

## Exercise 5 — `max_sliding_window`

**Subject:** Given a list of integers and a window size `k`, return the maximum value of each sliding window.

```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []
    result = []
    for i in range(len(nums) - k + 1):
        curr_window = nums[i:i+k]
        result.append(max(curr_window))
    return result
```

**Examples:**
```python
([1, 3, -1, -3, 5, 3, 6, 7], 3)  # → [3, 3, 5, 5, 6, 7]
([1, 2, 3, 4], 1)                  # → [1, 2, 3, 4]
([1, 3, -1, -3, 5], 5)            # → [5]
([], 3)                            # → []
([1, 2, 3], 0)                     # → []
([7, 7, 7, 7], 2)                  # → [7, 7, 7]
```

**Key points:**
- `range(len(nums) - k + 1)` gives exactly the right number of windows
- Guard against empty list and invalid `k`
- Simple O(n*k) solution is clean and sufficient for the exam

---

## General Tips for Exam Rank 04

- Always handle **edge cases first** (empty input, invalid params)
- Check the **exact return format** — `[["str"]]` vs `["str"]` can fail tests
- **Order matters** when specified — sort or use `heapq` for alphabetical
- **Memoization** is your friend for recursive problems
- Read the test file carefully — `assertEqual` vs `assertCountEqual` tells you if order matters