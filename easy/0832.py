"""832. Flipping an Image"""

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[int(not pixel) for pixel in reversed(row)] for row in image]
