all: build run-docker

run:
	python eval-prs.py

build:
	docker build -t eval-prs .

run-docker:
	docker run -v $(shell pwd)/template:/app/template:rw -v $(shell pwd)/data:/app/data:rw eval-prs