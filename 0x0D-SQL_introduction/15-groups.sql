-- A script that lists all rows of the table first_table from
-- the database hbtn_0c_0 in your MySQL server.
--      All fields should be printed
--      The database name will be passed as an argument of the mysql command
SELECT second_table.score,
    count(second_table.score) AS number
FROM second_table
GROUP BY second_table.score;