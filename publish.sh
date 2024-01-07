#!/bin/bash

# Ensure the required tools are installed
pip install twine

# Prompt the user for the PyPI token
read -p "Enter your PyPI token: " token

# Clean up any existing build and distribution files
rm -rf dist
python setup.py sdist bdist_wheel

# Upload the distribution files to PyPI using twine
TWINE_USERNAME=__token__ TWINE_PASSWORD="$token" twine upload dist/*

# Clean up the temporary build and distribution files
rm -rf dist
