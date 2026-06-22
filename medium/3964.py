"""
3964. Minimum Lights to Illuminate a Road

https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

Biweekly Contest 185
"""

from math import ceil


class Solution:
    def minLights(self, lights: list[int]) -> int:
        illuminated_sections: list[tuple[int, int]] = []

        for idx, light in enumerate(lights):
            if not light:
                continue

            illuminated_section: tuple[int, int] = (
                max(0, idx - light),
                min(len(lights), idx + light),
            )

            if illuminated_sections:
                last_section: tuple[int, int] = illuminated_sections[-1]

                if illuminated_section[0] - last_section[1] > 1:
                    illuminated_sections.append(illuminated_section)
                else:
                    new_section: tuple[int, int] = (
                        min(last_section[0], illuminated_section[0]),
                        max(last_section[1], illuminated_section[1]),
                    )
                    illuminated_sections[-1] = new_section
            else:
                illuminated_sections.append(illuminated_section)

        if not illuminated_sections:
            return ceil(len(lights) / 3)

        out: int = 0

        if illuminated_sections[0][0] > 0:
            out += ceil(illuminated_sections[0][0] / 3)

        if illuminated_sections[-1][1] < len(lights) - 1:
            out += ceil((len(lights) - 1 - illuminated_sections[-1][1]) / 3)

        for idx in range(len(illuminated_sections) - 1):
            section: tuple[int, int] = illuminated_sections[idx]
            next_section: tuple[int, int] = illuminated_sections[idx + 1]
            out += ceil((next_section[0] - section[1] - 1) / 3)

        return out
