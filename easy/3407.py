"""3407. Substring Matching Pattern"""

import re


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p.startswith("*"):
            return p[1:] in s

        if p.endswith("*"):
            return p[:-1] in s

        left, right = p.split("*")

        idx = s.find(left)

        if idx == -1:
            return False

        return right in s[idx + len(left) :]


# much slower:
class Solution2:
    def hasMatch(self, s: str, p: str) -> bool:
        if len(p) - 1 > len(s):
            return False

        pattern = re.compile(p.replace("*", "[a-z]*"))

        return bool(re.findall(pattern, s))
