select s.name
from districts d join schools s on d.id = s.district_id
where d.name = 'Cambridge'
order by s.name;
