select first_name, last_name
from players
where strftime('%Y',final_game) = '2022'
order by first_name, last_name;
