#!/usr/bin/env bash

set -o errexit
set -o pipefail


# cmd="$@"

export POSTGRES_USER=postgres
export DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@postgres:5431/postgres


function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$POSTGRES_USER", user="$POSTGRES_USER", password="$POSTGRES_PASSWORD", host="postgres")
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