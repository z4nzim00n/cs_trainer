#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'6\n1 2 3 4 5 6' $'Sum: 56\n'
run_case $'3\n1 3 5' $'Sum: 0\n'
run_case $'4\n-2 -1 0 2' $'Sum: 8\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
