#!/bin/sh
set -e

# Run migrations
echo "Running migrations..."
uv run python manage.py migrate --noinput

# Execute the main command
exec "$@"
