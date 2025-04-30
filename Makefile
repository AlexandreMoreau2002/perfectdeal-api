# Variables
SERVICE=perfectdeal_api

# ---------------------------
# 🐳 Docker
# ---------------------------

start:
	docker compose up -d

build:
	docker compose build

up: build start

stop: 
	docker compose stop

down:
	docker compose down

restart: down start

# ---------------------------
# 🧰 Dev utils
# ---------------------------

shell:
	docker exec -it $$(docker ps -qf "name=${SERVICE}") /bin/sh

logs:
	docker compose logs -f ${SERVICE}

py:
	docker exec -it $$(docker ps -qf "name=${SERVICE}") poetry run python