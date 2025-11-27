DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

CREATE TABLE Department(
    dep_id INT PRIMARY KEY,
    dep_name VARCHAR(100) NOT NULL,
    num_of_locations INT
);

CREATE TABLE Employee(
    ssn INT PRIMARY KEY,
    Fname VARCHAR(100) NOT NULL,
    Bdate VARCHAR(100) NOT NULL,
    Minit VARCHAR(1),
    Lname VARCHAR(100) NOT NULL,
    ee_address VARCHAR(100) NOT NULL,
    Salary INT,
    Supervisor_ssn INT,
    works_for_dep INT NOT NULL,
    manage_dep INT,
    FOREIGN KEY (works_for_dep) REFERENCES Department(dep_id),
    FOREIGN KEY (manage_dep) REFERENCES Department(dep_id)
);

CREATE TABLE Project(
    pj_id INT PRIMARY KEY,
    pj_name VARCHAR(100) NOT NULL,
    type ENUM("repair", "clean", "decoration", "weather_related", "harmful_chemicals", "mixture") NOT NULL,
    contractor VARCHAR(100)
);

CREATE TABLE Dependent(
    employee_ssn INT PRIMARY KEY,
    ful_name VARCHAR(100) NOT NULL,
    sex ENUM("male", "female") NOT NULL,
    birth_date VARCHAR(100),
    FOREIGN KEY (employee_ssn) REFERENCES Employee(ssn)
);

CREATE TABLE Employee_works_on_Project(
    pj_id INT,
    ee_ssn INT,
    working_time INT,
    PRIMARY KEY (pj_id, ee_ssn),
    FOREIGN KEY (pj_id) REFERENCES Project(pj_id),
    FOREIGN KEY (ee_ssn) REFERENCES Employee(ssn)
);

CREATE TABLE Department_in_charge_Project(
    dep_id INT,
    pj_id INT,
    PRIMARY KEY (dep_id, pj_id),
    FOREIGN KEY (dep_id) REFERENCES Department(dep_id),
    FOREIGN KEY (pj_id) REFERENCES Project(pj_id)
);

CREATE TABLE Location(
    building_name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    pj_id INT NOT NULL,
    date VARCHAR(100),
    PRIMARY KEY (building_name, address),
    FOREIGN KEY (pj_id) REFERENCES Project(pj_id)
);