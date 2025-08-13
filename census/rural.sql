create view rural as
select id, district, locality, families, households, population, male, female
from census
where locality like '%Rural%';
