# Intuition
- To determine which user has the highest number of requests, either sent or received, we need to aggregate all request activities for each user and then find the user with the maximum count.
- The challenge is to efficiently handle the union of requests where a user could be either a requester or an accepter.


<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Combine Requests:**
  - Use a Common Table Expression (CTE) to unify the `requester_id` and `accepter_id` into a single list of user IDs. This step combines both the requests sent and received by each user into one dataset.
- **Count Occurrences:**
  - Group the unified list of user IDs and count the occurrences of each user. This count represents the total number of requests each user has been involved in.
- **Find the Maximum Count:**
  - Order the results by the count in descending order and limit the result to the top record to get the user with the highest number of requests.

<!-- Describe your approach to solving the problem. -->


# Code
```mysql []
WITH virtualrequestaccepted AS
(
       SELECT requester_id AS id FROM   requestaccepted
       UNION ALL
       SELECT accepter_id AS id FROM   requestaccepted
)
SELECT   id, Count(*) AS num
FROM     virtualrequestaccepted
GROUP BY id
ORDER BY num DESC limit 1
```