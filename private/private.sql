create table cipher (
    id integer,
    sentence integer,
    character integer,
    length integer,
    primary key(id)
);

insert into cipher (sentence, character, length) values
(14,98,4),
(114,3,5),
(618,72,9),
(630,7,3),
(932,12,5),
(2230,50,7),
(2346,44,10),
(3041,14,5);

create view message as
select substr(s.sentence, c.character, c.length) as phrase
from sentences s
join cipher c on s.id = c.sentence;
