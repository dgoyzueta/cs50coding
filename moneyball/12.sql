with lowest_dollars_per_hit as (
    select pf.player_id,
        (s.salary / pf.h) as dollars_per_hit
    from performances pf
    join salaries s on pf.player_id = s.player_id and pf.team_id = s.team_id
    where pf.year = 2001 and pf.year = s.year
    and pf.h <> 0
    order by dollars_per_hit
    limit 10
),
lowest_dollars_per_rbi as (
    select pf.player_id,
        (s.salary / pf.rbi) as dollars_per_rbi
    from performances pf
    join salaries s on pf.player_id = s.player_id and pf.team_id = s.team_id
    where pf.year = 2001 and pf.year = s.year
    and pf.rbi <> 0
    order by dollars_per_rbi
    limit 10
)
select first_name, last_name
from players
join lowest_dollars_per_hit h on id = h.player_id
join lowest_dollars_per_rbi r on id = r.player_id
where h.player_id = r.player_id
order by id;
