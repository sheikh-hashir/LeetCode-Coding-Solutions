# Intuition
- To retrieve the IDs of tweets with content longer than 15 characters, we need to filter the tweets based on the length of their content.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Filter by Length:**
  - Use the `LENGTH` function to check the length of the tweet content.
- **Select Tweet IDs:**
  - Retrieve the `tweet_id` for tweets where the content length exceeds 15 characters.

# Code
```
# Write your MySQL query statement below
SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;

```