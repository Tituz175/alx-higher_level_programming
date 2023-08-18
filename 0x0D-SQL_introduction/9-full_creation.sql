-- A script that lists all rows of the table first_table from
-- the database hbtn_0c_0 in your MySQL server.
--      All fields should be printed
--      The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8);