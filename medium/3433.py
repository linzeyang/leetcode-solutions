"""3433. Count Mentions Per User"""

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda ele: (int(ele[1]), int(ele[0] == "MESSAGE")))

        out: dict[int, int] = dict.fromkeys(range(numberOfUsers), 0)

        offline_id_ts: dict[int, int] = {}

        for event in events:
            event_type, ts, rest = event

            ts = int(ts)

            offline_ids = list(offline_id_ts.keys())

            for oid in offline_ids:
                if ts - offline_id_ts[oid] >= 60:
                    del offline_id_ts[oid]

            if event_type == "MESSAGE":
                if rest == "ALL":
                    for uid in out:
                        out[uid] += 1
                elif rest == "HERE":
                    for uid in out:
                        if uid not in offline_id_ts:
                            out[uid] += 1
                else:
                    mentioned = [int(part[2:]) for part in rest.split(" ")]

                    for men in mentioned:
                        out[men] += 1

            else:  # OFFLINE
                offline_id_ts[int(rest)] = ts

        return list(out.values())
