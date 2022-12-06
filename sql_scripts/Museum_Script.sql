DROP DATABASE IF EXISTS MUSEUMART;
CREATE DATABASE MUSEUMART; 
USE MUSEUMART;


DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
	Unique_ID		varchar(3) not null,
    Epoch			varchar(30) not null,
    Title			varchar(50) not null,
    Year_C			varchar(30) not null,
    AODescription	varchar(300),
    artist_name     varchar(50) not null,
    in_collection      varchar(30) not null,
	primary key (Unique_ID)


);


INSERT INTO ART_OBJECT (Unique_ID, artist_name, Epoch, Title, Year_C,AODescription,in_collection)
VALUES
("001", "Renaissance","Benedetto da Rovezzano" ,"Angel Bearing Candlestick", "1527","Angel holding a candlestick.","The Met"),
('002', "Late Medieval","Unknown" , "Field Armor of King Henry VIII", "1544","Armor made by Kind Henry VIII","The Met"),
('003', "Late Medieval","Hans Holbein the Younger " , "Henry VIII", "1537","Portrait of Kings Henry VIII made in the mid 1500's.","The Met"),
('004', "Late Medieval","Unknown Netherlandish Painter" , "Henry VII", "1505","Portrait of King Henry VII made in the early 1500's.","The Met"),
('005', "Late Medieval","Affabel Partridge" , "Ewer", "1562","Ewer made in mid 1500's attributed to a British Artist Affabel Partridge","The Met"),
('006', "Late Medieval", "Affabel Partridge" , "Tankard", "1575","Tankard made in mid 1500's attributed to a British Artist Affabel Partridge","The Met"),
('007',"Renaissance","Jacques-Louis David" ,"Les Sabines","1799","Painting of a battle during the fall of the Romain Empire","Masterpieces of the Louvre"),
('008',"Ancient","Unknown" ,"Stele","-1792","Massive slab of rock with an image carved into the top","Masterpieces of the Louvre"),
('009',"Renaissance","Joseph Cope" ,"Diamond named the Regent","1705","Diamond considered to be the most beautiful in the world.","Masterpieces of the Louvre"),
('010',"Renaissance","Unkown" ,"The Holy Family","1770","Sculpture of the Holy Family","Acquisitions made in 2020"),
('011',"Renaissance","Jean-Valentin Morel" ,"Fossin Cup","1843","Fossin cup with lid included made in Paris","Acquisitions made in 2020"),
('012',"Renaissance","Jean-Honoré Fragonard" ,"Louis IX","1770","Drawing of Sain-Louis","Acquisitions made in 2020");

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
	Unique_ID		varchar(3) not null,
    Paint_type		varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

Insert into PAINTING (Unique_ID,Paint_type)
VALUES
('003', "Oil on panel"),
('004', "Oil on panel"),
('007', "Oil on Canvas"),
('012',"Pastel on blue paper");


DROP TABLE IF EXISTS SCULPTURE_STATUE;
CREATE TABLE SCULPTURE_STATUE (
	Unique_ID		varchar(3) not null,
    Weight			varchar(30) not null,
    Height			varchar(30) not null,
    Material		varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO SCULPTURE_STATUE(Unique_ID,Weight,Height,Material)
VALUES
('001', "141 kg","101 cm","Bronze"),
('002', "22.91 kg","184.2 cm","Steel"),
('008', "70 kg","225 cm","Basalt"),
('010',"4 kg","33 cm","Ivory");

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	Unique_ID		varchar(3) not null,
    OType			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);


INSERT INTO OTHER (Unique_ID, OType)
VALUES
('005',"Silver"),
('006',"Metalwork"),
('009',"Jewel"),
('011',"Agate");

DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION (
	Unique_ID				varchar(3) not null,
    Date_acquired			varchar(30) not null,
    Collection_Status		varchar(30) not null,
    Cost					varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO PERMANENT_COLLECTION(Unique_ID,Date_acquired,Collection_Status,Cost)
VALUES
('001',"1957","Loan","$19,500"),
('002',"1920","Display","$200,000"),
('003',"1930","Loan","$40,000"),
('004',"1955","Loan","$10,000"),
('005',"1890","Loan","$15,000"),
('006',"1890","Loan","$10,000");


DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
	Unique_ID		varchar(3) not null,
    Borrowed_from			varchar(30) not null,
    Date_borrowed			varchar(30) not null,
    Date_returned			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO BORROWED(Unique_ID,Borrowed_from,Date_borrowed,Date_returned)
VALUES
('007',"The State","1819","2050"),
('008',"The State","1902","2050"),
('009',"The State","1812","2200"),
('010',"The State","2020","2100"),
('011',"The State","2020","2050"),
('012',"The State","2020","2150");



DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
    Aname				varchar(30),
    Date_Born			varchar(30),
    Date_Died			varchar(30),
    Main_Style			varchar(30),
    Epoch				varchar(30),
    Origin_Country		varchar(30),
    ADescription		varchar(100),
	primary key (Aname)
);

INSERT INTO ARTIST (Aname, Date_Born, Date_Died,Origin_Country,Epoch,ADescription,Main_Style)
VALUES
( "Benedetto da Rovezzano", "1474", "1554","Italy","Renaissance","Italian Architect","Sculpture"),
( "Unknown", NULL, NULL,NULL,NULL,NULL,NULL),
( "Hans Holbein the Younger", "1497","1543","Germany","Late Medieval","German-Swiss Painter","Painting"),
( "Unknown Netherlandish Painter", NULL, NULL,NULL,NULL,NULL,NULL),
( "Affabel Partridge", "1551", "1580","England","Late Medieval","Goldsmith from London","Jewelry"),
( "Jacques-Louis David","1748","1825","France","Renaissance","French painter from Paris","Painting"),
( "Joseph Cope",NULL,NULL,NULL,NULL,NULL,NULL),
("Jean-Valentin Morel","1794","1860","France","Renaissance","French silversmith","Jewelry"),
("Jean-Honoré Fragonard","1732","1802","France","Renaissance","French Paitner","Painting");


DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS (
    Cname				varchar(30) not null,
    Contact_Person		varchar(30) not null,
    Phone				varchar(30) not null,
    Address				varchar(30) not null,
    CType				varchar(30),
    CDescription		varchar(300),
	primary key (Cname)
);

INSERT INTO COLLECTIONS (Cname,Contact_Person,Address,Phone,CType,CDescription)
VALUES
("Masterpieces of the Louvre","David Hasselhoff","325 Laplace Road","111-222-3333","Museum","Artworks essential to history and the history of art."),
("Acquisitions made in 2020","Yuki Tsunoda","111 University Road","777-777-7777","Museum","Artwork acquired recently in the year 2020."),
("The Met","Sir John Baptiste","123-456-7890","1820 Riverside Road","Museum","Includes all the art currently owned by The Met");

DROP TABLE IF EXISTS BACKGROUND;
CREATE TABLE BACKGROUND (
	Unique_ID		    varchar(3) not null,
    Origin				varchar(30) not null,
    Attribute			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);

INSERT INTO BACKGROUND(Unique_ID,Origin,Attribute)
VALUES
('001',"Italian","Renaissance"),
('002',"Italian","Late Medieval"),
('003',"Germany","Late Medieval"),
('004',"Dutch","Late Medieval"),
('005',"British","Late Medieval"),
('006',"British","Late Medieval"),
('007',"French","Fall of Rome"),
('008',"Iraq","Mesopotamia"),
('009',"British","Louis XIV"),
('010',"Spanish","Renaissance"),
('011',"French","July Monarchy"),
('012',"French","Renaissance");

DROP TABLE IF EXISTS EXHIBITIONS;
CREATE TABLE EXHIBITIONS (
	Unique_ID		    varchar(3) not null,
    Ename				varchar(30) not null,
    Start_date			varchar(30) not null,
    End_date			varchar(30) not null,
	primary key (Unique_ID),
    foreign key (Unique_ID) references ART_OBJECT(Unique_ID)
);


ALTER TABLE ART_OBJECT
ADD foreign key(artist_name) references artist(Aname),
ADD foreign key(in_collection) references COLLECTIONS(Cname);

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
=======
DROP ROLE IF EXISTS 'db_admin'@'localhost', 'write_access'@'localhost', 'read_access'@'localhost';
CREATE ROLE 'db_admin'@'localhost', 'write_access'@'localhost', 'read_access'@'localhost';

 GRANT ALL PRIVILEGES ON *.* TO 'db_admin'@'localhost' WITH GRANT OPTION;
 GRANT Insert ON MUSEUMART.* TO 'write_access'@'localhost';
 GRANT UPDATE ON MUSEUMART.* TO 'write_access'@'localhost';
 GRANT Select ON MUSEUMART.* TO 'read_access'@'localhost';

DROP USER IF EXISTS 'admin'@'localhost';
DROP USER IF EXISTS 'data_entry'@'localhost';
DROP USER IF EXISTS 'guest'@'localhost';

CREATE USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER 'data_entry'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER 'guest'@'localhost';

GRANT'db_admin'@'localhost' TO 'admin'@'localhost';

GRANT 'write_access'@'localhost' TO 'data_entry'@'localhost';
GRANT 'read_access'@'localhost' TO 'data_entry'@'localhost';

GRANT 'read_access'@'localhost' TO 'guest'@'localhost';

SET DEFAULT ROLE ALL TO 'admin'@'localhost';
SET DEFAULT ROLE ALL TO 'data_entry'@'localhost';
SET DEFAULT ROLE ALL TO 'guest'@'localhost';

