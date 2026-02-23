"""3848. Check Digitorial Permutation"""

from collections import Counter
from math import factorial


class Solution:
    """
    https://leetcode.com/problems/check-digitorial-permutation/
    Weekly Contest 490
    """

    def isDigitorialPermutation(self, n: int) -> bool:
        fac_sum: int = sum(factorial(int(char)) for char in str(n))

        return Counter(str(fac_sum)) == Counter(str(n))
