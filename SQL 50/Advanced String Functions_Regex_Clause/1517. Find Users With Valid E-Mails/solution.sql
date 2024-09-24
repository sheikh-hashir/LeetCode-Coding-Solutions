SELECT user_id,
       name,
       mail
FROM   users
WHERE  mail LIKE '%@leetcode.com'
       AND LEFT(mail, 1) REGEXP '^[a-zA-Z]'
       AND LEFT(mail, Length(mail) - 13) NOT REGEXP '[^A-Za-z0-9._-]'
