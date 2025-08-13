select distinct d.name, per_pupil_expenditure
from districts d
join expenditures e on d.id = e.district_id
join schools s on d.id = s.district_id
where s.type = 'Public School'
order by per_pupil_expenditure desc
limit 10;
