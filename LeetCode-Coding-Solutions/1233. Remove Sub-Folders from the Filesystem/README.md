# Topics
- Array
- String
- Sorting

# Intuition
- The main idea is to use sorting to arrange the folders in lexicographical order.
- This way, any subfolder will immediately follow its parent folder.
- By checking prefixes, we can identify subfolders and skip them to maintain only the top-level folders.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Sort the List:**
  - Sort the `folder` list in lexicographical order. This arrangement ensures that any subfolder will appear directly after its parent folder in the sorted list.
- **Iterate through the Folders:**
  - Use a list, `result`, to store only the top-level folders.
    - For each folder f, check if it starts with the last added folder in `result` plus a `/`.
    - If it doesn't, add `f` to `result` because it’s not a subfolder of the last folder in `result`.
- **Return the Result:**
  - `result` will contain only the top-level folders, with all subfolders filtered out.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Sorting the folders takes `O(nlogn)`, where `n` is the number of folders.
  - Iterating through the folders takes `O(n)`.
  - Thus, the overall time complexity is `O(nlogn)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - The space complexity is `O(n)` to store the resulting list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders to ensure that subfolders follow their parent folders.
        folder.sort()
        result = []

        for f in folder:
            if not result or not f.startswith(f'{result[-1]}/'):
                result.append(f)

        return result

```