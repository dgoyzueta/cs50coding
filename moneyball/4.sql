select players.first_name, players.last_name, salaries.salary
from players join salaries on players.id = salaries.player_id
where salaries.year = 2001
order by salaries.salary, players.first_name, players.last_name, players.id
limit 50;
