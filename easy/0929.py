"""929. Unique Email Addresses"""

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ss = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = "".join(local.split("."))
            ss.add((local, domain))

        return len(ss)
