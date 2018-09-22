#!/bin/bash
find -name 'gen_figs.py' -exec rm {} \;
configs_gen || exit 1
find -name 'gen_figs.py' -exec bash -c '(echo {} && cd $(dirname {}) && python3 gen_figs.py)' \;