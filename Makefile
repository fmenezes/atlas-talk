POETRY = poetry

CMAKE_ARGS = ""
FORCE_CMAKE = 0

ifneq ($(OS),Windows_NT)
	UNAME_S := $(shell uname -s)
	UNAME_P := $(shell uname -p)
	ifeq ($(UNAME_S),Darwin)
		ifneq ($(filter arm%,$(UNAME_P)),)
			CMAKE_ARGS = "-DLLAMA_METAL=on"
			FORCE_CMAKE = 1
		endif
	endif
endif

.PHONY: all
all: install

.PHONY: install
install:
	CMAKE_ARGS=$(CMAKE_ARGS) FORCE_CMAKE=$(FORCE_CMAKE) $(POETRY) install

.PHONY: prepare
prepare:
	$(POETRY) run prepare

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
	rm -rf *.egg-info
