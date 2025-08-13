select city, count(*) as num_schools
from schools
where type = 'Public School'
group by city
having num_schools <= 3
order by num_schools desc, city;
