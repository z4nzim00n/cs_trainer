#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 4 5' $'Sum: 15\nAverage: 3.00\n'
run_case $'3\n2 4 9' $'Sum: 15\nAverage: 5.00\n'
run_case $'1\n7' $'Sum: 7\nAverage: 7.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
