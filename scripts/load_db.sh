#!/bin/bash
# This script waits until the postgres server is available and then invokes
# whatever command is passed to it.

while true; do
  PGPASSWORD=jahvon psql --host db --user=jahvon -c "SELECT 1;" > /dev/null
  if [ $? -eq 0 ]; then
    break
  fi
  sleep 1
done

exec "$@"