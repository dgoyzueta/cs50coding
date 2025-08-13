create view june_vacancies as
select l.id, l.property_type, l.host_name, count(*) as days_vacant
from listings l
join availabilities a on l.id = a.listing_id
where a.available = 'TRUE'
and a.date between '2023-06-01' and '2023-06-30'
group by l.id, l.property_type, l.host_name;
