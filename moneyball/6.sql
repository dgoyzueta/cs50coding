select distinct t.name, sum(pr.h) as "total hits"
from performances pr
join teams t on t.id = pr.team_id
where pr.year = 2001
group by t.name
order by "total hits" desc
limit 5;
