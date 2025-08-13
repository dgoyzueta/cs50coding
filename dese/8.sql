select d.name, sum(e.pupils) as num_of_pupils
from districts d join expenditures e on d.id = e.district_id
group by d.name
order by d.name;
