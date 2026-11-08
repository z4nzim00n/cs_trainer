#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 1 4 2 5' $'1 2 3 4 5\n'
run_case $'4\n10 -1 3 0' $'-1 0 3 10\n'
run_case $'1\n42' $'42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
