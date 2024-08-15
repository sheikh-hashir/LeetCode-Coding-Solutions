# Intuition
- The goal is to determine the average processing time for each machine by calculating the difference between the `end` and `start` activity timestamps for the same process on the same machine.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Self-join:**
  - Join the `Activity` table with itself to pair `start` and `end` activities for the same machine and process.
- **Timestamp difference:**
  - Calculate the time difference between `end` and `start` activities.
- **Aggregation:**
  - Group by `machine_id` and compute the average processing time for each machine.

# Code
```
# Write your MySQL query statement below
SELECT a2.machine_id, round(avg(a1.timestamp - a2.timestamp), 3) as processing_time FROM Activity a1 INNER JOIN Activity a2 ON a1.machine_id = a2.machine_id and a1.process_id = a2.process_id and a1.activity_type = "end" and a2.activity_type = "start" group by a2.machine_id

```