"""2379. Minimum Recolors to Get K Consecutive Black Blocks"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_in_window = blocks[:k].count("W")

        out = w_in_window

        left = 0
        right = k - 1

        while right < len(blocks) - 1:
            if blocks[left] == "W":
                w_in_window -= 1
            if blocks[right + 1] == "W":
                w_in_window += 1

            out = min(out, w_in_window)

            left += 1
            right += 1

        return out
