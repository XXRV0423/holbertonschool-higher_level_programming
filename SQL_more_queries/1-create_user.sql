-- Creates user_0d_1 with all privileges
CREATE USER ID NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
