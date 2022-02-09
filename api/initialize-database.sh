#!/usr/bin/env bash

sqlite3 data/real_estate.db < init-db.sql
PYTHONPATH=src python3 src/utils/data_loader.py