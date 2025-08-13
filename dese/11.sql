select s.name, per_pupil_expenditure, g.graduated
from districts d
join expenditures e on d.id = e.district_id
join schools s on d.id = s.district_id
join graduation_rates g on s.id = g.school_id
order by per_pupil_expenditure desc, s.name;
