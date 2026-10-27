import unittest


def constellation_mapper(coordinates: list[tuple[int, int]], size: int) -> list[list[str]]:
    ...


class TestConstellationMapper(unittest.TestCase):

    def test_example_case(self):
        # Testing the original example provided
        self.assertEqual(
            constellation_mapper([(0, 0)], 3), 
            [["*.."], ["..."], ["..."]]
        )

    def test_multiple_stars(self):
        # Testing multiple stars within bounds
        self.assertEqual(
            constellation_mapper([(0, 0), (1, 2), (2, 1)], 3), 
            [["*.."], ["..*"], [".*."]]
        )

    def test_out_of_bounds_tuples(self):
        # Testing that coordinates outside the limits are safely skipped
        self.assertEqual(
            constellation_mapper([(-1, 0), (0, 0), (3, 3), (1, 5)], 3), 
            [["*.."], ["..."], ["..."]]
        )

    def test_empty_coordinates(self):
        # Testing with an empty list of coordinates
        self.assertEqual(
            constellation_mapper([], 2), 
            [[".."], [".."]]
        )

    def test_size_one(self):
        # Testing the smallest possible matrix size
        self.assertEqual(
            constellation_mapper([(0, 0)], 1), 
            [["*"]]
        )
        self.assertEqual(
            constellation_mapper([], 1), 
            [["."]]
        )


if __name__ == "__main__":
    unittest.main()