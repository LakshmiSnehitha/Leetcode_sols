-- Last updated: 7/28/2025, 3:29:23 PM
# Write your MySQL query statement below
select unique_id,name from employees left join employeeuni on employeeuni.id=employees.id ;