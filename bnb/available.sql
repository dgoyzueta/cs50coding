create view available as
select l.id, l.property_type, l.host_name, a.date
from listings l
join availabilities a on l.id = a.listing_id
where a.available = 'TRUE';
