\c kazikashika_db

CREATE SCHEMA kazikashika;

CREATE TABLE IF NOT EXISTS teams
(
    id varchar(128) PRIMARY KEY,
    name varchar(128) NOT NULL,
    record_update_time timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS users
(
    id varchar(128) PRIMARY KEY,
    name varchar(128) NOT NULL,
    mail_address varchar(128),
    age smallserial,
    gender smallserial,
    occupation varchar(128),
    record_update_time timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS houseworks
(
    id varchar(128) PRIMARY KEY,
    name varchar(128) NOT NULL,
    color smallserial NOT NULL,
    team_id varchar(128) NOT NULL,
    record_update_time timestamp NOT NULL,

    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS housework_recordes
(
    id varchar(128) PRIMARY KEY,
    housework_id varchar(128) NOT NULL,
    user_id varchar(128) NOT NULL,
    stress smallserial NOT NULL,
    housework_start timestamp NOT NULL,
    housework_end timestamp NOT NULL,
    record_update_time timestamp NOT NULL,

    FOREIGN KEY (housework_id) REFERENCES houseworks(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS participations
(
    id varchar(128) PRIMARY KEY,
    user_id varchar(128) NOT NULL,
    team_id varchar(128) NOT NULL,
    authority smallserial NOT NULL,
    record_update_time timestamp NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);