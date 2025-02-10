.PHONY: intall
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: super-user
super-user:
	poetry run python manage.py createsuperuser

.PHONY: run-server
run-server:
	poetry run python manage.py runserver

update: install migrate ;