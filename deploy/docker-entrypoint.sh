#!/bin/sh

set -e

# activate our virtual environment here
. /opt/stepik/.venv/bin/activate

# Evaluating passed command:
exec "$@"
