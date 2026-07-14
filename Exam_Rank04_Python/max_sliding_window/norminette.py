import unittest


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    ...


class TestMaxSlidingWindow(unittest.TestCase):

    def test_standard_case(self):
        # Sliding window of size 3
        # [1,3,-1] -> 3
        # [3,-1,-3] -> 3
        # [-1,-3,5] -> 5
        # [-3,5,3] -> 5
        # [5,3,6] -> 6
        # [3,6,7] -> 7
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3, 3, 5, 5, 6, 7])

    def test_window_size_one(self):
        # When k = 1, each window is just the element itself
        nums = [1, 2, 3, 4]
        k = 1
        self.assertEqual(max_sliding_window(nums, k), [1, 2, 3, 4])

    def test_window_size_equals_length(self):
        # When k matches the list length, it should just return the maximum of the entire list
        nums = [1, 3, -1, -3, 5]
        k = 5
        self.assertEqual(max_sliding_window(nums, k), [5])

    def test_empty_list(self):
        # Testing an empty input list
        self.assertEqual(max_sliding_window([], 3), [])

    def test_invalid_k(self):
        # Testing when k is 0 or negative
        nums = [1, 2, 3]
        self.assertEqual(max_sliding_window(nums, 0), [])
        self.assertEqual(max_sliding_window(nums, -1), [])

    def test_all_identical_elements(self):
        # Testing a list where all numbers are the same
        nums = [7, 7, 7, 7]
        k = 2
        self.assertEqual(max_sliding_window(nums, k), [7, 7, 7])


if __name__ == "__main__":
    unittest.main()