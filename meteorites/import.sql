.import --csv meteorites.csv temp

create table meteorites (
    id integer,
    name text,
    class text,
    mass numeric,
    discovery text,
    year integer,
    lat numeric,
    long numeric,
    primary key(id)
);

insert into meteorites (name, class, mass, discovery, year, lat , long)
select name, class, mass, discovery, year, lat, long
from temp
where nametype != 'Relict'
order by year, name;

update meteorites set mass = NULL where mass = '';
update meteorites set year = NULL where year = '';
update meteorites set lat = NULL where lat = '';
update meteorites set long = NULL where long = '';

update meteorites set mass = round(mass, 2);
update meteorites set lat = round(lat, 2);
update meteorites set long = round(long, 2);
