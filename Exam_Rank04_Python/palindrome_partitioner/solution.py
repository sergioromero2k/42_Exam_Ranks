# Recursión con memoización (top-down DP)
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