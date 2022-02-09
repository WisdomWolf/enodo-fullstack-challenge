#!/usr/bin/env bash

script_dir=`dirname "$0"`
echo "initializing database"
$script_dir/api/initialize-database.sh
docker-compose up -d
path=$(which open || which xdg-open || which gnome-open)
exec "$path" "http://localhost:8080" || echo "Couldn't open a browser. Please visit http://localhost:8080 to view the site"