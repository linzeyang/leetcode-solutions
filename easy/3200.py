"""3200. Maximum Height of a Triangle"""


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        pool_1 = [red, blue]
        pool_2 = pool_1[:]

        # red first
        level_1 = 0
        is_blue = False

        while pool_1[is_blue] - level_1 > 0:
            level_1 += 1
            pool_1[is_blue] -= level_1
            is_blue = not is_blue

        # blue first
        level_2 = 0
        is_blue = True

        while pool_2[is_blue] - level_2 > 0:
            level_2 += 1
            pool_2[is_blue] -= level_2
            is_blue = not is_blue

        return max(level_1, level_2)
