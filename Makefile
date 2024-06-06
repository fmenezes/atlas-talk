DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: chat
chat: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) src/main.py chat

.PHONY: prepare
prepare: $(VENV)/bin/activate
	@. $(VENV)/bin/activate
	@$(PYTHON) src/main.py prepare

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate
	@$(PIP) install -r requirements.txt

.PHONY: clean
clean:
	@rm -rf __pycache__ $(VENV)
