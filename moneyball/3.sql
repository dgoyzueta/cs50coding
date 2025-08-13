select performances.year, performances.hr
from players join performances on players.id = performances.player_id
where players.first_name = 'Ken' and players.last_name = 'Griffey'
and players.birth_year = 1969
order by 1 desc;
