APP = restapi

test:
	@flake8 . --exclude=venv

compose:
	@docker-compose up --buiild
	