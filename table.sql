CREATE DATABASE  TicTacToe;

USE TicTacToe;

CREATE TABLE players (
    id INT PRIMARY KEY IDENTITY(1,1),
    login VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    registration_date DATETIME NOT NULL DEFAULT GETDATE(),
    deletion_date DATETIME NULL,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    draws INT DEFAULT 0
);

SELECT * FROM players;