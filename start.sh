#! /usr/bin/env sh
set -e

# exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"

uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-8080}
