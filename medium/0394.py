"""394. Decode String"""


class Solution:
    def decodeString(self, s: str) -> str:
        str_list: list[str] = []
        segment_stack: list[list[str]] = []
        digit_stack: list[str] = []
        num_stack: list[int] = []

        for char in s:
            if char.isalpha():
                if not num_stack:
                    str_list.append(char)
                else:
                    segment_stack[-1].append(char)
            elif char.isdigit():
                digit_stack.append(char)
            elif char == "[":
                num_stack.append(int("".join(digit_stack)))
                digit_stack = []
                segment_stack.append([])
            else:
                sub_string = "".join(segment_stack.pop())
                num = num_stack.pop()

                if segment_stack:
                    segment_stack[-1].append(sub_string * num)
                else:
                    str_list.append(sub_string * num)

        return "".join(str_list)
