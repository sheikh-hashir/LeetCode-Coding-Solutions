# Topics
- Array
- Hash Table
- Sorting
- Python3

# Intuition
- The goal is to transform an array by replacing each element with its rank when sorted.
- The rank represents the position of the number in the sorted array, with no duplicate ranks for duplicate numbers.
- The idea is simple:
  - Sort the array, assign ranks to unique elements, and then map these ranks back to the original array.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Sort and Remove Duplicates:**
  - First, create a sorted list of unique elements from the input array. This will allow us to rank each element based on its position in the sorted order.

- **Create Rank Mapping:**
  - Create a dictionary that maps each unique element to its rank (starting from 1). The rank is essentially the index in the sorted list plus 1.

- **Transform the Array:**
  - For each element in the original array, replace it with its corresponding rank from the dictionary.

- **Steps:**
  - Sort the unique elements of the array to get their rank.
  - Use a dictionary to store each element’s rank.
  - Iterate through the original array and replace each element with its rank using the dictionary.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Sorting the array takes `O(nlogn)`, where `n` is the number of elements in the array.
  - Creating the rank dictionary and transforming the array both take linear time, `O(n)`.
  - Hence, the overall time complexity is `O(nlogn)` due to sorting.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - We need extra space for the dictionary and the sorted array, both of which take `O(n)` space.
  - Therefore, the space complexity is `O(n)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(set(arr))
        rank_dict = {val: idx + 1 for idx, val in enumerate(sorted_array)}
        return [rank_dict[num] for num in arr]

```