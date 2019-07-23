#!/bin/bash
psql -U postgres -d flask_tutorial << "EOSQL"
CREATE TABLE users (
        id SERIAL NOT NULL, 
        name VARCHAR(200), 
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        PRIMARY KEY (id)
);
EOSQL