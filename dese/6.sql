select s.name
from schools s join graduation_rates g on s.id = g.school_id
where graduated = 100
order by s.name;
