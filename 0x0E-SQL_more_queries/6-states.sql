-- A script that creates the table id_not_null on your MySQL server.

--      id_not_null description:
--          id INT with the default value 1
--          name VARCHAR(256)
--      The database name will be passed as an argument of the mysql command
--      If the table id_not_null already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);