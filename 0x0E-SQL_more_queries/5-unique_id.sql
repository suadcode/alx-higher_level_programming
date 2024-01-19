-- The script will create the table unique_id on the MySQL server.

-- table unique id is created
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
