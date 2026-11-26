# Detent. Python 3.11 or later; the model and checks use the standard library only.
PY ?= python3

.PHONY: all model docs check paper

all: model docs check

model:  ## write data/numbers.json and research/numbers.md from data/inputs.toml
	$(PY) model/detent.py --write

docs:   ## rewrite every ledger link to the model's value
	$(PY) tools/sync.py

check:  ## em dashes, model reproduces, docs synced, every citation and source identified
	$(PY) tools/check.py

paper:  ## build/detent-paper.md, the paper with ledger links flattened, for Paperwright
	$(PY) tools/paper.py
