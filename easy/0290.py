"""290. Word Pattern"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")

        if len(pattern) != len(list_s):
            return False

        pattern_mapping: dict[str, list[int]] = {}

        for idx, char in enumerate(pattern):
            if char not in pattern_mapping:
                pattern_mapping[char] = [idx]
            else:
                pattern_mapping[char].append(idx)

        word_mapping: dict[str, list[int]] = {}

        for jdx, word in enumerate(list_s):
            if word not in word_mapping:
                word_mapping[word] = [jdx]
            else:
                word_mapping[word].append(jdx)

        for char, word in zip(pattern_mapping.keys(), word_mapping.keys(), strict=True):
            if pattern_mapping[char] != word_mapping[word]:
                return False

        return True
