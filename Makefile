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

.PHONY: langchain-index
langchain-index: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) langchain-index/main.py

.PHONY: llamaindex-index
llamaindex-index: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) llamaindex-index/main.py

.PHONY: index
index: langchain-index llamaindex-index

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	$(PIP) install -r requirements.txt
	$(PYTHON) -m playwright install

.PHONY: clean
clean:
	rm -rf __pycache__ $(VENV)
