create table users (
    id int auto_increment,
    first_name varchar(20) not null,
    last_name varchar(30) not null,
    username varchar(20) not null,
    user_pwd varchar(30) not null,
    primary key(id)
);

create table schools (
    id smallint auto_increment,
    school_name varchar(50) not null,
    school_type varchar(20) not null,
    school_location varchar(50) not null,
    school_year_founded date not null,
    primary key(id)
);

create table companies (
    id smallint auto_increment,
    company_name varchar(50) not null,
    company_industry varchar(20) not null,
    company_location varchar(50) not null,
    primary key(id)
);

create table connection_to_users (
    id int auto_increment,
    user_id int not null,
    user_id_linked int not null,
    primary key(id),
    foreign key(user_id) references users(id),
    foreign key(user_id_linked) references users(id)
);

create table connection_to_schools (
    id int auto_increment,
    user_id int not null,
    school_id smallint not null,
    start_attending_date date not null,
    graduation_date date not null,
    degree_type varchar(20) not null,
    primary key(id),
    foreign key(user_id) references users(id),
    foreign key(school_id) references schools(id)
);

create table connection_to_companies (
    id int auto_increment,
    user_id int not null,
    company_id smallint not null,
    start_date_employment date not null,
    end_date_employment date not null,
    title varchar(30) not null,
    primary key(id),
    foreign key(user_id) references users(id),
    foreign key(company_id) references companies(id)
);
