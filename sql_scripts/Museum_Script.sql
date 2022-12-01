DROP DATABASE IF EXISTS MUSEUMART;
CREATE DATABASE MUSEUMART; 
USE MUSEUMART;


DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
	Unique_ID		int not null,
    Style			varchar(30) not null,
    Title			varchar(50) not null,
    Year_C			varchar(30) not null,
    AODescription	varchar(30) not null,
	primary key (Unique_ID)
);

INSERT INTO ART_OBJECT (Unique_ID, Style, Title, Year_C, AODescription)
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

DROP TABLE IF EXISTS SCULPTURE_STATUE;
CREATE TABLE SCULPTURE_STATUE (
	Unique_ID		int not null,
    Weight			varchar(30) not null,
    Height			varchar(30) not null,
    Material		varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	Unique_ID		int not null,
    OType			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	Unique_ID			int not null,
    AName				varchar(30),
    Date_Born			varchar(30),
    Date_Died			varchar(30),
    Main_Style			varchar(30),
    Epoch				varchar(30),
    Origin_Country		varchar(30),
    ADescription		varchar(30),
	primary key (Name),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO ARTIST (Unique_ID, Name, Date_Born, Date_Died, Main_Style, Epoch, Origin_Country, ADescription)
VALUES
(001, "Benedetto da Rovezzano", "1474", "1554"),
(002),
(003, "Unknown Netherlandish Painter"),
(004, "Late Medieval", "Henry VII", "1505"),
(005, "Affabel Partridge", "1551", "1580"),
(006, "Affabel Partridge");

DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
	Unique_ID			int not null,
    CName				varchar(30) not null,
    Contact_Person		varchar(30) not null,
    Phone				varchar(30) not null,
    Address				varchar(30) not null,
    CType				varchar(30),
    CDescription		varchar(30),
	primary key (Name),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);



