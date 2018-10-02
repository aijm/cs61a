CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name AS name, b.size AS size FROM dogs AS a, sizes AS b
    WHERE a.height <= b.max AND a.height > b.min;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT b.name FROM parents AS a, dogs AS b, dogs AS c 
    WHERE a.child ==  b.name AND a.parent == c.name ORDER BY c.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS sib1, b.child AS sib2 FROM parents AS a, parents AS b 
    WHERE a.parent == b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.sib1 || " and " || a.sib2 || " are " || b.size || " siblings"
    FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c 
    WHERE a.sib1 == b.name AND a.sib2 == c.name AND b.size == c.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT o.name||', '||t.name||', '||th.name||', '||f.name,
o.height+t.height+th.height+f.height, f.height
FROM dogs as o, dogs as t, dogs as th, dogs as f WHERE t.height > o.height AND th.height > t.height AND f.height > th.height;


CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper 
    WHERE stack_height >= 170 ORDER BY stack_height;
