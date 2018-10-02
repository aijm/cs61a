.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT this.date, this.color, this.pet, this.number, last.number 
    FROM students AS this, fa17students AS last
    WHERE this.date == last.date AND this.color == last.color AND this.pet == last.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven FROM students AS a, checkboxes AS b 
    WHERE a.time == b.time AND a.number == 7 AND b.'7' == 'True';

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, count(*) AS count FROM fa17students GROUP BY number ORDER BY count DESC LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, count(*) AS count FROM fa17students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, count(*) AS count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, count(*) AS count FROM students WHERE pet == 'dog' GROUP BY pet;


CREATE TABLE sp18alldogs AS
  SELECT pet, count(*) AS count FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, count(*) AS count FROM students
    WHERE seven == '7' GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*) AS count FROM students
    GROUP BY smallest;
