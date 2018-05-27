#!/usr/bin/env bash

if [ ! -z $MANUAL_MODE ] && $MANUAL_MODE; then
    echo
    echo "[WARNING] Manual mode active"
    echo "[WARNING] You can execute commands direct by docker[-compose] exec"
    echo
    sleep infinity
else
    set -o errexit
    set -o pipefail
    set -o xtrace
    set -o nounset
	sleep 5
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --no-input
    python manage.py runserver 0.0.0.0:80 --insecure
fi