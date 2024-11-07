import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Initialize a new 'bonus' column to 0 for all employees
    employees["bonus"] = 0

    # Assign the 'salary' as 'bonus' where conditions are met (name does not start with 'M' and employee_id is odd)
    employees.loc[
        (~employees["name"].str.startswith("M")) & (employees["employee_id"] % 2 == 1),
        "bonus",
    ] = employees["salary"]
    # Return only the 'employee_id' and 'bonus' columns
    return employees[["employee_id", "bonus"]].sort_values(
        by="employee_id", ascending=True
    )
