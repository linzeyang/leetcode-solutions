"""386. Lexicographical Numbers"""

from typing import List


# This runs faster
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)


# This runs slower

# from functools import cmp_to_key


# def comp(lhs: int, rhs: int) -> int:
#     l_str = str(lhs)
#     r_str = str(rhs)

#     for idx in range(min(len(l_str), len(r_str))):
#         if l_str[idx] < r_str[idx]:
#             return -1
#         elif l_str[idx] > r_str[idx]:
#             return 1

#     if len(l_str) < len(r_str):
#         return -1

#     return 1

# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         return sorted(range(1, n + 1), key=cmp_to_key(comp))
