APP = restapi

test:
	@bandit -r . -x './venv','./tests/'
	@black .
	@flake8 . --exclude=venv
	@pytest -v --disable-warnings

compose:
	@docker-compose up --build
	
setup-dev:
	@kind create cluster --config kubernetes/config/config.yaml
	@helm repo add bitnami https://charts.bitnami.com/bitnami
	@helm install mongodb bitnami/mongodb --version 18.1.20 -f kubernetes/config/mongodb-values.yaml
	@kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=mongodb --timeout=270s
teardown-dev:
	@kind delete clusters kind