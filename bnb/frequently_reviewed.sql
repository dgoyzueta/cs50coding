create view frequently_reviewed as
select l.id, l.property_type, l.host_name, count(*) as reviews
from listings l
join reviews r on l.id = r.listing_id
group by l.id, l.property_type, l.host_name
order by reviews desc, l.property_type, l.host_name limit 100;
