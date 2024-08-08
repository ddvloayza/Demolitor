docker-local-createsuperuser:
	docker-compose -f ./docker/docker-compose.yml exec web python ./src/manage.py createsuperuser --settings=config.settings.local
docker-local-migrate:
	docker-compose -f ./docker/docker-compose.yml exec web python ./src/manage.py migrate --settings=config.settings.local
docker-local-migrations:
	docker-compose -f ./docker/docker-compose.yml exec web python ./src/manage.py makemigrations --settings=config.settings.local
docker-local-migrations-merge:
	docker-compose -f ./docker/docker-compose.yml exec web python ./src/manage.py makemigrations --merge --settings=config.settings.local
docker-flake:
	docker-compose -f ./docker/docker-compose.yml exec web flake8 .
docker-test-build:
	docker-compose -f ./docker/docker-compose-test.yml build
docker-test-run:
	docker-compose -f ./docker/docker-compose-test.yml up -d
docker-test-python:
	docker-compose -f ./docker/docker-compose-test.yml exec web python ./src/manage.py test --settings=config.settings.testing
docker-bash:
	docker-compose -f ./docker/docker-compose.yml exec web sh
docker-local-run:
	docker-compose -f ./docker/docker-compose.yml up
docker-local-build:
	docker-compose -f ./docker/docker-compose.yml build
docker-local-down:
	docker-compose -f ./docker/docker-compose.yml down
docker-stage-run:
	docker-compose -f ./docker/docker-compose-stage.yml up -d
docker-stage-build:
	docker-compose -f ./docker/docker-compose-stage.yml build
docker-stage-down:
	docker-compose -f ./docker/docker-compose-stage.yml down
docker-stage-migrate:
	docker-compose -f ./docker/docker-compose-stage.yml exec web python ./src/manage.py migrate --settings=config.settings.stage
docker-stage-migrations:
	docker-compose -f ./docker/docker-compose-stage.yml exec web python ./src/manage.py makemigrations --settings=config.settings.stage
docker-stage-migrations-merge:
	docker-compose -f ./docker/docker-compose-stage.yml exec web python ./src/manage.py makemigrations --merge --settings=config.settings.stage
docker-prod-run: clean docker-prod-build
	docker run --name weeare-prod --env-file docker/.env -p 80:8002 -d -t weeare-prod
docker-prod-build:
	docker build . -t weeare-prod
docker-prod-stop:
	docker stop weeare-prod
docker-prod-migrate:
	docker exec weeare-prod python ./src/manage.py migrate --settings=config.settings.production
docker-prod-migrations:
	docker exec weeare-prod python ./src/manage.py makemigrations --settings=config.settings.production
docker-prod-migrations-merge:
	docker exec weeare-prod python ./src/manage.py makemigrations --merge --settings=config.settings.production
docker-prod-static:
	docker exec weeare-prod python ./src/manage.py collectstatic --settings=config.settings.production --no-input
startapp:
	@ docker-compose -f ./docker/docker-compose.yml exec web mkdir ./src/apps/${APP_NAME}
	@ docker-compose -f ./docker/docker-compose.yml exec web python ./src/manage.py startapp ${APP_NAME} ./src/apps/${APP_NAME}
	@ sudo chown -R ${USER}:${USER} ./src/apps/${APP_NAME}
startapp-plugins:
	@ mkdir ./src/apps_plugins/${APP_NAME}
	@ docker-compose -f ./docker/docker-compose.yml exec web django-admin startapp ${APP_NAME} ./src/apps_plugins/${APP_NAME}
	@ sudo chown -R ${USER}:${USER} ./src/apps_plugins/${APP_NAME}
clean:
	- docker rm -f $$(docker ps -a -q)
	@$(PRINT_OK)
