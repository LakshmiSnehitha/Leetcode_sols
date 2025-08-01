-- Last updated: 8/1/2025, 9:07:14 AM
# Write your MySQL query statement below
select teacher_id, count(distinct subject_id)as cnt from Teacher group by teacher_id ;