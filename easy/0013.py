"""
13. Roman to Integer
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        base = 0

        seq = s

        while seq:
            if len(seq) == 1:
                base += mapping[seq[0]]
                break

            if seq[0] == "I":
                if seq[1] == "V":
                    base += 4
                    seq = seq[2:]
                elif seq[1] == "X":
                    base += 9
                    seq = seq[2:]
                else:
                    base += mapping["I"]
                    seq = seq[1:]
            elif seq[0] == "X":
                if seq[1] == "L":
                    base += 40
                    seq = seq[2:]
                elif seq[1] == "C":
                    base += 90
                    seq = seq[2:]
                else:
                    base += mapping["X"]
                    seq = seq[1:]
            elif seq[0] == "C":
                if seq[1] == "D":
                    base += 400
                    seq = seq[2:]
                elif seq[1] == "M":
                    base += 900
                    seq = seq[2:]
                else:
                    base += mapping["C"]
                    seq = seq[1:]
            else:
                base += mapping[seq[0]]
                seq = seq[1:]

        return base
