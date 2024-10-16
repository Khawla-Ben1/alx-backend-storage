-- This script creates a "users" table with an auto-incrementing primary key,
-- a unique email address column, and an optional name column.
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
