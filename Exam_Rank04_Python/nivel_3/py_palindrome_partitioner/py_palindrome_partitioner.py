# Recursión con memoización (top-down DP)
# def palindrome_splitter(s: str) -> int:
def min_cuts_no_modules(s: str) -> int:
    n = len(s)
    cuts = list(range(-1, n))
    for c in range(n):
        for r in (c, c + 1):
            l = c
            while l >= 0 and r < n and s[l] == s[r]:
                cuts[r + 1] = min(cuts[r + 1], cuts[l] + 1)
                l, r = l - 1, r + 1
    return max(cuts[n], 0)
