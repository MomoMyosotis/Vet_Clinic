-- first line

--      table for owners

CREATE TABLE owners (

    CF VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20),
    surname VARCHAR(20),
    birthday DATE,
    gender BOOLEAN
)

CREATE TABLE illness (

    code SERIAL PRIMARY KEY,
    name VARCHAR(30),
    descritpion VARCHAR(100),
    cure VARCHAR(30) NULL,
    lethality BOOLEAN,
    life_cycles INT

)

--      table for the pets

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    species VARCHAR(40),
    age INT,
    weight INT,
    height INT,
    birth DATE NULL,
    death DATE NULL,
    condition VARCHAR(30) REFERENCES illness(name) NULL,
    owner_id VARCHAR(20) REFERENCES owner(CF) NULL

)

-- trovare come far parlare SQL con POSTGRES con python

-- last line