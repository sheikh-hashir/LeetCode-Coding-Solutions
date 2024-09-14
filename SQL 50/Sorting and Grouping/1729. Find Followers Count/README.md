# Intuition
- The problem asks to count the number of followers each user has in a social media database.
- The simplest approach is to group followers by their respective `user_id` and count the occurrences of each user being followed.
- This helps us easily determine the follower count for each user.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- The Followers table stores the `user_id` and `follower_id`.
- We need to count how many times each `user_id` appears in the `follower_id` column.
- Using the `COUNT()` function, we calculate the number of followers for each `user_id`.
- We apply `GROUP BY user_id` to group the results by user, and finally, `ORDER BY user_id` to sort the results.

<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT user_id, COUNT(follower_id) AS followers_count FROM Followers GROUP BY user_id ORDER BY user_id;
```