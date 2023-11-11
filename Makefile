.PHONY: build up console

build:
	docker-compose build

up:
	docker-compose up

console:
	docker-compose run --rm app console
