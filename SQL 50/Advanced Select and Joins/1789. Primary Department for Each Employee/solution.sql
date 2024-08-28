SELECT
    e.employee_id,
    CASE
        WHEN COUNT(e.employee_id) = 1 THEN e.department_id
        ELSE (
            SELECT department_id
            FROM Employee
            WHERE employee_id = e.employee_id
            AND primary_flag = 'Y'
        )
    END AS department_id
FROM
    Employee e
GROUP BY
    e.employee_id;
