--explain query plan
select users.username
from users
join messages on users.id = messages.to_user_id
group by users.username
order by count(*) desc
limit 1;
