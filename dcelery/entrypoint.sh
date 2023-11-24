#!/bin/ash

echo "Apply database migrations"
python manage.py migrate

# This line uses the exec command to replace the current shell process with a new one.
# The $@ is a special variable in Bash that represents all the arguments passed to the script.
# This line essentially passes any command-line arguments provided when running the script to the new shell process.
exec "$@"