-- first line


--      table for owners

CREATE TABLE owners (

    CF VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20),
    surname varchar(20),
    birthday DATE,
    gender BOOLEAN
)


--      table for the pets

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name varchar(20),
    species varchar(40),
    age INT,
    weight INT,
    height INT,
    condition VARCHAR(100), -- maybe use this as reference for a database of illness
    owner_id VARCHAR(20) REFERENCES owner(CF)

)

-- CREATE TABLE sickness()
)
-- trovare come far parlare SQL con POSTGRES con python

-- last line