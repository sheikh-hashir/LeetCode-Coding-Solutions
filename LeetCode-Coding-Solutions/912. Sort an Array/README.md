# Topics

- Python3
- Merge Sort
- Divide and Conquer
- Array
- Sorting

# Approach

### Merge Sort Overview

Merge Sort is a divide-and-conquer algorithm that sorts an array by recursively dividing it into smaller subarrays, sorting those subarrays, and then merging them back together in sorted order.

### **Steps**

- **Divide:** The array is divided into two halves from the middle. This division continues recursively until each subarray contains only one element (or is empty).
- **Conquer:** Each of these single-element subarrays is considered sorted. The algorithm then starts merging these small subarrays back together while sorting them.
- **Combine:** The merging process combines two sorted subarrays into a single sorted subarray. This process is repeated until the entire array is merged and sorted.

### **Implementation Details**

- **Merge Function**
  This function merges two sorted subarrays into a single sorted subarray.

  - **Inputs:** The array to be merged, the indices marking the start, middle, and end of the subarrays.

  - **Steps**:
    - Create temporary subarrays `left_array` and `right_array` from the original array.
    - Use three indices to keep track of the current position in the left subarray, the right subarray, and the merged array.
    - Compare elements from the left and right subarrays and copy the smaller element into the original array.
    - Copy any remaining elements from the left and right subarrays back into the original array.

- **MergeSort Function**
  This function recursively sorts the array.

  - **Inputs:** The array to be sorted, the starting index, and the ending index.
  - **Steps:**
    - If the starting index is greater than or equal to the ending index, return (base case for the recursion).
    - Calculate the middle index of the array.
    - Recursively call `mergeSort` on the left half of the array.
    - Recursively call `mergeSort` on the right half of the array.
    - Call the `merge` function to merge the two sorted halves.

- **Putting It All Together**
The sortArray method initializes the sorting process by calling mergeSort on the entire array.
<!-- Describe your approach to solving the problem. -->

# Complexity

- Time complexity: `O(nlogn)` because the array is divided in half for each recursive call (`log𝑛` levels of recursion) and the merge process takes linear time `(O(n))` for each level.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` for the temporary subarrays used during the merge process.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array, left, mid, right):
            left_array = array[left:mid + 1]
            right_array = array[mid + 1:right + 1]

            array_one_idx = 0  # Initial index of first sub-array
            array_two_idx = 0  # Initial index of second sub-array
            merged_array_idx = left  # Initial index of merged array

            left_array_length = len(left_array)
            right_array_length =  len(right_array)
            # Merge the temp arrays back into array[left..right]
            while array_one_idx < left_array_length and array_two_idx < right_array_length:
                if left_array[array_one_idx] <= right_array[array_two_idx]:
                    array[merged_array_idx] = left_array[array_one_idx]
                    array_one_idx += 1
                else:
                    array[merged_array_idx] = right_array[array_two_idx]
                    array_two_idx += 1
                merged_array_idx += 1

            # Copy the remaining elements of left[], if any
            while array_one_idx < left_array_length:
                array[merged_array_idx] = left_array[array_one_idx]
                array_one_idx += 1
                merged_array_idx += 1

            # Copy the remaining elements of right[], if any
            while array_one_idx < right_array_length:
                array[merged_array_idx] = right_array[array_two_idx]
                array_two_idx += 1
                merged_array_idx += 1

        def mergeSort(nums: list, start: int, end: int):
            if start >= end:
                return

            mid = start + (end - start) // 2
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums)-1)
        return nums
```
