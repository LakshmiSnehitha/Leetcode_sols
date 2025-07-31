-- Last updated: 7/31/2025, 10:46:22 AM
# Write your MySQL query statement below
update Salary set sex=
CASE sex
       when 'm' then 'f'
       else 'm'
end