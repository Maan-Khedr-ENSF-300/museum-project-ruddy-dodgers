-- 1) Show all tables and explain how they are related to one another (keys, triggers, etc.)
SELECT *
FROM
    information_schema.tables
WHERE
    table_schema = 'MUSEUMART';

-- show primary keys
select t.table_name, s.column_name
from information_schema.tables as t join information_schema.statistics as s 
    on s.table_schema = t.table_schema and s.table_name = t.table_name 
where t.table_schema = 'MUSEUMART' and s.index_name = 'PRIMARY';


-- show triggers
select *
from information_schema.triggers
where trigger_schema = 'MUSEUMART';

-- Show keys
select *
from information_schema.key_column_usage
where table_schema = 'MUSEUMART';


-- 2) A basic retrieval query
select *
FROM ART_OBJECT
Where Epoch = "Late Medieval"

-- 3) A retrieval query with ordered results

Select *
FROM ARTIST
ORDER BY DAte_Died desc;

-- 4) A nested retrieval query

--Show all information on art objects created by artists born after 1700 by using a nested query

select *
from ART_OBJECT as AO
where AO.artist_name in (select A.Aname
                    from artist as A
                    where A.Date_Born > 1700);

-- 5) A retrieval query using joined tables


-- Find all art made by artists whose main style is jewelry using a join table

select *
FROM (art_object join artist on artist_name = aname)
WHERE main_style = "jewelry";

-- 6) An update operation with any necessary triggers


DROP TRIGGER IF EXISTS ARTIST_TRIGGER;

CREATE TRIGGER ARTIST_TRIGGER
AFTER UPDATE ON ART_OBJECT 
FOR EACH ROW
   UPDATE ARTIST
   SET ADescription = NEW.artist_name;


UPDATE ART_OBJECT
SET artist_name = 'TEST NAME'
WHERE UNIQUE_ID = '001';


-- 7) A deletion operation with any necessary triggers

DROP TRIGGER IF EXISTS ARTIST_D_TRIGGER;

CREATE TRIGGER ARTIST_TRIGGER
AFTER UPDATE ON ART_OBJECT 
FOR EACH ROW
   UPDATE ARTIST
   SET ADescription = NEW.artist_name;