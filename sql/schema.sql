/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS `SimplestLib`;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `SimplestLib`;


USE `SimplestLib`;

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE Author (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100)
);

CREATE TABLE Book (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre_id INT,
    language VARCHAR(255),
	FOREIGN KEY (author_id) REFERENCES Author(author_id),
	FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Borrower (
    borrower_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    phone_number VARCHAR(20),
    email_address VARCHAR(255)
);

CREATE TABLE Loan (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    borrower_id INT,
    book_id INT,
    date_of_borrowing DATE,
	due_date DATE,
    return_date DATE,
    FOREIGN KEY (borrower_id) REFERENCES Borrower(borrower_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);