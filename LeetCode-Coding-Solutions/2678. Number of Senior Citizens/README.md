# Approach
- **Extract Age:**
  - For each string in the list, extract the substring that represents the age.
- **Convert and Compare:**
  - Convert the extracted substring to an integer and check if it's greater than 60.
- **Count Seniors:**
  - Use a generator expression within the `sum` function to count how many times the age exceeds 60.
<!-- Describe your approach to solving the problem. -->

# Code
```
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 if int(detail[11:13]) > 60 else 0 for detail in details)
```