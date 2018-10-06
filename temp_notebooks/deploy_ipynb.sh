#!/bin/bash

(cd chapters && find . -name '*.ipynb' -exec cp --parents {} ../../notebook_thesis/chapters/ \;)
