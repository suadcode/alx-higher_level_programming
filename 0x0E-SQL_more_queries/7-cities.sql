-- The script will create the database hbtn_0d_usa and the table
-- cities (in the database hbtn_0d_usa) on the MySQL server.

-- database is created
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- cd/use the created database
USE hbtn_0d_usa;

-- table 'cities' is created
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);
