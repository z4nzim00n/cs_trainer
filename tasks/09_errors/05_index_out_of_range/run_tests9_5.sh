#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 4 5\n2' $'Value: 3\n'
run_case $'5\n1 2 3 4 5\n10' $'Error: index out of range\n'
run_case $'3\n1 2 3\n-1' $'Error: index out of range\n'
run_case $'1\n7\n0' $'Value: 7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
