# Intuition
- The goal is to calculate the percentage of users who have registered for each contest and then display the contests in descending order of their registration percentages.
- The initial thought is to join the `users` and `register` tables and calculate the percentage by dividing the number of registrations for each contest by the total number of users.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Join Tables:**
  - Use an `INNER JOIN` between the `users` and `register` tables based on `user_id` to link each registration with the respective user.
- **Count Registrations:**
  - For each contest, count the number of registered users.
- **Calculate Percentage:**
  - Calculate the percentage of users who registered for each contest by dividing the count of registrations by the total number of users and then multiplying by 100.
  - The result is rounded to two decimal places.
- **Group and Order:**
  - Group the results by `contest_id`, and then order the contests by the calculated percentage in descending order. If two contests have the same percentage, order them by `contest_id`.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT r.contest_id,
       Round(( Count(r.contest_id) / (SELECT Count(user_id)
                                      FROM   users) * 100 ), 2) AS percentage
FROM   users u
       INNER JOIN register r
               ON u.user_id = r.user_id
GROUP  BY r.contest_id
ORDER  BY percentage DESC,
          r.contest_id
```