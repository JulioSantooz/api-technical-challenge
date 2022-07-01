CREATE DATABASE bookstore;

USE bookstore;

CREATE TABLE admin (
    idAdmin INT NOT NULL AUTO_INCREMENT,
    nameAdmin VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    passAdmin VARCHAR(30) NOT NULL,
    PRIMARY KEY(idAdmin)
);

CREATE TABLE default (
    idDefault INT NOT NULL AUTO_INCREMENT,
    nameDefault VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    passDefault VARCHAR(30) NOT NULL,
    PRIMARY KEY(idDefault)
);

CREATE TABLE actors (
    idActor INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    image TEXT,
    PRIMARY KEY(idActor)
);

CREATE TABLE papers (
    idPaper INT NOT NULL AUTO_INCREMENT,
    category VARCHAR(30),
    title VARCHAR(30),
    summary VARCHAR(30),
    firstParagraph VARCHAR(30),
    body VARCHAR(255),
    PRIMARY KEY(idPaper)
);


ALTER TABLE actors
    ADD CONSTRAINT fk_a FOREIGN KEY (idAdmin) REFERENCES admin (idAdmin);

ALTER TABLE papers
    ADD CONSTRAINT fk_aut FOREIGN KEY (idActor) REFERENCES actors (idActor),
    ADD CONSTRAINT fk_an FOREIGN KEY (idAdmin) REFERENCES admin (idAdmin);

