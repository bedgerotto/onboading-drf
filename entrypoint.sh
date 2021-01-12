#! /bin/bash
set -e

# install dependencies
python -c "import pkg_resources; pkg_resources.require(open('requirements.txt',mode='r'))" &>/dev/null || pip install --ignore-installed -r requirements.txt

# Replace the shell with the given command:
exec "$@"