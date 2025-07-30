-- Last updated: 7/30/2025, 8:14:34 PM
# Write your MySQL query statement below
select email from Person group by email having count(email)>1;