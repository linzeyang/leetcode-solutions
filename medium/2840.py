"""2840. Check if Strings Can be Made Equal With Operations II"""


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_counter_1 = {}
        even_counter_2 = {}
        odd_counter_1 = {}
        odd_counter_2 = {}

        for idx in range(0, len(s1), 2):
            if s1[idx] not in even_counter_1:
                even_counter_1[s1[idx]] = 1
            else:
                even_counter_1[s1[idx]] += 1

            if s2[idx] not in even_counter_2:
                even_counter_2[s2[idx]] = 1
            else:
                even_counter_2[s2[idx]] += 1

        if even_counter_1 != even_counter_2:
            return False

        for idx in range(1, len(s1), 2):
            if s1[idx] not in odd_counter_1:
                odd_counter_1[s1[idx]] = 1
            else:
                odd_counter_1[s1[idx]] += 1

            if s2[idx] not in odd_counter_2:
                odd_counter_2[s2[idx]] = 1
            else:
                odd_counter_2[s2[idx]] += 1

        return odd_counter_1 == odd_counter_2
