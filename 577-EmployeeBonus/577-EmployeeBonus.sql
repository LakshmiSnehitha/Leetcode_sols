-- Last updated: 7/30/2025, 8:14:17 PM
# Write your MySQL query statement below
-- select e.name,b.bonus from Employee e  JOIN Bonus b on e.empId =b.empId WHERE b.bonus<1000;
select e.name, b.bonus from Employee e LEFT JOIN Bonus b on e.empId = b.empId where b.bonus<1000 or b.bonus IS NULL;

