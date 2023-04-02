FROM python:3.10-slim-bullseye AS build

WORKDIR /dist
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade --no-cache-dir poetry==1.1.15 \
  && poetry export -f requirements.txt --output requirements.txt  \
  --without-hashes


FROM python:3.10-slim-bullseye AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY --from=build /dist/requirements.txt requirements.txt
RUN apt-get update \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade --no-cache-dir gunicorn==20.1.0 \
  && pip install --upgrade --no-cache-dir -r requirements.txt \
  && rm -f requirements.txt \
  && mkdir -p /app/logs
COPY scripts/docker-entrypoint.sh manage.py ./
COPY social_network social_network

EXPOSE 80

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["-b", "0.0.0.0:80", "social_network.wsgi"]
