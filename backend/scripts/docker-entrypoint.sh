#!/usr/bin/env sh
set -e

main() {
  if [ "$DJANGO_COLLECTSTATIC" -ne 0 ]; then
    ./manage.py collectstatic -v 2 --noinput
  fi

  if [ "$DJANGO_MIGRATE" -ne 0 ]; then
    ./manage.py migrate
  fi

  if [ -n "$SUPERUSER_USERNAME" ] && [ -n "$SUPERUSER_EMAIL" ] &&
    [ -n "$SUPERUSER_PASSWORD" ]; then
    ./manage.py createsuperuser_ \
      --username "$SUPERUSER_USERNAME" \
      --email "$SUPERUSER_EMAIL" \
      --password "$SUPERUSER_PASSWORD"
  fi

  exec gunicorn "$@"
}

main "$@"
