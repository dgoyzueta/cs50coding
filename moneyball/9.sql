select (select name from teams where id = s.team_id) as name,
       round(avg(s.salary), 2) as "average_salary"
from salaries s
where s.year = 2001
group by name
order by "average_salary"
limit 5;
