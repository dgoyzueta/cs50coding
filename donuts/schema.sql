create table ingredients (
    id integer,
    ingredient text not null,
    unit text not null,
    price numeric not null check(price >= 0),
    primary key(id)
);

create table donuts (
    id integer,
    donut_name text not null,
    gluten_free integer not null,
    price numeric not null check(price >= 0),
    primary key(id)
);

create table ingredients_per_donut (
    donut_id integer not null,
    ingredient_id integer not null,
    units_applied integer not null,
    primary key(donut_id, ingredient_id),
    foreign key(donut_id) references donuts(id),
    foreign key(ingredient_id) references ingredients(id)
);

create table customers (
    id integer,
    first_name text not null,
    last_name text not null,
    primary key(id)
);

create table orders (
    id integer,
    customer_id integer not null,
    order_datetime numeric not null default current_timestamp,
    sale_channel text not null,
    total_qty integer not null check(total_qty >= 0),
    total_price numeric not null check(total_price >= 0),
    tax numeric not null check(tax >= 0),
    total_after_tax numeric not null check(total_after_tax >= 0),
    primary key(id),
    foreign key(customer_id) references customers(id)
);

create table orders_detail (
    order_id integer not null,
    donut_id integer not null,
    qty integer not null check(qty >= 0),
    price numeric not null check(price >= 0),
    primary key(order_id, donut_id),
    foreign key(order_id) references orders(id),
    foreign key(donut_id) references donuts(id)
)
