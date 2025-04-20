"""781. Rabbits in Forest"""

from collections import Counter
from math import ceil
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)

        return sum((key + 1) * ceil(val / (key + 1)) for key, val in counter.items())
