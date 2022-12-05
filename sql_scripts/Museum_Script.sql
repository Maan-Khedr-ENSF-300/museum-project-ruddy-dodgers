DROP DATABASE IF EXISTS MUSEUMART;
CREATE DATABASE MUSEUMART; 
USE MUSEUMART;


DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
	Unique_ID		int not null,
    Style			varchar(30) not null,
    Title			varchar(50) not null,
    Year_C			varchar(30) not null,
    AODescription	varchar(30),
	primary key (Unique_ID)
);


INSERT INTO ART_OBJECT (Unique_ID, Style, Title, Year_C)
VALUES
(001, "Renaissance", "Angel Bearing Candlestick", "1524-29"),
(002, "Late Medieval", "Field Armor of King Henry VIII", "1509-47"),
(003, "Late Medieval", "King Henry VIII", "1524-29"),
(004, "Late Medieval", "Henry VII", "1505"),
(005, "Late Medieval", "Ewer", "1562"),
(006, "Late Medieval", "Tankard", "1575");


DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
	Unique_ID		int not null,
    Paint_type		varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

Insert into PAINTING (Unique_ID,Paint_type)
VALUES
(004, "Oil");


DROP TABLE IF EXISTS SCULPTURE_STATUE;
CREATE TABLE SCULPTURE_STATUE (
	Unique_ID		int not null,
    Weight			varchar(30) not null,
    Height			varchar(30) not null,
    Material		varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO SCULPTURE_STATUE(Unique_ID,Weight,Height,Material)
VALUES
(001, "141 kg","101 cm","Bronze"),
(002, "22.91 kg","184.2 cm","Steel");

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	Unique_ID		int not null,
    OType			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);


INSERT INTO OTHER (Unique_ID, OType)
VALUES
(005,"Silver"),
(006,"Metalwork");
DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION (
	Unique_ID				int not null,
    Date_acquired			varchar(30) not null,
    Collection_Status		varchar(30) not null,
    Cost					varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);




DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
	Unique_ID		int not null,
    Borrowed_from			varchar(30) not null,
    Date_borrowed			varchar(30) not null,
    Date_returned			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);



DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	Unique_ID			int not null,
    Aname				varchar(30),
    Date_Born			varchar(30),
    Date_Died			varchar(30),
    Main_Style			varchar(30),
    Epoch				varchar(30),
    Origin_Country		varchar(30),
    ADescription		varchar(30),
	primary key (Aname),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO ARTIST (Unique_ID, Aname, Date_Born, Date_Died)
VALUES
(001, "Benedetto da Rovezzano", "1474", "1554"),
(002, "Unknown", NULL, NULL),
(003, "Unknown Netherlandish Painter", NULL, NULL),
(004, "Late Medieval", "Henry VII", "1505"),
(005, "Affabel Partridge", "1551", "1580");

DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
	Unique_ID			int not null,
    Cname				varchar(30) not null,
    Contact_Person		varchar(30) not null,
    Phone				varchar(30) not null,
    Address				varchar(30) not null,
    CType				varchar(30),
    CDescription		varchar(30),
	primary key (Cname),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

DROP TABLE IF EXISTS BACKGROUND;
CREATE TABLE BACKGROUND (
	Unique_ID		int not null,
    Origin				varchar(30) not null,
    Attribute			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

DROP TABLE IF EXISTS EXHIBITIONS;
CREATE TABLE EXHIBITIONS (
	Unique_ID		int not null,
    Ename				varchar(30) not null,
    Start_date			varchar(30) not null,
    End_date			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

DROP ROLE IF EXISTS db_admin@localhost, data_access@localhost, read_access@localhost;
CREATE ROLE db_admin@localhost, data_access@localhost, read_access@localhost;
GRANT ALL PRIVILEGES ON MUSEUMART.* TO db_admin@localhost;
GRANT Insert ON MUSEUMART.* TO data_access@localhost;
GRANT Select ON MUSEUMART.* TO read_access@localhost;

DROP USER IF EXISTS administrator@localhost;
DROP USER IF EXISTS data_entry_user@localhost;
DROP USER IF EXISTS guest@localhost;

CREATE USER administrator@localhost IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER data_entry_user@localhost IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER guest@localhost;

GRANT db_admin@localhost TO administrator@localhost;
GRANT data_access@localhost TO data_entry_user@localhost;
GRANT read_access@localhost TO guest@localhost;

SET DEFAULT ROLE ALL TO administrator@localhost;
SET DEFAULT ROLE ALL TO data_entry_user@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;

