CREATE TABLE IF NOT EXISTS dim_date
(
    date_id int auto_increment primary key,
    date date not null,
    year int not null,
    month int not null,
    day varchar(20) not null,
    day_type varchar(20) not null
);