create table products (
    id integer primary key,
    name text not null,
    price integer no null
);
insert into products (id, name, price)
values (1, "jablko", 5)

insert into products (id, name, price)
values (2, "gruszka", 20)

insert into products (id, name, price)
values (3, "banan", 10)

insert into products (id, name, price)
values (4, "arbuz", 25)

insert into products (id, name, price)
values (5, "ananas", 29)

select * from products

select * from products where price > 20

select * from products sortby(price)

update price from products where id = 1

delete from products where id = 2