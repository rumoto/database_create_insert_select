import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:********@localhost:5432/music_site')
connection = engine.connect()

connection.execute("""create table if not exists genre (
		id serial primary key,
		name varchar(40)
		);
		create table if not exists singer (
		id serial primary key,
		name varchar(40)
);

create table if not exists singer_genre (
		singer_id integer references singer(id),
		genre_id integer references genre(id),
		constraint pk primary key (singer_id, genre_id)
);

create table if not exists album (
		id serial primary key,
		name varchar(40),
		year integer
);

create table if not exists album_singer (
		singer_id integer references singer(id),
		album_id integer references album(id),
		constraint pk1 primary key (singer_id, album_id)
);

create table if not exists track (
		id serial primary key,
		album_id integer references album(id),
		name varchar(40),
		duration integer
);

create table if not exists music_collection (
		id serial primary key,
		name varchar(40),
		year integer
);

create table if not exists track_collection (
		track_id integer references track(id),
		collection_id integer references music_collection(id),
		constraint pk2 primary key (track_id, collection_id)
);

""")

connection.execute("""INSERT INTO genre (name)
            VALUES ('Поп'),
                   ('Рок'),
                   ('Рэп'),
                   ('Электронная музыка'),
                   ('Шансон');""")

connection.execute("""INSERT INTO singer (name)
              VALUES ('Лолита'),
                     ('Дискотека Авария'),
                     ('Филипп Киркоров'),
                     ('Нюша'),
                     ('Любэ'),
                     ('Дима Билан'),
                     ('Валерия'),
                     ('Руки Вверх');""")

connection.execute("""INSERT INTO album (name, year)
              VALUES ('Лето', 2018),
                     ('Осень', 2019),
                     ('Зима', 2001),
                     ('Весна', 2009),
                     ('Лучший альбом', 2018),
                     ('От души', 2022),
                     ('Альбом1', 2018),
                     ('Альбом2', 2017);""")

connection.execute("""INSERT INTO track (album_id, name, duration)
              VALUES (1, 'Трек1', 220),
                     (2, 'Мой трек', 120),
                     (3, 'My track', 300),
                     (4, 'Мой любимый трек', 280),
                     (5, 'Трек2', 219),
                     (6, 'Трек3', 210),
                     (7, 'Трек4', 260),
                     (8, 'Трек5', 200),
                     (1, 'Трек6', 120),
                     (2, 'Трек7', 190),
                     (3, 'Трек8', 230),
                     (4, 'Самый длинный трек', 420),
                     (5, 'Трек10', 320),
                     (6, 'Трек11', 180),
                     (7, 'Трек12', 170);""")

connection.execute("""INSERT INTO music_collection (name, year)
              VALUES ('Сборник1', 2018),
                     ('Сборник2', 2019),
                     ('Сборник3', 2001),
                     ('Сборник4', 2009),
                     ('Сборник5', 2020),
                     ('Сборник6', 2022),
                     ('Сборник7', 2018),
                     ('Сборник8', 2017);""")

sel1 = connection.execute("""SELECT name, year FROM album
           WHERE year = 2018;
           """).fetchall()
print('Название и год выхода альбомов, вышедших в 2018 году: ', sel1)

sel2 = connection.execute("""SELECT name, duration FROM track
           ORDER BY duration DESC;
           """).fetchone()
print('название и продолжительность самого длительного трека: ', sel2)

sel3 = connection.execute("""SELECT name FROM track
           WHERE duration >= 210;
           """).fetchall()
print('название треков, продолжительность которых не менее 3,5 минуты: ', sel3)

sel4 = connection.execute("""SELECT name FROM music_collection
           WHERE year BETWEEN 2018 AND 2020;
           """).fetchall()
print('названия сборников, вышедших в период с 2018 по 2020 год включительно: ', sel4)

sel5 = connection.execute("""SELECT name FROM singer
           WHERE name NOT LIKE '%% %%';
           """).fetchall()
print('исполнители, чье имя состоит из 1 слова: ', sel5)

sel6 = connection.execute("""SELECT name FROM track
           WHERE name iLIKE '%%мой%%';
           """).fetchall()
print('название треков, которые содержат слово "мой"/"my":', sel6)