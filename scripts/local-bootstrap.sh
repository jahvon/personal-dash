#!/bin/bash

docker-compose stop

docker-compose rm --stop --force db

docker-compose run web bash <<EOF
echo "Loading DB container"
build/load_db.sh echo "Database container loaded!"

echo "Rebuilding development database"
PGPASSWORD=jahvon psql --host db --user=jahvon -c "CREATE DATABASE personaldash OWNER jahvon;"
flask db migrate
flask db upgrade
python3 seed.py
EOF