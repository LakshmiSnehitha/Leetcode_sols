-- Last updated: 8/4/2025, 7:28:06 PM
-- # Write your MySQL query statement below
-- select P.product_name,S.year,S.price from Sales S left join Product P on S.product_id = P.product_name

SELECT P.product_name, S.year, S.price
FROM Sales S
JOIN Product P ON S.product_id = P.product_id;
