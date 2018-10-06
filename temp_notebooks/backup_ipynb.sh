#!/bin/bash

(cd ../../notebook_thesis/chapters && find . -name '*.ipynb' -exec cp --parents {} ../../notebook_thesis/temp_notebooks/chapters/ \;)
