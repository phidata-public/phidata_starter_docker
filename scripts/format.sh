#!/bin/bash

############################################################################
#
# Format workspace using black and mypy
# Usage:
#   ./scripts/format.sh
#
############################################################################

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$( dirname $SCRIPTS_DIR )"
DATA_DIR=$ROOT_DIR/data

print_horizontal_line() {
  echo "------------------------------------------------------------"
}

print_heading() {
  print_horizontal_line
  echo "--*--> $1"
  print_horizontal_line
}

main() {
  print_heading "Running: black $DATA_DIR"
  black $DATA_DIR
  print_heading "Running: mypy $DATA_DIR"
  mypy $DATA_DIR
}

main "$@"
