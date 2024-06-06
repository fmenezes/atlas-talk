DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: chat
chat: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) src/main.py

.PHONY: prepare
prepare: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) src/atlas_talk/scripts/prepare.py

.PHONY: jsonl
jsonl: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) src/atlas_talk/scripts/jsonl.py


.PHONY: test
test: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	pytest

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate
	@$(PIP) install -e '.[dev]'

.PHONY: clean
clean:
	@rm -rf __pycache__ $(VENV)
