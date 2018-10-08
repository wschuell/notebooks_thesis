#!/bin/bash

(cd chapters && find . -name '*.ipynb' -exec cp --parents -t ../../chapters/ '{}' \;)
