1) Show all tables and explain how they are related to one another (keys, triggers, etc.)
SELECT 
    *
FROM
    information_schema.tables;


2) A basic retrieval query
select *
FROM ART_OBJECT
Where style = "Late Medieval"

3) A retrieval query with ordered results

Select *
FROM ARTIST
ORDER BY DAte_Died desc;

4) A nested retrieval query

5) A retrieval query using joined tables


6) An update operation with any necessary triggers


7) A deletion operation with any necessary triggers