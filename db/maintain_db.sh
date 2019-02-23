#!/bin/bash

CONFIG="flyway/conf/flyway.conf"
if [ ! -e "$CONFIG" ]; then
    echo "ERROR: No configuration file detected at path:"
    echo "  $CONFIG"
    echo
    echo "Ensure you have supplied a configuration file and try again. Exiting..."
    exit 1
fi

DB_NAME=$(cat flyway/conf/flyway.conf | grep "^flyway.url" | sed 's/^.*\///')

echo local: ensuring database exists: $DB_NAME
CREATE_SCRIPT="echo CREATE DATABASE IF NOT EXISTS $DB_NAME | mysql --password=password"
if docker-compose exec mysql bash -c "$CREATE_SCRIPT"; then
    echo local: database either exists or was created
else
    echo local: error ensuring database exists
    exit 2
fi

exec docker-compose run flyway \
    -configFiles="$CONFIG" \
    "$@"
