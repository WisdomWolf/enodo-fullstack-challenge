#!/usr/bin/env bash

URL="http://localhost:8080"

script_dir=`dirname "$0"`
echo "initializing database"
$script_dir/api/initialize-database.sh
docker-compose up -d
path=$(which open 2>/dev/null || which xdg-open 2>/dev/null|| which gnome-open 2>/dev/null)
exec "$path" "http://localhost:8080" && echo "browser should have opened to $URL" || echo "Couldn't open a browser. Please visit $URL to view the site"