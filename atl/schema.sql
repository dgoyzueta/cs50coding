create table passengers (
    id integer,
    first_name text not null,
    last_name text not null,
    age integer not null check(age > 0),
    primary key(id)
);

create table check_ins (
    id integer,
    passenger_id integer not null,
    checkin_datetime numeric not null default current_timestamp,
    flight_id integer not null,
    primary key(id),
    foreign key(passenger_id) references passengers(id),
    foreign key(flight_id) references flights(id)
);

create table flights(
    id integer,
    flight_number integer not null check(flight_number >= 0),
    airline_id integer not null,
    airport_departure text not null,
    airport_destination text not null,
    expected_departure numeric not null,
    expected_arrival numeric not null,
    primary key(id),
    foreign key(airline_id) references airlines(id)
);

create table airlines (
    id integer,
    airline_name text not null,
    concourse text not null check(concourse in ('A', 'B', 'C', 'D', 'E', 'F', 'T')),
    primary key(id)
);
