# Intuition
- To format user names consistently while retrieving user information, we need to ensure that each name starts with an uppercase letter followed by all lowercase letters.
- This can be achieved using SQL string manipulation functions to adjust the case of each name properly.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Format the Name:**
  - Use SQL string functions to convert the first character of the `name` to uppercase and the remaining characters to lowercase.
  - This is done using `UPPER()` and `LOWER()` functions along with `SUBSTRING()` to extract and transform the appropriate parts of the name.
- **Retrieve and Sort Data:**
  - Select the `user_id` and the formatted `name`, and then order the results by `user_id` to ensure they are listed in ascending order.
<!-- Describe your approach to solving the problem. -->



# Code
```mysql []
# Write your MySQL query statement below
SELECT user_id,
       CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2,
                                                  LENGTH(name)))) AS
       name
FROM   Users ORDER BY user_id

```