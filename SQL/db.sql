-- first line

--      table for owners

CREATE TABLE IF NOT EXISTS owners (

    CF VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20),
    surname VARCHAR(20),
    birthday DATE,
    gender VARCHAR(1)
);

--          table for the illness
CREATE TABLE IF NOT EXISTS illness (

    code SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(100),
    cure VARCHAR(50) NULL,
    lethality BOOLEAN,
    life_cycles INT

);

--      table for the pets

CREATE TABLE IF NOT EXISTS pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    species VARCHAR(40),
    age FLOAT,
    peso FLOAT,
    height FLOAT,
    birth DATE NULL,
    death DATE NULL,
    stato BOOLEAN,
    condition INT REFERENCES illness(code) NULL,
    owner_id VARCHAR(20) REFERENCES owners(CF) NULL

);


-- last line