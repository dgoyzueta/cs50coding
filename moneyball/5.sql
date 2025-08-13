select distinct t.name
from players p
join performances pr on p.id = pr.player_id
join teams t on t.id = pr.team_id
where p.first_name = 'Satchel' and p.last_name = 'Paige'
order by t.name;
