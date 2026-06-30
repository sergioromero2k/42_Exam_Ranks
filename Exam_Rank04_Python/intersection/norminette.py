import unittest


def find_common_elements(lists: list[list[int]]) -> list[int]:
    ...


class TestFindCommonElements(unittest.TestCase):

    def test_basic_common_elements(self):
        # 2 is in all three lists; 1 and 3 are not
        input_lists = [[1, 2, 3], [2, 4, 5], [6, 2, 7]]
        # Using set comparison in assertCountEqual because order doesn't matter
        self.assertCountEqual(find_common_elements(input_lists), [2])

    def test_no_common_elements(self):
        # No single number exists across all three lists
        input_lists = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(find_common_elements(input_lists), [])

    def test_all_elements_common(self):
        # All elements match exactly
        input_lists = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
        self.assertCountEqual(find_common_elements(input_lists), [1, 2, 3])

    def test_empty_input(self):
        # Testing an empty outer list
        self.assertEqual(find_common_elements([]), [])

    def test_one_empty_sublist(self):
        # One empty list means the total intersection must be empty
        input_lists = [[1, 2], [], [1, 2, 3]]
        self.assertEqual(find_common_elements(input_lists), [])

    def test_single_sublist(self):
        # Only one list provided should return its own unique elements
        input_lists = [[1, 2, 2, 3]]
        self.assertCountEqual(find_common_elements(input_lists), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()