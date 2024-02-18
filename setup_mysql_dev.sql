-- Create a database named hbnb_dev_db if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a user named hbnb_dev if it does not already exist
CREATE USER IF NOT EXISTS hbnb_dev@localhost;
-- Set the password for the hbnb_dev user to 'hbnb_dev_pwd'
SET PASSWORD FOR hbnb_dev@localhost = 'hbnb_dev_pwd';
-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO hbnb_dev@localhost;
-- Grant SELECT privileges on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema . * TO hbnb_dev@localhost;
-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
