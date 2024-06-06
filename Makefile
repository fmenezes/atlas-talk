DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: langchain-run
langchain-run: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) langchain/main.py

.PHONY: llamaindex-run
llamaindex-run: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) llamaindex/main.py

.PHONY: collect
collect: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) collect/main.py

.PHONY: langchain-prepare
langchain-prepare: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) langchain-prepare/main.py

.PHONY: llamaindex-prepare
llamaindex-prepare: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) llamaindex-prepare/main.py

.PHONY: prepare
prepare: langchain-prepare llamaindex-prepare

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	$(PIP) install -r requirements.txt
	$(PYTHON) -m playwright install

.PHONY: clean
clean:
	rm -rf __pycache__ $(VENV)
