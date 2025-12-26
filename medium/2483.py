"""2483. Minimum Penalty for a Shop"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty: int = customers.count("Y")  # idx = 0
        min_penalty: int = penalty
        best_idx: int = 0

        for idx, char in enumerate(customers, start=1):
            match char:
                case "Y":
                    penalty -= 1
                case "N":
                    penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                best_idx = idx

        return best_idx
