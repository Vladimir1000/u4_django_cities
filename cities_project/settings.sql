-- settings.sql
CREATE DATABASE cities;
CREATE USER citiesuser WITH PASSWORD 'cities';
GRANT ALL PRIVILEGES ON DATABASE cities TO citiesuser;