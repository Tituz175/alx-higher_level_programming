-- A script that creates the MySQL server user user_0d_1.
--      user_0d_1 should have all privileges on your MySQL server
--      The user_0d_1 password should be set to user_0d_1_pwd
--      If the user user_0d_1 already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0c_0
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' WITH PASSWORD 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'