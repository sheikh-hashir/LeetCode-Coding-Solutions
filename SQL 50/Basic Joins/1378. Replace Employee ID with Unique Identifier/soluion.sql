select eu.unique_id, e.name from Employees e left join EmployeeUNI eu ON e.id = eu.id
