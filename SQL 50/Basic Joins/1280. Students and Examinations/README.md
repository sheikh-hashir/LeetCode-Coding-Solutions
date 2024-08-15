# Intuition
- To determine how many exams each student has attended for each subject, we need to list all combinations of students and subjects, then count the number of attended exams.
- This approach ensures that we account for all possible student-subject pairs, even if a student has not attended any exams for a particular subject.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Generate All Student-Subject Pairs:**
  - Use `CROSS JOIN` to create a Cartesian product of students and subjects, ensuring every student is paired with every subject.
- **Count Attended Exams:**
  - Use `LEFT JOIN` to link the examinations table to the student-subject pairs, counting the number of exams attended by each student for each subject.
- **Group and Order Results:**
  - Group by student ID, student name, and subject name to get the count of attended exams for each pair. Order the results by student ID and subject name for better readability.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT s.student_id,
       s.student_name,
       sub.subject_name,
       count(e.subject_name) as attended_exams
FROM Students s
    CROSS JOIN Subjects sub
    LEFT JOIN Examinations e
        ON s.student_id = e.student_id
           AND sub.subject_name = e.subject_name
GROUP BY s.student_id,
         s.student_name,
         sub.subject_name
ORDER BY s.student_id,
         sub.subject_name;

```