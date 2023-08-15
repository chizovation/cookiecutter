#!/usr/bin/env bash
set -euo pipefail

# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html

# initialise git
git init

# find the dotfiles, and git add them (in one step)
find . -maxdepth 1 -type f -name ".*" -exec git add {} +

# commit them
git commit -m "Initial commit"

# add everything else
git add .
# and commit
git commit -m "Add project files (cookiecutter)"
