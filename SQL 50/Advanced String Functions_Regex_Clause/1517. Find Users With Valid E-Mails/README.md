# Intuition
- To find valid email addresses from the users table, we need to check several conditions:
- The email must end with `@leetcode.com`.
- The first character before the `@` must be an alphabet letter.
- The local part (before the `@`) can only contain letters, digits, underscores, hyphens, and periods.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Check the Ending:**
  - Use the LIKE operator to confirm that the email ends with `@leetcode.com`.
- **First Character Validation:**
  - Use `LEFT(mail, 1)` to ensure the first character of the local part is a letter.
- **Local Part Validation:**
  - Extract the local part using `SUBSTRING_INDEX(mail, '@', 1)` and check if it only contains valid characters using a regular expression.
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
SELECT user_id,
       name,
       mail
FROM   users
WHERE  mail LIKE '%@leetcode.com'
       AND LEFT(mail, 1) REGEXP '^[a-zA-Z]'
       AND LEFT(mail, Length(mail) - 13) NOT REGEXP '[^A-Za-z0-9._-]'

```