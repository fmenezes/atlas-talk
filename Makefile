POETRY = poetry

.PHONY: all
all: install

.PHONY: install
install:
	$(POETRY) install

.PHONY: prepare
prepare:
	$(POETRY) run prepare

.PHONY: server
server:
	$(POETRY) run server

.PHONY: chat
chat:
	$(POETRY) run chat

.PHONY: test
test:
	$(POETRY) run pytest

.PHONY: lint
lint:
	$(POETRY) run pylint src

.PHONY: format
format:
	$(POETRY) run black src
	$(POETRY) run isort src

.PHONY: build
build:
	$(POETRY) build

.PHONY: clean
clean:
	rm -rf dist
	rm -rf build
	rm -rf .venv
	rm -rf .pytest_cache
	find src -type d -name *.egg-info -exec rm -rf {} +
	find src -type d -name __pycache__ -exec rm -rf {} +
