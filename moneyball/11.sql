select p.first_name, p.last_name, (s.salary / pf.h) as "dollars per hit"
from performances pf
join salaries s on pf.player_id = s.player_id and pf.team_id = s.team_id
join players p on p.id = pf.player_id
where pf.year = 2001 and pf.year = s.year
and pf.h <> 0
order by "dollars per hit", p.first_name, p.last_name
limit 10;
