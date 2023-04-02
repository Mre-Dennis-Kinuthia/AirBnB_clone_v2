-- Create a new database for testing
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user with all privileges on the hbnb_test_db database
CREATE USER
    IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Give the hbnb_test user SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';