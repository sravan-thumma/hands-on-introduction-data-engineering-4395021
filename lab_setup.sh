#!/bin/sh
mkdir -p /home/codespace/manual
mkdir -p /home/codespace/orchestrated

sqlite3 /home/codespace/manual/manual-etl-database.db <<EOF
.read /workspaces/hands-on-introduction-data-engineering-4395021/create_table.sql
.headers on
.mode csv
.quit
EOF

sqlite3 /home/codespace/orchestrated/airflow-etl-database.db <<EOF
.read /workspaces/hands-on-introduction-data-engineering-4395021/create_table.sql
.headers on
.mode csv
.quit
EOF


