"""3633. Earliest Finish Time for Land and Water Rides I"""

from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        # land first
        min_land_finish = min(
            start + duration
            for start, duration in zip(landStartTime, landDuration, strict=False)
        )
        min_land = min(
            max(min_land_finish, start) + waterDuration[jdx]
            for jdx, start in enumerate(waterStartTime)
        )

        # water first
        min_water_finish = min(
            start + duration
            for start, duration in zip(waterStartTime, waterDuration, strict=False)
        )
        min_water = min(
            max(min_water_finish, start) + landDuration[jdx]
            for jdx, start in enumerate(landStartTime)
        )

        return min(min_land, min_water)
