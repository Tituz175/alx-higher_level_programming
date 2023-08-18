-- A script that lists all rows of the table first_table from
-- the database hbtn_0c_0 in your MySQL server.
--      All fields should be printed
--      The database name will be passed as an argument of the mysql command
SELECT second_table.score,
    second_table.name
FROM second_table
WHERE second_table.name IS NOT NULL
ORDER BY second_table.score DESC;