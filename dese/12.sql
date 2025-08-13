with ppe_public as (
    select distinct e.district_id, e.per_pupil_expenditure
    from expenditures e join districts d on d.id = e.district_id
),
exemplary_public as (
    select distinct s.district_id, s.exemplary
    from staff_evaluations s join districts d on d.id = s.district_id
)
select d.name, ppe.per_pupil_expenditure, exem.exemplary
from districts d
join ppe_public ppe on d.id = ppe.district_id
join exemplary_public exem on d.id = exem.district_id
where d.state = 'MA' and d.type = 'Public School District'
and ppe.per_pupil_expenditure > (select avg(per_pupil_expenditure) from ppe_public)
and exem.exemplary > (select avg(exemplary) from exemplary_public)
order by exem.exemplary desc, ppe.per_pupil_expenditure desc;
