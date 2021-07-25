format:
	poetry run isort --recursive  --apply --atomic ./app

build:
	poetry export --no-ansi --no-interaction --without-hashes -E uwsgi -o ./deploy/requirements.txt

migrate:
	docker-compose exec app python manage.py migrate

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans