"""1233. Remove Sub-Folders from the Filesystem"""

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        out: list[tuple[str, ...]] = []

        for fold in folder:
            if fold == "/":
                continue

            fold = tuple(fold.split("/"))

            for o in out:
                if self._is_sub(fold, o):
                    break
            else:
                out.append(fold)

        return ["/".join(o) for o in out]

    def _is_sub(self, fold: tuple, target: tuple) -> bool:
        if len(fold) <= len(target):
            return False

        for idx, part in enumerate(target):
            if fold[idx] != part:
                return False

        return True
