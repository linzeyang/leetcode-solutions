"""3842. Toggle Light Bulbs"""


class Solution:
    """
    https://leetcode.com/problems/toggle-light-bulbs/
    Weekly Contest 489
    """

    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        active_bulbs: set[int] = set()

        for bulb in bulbs:
            if bulb in active_bulbs:
                active_bulbs.remove(bulb)
            else:
                active_bulbs.add(bulb)

        return sorted(active_bulbs)
