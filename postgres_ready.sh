#!/usr/bin/env bash

set -o errexit

cmd="$@"

# export DATABASE_URL=postgres://postgres:$POSTGRES_PASSWORD@postgres:5431/postgres

postgres_ready () {
python << END
import sys
import psycopg2
print($POSTGRES_USER, $POSTGRES_USER, $POSTGRES_PASSWORD)
try:
    conn = psycopg2.connect(dbname="postgres", user="$POSTGRES_USER", password="$POSTGRES_PASSWORD", host="db")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres not ready. Waiting..."
  sleep 1
done

>&2 echo "Postgres is ready!"
exec $cmd
