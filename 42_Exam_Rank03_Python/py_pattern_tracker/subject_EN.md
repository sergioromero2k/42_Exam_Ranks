# py_pattern_tracker
---
Write a function
```
def pattern_tracker(text: str) -> int:
```
Count how many times two consecutive characters in the string are digits.
The second digit must be exactly one greater than the first (e.g., "1" followed by "2").

* Only consecutive positions count (no skipping characters).
* Return the total count of such patterns found in the string.

### Examples
```
pattern_tracker("12a34")   →  2
pattern_tracker("1234")    →  3
pattern_tracker("a1b2c3")  →  0
pattern_tracker("98")      →  0
```
