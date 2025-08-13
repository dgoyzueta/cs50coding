select s.salary
from salaries s
where s.year = 2001
and s.player_id in (select player_id from performances pr where year = 2001 order by hr desc limit 1);
