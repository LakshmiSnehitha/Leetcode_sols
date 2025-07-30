-- Last updated: 7/30/2025, 8:41:27 PM
# Write your MySQL query statement below
-- select * from Person where 
-- delete * from Person  group by email having count(email)>1
-- DELETE p1 FROM Person p1
-- JOIN Person p2 
-- ON p1.email = p2.email AND p1.id > p2.id;

delete p1 from Person p1
join Person p2 on p1.email =p2.email Where p1.id > p2.id