"""
3921. Score Validator

https://leetcode.com/problems/score-validator/

Biweekly Contest 182
"""


class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score: int = 0
        counter: int = 0

        for event in events:
            if event.isdigit():
                score += int(event)
            elif event == "W":
                counter += 1
            else:
                score += 1

            if counter == 10:
                break

        return [score, counter]
