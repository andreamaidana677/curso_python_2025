CREATE DATABASE IF NOT EXISTS jaguarete;
Use jaguarete;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    pass VARCHAR(255) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users(username, pass) VALUES ('unida', 'unida123');

select  * FROM users;

