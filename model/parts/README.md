# model/parts

One module per part of the work, named `NN_name.py` and run in name order after the core in
`model/subcritical.py`. Each defines `build(L, here)` and derives its numbers with
`L.derive(id, fn, formula, ..., defined_in=here())`, reading inputs from its own
`data/inputs/NN-name.toml`. One file per part, so writers working in parallel never edit the same
file. A part may read numbers an earlier part defined, never a later one's.
