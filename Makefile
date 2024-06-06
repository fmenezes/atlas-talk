DEFAULT_GOAL := run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


docs/touchfile:
	cd ./scripts/gendocs && go run .
	touch docs/touchfile

index/index.faiss: docs/touchfile venv
	. venv/bin/activate; python main.py save-index

memory/touchfile:
	mkdir -p memory
	touch memory/touchfile

.PHONY: run
run: $(VENV)/bin/activate index/index.faiss memory/touchfile
	$(PYTHON) main.py chat

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt


.PHONY: clean
clean:
	rm -rf __pycache__ $(VENV) memory docs index
