# Intuition
- The problem requires us to find the classes that have at least 5 students enrolled.
- This suggests a `GROUP BY` clause to aggregate the students by class and a `HAVING` clause to filter the classes that meet the required threshold.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Group by class:**
  - We'll group the rows by the `class` field to get the student count per class.
- **Count the students:**
  - For each class, we'll count the number of students using the `COUNT()` function.
- **Filter classes with at least 5 students:**
  - We'll use the `HAVING` clause to only select the classes where the student count is greater than or equal to `5`.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5;
```