#!/bin/bash

############################################################################
#
# Install python dependencies
# Usage:
#   ./scripts/install_ws.sh    : Install dependencies
#   ./scripts/install_ws.sh -u : Upgrade + Install dependencies
#
############################################################################

CURR_SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
ROOT_DIR="$( dirname $CURR_SCRIPT_PATH )"

print_horizontal_line() {
  echo "------------------------------------------------------------"
}

print_heading() {
  print_horizontal_line
  echo "--*--> $1"
  print_horizontal_line
}

install_python_deps() {
  print_heading "Installing dependencies"
  pip install -r $ROOT_DIR/requirements.txt --no-deps

  print_heading "Installing airflow dependencies for code completion"
  pip install -r $REQUIREMENTS_DIR/airflow-requirements.txt --no-deps
}

update_python_deps() {
  print_heading "Compiling requirements"
  CUSTOM_COMPILE_COMMAND="./scripts/install_ws.sh -u" \
    pip-compile --upgrade $ROOT_DIR/requirements.in
}

install_workspace() {
  print_heading "Installing workspace $ROOT_DIR"
  pip3 install --editable $ROOT_DIR
}

main() {
  UPDATE=0
  if [[ "$#" -ge 1 ]] && [[ "$1" = "-u" || "$1" = "update" ]]; then
    UPDATE=1
  fi

  print_heading "Installing workspace: ${ROOT_DIR}"
  print_heading "Installing pip-tools"
  python -m pip install pip-tools

  if [[ $UPDATE -eq 1 ]]; then
    print_horizontal_line
    update_python_deps
    print_horizontal_line
  fi

  install_python_deps
  print_horizontal_line
  install_workspace
  print_horizontal_line
}

main "$@"
