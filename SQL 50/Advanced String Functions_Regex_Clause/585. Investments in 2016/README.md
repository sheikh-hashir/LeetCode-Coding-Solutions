# Intuition
- We need to calculate the sum of `tiv_2016` for specific conditions:
  - The `tiv_2015` value must appear more than once across different records.
  - The location (latitude and longitude) must appear only once across all records.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Filter records based on `tiv_2015`:**
  - We select only those records where `tiv_2015` is duplicated, which can be done by using `GROUP BY` and `HAVING` with a count condition.
- **Filter records based on unique locations:**
  - We further narrow the selection by ensuring that the latitude (`lat`) and longitude (`lon`) of the records appear exactly once across all records, again using `GROUP BY` and `HAVING`.
- **Final result:**
  - We sum the `tiv_2016` values for records meeting both conditions (duplicated `tiv_2015` and unique `lat`, `lon` pairs).
<!-- Describe your approach to solving the problem. -->

# Code
```mysql []
# Write your MySQL query statement below
SELECT Round(Sum(tiv_2016), 2) AS tiv_2016
FROM   insurance
WHERE  tiv_2015 IN (SELECT tiv_2015
                    FROM   insurance
                    GROUP  BY tiv_2015
                    HAVING Count(*) > 1)
       AND ( lat, lon ) IN (SELECT lat,
                                   lon
                            FROM   insurance
                            GROUP  BY lat,
                                      lon
                            HAVING Count(*) = 1);
```