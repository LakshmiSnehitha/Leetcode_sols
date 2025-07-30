-- Last updated: 7/30/2025, 8:14:32 PM
# Write your MySQL query statement below
select c.name as Customers from Customers c  left join Orders o  on c.id = o.customerId where o.id is null ;
