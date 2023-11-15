.PHONY:

dc-build-dev:
	docker-compose -f ./docker-compose.dev.yml --env-file ./dev.env build

dc-build:
	docker-compose -f ./docker-compose.yml --env-file ./.env build

dc-run-dev:
	docker-compose -f ./docker-compose.dev.yml --env-file ./dev.env up --remove-orphans -d

dc-run:
	docker-compose -f ./docker-compose.yml --env-file ./.env up --remove-orphans -d

run-dev: dc-build-dev dc-run-dev

run: dc-build dc-run
