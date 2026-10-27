# Exam Rank 04 — Python Common Core

> LeetCode-style Python exam practice, organized by difficulty level.
> Order matters, alphabetical tie-breaking, edge cases are key.

This repository contains the subjects and my practice attempts for the Python Exam Rank 04. **No solutions are listed in this README** — each exercise folder contains its own `subject.md` with the full statement.

---

## Repository structure

```
.
├── nivel_1
│   ├── py_array_rotation_detector
│   └── py_constellation_mapper
├── nivel_2
│   ├── py_list_intersection_finder
│   └── py_merge_sorted_lists
├── nivel_3
│   ├── py_palindrome_partitioner
│   └── resolve_dependencies
├── nivel_4
│   └── py_sliding_window_maximum
└── README.md
```

Each exercise folder contains:

| File | Purpose |
|------|---------|
| `subject.md` | Full problem statement |
| `*.py` / `solution.py` | My implementation |
| `norminette.py` | Style checker (only in some folders) |

---

## Exercise overview

| Level | Exercise | Topic |
|:-----:|----------|-------|
| 1 | `py_array_rotation_detector` | Arrays / rotations |
| 1 | `py_constellation_mapper` | 2D grids |
| 2 | `py_list_intersection_finder` | Sets / intersection |
| 2 | `py_merge_sorted_lists` | Sorted sequences |
| 3 | `py_palindrome_partitioner` | Strings / dynamic programming |
| 3 | `resolve_dependencies` | Graphs / ordering |
| 4 | `py_sliding_window_maximum` | Sliding windows |

---

## Level 1

### `py_array_rotation_detector`
Work with arrays and detect rotations. See `subject.md` for the exact definition, signature and expected output.

### `py_constellation_mapper`
Given a list of `(row, col)` coordinates and a `size`, build a `size x size` grid of `"."` and mark the given coordinates with `"*"`. Return each row as a string wrapped in its own list.

```python
constellation_mapper([(0, 0), (1, 2), (2, 1)], 3)  # → [["*.."], ["..*"], [".*."]]
constellation_mapper([(-1, 0), (0, 0), (3, 3)], 3) # → [["*.."], ["..."], ["..."]]
constellation_mapper([], 2)                        # → [[".."], [".."]]
```

**Watch out for:** out-of-bounds coordinates, empty input, the exact nested return format.

---

## Level 2

### `py_list_intersection_finder`
Given a list of lists of integers, return the elements that appear in **all** of them. Return `[]` if the input is empty or nothing is shared.

```python
[[1, 2, 3], [2, 4, 5], [6, 2, 7]]  # → [2]
[[1, 2], [3, 4], [5, 6]]           # → []
[[1, 2], [], [1, 2, 3]]            # → []
[[1, 2, 2, 3]]                     # → [1, 2, 3]
```

**Watch out for:** empty input, empty sublists, duplicates, whether output order is checked.

### `py_merge_sorted_lists`
Merge sorted lists into a single sorted result. See `subject.md` for the exact signature and constraints.

---

## Level 3

### `py_palindrome_partitioner`
Given a string, return the **minimum number of cuts** needed so that every resulting part is a palindrome. No external modules allowed.

```python
""         # → 0
"racecar"  # → 0
"ab"       # → 1
"aab"      # → 1
"abacd"    # → 2
```

**Watch out for:** empty strings, strings that are already palindromes, performance on long inputs.

### `resolve_dependencies`
Given a dictionary mapping packages to their dependencies, return a valid installation order (dependencies first).

- Skip packages that depend on missing packages (and anything depending on those).
- Return `[]` if there is any cycle.
- Break ties alphabetically.

```python
{"A": ["B"], "B": ["C"], "C": []}                   # → ["C", "B", "A"]
{"Z": [], "M": [], "A": []}                         # → ["A", "M", "Z"]
{"ValidPackage": [], "BrokenPackage": ["GhostDep"]} # → ["ValidPackage"]
{"chicken": ["egg"], "egg": ["chicken"]}            # → []
{}                                                  # → []
```

**Watch out for:** missing dependencies propagating, cycles anywhere in the graph, deterministic ordering.

---

## Level 4

### `py_sliding_window_maximum`
Given a list of integers and a window size `k`, return the maximum value of each sliding window.

```python
([1, 3, -1, -3, 5, 3, 6, 7], 3)  # → [3, 3, 5, 5, 6, 7]
([1, 3, -1, -3, 5], 5)           # → [5]
([], 3)                          # → []
([1, 2, 3], 0)                   # → []
```

**Watch out for:** empty lists, `k <= 0`, `k` equal to the list length.

---

## General tips

- Handle **edge cases first**: empty input, invalid parameters, single elements.
- Check the **exact return format** — `[["str"]]` vs `["str"]` can fail tests.
- **Order matters** when the subject says so; apply alphabetical tie-breaking where required.
- Read the test file: `assertEqual` means order matters, `assertCountEqual` means it doesn't.
- Respect restrictions such as "no external modules".
- Run `norminette.py` where available before submitting.