select city, count(*) as num_schools
from schools
where type = 'Public School'
group by city
order by num_schools desc, city
limit 10;
