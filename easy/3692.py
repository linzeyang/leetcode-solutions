"""3692. Majority Frequency Characters"""

from collections import Counter


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter: Counter[str] = Counter(s)

        freq_dict: dict[int, list[str]] = {}

        for char, freq in counter.items():
            if freq not in freq_dict:
                freq_dict[freq] = [char]
            else:
                freq_dict[freq].append(char)

        max_count: int = max(len(val) for val in freq_dict.values())

        candidates: dict[int, list[str]] = {
            k: v for k, v in freq_dict.items() if len(v) == max_count
        }

        max_k: int = max(candidates.keys())

        return "".join(candidates[max_k])
