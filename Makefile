build:
	docker build -t lit3d-web -f Dockerfile.django .

stop:
	docker stop lit3d-web

start:
	docker run -d -p 8000:8000 --name lit3d-web \
	--env-file .env \
	--restart unless-stopped \
	lit3d-web

restart:
	make stop && make start

down:
	docker stop lit3d-web
	docker rm lit3d-web

envs:
	cp .env.example .env