# Social Network
___
### Simple project with JWT Auth for posts managing and liking

## Configuration
___
Add `.env` file with environment variables to `social_network folder`:
```
# Database
DB_PORT=5432
DB_HOST=db
DB_NAME=db
DB_USER=user
DB_PASSWORD=database

# Grafana database
GRAFANA_DB_PORT=5437
GRAFANA_DB_HOST=grafana-db
GRAFANA_DB_NAME=grafana-db
GRAFANA_DB_USER=user
GRAFANA_DB_PASSWORD=grafana
GRAFANA_SECURITY_ADMIN_USER=admin
GRAFANA_SECURITY_ADMIN_PASSWORD=grafana

# Auth
SECRET_KEY=secret-key

# Superuser
SUPERUSER_USERNAME=admin
SUPERUSER_EMAIL=admin
SUPERUSER_PASSWORD=admin
```
## Run
1. For development purpose: <br>
`docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build`
2. Production run: <br>
`docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.prod.yml up --build`
3. Go to `http://localhost/api/docs` to see APIs, `http://localhost/admin` for Django Admin, `http://localhost:3000`
for Grafana dashboard.

## Main features
1. User registration
2. JWT Auth
3. Posts managing and liking
4. Likes analytics
5. Users' activity
6. Grafana dashboard
