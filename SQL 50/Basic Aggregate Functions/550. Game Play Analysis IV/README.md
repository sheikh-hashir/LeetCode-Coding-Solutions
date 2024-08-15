# Intuition
- The problem involves calculating the fraction of players who used their device on the day immediately following their first activity.
- The goal is to find out how many players were active on the day after their first recorded activity and determine the ratio of such players to the total number of unique players.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Find the Earliest Event for Each Player:**
  - First, determine the earliest event (activity) date for each player.
- **Calculate Next Day Activity:**
  - Join the `Activity` table with itself to find records where the player was active exactly one day after their first activity.
- **Calculate the Fraction:**
  - Count the number of players who have such next-day activities and divide by the total number of unique players.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT
    ROUND(COUNT(DISTINCT a1.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
    Activity a
INNER JOIN
    (SELECT player_id, MIN(event_date) AS min_event_date
     FROM Activity
     GROUP BY player_id) a1
ON
    a.player_id = a1.player_id
WHERE
    DATEDIFF(a.event_date, a1.min_event_date) = 1;

```