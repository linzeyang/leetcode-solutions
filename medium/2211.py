"""2211. Count Collisions on a Road"""

from typing import Literal


class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        - Any L cars on the far left will never collide (they drive away to infinity).
        - Any R cars on the far right will never collide.
        - All other cars in the middle will eventually be involved in a collision
          (either directly or hitting a pile-up).
        - Every L in the middle contributes 1 collision (hits something to its left).
        - Every R in the middle contributes 1 collision (hits something to its right;
          effectively part of a chain).
        - Note: An R colliding with L counts as 2, which is mathematically consistent
          with counting the R as 1 and L as 1.
        """

        # Remove escaping Ls from left and Rs from right
        trimmed: str = directions.lstrip("L").rstrip("R")

        # All remaining moving cars (L or R) will collide
        return len(trimmed) - trimmed.count("S")


class Solution2:
    def countCollisions(self, directions: str) -> int:
        """Simulate the collisions using a stack."""

        if len(directions) < 2:
            return 0

        out: int = 0
        stack: list[Literal["R", "S"]] = []

        for direction in directions:
            match direction:
                case "L":
                    if not stack:
                        continue
                    if stack[-1] == "S":
                        out += 1
                    else:
                        out += len(stack) + 1
                        stack.clear()
                        stack.append("S")
                case "R":
                    if stack and stack[-1] == "S":
                        stack.clear()
                    stack.append("R")
                case "S":
                    if stack and stack[-1] == "S":
                        continue

                    out += len(stack)
                    stack.clear()
                    stack.append("S")

        return out
