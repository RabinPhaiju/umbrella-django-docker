 
build:
	docker-compose build

build-prod:
	docker-compose -f docker-compose.prod.yml up -d --build

build-prod-log:
	docker-compose -f docker-compose.prod.yml logs -f

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

down:
	docker-compose down

down-v:
	docker-compose down -v

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti nz01 /bin/sh

shell-web:
	docker exec -ti dz01 /bin/sh

shell-db:
	docker exec -ti pz01 /bin/sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log:
	docker logs -f clapgy_web_1

log-db:
	docker-compose logs db

collectstatic:
	docker exec dz01 /bin/sh -c "python manage.py collectstatic --noinput"

migrate:
	docker-compose exec web python manage.py migrate

migrations:
	docker-compose exec web python manage.py makemigrations

create-superuser:
	docker-compose exec web python manage.py createsuperuser

flush:
	docker-compose exec web python manage.py flush --no-input

ensure_table:
	docker-compose exec db psql --username=clapgy --dbname=clapgy_dev
# Enter list of databases -> \l
# Enter a table -> \c [table_name]
# List of relation in that table -> \dt
# Exit -> \q

check_volume:
	docker volume inspect clapgy-django-docker_postgres_data