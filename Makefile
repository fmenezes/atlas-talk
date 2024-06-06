DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

index: index/index.faiss

index/index.faiss: $(VENV)/bin/activate
	python3 -m venv $(VENV); $(PYTHON) main.py save-index

memory/touchfile:
	mkdir -p memory
	touch memory/touchfile

.PHONY: run
run: $(VENV)/bin/activate index/index.faiss memory/touchfile
	python3 -m venv $(VENV); $(PYTHON) main.py chat

$(VENV): $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV); $(PIP) install -r requirements.txt; $(PYTHON) -m playwright install

.PHONY: clean
clean:
	rm -rf __pycache__ $(VENV) memory docs index
