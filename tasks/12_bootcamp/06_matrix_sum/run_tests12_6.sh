#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'2\n1 2\n3 4' $'Sum: 10\nDiagonal: 5\n'
run_case $'3\n1 2 3\n4 5 6\n7 8 9' $'Sum: 45\nDiagonal: 15\n'
run_case $'1\n7' $'Sum: 7\nDiagonal: 7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
