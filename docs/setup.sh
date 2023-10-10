#!/bin/bash
###
### Setup script for Markdown Docs
###
APP_NAME="markdown-docs-setup"
YOUR_NAME="David Hooton"

# Get location of this script
echo "Getting location of this script"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "I live in $DIR"

# Install PIP requirements
echo "Installing PIP requirements"
pip install -q -r $DIR/requirements.txt

# Run sphinx-apidoc
echo "Running sphinx-apidoc"
cd $DIR
sphinx-apidoc -o Sphinx-docs . sphinx-apidoc --full -A "${YOUR_NAME}"

# Generate conf.py
echo " import os
import sys
sys.path.insert(0,os.path.abspath('../'))
def skip(app, what, name, obj,would_skip, options):
    if name in ( '__init__',):
        return False
    return would_skip
def setup(app):
    app.connect('autodoc-skip-member', skip)
" >> Sphinx-docs/conf.py;

# Generate docs
cd $DIR/docs/Sphinx-docs/
make markdown

# Copy README.md to root
#cd ..
#cat _build/markdown/*.md >> new_README.md;
#rm -r Sphinx-docs;