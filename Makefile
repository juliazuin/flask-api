APP = restapi-flask

test:
	@bandit -r . -x './venv','./tests/'
	@black .
	@flake8 . --exclude=venv
	@pytest -v --disable-warnings

compose:
	@docker-compose up --build
	
setup-dev:
	@kind create cluster --config=kubernetes/config/config.yaml
	@kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/kind/deploy.yaml
	@kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=120s
	@helm repo add bitnami https://charts.bitnami.com/bitnami
	@helm install mongodb bitnami/mongodb --version 18.1.20 -f kubernetes/config/mongodb-values.yaml
	@kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=mongodb --timeout=270s
teardown-dev:
	@kind delete clusters kind

deploy-dev:
	@docker build -t $(APP):latest .
	@kind load docker-image $(APP):latest
	@kubectl apply -f kubernetes/manifests/.
	@kubectl rollout restart deployment restapi-flask

dev:
	@make setup-dev
	@make deploy-dev