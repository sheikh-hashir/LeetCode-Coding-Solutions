# Intuition
- The goal is to retrieve patient information from the `Patients` table where the conditions field contains a specific condition code, `"DIAB1"`. The condition might appear at the beginning or somewhere in the middle of the `conditions` string.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Select Relevant Columns:**
  - Retrieve columns `patient_id`, `patient_name`, and `conditions` from the `Patients` table.

- **Filter by Conditions:**
  - Use the `LIKE` operator to filter rows where the `conditions` field contains the string `"DIAB1"`:
    - LIKE `"DIAB1%"` checks if `"DIAB1"` is at the start of the conditions string.
    - LIKE `"% DIAB1%"` checks if `"DIAB1"` appears anywhere in the middle of the `conditions` string, preceded by a space.
<!-- Describe your approach to solving the problem. -->


# Code
```mysql []
SELECT patient_id,
       patient_name,
       conditions
FROM   Patients
WHERE  conditions LIKE "DIAB1%"
        OR conditions LIKE "% DIAB1%"

```