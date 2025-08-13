select p.first_name, p.last_name, s.salary, pf.hr, s.year
from players p
join salaries s on p.id = s.player_id
join performances pf on p.id = pf.player_id
where s.year = pf.year
order by p.id, s.year desc, pf.hr desc, s.salary desc;
