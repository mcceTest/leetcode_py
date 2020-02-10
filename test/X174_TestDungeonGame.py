import unittest
from X174_DungeonGame import Solution


class TestSum(unittest.TestCase):

    def test1(self):
        sol = Solution()
        dungeon = [
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5]
        ]
        self.assertEqual(sol.calculateMinimumHP(dungeon), 7)

    def test2(self):
        sol = Solution()
        dungeon = [
            [ -5]
        ]
        self.assertEqual(sol.calculateMinimumHP(dungeon), 6)

    def test3(self):
        sol = Solution()
        dungeon = [
            [0, -3]
        ]
        self.assertEqual(sol.calculateMinimumHP(dungeon), 4)


if __name__ == "__main__":
    unittest.main()