.PHONY: all install test lint build deploy run_celery clean

all: install test lint build deploy

install:
	pip install -r src/ai_chatbot/requirements.txt
	pip install -r src/ai_chatbot/requirements-dev.txt

test:
	pytest tests/ --cov=src --cov-report=term-missing

lint:
	black src tests
	flake8 src tests
	mypy src

build:
	docker-compose build

deploy:
	kubectl apply -f deployment/k8s/

run_celery:
	docker-compose run --rm celery_worker

monitor:
	docker-compose up prometheus grafana

clean:
	docker-compose down
	docker system prune -f
	find . -type d -name "__pycache__" -exec rm -r {} +