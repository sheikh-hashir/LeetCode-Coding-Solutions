from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders to ensure that subfolders follow their parent folders.
        folder.sort()
        result = []

        for f in folder:
            if not result or not f.startswith(f"{result[-1]}/"):
                result.append(f)

        return result
