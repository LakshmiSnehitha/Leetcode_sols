-- Last updated: 7/30/2025, 8:14:35 PM
# Write your MySQL query statement below
select p.firstName,p.lastName ,a.city,a.state from Person p LEFT JOIN Address a on p.personId=a.personId;