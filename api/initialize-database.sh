#!/usr/bin/env bash

script_dir=`dirname "$0"`

sqlite3 $script_dir/data/real_estate.db < $script_dir/init-db.sql
PYTHONPATH=$script_dir/src python3 $script_dir/src/utils/data_loader.py
echo "Database reloaded with fresh data"