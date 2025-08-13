select d.name
from districts d join expenditures e on d.id = e.district_id
where e.pupils = (select min(pupils) from expenditures)
group by d.name
order by d.name;
