"""2409. Count Days Spent Together"""


class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        if arriveAlice > leaveBob or arriveBob > leaveAlice:
            return 0

        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)

        arr_mon, arr_dat = arrive.split("-")
        lea_mon, lea_dat = leave.split("-")

        arr_mon = int(arr_mon)
        arr_dat = int(arr_dat)
        lea_mon = int(lea_mon)
        lea_dat = int(lea_dat)

        if arr_mon == lea_mon:
            return lea_dat - arr_dat + 1

        mons = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = mons[arr_mon - 1] - arr_dat + 1

        for m in range(arr_mon, lea_mon - 1):
            days += mons[m]

        days += lea_dat

        return days
