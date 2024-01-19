-- The script creates the MySQL server user user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- privileges will be flush after creating a user or granting a user permissions
FLUSH PRIVILEGES;

-- a user will be granted all permissions in root
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
