create table if not exists test(
    id  int  primary key,
    name text,
    age  int
);

create table if not exists school(
    userid int primary key,
    class   text
);


create table if not exists files(
    id INTEGER PRIMARY KEY autoincrement,
    name text,
    ext text,
    path text,
    size float,
    md5hash text,
    sha1hash text
)