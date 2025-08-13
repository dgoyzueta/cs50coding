create table users (
    id integer,
    first_name text not null,
    last_name text not null,
    username text not null,
    user_pwd text not null,
    primary key(id)
);

create table schools (
    id integer,
    school_name text not null,
    school_type text not null,
    school_location text not null,
    school_year_founded numeric not null,
    primary key(id)
);

create table companies (
    id integer,
    company_name text not null,
    company_industry text not null,
    company_location text not null,
    primary key(id)
);

create table connection_to_users (
    id integer,
    user_id integer not null,
    user_id_linked integer not null,
    primary key(id),
    foreign key(user_id) references users(id),
    foreign key(user_id_linked) references users(id)
);

create table connection_to_schools (
    id integer,
    user_id integer not null,
    school_id integer not null,
    start_attending_date numeric not null,
    graduation_date numeric not null,
    degree_type text not null,
    primary key(id),
    foreign key(user_id) references users(id),
    foreign key(school_id) references schools(id)
);

create table connection_to_companies (
    id integer,
    user_id integer not null,
    company_id integer not null,
    start_date_employment numeric not null,
    end_date_employment numeric not null,
    title text not null,
    primary key(id),
    foreign key(user_id) references users(id),
    foreign key(company_id) references companies(id)
);
