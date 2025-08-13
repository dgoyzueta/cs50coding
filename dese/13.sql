select sch.*, s.exemplary
from schools sch
join staff_evaluations s on sch.district_id = s.district_id
where s.exemplary > 75
order by s.exemplary desc
