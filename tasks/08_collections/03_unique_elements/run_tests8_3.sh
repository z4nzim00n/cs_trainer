#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 1 3 2 1' $'Unique: 3\n1 2 3\n'
run_case $'4\n7 7 7 7' $'Unique: 1\n7\n'
run_case $'5\n5 4 3 2 1' $'Unique: 5\n1 2 3 4 5\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
