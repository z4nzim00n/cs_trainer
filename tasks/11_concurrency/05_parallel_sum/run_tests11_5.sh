#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 4 5' $'Sum: 15\n'
run_case $'4\n-1 10 -2 3' $'Sum: 10\n'
run_case $'1\n7' $'Sum: 7\n'
run_case $'0\n' $'Sum: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
