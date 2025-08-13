select bats,
       throws,
       round(avg(height),2) as avg_height,
       round(avg(weight),2) as avg_weight
from players
where strftime('%Y',final_game) between '2020' and '2022'
group by bats, throws
order by bats, throws;
