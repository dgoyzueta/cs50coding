select movies.title
from stars m1
join stars m2
on m1.movie_id = m2.movie_id
join movies on m1.movie_id = movies.id
where m1.person_id in (select id from people where name = 'Bradley Cooper')
and m2.person_id in (select id from people where name = 'Jennifer Lawrence')
order by movies.title;
