select salaries.year, salaries.salary
from players join salaries on players.id = salaries.player_id
where first_name = 'Cal' and last_name = 'Ripken'
order by 1 desc;
