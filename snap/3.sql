--explain query plan
select messages.to_user_id
from users
join messages on users.id = messages.from_user_id
where username = 'creativewisdom377'
group by messages.to_user_id
order by count(*) desc
limit 3;
