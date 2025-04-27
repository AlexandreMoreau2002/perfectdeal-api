# Variables
SERVICE=perfectdeal_api

# ---------------------------
# 🐳 Docker
# ---------------------------

up:
	docker compose up -d

build:
	docker compose build

start: build up -d

down:
	docker compose down

restart: down up

# ---------------------------
# 🧰 Dev utils
# ---------------------------

shell:
	docker exec -it $$(docker ps -qf "name=${SERVICE}") /bin/sh

logs:
	docker compose logs -f ${SERVICE}

py:
	docker exec -it $$(docker ps -qf "name=${SERVICE}") poetry run python