# Intuition
- The problem is to determine whether three given sides can form a valid triangle.
- My first thought is to use the basic triangle inequality theorem, which states that the sum of any two sides of a triangle must be greater than the third side.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- We will use the triangle inequality theorem to check if the given sides can form a triangle.
- For each set of sides (`x, y, z`), if `x + y > z`, `y + z > x`, and `z + x > y`, then the sides can form a triangle, and we return "Yes".
- If the sides do not satisfy the inequality conditions, we return `"No"`.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT x,
       y,
       z,
       CASE
         WHEN x + y > z
              AND y + z > x
              AND z + x > y THEN "Yes"
         ELSE "No"
       END triangle
FROM   triangle;
```
