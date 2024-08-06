# Intuition
- The task requires finding days in the weather dataset where the temperature on the next day is higher than the current day.
- This involves comparing each day's temperature with the temperature of the subsequent day.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Self-join:**
  - Join the `Weather` table with itself to compare the temperatures of consecutive days.
- **Date difference:**
  - Use `DATEDIFF` to ensure that we are only comparing temperatures of consecutive days.
- **Temperature comparison:** Check if the temperature on the next day is higher than the current day's temperature.
<!-- Describe your approach to solving the problem. -->

# Code
```
SELECT w1.id AS Id FROM Weather w JOIN Weather w1 ON DATEDIFF(w1.recordDate, w.recordDate) = 1 WHERE w1.temperature > w.temperature;
```