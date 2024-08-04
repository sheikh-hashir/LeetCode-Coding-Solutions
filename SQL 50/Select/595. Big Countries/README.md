# Intuition
- The goal is to retrieve the names, populations, and areas of countries where the area is at least `3,000,000` square kilometers or the population is at least `25,000,000`.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Filter Criteria:**
  -  Use a `WHERE` clause to filter rows based on the specified conditions: `area >= 3000000` or `population >= 25000000`.
- **Select Columns:**
  - Select the `name`, `population`, and `area` columns for the rows that meet the filter criteria.
<!-- Describe your approach to solving the problem. -->

# Code
```
# Write your MySQL query statement below
SELECT name, population, area from world WHERE area >= 3000000 or population >= 25000000;

```