--select year, month, sum(pax) sum_pax
--from air_traffic
--where year = 2022
--group by year, month
--having sum_pax > 80000000
--order by year, month;

--with pax_subset as (
--    select
--    year, month, pax,
--    row_number() over (order by year, month, pax desc) as rn
--    from air_traffic
--)
--select year, month, pax, rn from pax_subset where rn >= 240;

--with pax_subset as (
--    select
--    year, month, pax,
--    rank() over (order by year, month, pax desc) as rank
--    from air_traffic
--)
--select year, month, pax, rank from pax_subset where rank >= 240;

with pax_subset as (
    select
    year, pax,
    ntile(4) over (partition by year order by pax) as quartile
    from air_traffic
),
quart as (
    select year, quartile, sum(pax) as sum_pax
    from pax_subset
    group by year, quartile
)
select year, quartile, sum_pax
from quart
where quartile in (1,4)
and year >=2022;
