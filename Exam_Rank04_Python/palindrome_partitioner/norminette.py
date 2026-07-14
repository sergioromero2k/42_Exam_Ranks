import unittest


def min_cuts_no_modules(s: str) -> int:
    ...


# --- The Testing Suite ---
class TestPalindromePartitioning(unittest.TestCase):

    def test_empty_and_single_chars(self):
        """Edge cases: Strings that require no cuts by default."""
        self.assertEqual(min_cuts_no_modules(""), 0)
        self.assertEqual(min_cuts_no_modules("a"), 0)
        self.assertEqual(min_cuts_no_modules("z"), 0)

    def test_already_palindromes(self):
        """Strings that are already palindromes (both even and odd lengths)."""
        self.assertEqual(min_cuts_no_modules("aa"), 0)
        self.assertEqual(min_cuts_no_modules("aba"), 0)
        self.assertEqual(min_cuts_no_modules("racecar"), 0)
        self.assertEqual(min_cuts_no_modules("xxyyxx"), 0)

    def test_worst_case_no_palindromes(self):
        """Strings where every character is unique (requires cuts between every letter)."""
        self.assertEqual(min_cuts_no_modules("ab"), 1)        # "a" | "b"
        self.assertEqual(min_cuts_no_modules("abc"), 2)       # "a" | "b" | "c"
        self.assertEqual(min_cuts_no_modules("abcdef"), 5)    # 6 letters, 5 cuts

    def test_mixed_palindromes(self):
        """Standard cases requiring a mix of logic and backtracking."""
        self.assertEqual(min_cuts_no_modules("aab"), 1)       # "aa" | "b"
        self.assertEqual(min_cuts_no_modules("abac"), 1)      # "aba" | "c"
        self.assertEqual(min_cuts_no_modules("aaba"), 1)      # "a" | "aba"
        
        # Here is the corrected aabcb test:
        self.assertEqual(min_cuts_no_modules("aabcb"), 1)     # "aa" | "bcb"
        
        # And here is a string that legitimately requires exactly 2 cuts:
        self.assertEqual(min_cuts_no_modules("abacd"), 2)     # "aba" | "c" | "d"     

    def test_complex_memoization_cases(self):
        """Longer strings that will fail (timeout) without the memory dictionary."""
        # "ababbbabbababa" -> "a" | "babbbab" | "b" | "ababa" ... wait, the optimal is 3 cuts
        self.assertEqual(min_cuts_no_modules("ababbbabbababa"), 3)

        # A long string with many overlapping subproblems
        long_string = "a" * 20 + "b" * 20 + "a" * 20
        # "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaa"
        # It's a massive palindrome on its own, but we'll add some noise to the end
        noisy_long_string = long_string + "cd"
        self.assertEqual(min_cuts_no_modules(noisy_long_string), 2) # the big palindrome | "c" | "d"


if __name__ == '__main__':
    # This runs the tests and prints the results nicely to the console
    unittest.main(verbosity=2)