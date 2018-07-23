.PHONY: build run makemigrations migrate loaddata

build:
	git submodule update --init --recursive
	docker-compose build
run:
	docker-compose up

makemigrations:
	docker exec -it elixirfestjp_web_1 apps/manage.py makemigrations ${app}

migrate:
	docker exec -it elixirfestjp_web_1 apps/manage.py migrate

createsuperuser:
	docker exec -it elixirfestjp_web_1 apps/manage.py createsuperuser

loaddata:
	docker cp apps/fixtures/media elixirfestjp_web_1:/code/
	docker cp apps/fixtures/core.json elixirfestjp_web_1:/tmp
	docker exec -it elixirfestjp_web_1 apps/manage.py loaddata /tmp/core.json
