DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

langchain/index: langchain/index/touchfile

langchain/index/touchfile: $(VENV)
	. $(VENV)/bin/activate
	$(PYTHON) langchain/main.py save-index
	touch langchain/index/touchfile

langchain/memory: langchain/memory/touchfile

langchain/memory/touchfile:
	mkdir -p memory
	touch langchain/memory/touchfile

.PHONY: langchain-run
langchain-run: $(VENV)/bin/activate langchain/index langchain/memory
	. $(VENV)/bin/activate
	$(PYTHON) langchain/main.py chat

.PHONY: llamaindex-run
llamaindex-run: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) llamaindex/main.py chat

.PHONY: collect
collect: $(VENV)/bin/activate
	. $(VENV)/bin/activate
	$(PYTHON) collect/main.py

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	$(PIP) install -r requirements.txt
	$(PYTHON) -m playwright install

.PHONY: langchain-clean
langchain-clean:
	rm -rf __pycache__ $(VENV) langchain/memory langchain/index

.PHONY: clean
clean: langchain-clean
