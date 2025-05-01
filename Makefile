up:
	docker compose -f Docker-compose.yaml up -d

stop:
	docker compose -f Docker-compose.yaml stop

start:
	docker compose -f Docker-compose.yaml start

restart:
	make stop && make start

down:
	docker compose -f Docker-compose.yaml down

envs:
	cp .env.example .env