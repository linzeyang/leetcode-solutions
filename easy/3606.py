"""3606. Coupon Code Validator"""

from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        candidates: list[tuple[str, str]] = []

        for idx, cod in enumerate(code):
            if not self._is_valid_code(cod):
                continue

            if businessLine[idx] not in (
                "electronics",
                "grocery",
                "pharmacy",
                "restaurant",
            ):
                continue

            if not isActive[idx]:
                continue

            candidates.append((cod, businessLine[idx]))

        candidates.sort(key=lambda tup: (tup[1], tup[0]))

        return [cand[0] for cand in candidates]

    def _is_valid_code(self, code: str) -> bool:
        if not code:
            return False

        for char in code:
            if not (
                "a" <= char <= "z"
                or "A" <= char <= "Z"
                or "0" <= char <= "9"
                or char == "_"
            ):
                return False

        return True
