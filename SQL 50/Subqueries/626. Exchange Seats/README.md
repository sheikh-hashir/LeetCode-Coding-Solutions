# Intuition
- The goal is to find the student sitting in the seat with a given ID, considering a specific pattern.
- If the ID is even, we look for the student in the preceding seat (i.e., ID - 1).
- If the ID is odd, we check the next seat (i.e., ID + 1) and use the current seat's student if the next seat is unavailable.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- For each seat ID, determine if it is even or odd.
- If the ID is even, retrieve the student from the seat with ID - 1.
- If the ID is odd, retrieve the student from the seat with ID + 1. If the seat with ID + 1 does not exist, use the student from the current seat.
- Use a `CASE` statement to handle the two scenarios and `IFNULL` to handle cases where the next seat is not available.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT s.id,
       CASE
         WHEN s.id % 2 = 0 THEN (SELECT student
                                 FROM   Seat
                                 WHERE  id = s.id - 1)
         ELSE IFNULL((SELECT student
                      FROM   Seat
                      WHERE  id = s.id + 1), s.student)
       END student
FROM   Seat s
```