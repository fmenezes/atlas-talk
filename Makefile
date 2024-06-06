DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: chat
chat: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) chat/main.py

.PHONY: collect
collect: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) collect/main.py

.PHONY: prepare
prepare: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) prepare/main.py

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate
	@$(PIP) install -r requirements.txt

.PHONY: clean
clean:
	@rm -rf __pycache__ $(VENV)
